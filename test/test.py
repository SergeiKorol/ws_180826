import requests


"""
Тест на проверку статуса задачи, 
выполнено или нет
"""
def test_add_2():
    body = {"title": "generated", "completed": False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    response_body = response.json()
    id = response.json()["id"]

    # проверка статус-кода ответа
    assert response.status_code == 200
    # проверка отметки о выполнении
    assert response_body['completed'] == False

    body = {"title": "generated", "completed": True}
    response = requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)
    # проверка статус-кода ответа
    assert response.status_code == 200
    # проверка отметки о выполнении
    assert response_body['completed'] == False
