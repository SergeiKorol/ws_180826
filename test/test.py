import requests


"""
Тест на проверку статуса задачи, 
выполнено или нет
"""
def test_add_2():
    body = {"title": "generated01", "completed": False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    response_body = response.json()
    id = response.json()["id"]

    # проверка статус-кода ответа
    assert response.status_code == 200
    # проверка отметки о выполнении
    assert response_body['completed'] == False

    body = {"title": "generated003", "completed": True}
    resp = requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)
    resp_body = resp.json()
    # проверка статус-кода ответа
    assert resp.status_code == 200
    # проверка отметки о выполнении
    assert resp_body['completed'] == True
