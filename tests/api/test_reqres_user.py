import allure
import pytest

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
    def test_create_update_delete_user(self, retrieve_api_url_endpoint, new_user_name, new_user_job,
                                       update_user_name_patch, update_user_job_patch, update_user_name_put,
                                       update_user_job_put):
        user_obj = create_user(new_user_name, new_user_job)
        print(user_obj)  # TODO delete
        user_obj.id = "12"  # TODO delete in real test

        get_user_obj = get_user_by_id(user_obj.id)
        print(get_user_obj)  # TODO delete

        update_user_obj_patch = update_user_by_patch(user_obj.id, update_user_name_patch, update_user_job_patch)
        print(update_user_obj_patch)  # TODO delete

        update_user_obj_put = update_user_by_put(user_obj.id, update_user_name_put, update_user_job_put)
        print(update_user_obj_put)  # TODO delete

        delete_user_by_id(user_obj.id)
