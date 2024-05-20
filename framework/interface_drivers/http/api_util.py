import requests
from test_project.models.header import HeaderModel
from test_project.models.access import AccessModel


def get(url: str, headers: HeaderModel.Authorization):
    response = requests.get(url, headers=dict(headers))
    return response.status_code, response.json()


def post(url: str, body: AccessModel, headers: HeaderModel.Headers):
    response = requests.post(url, data=dict(body), headers=dict(headers))
    return response.status_code, response.json()
