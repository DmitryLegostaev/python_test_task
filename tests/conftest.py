import json
import os

import pytest


@pytest.fixture(scope="package")
def retrieve_api_url_endpoint():
    configuration_file_path = os.path.join("tests", "configuration.json")

    with open(configuration_file_path) as config_file:
        data = json.load(config_file)

    yield data["ApiUrlEndpoint"]


@pytest.fixture(scope="package")
def retrieve_ui_url_endpoint():
    configuration_file_path = os.path.join("tests", "configuration.json")

    with open(configuration_file_path) as config_file:
        data = json.load(config_file)

    yield data["UiUrlEndpoint"]
