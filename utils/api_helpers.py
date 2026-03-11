def assert_has_keys(response_object, expected_keys):
    for key in expected_keys:
        assert key in response_object, f"Expected key '{key}' was not found in response object"