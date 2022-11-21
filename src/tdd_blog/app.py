import functools
import json

from flask import Blueprint, jsonify, request

bp = Blueprint("blog", __name__, url_prefix="")


@bp.route(
    "/posts",
    methods=("GET", "POST"),
)
def blog_post():
    return {"id": "apa"}, 200

@bp.route(
    "/posts/<id>",
    methods=("GET",),
)
def get_blog(id: int):
    return {
        "id": "apa",
        "title": "First Post",
        "body": "Informative body",
    }, 200
