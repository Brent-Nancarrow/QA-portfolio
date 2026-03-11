import pytest
from playwright.sync_api import APIRequestContext
from utils.api_helpers import assert_has_keys

pytestmark = pytest.mark.api


def test_get_all_posts_returns_200(api_context: APIRequestContext):
    response = api_context.get("/posts")
    assert response.status == 200


def test_get_all_posts_returns_a_non_empty_list(api_context: APIRequestContext):
    response = api_context.get("/posts")
    posts = response.json()

    assert isinstance(posts, list)
    assert len(posts) > 0


def test_first_post_contains_expected_fields(api_context: APIRequestContext):
    response = api_context.get("/posts")
    posts = response.json()
    first_post = posts[0]

    assert_has_keys(first_post, ["userId", "id", "title", "body"])


def test_get_non_existent_post_returns_404(api_context: APIRequestContext):
    response = api_context.get("/posts/999999")
    response_body = response.json()

    assert response.status == 404
    assert response_body == {}