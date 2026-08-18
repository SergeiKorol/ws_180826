import requests


# Создать задачу,
# Проставить отметку о выполнении и проверить,
# что completed ==True
def test_add_2():
    body = {"title": "generated", "completed": False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    response_body = response.json()
    id = response.json()["id"]

    assert response.status_code == 200
    assert response_body['completed'] == False

    body = {"title": "generated", "completed": True}
    response = requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)
    assert response.status_code == 200
    assert response_body['completed'] == False
