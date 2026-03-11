from playwright.sync_api import APIRequestContext


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

    assert "id" in first_user
    assert "name" in first_user
    assert "email" in first_user


def test_first_user_email_looks_valid(api_context: APIRequestContext):
    response = api_context.get("/users")
    users = response.json()
    first_user = users[0]

    assert "@" in first_user["email"]