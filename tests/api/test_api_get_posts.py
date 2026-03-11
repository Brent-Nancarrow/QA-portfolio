from playwright.sync_api import APIRequestContext


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

    assert "userId" in first_post
    assert "id" in first_post
    assert "title" in first_post
    assert "body" in first_post


def test_get_non_existent_post_returns_404(api_context: APIRequestContext):
    response = api_context.get("/posts/999999")
    response_body = response.json()

    assert response.status == 404
    assert response_body == {}