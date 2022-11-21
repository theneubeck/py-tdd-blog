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
