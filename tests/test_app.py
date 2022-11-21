def test_create_post(client):
    response = client.post("/posts", json={"title": "First Post", "body": "Informative body"})
    assert response.status_code == 200
    assert response.json["id"] is not None

    response2 = client.get(f"/posts/{response.json['id']}")
    assert response2.status_code == 200
