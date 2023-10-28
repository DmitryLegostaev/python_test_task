import allure
import pytest

from tests.api.status_code_steps import status_code_check
from user_steps import *


class TestReqResUser:
    @allure.title("Create, update and delete user")
    @allure.description(
        "An API test with CRUD operations around the User flow using the following Portal: https://reqres.in/")
    @allure.suite("API")
    @pytest.mark.parametrize(
        "new_user_name, new_user_job, update_user_name_patch, update_user_job_patch, "
        "update_user_name_put, update_user_job_put",
        [
            ("Derek", "Zoolander", "Hansel", "Fashion star", "Mugatu", "Fashion guru")
        ])
    def test_create_update_delete_user(self, api_url_endpoint, new_user_name, new_user_job,
                                       update_user_name_patch, update_user_job_patch, update_user_name_put,
                                       update_user_job_put):
        status_code, user_obj = create_user(api_url_endpoint, new_user_name, new_user_job)
        status_code_check(status_code, 201)
        user_obj.id = "12"  # TODO delete in real test

        status_code, get_user_obj = get_user_by_id(api_url_endpoint, user_obj.id)
        status_code_check(status_code, 200)

        status_code, update_user_obj_patch = update_user_by_patch(api_url_endpoint, user_obj.id, update_user_name_patch, update_user_job_patch)
        status_code_check(status_code, 200)

        status_code, update_user_obj_put = update_user_by_put(api_url_endpoint, user_obj.id, update_user_name_put, update_user_job_put)
        status_code_check(status_code, 200)

        status_code = delete_user_by_id(api_url_endpoint, user_obj.id)
        status_code_check(status_code, 204)
