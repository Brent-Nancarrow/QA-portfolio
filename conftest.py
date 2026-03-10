import os
import pytest


@pytest.fixture(scope="session")
def browser_type_launch_args():
    is_ci = os.getenv("CI") == "true"

    return {
        "headless": is_ci,
        "slow_mo": 0 if is_ci else 500
    }