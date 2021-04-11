def test_list(client):
    res = client.get('/list')
    assert res.status_code == 200
    assert b'Madrid' in res.data
    assert b'28027' in res.data
    