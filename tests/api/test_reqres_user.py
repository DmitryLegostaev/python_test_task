import pytest

from tests.api.status_code_steps import status_code_check
from tests.api.user_check_steps import check_created_user_data, check_updated_user_data, check_existing_user_data
from user_crud_steps import *


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
        check_created_user_data(user_obj, new_user_name, new_user_job)
        user_obj.id = "12"  # TODO delete in real test

        status_code, get_user_obj = get_user_by_id(api_url_endpoint, user_obj.id)
        status_code_check(status_code, 200)
        check_existing_user_data(get_user_obj, "rachel.howell@reqres.in", "Rachel", "Howell",
                                 "https://reqres.in/img/faces/12-image.jpg")  # TODO delete hardcode in real test

        status_code, update_user_obj_patch = update_user_by_patch(api_url_endpoint, user_obj.id, update_user_name_patch,
                                                                  update_user_job_patch)
        status_code_check(status_code, 200)
        check_updated_user_data(update_user_obj_patch, update_user_name_patch, update_user_job_patch)

        status_code, update_user_obj_put = update_user_by_put(api_url_endpoint, user_obj.id, update_user_name_put,
                                                              update_user_job_put)
        status_code_check(status_code, 200)
        check_updated_user_data(update_user_obj_put, update_user_name_put, update_user_job_put)

        status_code = delete_user_by_id(api_url_endpoint, user_obj.id)
        status_code_check(status_code, 204)
