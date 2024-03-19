import requests
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)


# Доработка задачи на семинаре
def test_01(title, login):
    response = requests.get(data['website2'], headers={'X-Auth-Token': login},
                            params={"owner": "notMe", "order": "DESC"})
    titles = [i["title"] for i in response.json()['data']]
    assert response.status_code == 200 and title in titles


# Практическое задание к первому семинару
def test_02(login):
    response = requests.post(data['website3'], headers={'X-Auth-Token': login}, data={'title': data['title'],
                                                                                      'description': data[
                                                                                      'description'],
                                                                                      'content': data['content']})
    response2 = requests.get(data['website2'], headers={'X-Auth-Token': login})
    descriptions = [i["description"] for i in response2.json()['data']]
    if response.status_code == response2.status_code == 200:
        assert data['description'] in descriptions
