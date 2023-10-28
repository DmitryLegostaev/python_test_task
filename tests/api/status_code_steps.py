import allure


@allure.step("Check status code")
def status_code_check(actual_status_code: int, expected_status_code: int):
    assert actual_status_code == expected_status_code, (f"Expected status code: {expected_status_code}. Actual "
                                                        f"status code: {actual_status_code}")
