import requests

def test_complete_task():
    """
    Создать задачу, проставить отметку о выполнении и
    проверить что completed ==True
    """
    # создала задачу с наименованием "Задача Елены"
    body = {
        "title": "Задача Елены",
        "completed": False
    }
    response = requests.post("http://5.101.50.9:8014/", json=body)

    task_id = response.json()['id']

    # Отметила как выполненную
    response = requests.patch(
        f"http://5.101.50.9:8014/{task_id}",
        json={"completed": True}
    )

    response = requests.get(f"http://5.101.50.9:8014/{task_id}")

    assert response.status_code == 200
    assert response.json()['completed'] is True


