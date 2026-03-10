from playwright.sync_api import Playwright, APIRequestContext, expect


def test_get_posts_returns_200(playwright: Playwright) -> None:
    api_context: APIRequestContext = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )

    response = api_context.get("/posts")

    assert response.status == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

    api_context.dispose()


def test_get_single_post_has_expected_fields(playwright: Playwright) -> None:
    api_context: APIRequestContext = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )

    response = api_context.get("/posts/1")

    assert response.status == 200

    data = response.json()
    assert data["id"] == 1
    assert "userId" in data
    assert "title" in data
    assert "body" in data

    api_context.dispose()


def test_get_missing_post_returns_404(playwright: Playwright) -> None:
    api_context: APIRequestContext = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )

    response = api_context.get("/posts/999999")

    assert response.status == 404

    api_context.dispose()