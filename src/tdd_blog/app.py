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
