import functools
from . import db
import json
import uuid
from typing import Dict

from flask import Blueprint, jsonify, request

bp = Blueprint("blog", __name__, url_prefix="/blog")


def write_to_db(id: str, body: Dict) -> None:
    db.set(id, body)


def create_blog_post(body: Dict) -> str:
    guid = str(uuid.uuid4())
    body["id"] = guid
    body["type"] = "post"
    write_to_db(guid, body)
    return guid


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
        if not request.json:
            return {"errors": [{"title": "is required", "body": "is required"}]}, 400
        if "title" not in request.json:
            return {"errors": [{"title": "is required"}]}, 400
        if len(request.json["body"]) < 50:
            return {"errors": [{"body": "must be at least 50 chars"}]}, 400

        body = request.json
        return {"id": create_blog_post(body), "type": "post"}, 201
    return {"error": "method not allowed"}, 406


@bp.route(
    "/<id>",
    methods=("GET","PUT"),
)
def blog_post_by_id(id: str):
    if request.method == "GET":
        return db.get(id), 200
    elif request.method == "PUT":
        write_to_db(id, request.json)
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
