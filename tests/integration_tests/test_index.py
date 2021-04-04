def test_index(client):
    response = client.get('/')

    assert response.content_type == 'text/html; charset=utf-8'
    assert response.status == '200 OK'
