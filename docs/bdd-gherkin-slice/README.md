# BDD / Gherkin Slice

This small slice shows how business-readable **BDD / Gherkin** scenarios can sit alongside automated tests, traceability and stakeholder assurance artefacts.

The aim is not to turn this portfolio into a full BDD automation framework. The aim is to show that requirements and acceptance criteria can be expressed clearly enough for QA, product, delivery and stakeholder review.

## Why this slice exists

BDD is useful when it helps teams agree what good looks like before or during testing.

In this portfolio, the Gherkin files help demonstrate:

- clear acceptance criteria written in plain English
- alignment between business behaviour and automated checks
- traceability back to existing requirement IDs
- stakeholder-readable test intent
- a lightweight approach that avoids unnecessary framework complexity

## What Gherkin means in plain English

**Gherkin** is a structured way of writing expected behaviour.

It normally uses:

- **Feature** = the business capability being described
- **Scenario** = one specific example of expected behaviour
- **Given** = the starting context
- **When** = the action or event
- **Then** = the expected outcome

Example:

```gherkin
Scenario: Standard user can access the inventory page
  Given the Sauce Demo login page is available
  When the standard user signs in with valid credentials
  Then the inventory page should be displayed
```

## Files included

| File | Purpose |
|---|---|
| `features/login.feature` | Business-readable login and access scenarios |
| `features/reporting-dashboard.feature` | Business-readable dashboard/reporting assurance scenarios |
| `bdd-to-automation-mapping.md` | Links Gherkin scenarios to existing automated tests and requirement IDs |

## How this is validated

The repository includes a small pytest check under:

- `tests/docs/test_bdd_gherkin_slice.py`

This test does **not** execute Gherkin as a full BDD framework. Instead, it checks that the BDD artefacts remain present, structured and traceable.

That choice is deliberate. It keeps this portfolio aligned to an assurance-led QA profile rather than adding a heavier automation framework purely for demonstration purposes.

## Future extension option

If this portfolio was extended later, these `.feature` files could be automated using a tool such as:

- `pytest-bdd`
- `behave`

For the current portfolio, the business-readable feature files and mapping are enough to demonstrate BDD thinking without adding avoidable maintenance overhead.
