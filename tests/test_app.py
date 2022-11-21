def create_blog_post(client, title: str, body: str):
    return client.post("/posts", json={"title": title, "body": body})


def test_create_empty_blog_post(client):
    r = client.post("/posts", json={})
    assert r.status_code == 400


def test_create_blog_post_without_body(client):
    r = client.post("/posts", json={"title": "Title yes"})
    assert r.status_code == 400


def test_create_blog_post_with_empty_body(client):
    r = client.post("/posts", json={"title": "title", "body": ""})
    assert r.status_code == 400


def test_create_post_1(client):
    data = {"title": "First Post", "body": "Informative body"}
    response = client.post("/posts", json=data)
    assert response.status_code == 200
    assert response.json["id"] is not None

    response2 = client.get(f"/posts/{response.json['id']}")
    assert response2.status_code == 200
    assert response2.json["id"] == response.json["id"]
    assert response2.json["title"] == data["title"]
    assert response2.json["body"] == data["body"]


def test_create_post_2(client):
    data = {"title": "Second Post", "body": "Offensive body"}
    response = client.post("/posts", json=data)
    assert response.status_code == 200
    assert response.json["id"] is not None

    response2 = client.get(f"/posts/{response.json['id']}")
    assert response2.status_code == 200
    assert response2.json["id"] == response.json["id"]
    assert response2.json["title"] == data["title"]
    assert response2.json["body"] == data["body"]


def test_get_unexisting_blog_post(client):
    response = client.get(f"/posts/id_that_does_not_exist")
    assert response.status_code == 404


def test_get_all_blog_posts(client):
    response = client.get("/posts")
    assert response.status_code == 200
    assert response.json["posts"] == []


def test_get_post_from_start_page(client):
    title = "new_blog_post"
    body = "body"
    response = create_blog_post(client, title, body)
    response2 = client.get(f"/posts")
    assert response2.status_code == 200
    blog_posts = response2.json["posts"]
    assert response.json["id"] in [post["id"] for post in blog_posts]
    post = [post for post in blog_posts if post["id"] == response.json["id"]][0]
    assert post["title"] == title
    assert post["body"] == body
