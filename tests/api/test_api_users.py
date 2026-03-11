import pytest
from playwright.sync_api import APIRequestContext
from utils.api_helpers import assert_has_keys

pytestmark = pytest.mark.api


def test_get_users_returns_200(api_context: APIRequestContext):
    response = api_context.get("/users")
    assert response.status == 200


def test_get_users_returns_a_list(api_context: APIRequestContext):
    response = api_context.get("/users")
    users = response.json()

    assert isinstance(users, list)
    assert len(users) > 0


def test_first_user_contains_expected_fields(api_context: APIRequestContext):
    response = api_context.get("/users")
    users = response.json()
    first_user = users[0]

    assert_has_keys(first_user, ["id", "name", "email"])


def test_first_user_email_looks_valid(api_context: APIRequestContext):
    response = api_context.get("/users")
    users = response.json()
    first_user = users[0]

    assert "@" in first_user["email"]