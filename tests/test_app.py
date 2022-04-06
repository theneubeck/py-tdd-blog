# helpers
from pydoc import cli

valid_body = "bodyz " * 10


def create_blog_post(client, body=None):
    body = body or {"title": "hey", "body": valid_body}
    response = client.post("/blog/", json=body)
    assert response.status_code == 201
    return response


# tests
## index tests
def test_view_empty_index(client):
    response = client.get("/blog/")
    assert response.status_code == 200
    assert response.json == {"posts": []}


def test_view_blog_posts(client):
    creation = create_blog_post(client, {"title": "hey", "body": valid_body})
    response = client.get("/blog/")
    assert response.status_code == 200
    assert response.json == {"posts": [{"id": creation.json["id"], "type": "post", "title": "hey", "body": valid_body}]}


# creation
def test_create_new_blog_post(client):
    response = create_blog_post(client, {"title": "hey", "body": valid_body})
    assert response.json["id"] is not None
    assert response.json["type"] == "post"


def test_create_new_blog_post_and_read_it(client):
    creation = create_blog_post(client, {"title": "hey", "body": valid_body})
    response = client.get(f"/blog/{creation.json['id']}")
    assert response.status_code == 200
    assert response.json["id"] is not None
    assert response.json["type"] == "post"
    assert response.json["title"] == "hey"
    assert response.json["body"] == valid_body


def test_create_with_missing_title(client):
    response = client.post("/blog/", json={"body": valid_body})
    assert response.status_code == 400
    assert response.json["errors"] == [{"title": "is required"}]


def test_create_with_missing_too_short_body(client):
    response = client.post("/blog/", json={"title": "my-title", "body": "too short"})
    assert response.status_code == 400
    assert response.json["errors"] == [{"body": "must be at least 50 chars"}]


def test_create_with_missing_body(client):
    response = client.post("/blog/", json={})
    assert response.status_code == 400
    assert response.json["errors"] == [{"body": "is required", "title": "is required"}]


# edit
def test_update_blog_post_title(client):
    creation = create_blog_post(client, {"title": "hey", "body": valid_body})
    response = client.put(f"/blog/{creation.json['id']}", json={"title": "a new title", "body": valid_body})
    assert response.status_code == 200
    response = client.get(f"/blog/{creation.json['id']}")
    assert response.json["title"] == "a new title"


def test_update_blog_post_body(client):
    creation = create_blog_post(client, {"title": "hey", "body": valid_body})
    response = client.put(f"/blog/{creation.json['id']}", json={"title": "hey", "body": f"a new title {valid_body}"})
    assert response.status_code == 200
    response = client.get(f"/blog/{creation.json['id']}")
    assert response.json["body"] == f"a new title {valid_body}"


def test_update_blog_post_body_and_list(client):
    creation = create_blog_post(client, {"title": "hey", "body": valid_body})
    response = client.put(
        f"/blog/{creation.json['id']}", json={"title": "a new title", "body": f"a new title {valid_body}"}
    )
    assert response.status_code == 200
    response = client.get(f"/blog/")
    assert response.status_code == 200
    assert response.json == {
        "posts": [
            {"id": creation.json["id"], "type": "post", "title": "a new title", "body": f"a new title {valid_body}"}
        ]
    }


def test_update_missing_blog_post(client):
    response = client.put(
        f"/blog/2698a490-5fa2-4736-a674-3db24fd10f1d", json={"title": "hey", "body": f"a new title {valid_body}"}
    )
    assert response.status_code == 404


def test_update_blog_post_with_missing_body(client):
    creation = create_blog_post(client, {"title": "hey", "body": valid_body})
    response = client.put(f"/blog/{creation.json['id']}", json={})
    assert response.status_code == 400
    assert response.json["errors"] == [{"body": "is required", "title": "is required"}]
    response = client.get(f"/blog/{creation.json['id']}")
    assert response.json["body"] == valid_body
    assert response.json["title"] == "hey"
