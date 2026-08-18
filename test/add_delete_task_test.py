import requests

def add_delete_task ():
    body = {"title":"generated","completed":False}
    add_task = requests.post ("http://5.101.50.9:8014/", json=body)
    id = add_task.json()["id"]
    delete_task = requests.delete(f'http://5.101.50.9:8014/{id}')
    assert delete_task.status_code == 404

