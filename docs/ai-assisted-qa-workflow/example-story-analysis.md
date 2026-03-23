# Example Story Analysis

This example shows how AI might be used to support story-level QA analysis, followed by human review and refinement.

---

## Example feature

A reporting dashboard allows users to export order summary data as JSON.

### Acceptance criteria

- user can export dashboard summary data
- export contains total orders
- export contains completed revenue
- export contains status breakdown
- only authorised users can export
- export should not include duplicate order IDs

---

## Possible AI-assisted first draft

AI may help suggest:

### Positive scenarios
- export succeeds for authorised user
- export file contains expected summary fields
- export values match dashboard totals

### Negative scenarios
- export blocked for unauthorised user
- export fails gracefully if source data is missing
- export rejects malformed source data

### Edge cases
- zero orders
- all orders cancelled
- duplicate order IDs
- negative amount values
- unknown status values

### Questions raised
- should empty export still be allowed?
- what is the expected behaviour if one row is invalid?
- should partially corrupt data block the whole export?

---

## Human QA review added value

After review, a human tester may refine this by:

- removing generic or duplicate ideas
- prioritising business-critical scenarios first
- clarifying expected behaviour with stakeholders
- adding role-based access testing
- adding data reconciliation against SQL source queries
- deciding which scenarios belong in UI, API or data-layer checks

---

## Final selected focus areas

For this portfolio, the strongest selected checks would be:

- export values match SQL-derived totals
- export includes required summary fields
- duplicate order IDs are detected
- negative amounts are flagged
- valid statuses are enforced
- dashboard mock values align with exported figures

---

## Key learning

AI can help generate a starting point faster.

However, the human tester still decides:
- what matters most
- what is realistic
- what is risky
- what should actually be tested