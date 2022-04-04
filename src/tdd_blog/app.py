import functools
import json

from flask import Blueprint, jsonify, request

bp = Blueprint("blog", __name__, url_prefix="/blog")


@bp.route(
    "/",
    methods=(
        "GET",
        "POST",
    ),
)
def blog_post():
    if request.method == "GET":
        return jsonify({"posts": [{"title": "hey", "body": "baberiba", "id": 1, "type": "post"}]}), 200
    elif request.method == "POST":
        if "title" not in request.json:
            return {"errors": [{"title": "is required"}]}, 400
        return {"id": 1, "type": "post"}, 201
    return {"error": "method not allowed"}, 406


@bp.route(
    "/1",
    methods=("GET",),
)
def blog_post_by_id():
    if request.method == "GET":
        return jsonify({"title": "hey", "id": 1, "type": "post", "body": "baberiba"}), 200
    return {"error": "method not allowed"}, 406
