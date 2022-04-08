import functools
import json

from flask import Blueprint, jsonify, request

bp = Blueprint("blog", __name__, url_prefix="/blog")


@bp.route(
    "/",
    methods=("GET",),
)
def blog_post():
    return {"posts": [{"title": "My first POST"}]}, 200
