import functools
import json

from flask import Blueprint, jsonify, request

# from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint("blog", __name__, url_prefix="/blog")


@bp.route(
    "/",
    methods=(
        "GET",
        "POST",
    ),
)
def blog_post():
    if request.method != "GET":
        return {"error": "method not allowed"}, 406
    return {"title": "My first POST"}, 200
