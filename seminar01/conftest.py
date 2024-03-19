import pytest
import requests
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def login():
    response = requests.post(data['website1'], data={'username': data['username'], 'password': data['password']})
    if response.status_code == 200:
        return response.json()['token']


@pytest.fixture()
def title():
    return "Котик"
