import functools
from . import db
import json
import uuid

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
        return {"posts": list(db.values())}, 200
    elif request.method == "POST":
        if not request.json:
            return {"errors": [{"title": "is required", "body": "is required"}]}, 400
        if "title" not in request.json:
            return {"errors": [{"title": "is required"}]}, 400
        if len(request.json["body"]) < 50:
            return {"errors": [{"body": "must be at least 50 chars"}]}, 400

        body = request.json
        guid = str(uuid.uuid4())
        body["id"] = guid
        body["type"] = "post"
        db.set(guid, body)
        return {"id": guid, "type": "post"}, 201
    return {"error": "method not allowed"}, 406


@bp.route(
    "/<id>",
    methods=("GET",),
)
def blog_post_by_id(id: str):
    if request.method == "GET":
        import sys
        print(db.items(), file=sys.stderr)
        print(id, file=sys.stderr)
        print(type(id), file=sys.stderr)
        return db.get(id), 200
    return {"error": "method not allowed"}, 406
