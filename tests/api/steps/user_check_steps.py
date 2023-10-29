import allure

from tests.api.models.user_model import CreatedUser, UpdatedUser, ExistingUser


@allure.step("Check created user data")
def check_created_user_data(created_user: CreatedUser, expected_name: str, expected_job: str):
    assert created_user.name == expected_name, (
        f"Actual name of created user: {created_user.name}. Expected name: {expected_name}")
    assert created_user.job == expected_job, (
        f"Actual job of created user: {created_user.job}. Expected job: {expected_job}")


@allure.step("Check updated user data")
def check_updated_user_data(updated_user: UpdatedUser, expected_name: str, expected_job: str):
    assert updated_user.name == expected_name, (
        f"Actual name of updated user: {updated_user.name}. Expected name: {expected_name}")
    assert updated_user.job == expected_job, (
        f"Actual job of updated user: {updated_user.job}. Expected job: {expected_job}")


@allure.step("Check existing user data")
def check_existing_user_data(existing_user: ExistingUser, expected_email: str, expected_first_name: str,
                             expected_last_name: str, expected_avatar: str):
    assert existing_user.email == expected_email, (
        f"Actual email of existing user: {existing_user.email}. Expected email: {expected_email}")
    assert existing_user.first_name == expected_first_name, (
        f"Actual first name of existing user: {existing_user.first_name}. Expected first name: {expected_first_name}")
    assert existing_user.last_name == expected_last_name, (
        f"Actual last name of existing user: {existing_user.last_name}. Expected last name: {expected_last_name}")
    assert existing_user.avatar == expected_avatar, (
        f"Actual avatar of existing user: {existing_user.avatar}. Expected avatar: {expected_avatar}")
