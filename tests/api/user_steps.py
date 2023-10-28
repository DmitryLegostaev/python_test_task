import json

import allure
import requests
from requests.compat import urljoin

from tests.api.data_templates.user_data_templates import create_or_update_user_data_template
from tests.api.models.user_model import *


@allure.step("Create user. POST")
def create_user(name: str, job: str, expected_status_code: int = 201):
    path = "/api/users/"
    base_url = "https://reqres.in/"     # TODO replace with dynamic

    response = requests.post(urljoin(base_url, path), create_or_update_user_data_template(name, job))
    response_status_code = response.status_code

    assert response_status_code == expected_status_code

    json_data = json.loads(response.text)
    return CreatedUser(**json_data)


@allure.step("Get user info by user id. GET")
def get_user_by_id(user_id: str, expected_status_code: int = 200):
    path = "/api/users/"
    base_url = "https://reqres.in/"     # TODO replace with dynamic
    print(urljoin(urljoin(base_url, path), user_id))

    response = requests.get(urljoin(urljoin(base_url, path), user_id))
    response_status_code = response.status_code

    assert response_status_code == expected_status_code

    json_data = json.loads(response.text)
    return ExistingUser(**json_data["data"])


@allure.step("Update user by user id. PATCH")
def update_user_by_patch(user_id: str, name: str, job: str, expected_status_code: int = 200):
    path = "/api/users/"
    base_url = "https://reqres.in/"     # TODO replace with dynamic

    print(urljoin(urljoin(base_url, path), user_id))

    response = requests.patch(urljoin(urljoin(base_url, path), user_id), create_or_update_user_data_template(name, job))
    response_status_code = response.status_code

    assert response_status_code == expected_status_code

    json_data = json.loads(response.text)
    return UpdatedUser(**json_data)


@allure.step("Update user by user id. PUT")
def update_user_by_put(user_id: str, name: str, job: str, expected_status_code: int = 200):
    path = "/api/users/"
    base_url = "https://reqres.in/"     # TODO replace with dynamic
    print(urljoin(urljoin(base_url, path), user_id))

    response = requests.put(urljoin(urljoin(base_url, path), user_id), create_or_update_user_data_template(name, job))
    response_status_code = response.status_code

    assert response_status_code == expected_status_code

    json_data = json.loads(response.text)
    return UpdatedUser(**json_data)


@allure.step("Delete user by user id. DELETE")
def delete_user_by_id(user_id: str, expected_status_code: int = 204):
    path = "/api/users/"
    base_url = "https://reqres.in/"     # TODO replace with dynamic
    print(urljoin(urljoin(base_url, path), user_id))

    response = requests.delete(urljoin(urljoin(base_url, path), user_id))
    response_status_code = response.status_code

    assert response_status_code == expected_status_code
