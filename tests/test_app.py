def test_create_post(client):
    response = client.post("/posts", json={"title": "First Post", "body": "Informative body"})
    assert response.status_code == 200
