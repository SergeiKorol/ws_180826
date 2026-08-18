import pytest
import requests

# создать задачу, изменить и проверить что ИД не поменялся

URL = "http://5.101.50.9:8014/"


def test_new_edit():
    """
    проверка, что id объекта не изменяется
    при изменении самого объекта
    """
    body = {"title": "new_task", "completed": False}
    response = requests.post(URL, json=body)
    id = response.json()["id"]

    body = {"title": "last_task"}
    response = requests.patch(f'{URL}/{id}', json=body)
    new_id = response.json()["id"]
    assert id == new_id

# Создать задачу, Проставить отметку о выполнении и проверить что completed ==True


def test_edit():
    """
    проверка, что параметр "completed" объекта
    изменен на True
    """
    body = {"title": "main_task", "completed": False}
    response = requests.post(URL, json=body)
    id = response.json()["id"]

    body = {"title": "main_task", "completed": True}
    response = requests.patch(f'URL/{id}', json=body)
    assert response.status_code == 200

    response = requests.get(f'URL/{id}')
    assert response.status_code == 200
    assert response.json()['completed'] == True
