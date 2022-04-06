# helpers
def create_blog_post(client, body=None):
    body = body or {"title": "hey", "body": "baberiba"}
    response = client.post("/blog/", json=body)
    assert response.status_code == 201
    return response


# tests
def test_view_empty_index(client):
    response = client.get("/blog/")
    assert response.status_code == 200
    assert response.json == {"posts": []}


def test_view_blog_posts(client):
    creation = create_blog_post(client, {"title": "hey", "body": "baberiba"})
    response = client.get("/blog/")
    assert response.status_code == 200
    assert response.json == {"posts": [{"id": creation.json["id"], "type": "post", "title": "hey", "body": "baberiba"}]}


def test_create_new_blog_post(client):
    response = create_blog_post(client, {"title": "hey", "body": "baberiba"})
    assert response.json["id"] is not None
    assert response.json["type"] == "post"


def test_create_new_blog_post_and_read_it(client):
    creation = create_blog_post(client, {"title": "hey", "body": "baberiba"})
    response = client.get(f"/blog/{creation.json['id']}")
    assert response.status_code == 200
    assert response.json["id"] is not None
    assert response.json["type"] == "post"
    assert response.json["title"] == "hey"
    assert response.json["body"] == "baberiba"


def test_create_with_missing_title(client):
    response = client.post("/blog/", json={"body": "baberiba"})
    assert response.status_code == 400
    assert response.json["errors"] == [{"title": "is required"}]
