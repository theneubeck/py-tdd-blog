def test_request_example(client):
    response = client.get("/blog/")
    assert response.status_code == 200
    assert response.json == [{"posts": {"title": "My first POST"}}]
