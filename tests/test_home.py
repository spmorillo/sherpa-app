def test_home(client):
    res = client.get('/')
    assert res.status_code == 200
    assert b'Bienvenido' in res.data
    #expected = {'hello': 'world'}
    #assert expected == json.loads(res.get_data(as_text=True))