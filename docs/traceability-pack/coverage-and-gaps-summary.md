# Coverage and Gaps Summary

This summary translates the traceability matrix into a more stakeholder-friendly view.

## Coverage currently demonstrated well

### 1. Core UI journey coverage
Current coverage demonstrates:
- login page availability
- successful login path
- locked-out user handling
- basic cart badge behaviour
- lightweight mobile viewport usability

### 2. API baseline coverage
Current coverage demonstrates:
- successful GET coverage
- simple structure/content validation
- negative 404 path coverage
- basic POST response validation
- simple email-format validation for returned user data

### 3. Reporting and data assurance coverage
Current coverage demonstrates:
- SQL-derived reconciliation against expected dashboard values
- basic data quality checks before trusting report outputs
- validation of exported dashboard/report content
- validation of the dashboard mock UI against expected values

---

## What is intentionally only partially covered

### UI partials
- no cross-browser comparison matrix beyond the configured Playwright project/browser setup
- no checkout journey coverage
- no session timeout, logout or security-focused UI checks
- no accessibility automation pack beyond the portfolio's broader mention of accessibility experience

### API partials
- no schema-contract tool such as OpenAPI contract validation
- no auth/authorisation coverage
- no rate-limit, retry or resilience coverage
- no deeper boundary-value coverage for payload validation

### Data/reporting partials
- no date-range filter logic coverage
- no drill-down or row-level reconciliation from UI to source records
- no failure-path coverage for malformed export files
- no versioned report comparison or trend analysis coverage

---

## Known gaps that should be described honestly in interviews

These are not weaknesses to hide. They are normal scope boundaries for a portfolio slice.

### Gap 1 — Traceability is sample-based
The current pack uses a deliberately small sample requirement set aligned to the existing portfolio.

That is appropriate for a portfolio, but in a real programme the matrix would usually be linked to:
- user stories
- acceptance criteria
- change requests
- defects
- test execution status
- release scope/version references

### Gap 2 — Evidence is execution-focused rather than release-managed
Evidence exists through:
- Allure steps and attachments
- Playwright failure artefacts
- SQL query/result attachments

In a production delivery environment, this would usually also link to:
- Jira/Xray or Azure DevOps test case IDs
- build/version identifiers
- environment references
- change/release records
- defect IDs and waiver decisions

### Gap 3 — Requirement coverage is functional-first
The current traceability is strongest for:
- functional UI flows
- basic API validation
- reporting/data assurance

It is lighter for:
- performance
- security
- accessibility evidence packs
- operational readiness/non-functional assurance

---

## Recommended interpretation

A fair and commercially realistic way to describe the current state is:

> The portfolio includes a lightweight requirement-to-test mapping pack that shows how I would connect requirements, acceptance criteria, automated checks and reviewable evidence. It is intentionally small, but it demonstrates the traceability thinking used in real assurance work: making coverage visible, identifying gaps honestly, and linking test outcomes back to requirements rather than treating execution as an isolated activity.
