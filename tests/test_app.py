def test_view_blog_posts(client):
    response = client.get("/blog/")
    assert response.status_code == 200
    assert response.json == {"posts": [{"title": "My first POST"}]}


def test_create_new_blog_post(client):
    response = client.post("/blog/")
    assert response.status_code == 201
    assert response.json["id"] is not None
    assert response.json["type"] == "blog"


def test_create_new_blog_post_and_read_it(client):
    creation = client.post("/blog/", json={"title": "hey", "body": "baberiba"})
    response = client.get(f"/blog/{creation.json['id']}")
    assert response.status_code == 200
    assert response.json["title"] == "hey"
    assert response.json["body"] == "baberiba"
