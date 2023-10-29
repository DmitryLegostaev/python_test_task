import json

import allure
import requests
from requests.compat import urljoin

from tests.api.data_templates.user_data_templates import create_or_update_user_data_template
from tests.api.models.user_model import CreatedUser, ExistingUser, UpdatedUser


@allure.step("Create user. POST")
def create_user(url: str, name: str, job: str):
    response = requests.post(url, create_or_update_user_data_template(name, job))

    json_data = json.loads(response.text)
    return response.status_code, CreatedUser(**json_data)


@allure.step("Get user info by user id. GET")
def get_user_by_id(url: str, user_id: str):
    response = requests.get(urljoin(url, user_id))

    json_data = json.loads(response.text)
    return response.status_code, ExistingUser(**json_data["data"])


@allure.step("Update user by user id. PATCH")
def update_user_by_patch(url: str, user_id: str, name: str, job: str):
    response = requests.patch(urljoin(url, user_id), create_or_update_user_data_template(name, job))

    json_data = json.loads(response.text)
    return response.status_code, UpdatedUser(**json_data)


@allure.step("Update user by user id. PUT")
def update_user_by_put(url: str, user_id: str, name: str, job: str):
    response = requests.put(urljoin(url, user_id), create_or_update_user_data_template(name, job))

    json_data = json.loads(response.text)
    return response.status_code, UpdatedUser(**json_data)


@allure.step("Delete user by user id. DELETE")
def delete_user_by_id(url: str, user_id: str):
    response = requests.delete(urljoin(url, user_id))

    return response.status_code
