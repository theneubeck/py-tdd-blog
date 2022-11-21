import functools
import json
import uuid

from flask import Blueprint, jsonify, request

from tdd_blog import db

bp = Blueprint("blog", __name__, url_prefix="")


@bp.route(
    "/posts",
    methods=("GET", "POST"),
)
def blog_post():
    payload = request.json
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
