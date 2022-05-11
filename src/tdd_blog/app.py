import functools
import json
import uuid
from typing import Dict, Optional

from flask import Blueprint, jsonify, request

from . import db

bp = Blueprint("blog", __name__, url_prefix="/blog")


def check_exist(func):
    def wrapper(id, *args, **kwargs):
        if not db.get(id):
            return {}, 404
        return func(id, *args, **kwargs)

    return wrapper


def write_to_db(id: str, body: Dict) -> None:
    body["id"] = id
    body["type"] = "post"
    db.set(id, body)


def create_blog_post(body: Dict) -> str:
    guid = str(uuid.uuid4())
    write_to_db(guid, body)
    return guid


def validate_blog_post(post: Dict) -> Optional[Dict]:
    if not post:
        return {"errors": [{"title": "is required", "body": "is required"}]}
    if "title" not in post:
        return {"errors": [{"title": "is required"}]}
    if "body" not in post:
        return {"errors": [{"body": "is required"}]}
    if len(post["body"]) < 50:
        return {"errors": [{"body": "must be at least 50 chars"}]}


@bp.route(
    "/",
    methods=(
        "GET",
        "POST",
    ),
)
def blog_post():
    if request.method == "GET":
        return {"posts": list(db.values())}, 200
    elif request.method == "POST":
        errors = validate_blog_post(request.json)
        if errors:
            return errors, 400

        body = request.json
        return {"id": create_blog_post(body), "type": "post"}, 201
    return {"error": "method not allowed"}, 406


@bp.route(
    "/<id>",
    methods=("GET", "PUT", "DELETE"),
)
@check_exist
def blog_post_by_id(id: str):
    if request.method == "GET":
        return db.get(id), 200
    elif request.method == "PUT":
        errors = validate_blog_post(request.json)
        if errors:
            return errors, 400

        write_to_db(id, request.json)
        return {}, 200
    elif request.method == "DELETE":
        db.delete(id)
        return {}, 200
    return {"error": "method not allowed"}, 406


@bp.route(
    "/post/<id>",
    methods=("POST",),
)
def edit_blog_post_by_id(id: str):
    if request.method == "POST":
        body = request.json
        write_to_db(id, body)

    return {"error": "method not allowed"}, 406

@bp.route(
    "/post/<id>/comments",
    methods=("POST", "GET",)
)
def create_post_comment(id: str):
    post = db.get(id)
    if request.method == "POST":
        body = request.json
        if not body["comment"]:
            return {}, 400
        post["comments"] = post.get("comments", [])
        post["comments"].append(body)
        write_to_db(id, post)
        return {}, 201
    return {"comments": post.get("comments", [])}, 200
