import allure
import pytest
from playwright.sync_api import APIRequestContext

from utils.allure_helpers import attach_json

pytestmark = pytest.mark.api


@allure.feature("JSONPlaceholder API")
@allure.story("Posts")
@allure.title("Create post returns HTTP 201 and echoes the submitted data")
def test_create_post_returns_expected_status_and_data(api_context: APIRequestContext):
    new_post = {
        "title": "QA Portfolio Test Post",
        "body": "This is a sample API test payload",
        "userId": 1,
    }

    attach_json("request-payload", new_post)

    with allure.step("Send POST /posts with a sample payload"):
        response = api_context.post("/posts", data=new_post)
        response_body = response.json()
        attach_json("response-body", response_body)

    with allure.step("Check the response status is 201"):
        assert response.status == 201

    with allure.step("Check the response echoes the submitted fields"):
        assert response_body["title"] == new_post["title"]
        assert response_body["body"] == new_post["body"]
        assert response_body["userId"] == new_post["userId"]
        assert "id" in response_body