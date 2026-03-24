# Stakeholder Coverage Summary Linked to the Traceability Matrix

This short summary translates the detailed requirement-to-test matrix into a stakeholder-facing view.

It is designed to answer a simple assurance question:

> Based on the current mapped coverage, what looks well covered, what has lighter coverage, and what should a stakeholder still treat as residual risk?

## Linked source

This summary should be read alongside:

- `requirements-to-test-matrix.md`
- `requirements-to-test-matrix.csv`
- `coverage-and-gaps-summary.md`

## Coverage position at a glance

| Area | Coverage position | Linked requirement IDs | Evidence style |
|---|---|---|---|
| UI login smoke and core access | Good for portfolio scope | RQ-UI-001, RQ-UI-002, RQ-UI-003 | Playwright execution evidence, Allure steps, failure screenshots when relevant |
| API baseline behaviour | Good for portfolio scope | RQ-API-001, RQ-API-002, RQ-API-003, RQ-API-004 | HTTP status checks, body/content checks, attached JSON evidence |
| Data and reporting assurance | Strongest area in the portfolio | RQ-DATA-001, RQ-DATA-002, RQ-DATA-003, RQ-DATA-004 | SQL query evidence, expected-vs-actual comparisons, dashboard output checks |
| Broader non-functional coverage | Limited / intentionally light | Not fully modelled in current matrix | Not a current focus of this portfolio slice |

## Stakeholder interpretation

### What currently gives the strongest confidence

The strongest confidence sits in the **data and reporting slice** because the portfolio does not only check surface-level UI display.
It also links:

- source data checks
- expected dashboard values
- exported report validation
- visible dashboard output checks

That makes this the clearest example of **requirement -> test -> evidence -> confidence**.

### What is covered well enough for a portfolio demonstration

The UI and API layers provide a solid, commercially believable sample of:

- smoke coverage
- positive and negative checks
- response/content validation
- basic output assurance

This is enough to demonstrate coverage thinking without pretending the project is a full enterprise regression pack.

### What should still be treated as residual risk

A stakeholder should still assume that the following are either partial or out of scope in the current portfolio:

- deeper accessibility coverage
- cross-browser/device breadth beyond the current lightweight slice
- security-focused validation
- performance or load coverage
- broader end-to-end integration dependencies

## Why the code-level tags were added

A small number of representative automated tests now include lightweight traceability tags in code.

This is useful because it shows that traceability is not only documented in a matrix. It can also be reflected directly in the automated checks that support requirement coverage.

The tagging is intentionally selective rather than exhaustive, to keep the project commercially realistic and maintainable.

## Example assurance statement

> Based on the current traceability matrix and the linked execution evidence, I would describe this portfolio slice as having good visible coverage across core UI, API and reporting scenarios, with the strongest confidence in the SQL-backed data/report validation layer. Residual risk remains in broader non-functional and wider integration areas, which are acknowledged rather than hidden.
