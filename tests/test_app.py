# helpers
def create_blog_post(client, body=None):
    body = body or {"title": "hey", "body": "baberiba"}
    response = client.post("/blog/", json={"title": "hey", "body": "baberiba"})
    assert response.status_code == 201
    return response


# tests
def test_view_blog_posts(client):
    create_blog_post(client, {"title": "hey", "body": "baberiba"})
    response = client.get("/blog/")
    assert response.status_code == 200
    assert response.json == {"posts": [{"title": "hey", "body": "baberiba"}]}


def test_create_new_blog_post(client):
    response = create_blog_post(client, {"title": "hey", "body": "baberiba"})
    assert response.json["id"] is not None
    assert response.json["type"] == "blog"


def test_create_new_blog_post_and_read_it(client):
    creation = create_blog_post(client, {"title": "hey", "body": "baberiba"})
    response = client.get(f"/blog/{creation.json['id']}")
    assert response.status_code == 200
    assert response.json["title"] == "hey"
    assert response.json["body"] == "baberiba"
