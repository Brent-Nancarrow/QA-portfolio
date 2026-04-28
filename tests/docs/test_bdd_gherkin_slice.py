from pathlib import Path
import re

import pytest

pytestmark = pytest.mark.bdd

BASE_DIR = Path(__file__).resolve().parents[2]
BDD_DIR = BASE_DIR / "docs" / "bdd-gherkin-slice"
FEATURE_DIR = BDD_DIR / "features"

EXPECTED_FEATURE_FILES = [
    FEATURE_DIR / "login.feature",
    FEATURE_DIR / "reporting-dashboard.feature",
]

EXPECTED_AUTOMATION_REFERENCES = [
    "tests/ui/test_saucedemo_login.py::test_login_behaviour_by_user_type",
    "tests/ui/test_saucedemo_inventory.py::test_inventory_page_shows_products",
    "tests/data/test_orders_dashboard_sql.py::test_total_orders_matches_expected_dashboard_value",
    "tests/data/test_orders_dashboard_sql.py::test_completed_order_revenue_matches_expected_dashboard_value",
    "tests/data/test_dashboard_export_validation.py::test_dashboard_export_contains_expected_metadata",
    "tests/ui/test_reporting_dashboard_mock.py::test_reporting_dashboard_mock_displays_expected_values",
]


@pytest.mark.parametrize("feature_file", EXPECTED_FEATURE_FILES)
def test_bdd_feature_files_exist(feature_file: Path) -> None:
    assert feature_file.exists(), f"Missing BDD feature file: {feature_file}"


@pytest.mark.parametrize("feature_file", EXPECTED_FEATURE_FILES)
def test_bdd_feature_files_have_basic_gherkin_structure(feature_file: Path) -> None:
    """
    This is a lightweight documentation quality check.

    It does not execute the Gherkin scenarios. It confirms that the feature files
    keep the basic business-readable Given / When / Then structure expected from
    a BDD artefact.
    """
    feature_text = feature_file.read_text(encoding="utf-8")

    assert re.search(r"^Feature:", feature_text, re.MULTILINE)
    assert re.search(r"^\s*Scenario:", feature_text, re.MULTILINE)

    for keyword in ("Given", "When", "Then"):
        assert re.search(rf"^\s*{keyword}\b", feature_text, re.MULTILINE), (
            f"{feature_file.name} is missing a {keyword} step"
        )


@pytest.mark.parametrize("feature_file", EXPECTED_FEATURE_FILES)
def test_bdd_feature_files_include_traceability_tags(feature_file: Path) -> None:
    feature_text = feature_file.read_text(encoding="utf-8")

    requirement_tags = re.findall(r"@RQ-[A-Z]+-\d{3}", feature_text)

    assert requirement_tags, f"{feature_file.name} should include at least one requirement tag"


def test_bdd_mapping_references_existing_automation_checks() -> None:
    mapping_file = BDD_DIR / "bdd-to-automation-mapping.md"
    mapping_text = mapping_file.read_text(encoding="utf-8")

    for reference in EXPECTED_AUTOMATION_REFERENCES:
        test_file = BASE_DIR / reference.split("::")[0]
        assert test_file.exists(), f"Mapped test file does not exist: {test_file}"
        assert reference in mapping_text, f"Mapping is missing automation reference: {reference}"
