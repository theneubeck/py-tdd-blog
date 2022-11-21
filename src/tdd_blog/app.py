import functools
import http
import json
import uuid
from typing import Dict

from flask import Blueprint, jsonify, request

from tdd_blog import db

bp = Blueprint("blog", __name__, url_prefix="")


def validate_blogpost(blog_post: Dict) -> bool:
    if not blog_post:
        return False
    if not blog_post.get("body"):
        return False
    if (not (title := blog_post.get("title"))) or len(title) < 5:
        return False
    return True



@bp.route(
    "/posts",
    methods=("GET", "POST"),
)
def blog_post():
    if request.method == "GET":
        return {"posts": [{"id": _id, **post} for _id, post in db.items()]}, 200

    payload = request.json
    if not validate_blogpost(payload):
        return {}, http.HTTPStatus.BAD_REQUEST
    post_id = str(uuid.uuid4())
    db.set(post_id, payload)
    return {"id": post_id}, 200

@bp.route(
    "/posts/<id>",
    methods=("GET",),
)
def get_blog(id: str):
    post = db.get(id)
    if not post:
        return {}, 404
    return {
        "id": id,
        **post
    }, 200
