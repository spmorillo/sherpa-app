import json
import random

def test_user(client):
    res = client.get('/user')
    assert res.status_code == 200
    assert b'ID del usuario' in res.data

def test_adduser(client):
    n = random.randint(0,1000000)
    data = {"user": "prueba"+str(n), "cp": 28027} # Quick but faulty fix. Needs sth better.
    res = client.post("/adduser", data=data)
    result_json = json.loads(res.get_data(as_text=True))
    assert res.status_code == 201

def test_adduser_duplicate(client):
    data = {"user": "qaqaqaqa", "cp": 28027}
    res = client.post("/adduser", data=data)
    assert res.status_code == 400
    res_json = json.loads(res.get_data(as_text=True))
    assert 'usuario' in res_json["message"] # Error in usuario
    

def test_adduser_wrong_cp(client):
    data = {"user": "fkmrekmf", "cp": 1}
    res = client.post("/adduser", data=data)
    assert res.status_code == 400
    res_json = json.loads(res.get_data(as_text=True))
    assert 'ciudad' in res_json["message"] # Error in ciudad (not generated bc wrong cp)