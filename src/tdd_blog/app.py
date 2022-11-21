import functools
import json

from flask import Blueprint, jsonify, request

bp = Blueprint("blog", __name__, url_prefix="")


@bp.route(
    "/",
    methods=("GET",),
)
def blog_post():
    return {"ok": True}, 200
