from __future__ import annotations

from functools import wraps
from typing import Callable

import allure


def traceability(*requirement_ids: str) -> Callable:
    """
    Lightweight decorator used to tag selected tests with requirement IDs.

    Why this helper exists:
    - keeps traceability tags readable in the test code
    - avoids repeating the same Allure label calls in every tagged test
    - stays intentionally lightweight for portfolio use

    In plain English, a decorator is a small wrapper that adds behaviour
    around a function without changing the test's main logic.
    """

    def decorator(test_func: Callable) -> Callable:
        @wraps(test_func)
        def wrapper(*args, **kwargs):
            for requirement_id in requirement_ids:
                allure.dynamic.label('requirement', requirement_id)
            return test_func(*args, **kwargs)

        return wrapper

    return decorator
