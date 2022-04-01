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
        return jsonify({"posts": [{"title": "My first POST"}]}), 200
    elif request.method == "POST":
        return {"id": -1, "type": "blog"}, 201

    return {"error": "method not allowed"}, 406
