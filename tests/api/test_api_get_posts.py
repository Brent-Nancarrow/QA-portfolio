import allure
import pytest
from playwright.sync_api import APIRequestContext

from utils.allure_helpers import attach_json
from utils.api_helpers import assert_has_keys
from utils.traceability import traceability

pytestmark = pytest.mark.api


@traceability("RQ-API-001")
@allure.feature("JSONPlaceholder API")
@allure.story("Posts")
@allure.title("Get all posts returns HTTP 200")
def test_get_all_posts_returns_200(api_context: APIRequestContext):
    with allure.step("Record the linked requirement for this API availability check"):
        allure.attach(
            "Requirement: RQ-API-001 - Posts endpoint availability",
            name="traceability-reference",
            attachment_type=allure.attachment_type.TEXT,
        )

    with allure.step("Send GET /posts"):
        response = api_context.get("/posts")

    with allure.step("Check the response status is 200"):
        assert response.status == 200


@traceability("RQ-API-001")
@allure.feature("JSONPlaceholder API")
@allure.story("Posts")
@allure.title("Get all posts returns a non-empty list")
def test_get_all_posts_returns_a_non_empty_list(api_context: APIRequestContext):
    with allure.step("Record the linked requirement for this API content check"):
        allure.attach(
            "Requirement: RQ-API-001 - Posts endpoint availability",
            name="traceability-reference",
            attachment_type=allure.attachment_type.TEXT,
        )

    with allure.step("Send GET /posts"):
        response = api_context.get("/posts")
        posts = response.json()
        attach_json("posts-response", posts[:3])

    with allure.step("Check the response is a non-empty list"):
        assert isinstance(posts, list)
        assert len(posts) > 0


@traceability("RQ-API-001")
@allure.feature("JSONPlaceholder API")
@allure.story("Posts")
@allure.title("First post contains the expected fields")
def test_first_post_contains_expected_fields(api_context: APIRequestContext):
    with allure.step("Record the linked requirement for this API structure check"):
        allure.attach(
            "Requirement: RQ-API-001 - Posts endpoint availability",
            name="traceability-reference",
            attachment_type=allure.attachment_type.TEXT,
        )

    with allure.step("Send GET /posts"):
        response = api_context.get("/posts")
        posts = response.json()
        first_post = posts[0]
        attach_json("first-post", first_post)

    with allure.step("Check the first post contains the expected keys"):
        assert_has_keys(first_post, ["userId", "id", "title", "body"])


@traceability("RQ-API-002")
@allure.feature("JSONPlaceholder API")
@allure.story("Posts")
@allure.title("Get a non-existent post returns HTTP 404 with an empty body")
def test_get_non_existent_post_returns_404(api_context: APIRequestContext):
    with allure.step("Record the linked requirement for this negative API check"):
        allure.attach(
            "Requirement: RQ-API-002 - Missing post handling",
            name="traceability-reference",
            attachment_type=allure.attachment_type.TEXT,
        )

    with allure.step("Send GET /posts/999999"):
        response = api_context.get("/posts/999999")
        response_body = response.json()
        attach_json("404-response-body", response_body)

    with allure.step("Check the response status is 404"):
        assert response.status == 404

    with allure.step("Check the response body is empty"):
        assert response_body == {}
