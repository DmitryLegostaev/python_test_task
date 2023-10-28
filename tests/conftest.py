import json
import os

import pytest

from requests.compat import urljoin


@pytest.fixture(scope="package")
def api_url_endpoint():
    configuration_file_path = os.path.join("tests", "configuration.json")

    with open(configuration_file_path) as config_file:
        data = json.load(config_file)

    yield urljoin(data["ApiUrlBaseUrl"], data["ApiUrlPath"])


@pytest.fixture(scope="package")
def retrieve_ui_url_endpoint():
    configuration_file_path = os.path.join("tests", "configuration.json")

    with open(configuration_file_path) as config_file:
        data = json.load(config_file)

    yield data["UiUrlEndpoint"]
