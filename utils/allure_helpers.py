import json

import allure
from allure_commons.types import AttachmentType


def attach_json(name: str, payload: dict | list) -> None:
    """Attach formatted JSON to the Allure report."""
    allure.attach(
        json.dumps(payload, indent=2),
        name=name,
        attachment_type=AttachmentType.JSON,
    )


def attach_text(name: str, value: str) -> None:
    """Attach plain text to the Allure report."""
    allure.attach(value, name=name, attachment_type=AttachmentType.TEXT)
