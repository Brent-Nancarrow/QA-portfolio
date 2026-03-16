import json
from pathlib import Path


def load_dashboard_export(json_path: Path) -> dict:
    """
    Load a dashboard/report export JSON file.

    In plain English:
    this reads the exported report values so tests can compare
    them with values calculated from the source data.
    """
    with open(json_path, "r", encoding="utf-8") as json_file:
        return json.load(json_file)