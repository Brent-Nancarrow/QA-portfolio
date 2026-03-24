import allure
import pytest
from playwright.sync_api import APIRequestContext

from utils.allure_helpers import attach_json
from utils.api_helpers import assert_has_keys
from utils.traceability import traceability

pytestmark = pytest.mark.api


@traceability("RQ-API-004")
@allure.feature("JSONPlaceholder API")
@allure.story("Users")
@allure.title("Get users returns HTTP 200")
def test_get_users_returns_200(api_context: APIRequestContext):
    with allure.step("Record the linked requirement for this users endpoint availability check"):
        allure.attach(
            "Requirement: RQ-API-004 - Users endpoint structure",
            name="traceability-reference",
            attachment_type=allure.attachment_type.TEXT,
        )

    with allure.step("Send GET /users"):
        response = api_context.get("/users")

    with allure.step("Check the response status is 200"):
        assert response.status == 200


@traceability("RQ-API-004")
@allure.feature("JSONPlaceholder API")
@allure.story("Users")
@allure.title("Get users returns a non-empty list")
def test_get_users_returns_a_list(api_context: APIRequestContext):
    with allure.step("Record the linked requirement for this users list check"):
        allure.attach(
            "Requirement: RQ-API-004 - Users endpoint structure",
            name="traceability-reference",
            attachment_type=allure.attachment_type.TEXT,
        )

    with allure.step("Send GET /users"):
        response = api_context.get("/users")
        users = response.json()
        attach_json("users-response", users[:3])

    with allure.step("Check the response is a non-empty list"):
        assert isinstance(users, list)
        assert len(users) > 0


@traceability("RQ-API-004")
@allure.feature("JSONPlaceholder API")
@allure.story("Users")
@allure.title("First user contains the expected fields")
def test_first_user_contains_expected_fields(api_context: APIRequestContext):
    with allure.step("Record the linked requirement for this users structure check"):
        allure.attach(
            "Requirement: RQ-API-004 - Users endpoint structure",
            name="traceability-reference",
            attachment_type=allure.attachment_type.TEXT,
        )

    with allure.step("Send GET /users"):
        response = api_context.get("/users")
        users = response.json()
        first_user = users[0]
        attach_json("first-user", first_user)

    with allure.step("Check the first user contains the expected keys"):
        assert_has_keys(first_user, ["id", "name", "email"])


@traceability("RQ-API-004")
@allure.feature("JSONPlaceholder API")
@allure.story("Users")
@allure.title("First user email contains an @ symbol")
def test_first_user_email_looks_valid(api_context: APIRequestContext):
    with allure.step("Record the linked requirement for this users email check"):
        allure.attach(
            "Requirement: RQ-API-004 - Users endpoint structure",
            name="traceability-reference",
            attachment_type=allure.attachment_type.TEXT,
        )

    with allure.step("Send GET /users"):
        response = api_context.get("/users")
        users = response.json()
        first_user = users[0]
        attach_json("first-user-email-check", first_user)

    with allure.step("Check the first user email looks valid"):
        assert "@" in first_user["email"]