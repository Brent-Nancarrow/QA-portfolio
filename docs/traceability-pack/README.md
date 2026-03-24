# Traceability and Requirement-to-Test Mapping Pack

This pack shows how requirements, acceptance criteria, tests, execution evidence and residual gaps can be linked together in a simple but commercially realistic way.

The aim is to demonstrate **traceability thinking**, not bureaucracy for its own sake.

## What this pack demonstrates

- turning sample requirements into testable acceptance criteria
- mapping requirements to existing UI, API and data/report validation tests
- showing where evidence would come from during execution
- making coverage and gaps visible to stakeholders
- supporting release-readiness and assurance conversations with clearer coverage logic

## Why this matters

In many delivery environments, QA value is not only about running tests. It is also about answering questions such as:

- Which requirements are covered?
- Which tests support that claim?
- What evidence exists?
- What is only partially covered?
- What remains out of scope or still needs attention?

This pack is included to support my positioning as a **hands-on QA / Workstream Test Lead / assurance-led QA professional** who can connect requirements, test execution, evidence and release confidence.

## Files in this pack

- `sample-requirements-and-acceptance-criteria.md`  
  A lightweight example set of requirements aligned to the portfolio coverage

- `requirements-to-test-matrix.md`  
  A readable traceability matrix linking requirement IDs to tests and evidence

- `requirements-to-test-matrix.csv`  
  The same mapping in a simple spreadsheet-friendly format

- `coverage-and-gaps-summary.md`  
  A stakeholder-friendly summary of what is covered, partially covered and not covered

- `stakeholder-coverage-summary.md`  
  A short stakeholder-facing interpretation linked back to the matrix

## Portfolio relevance

This pack deliberately complements the existing:

- hands-on UI, API and data validation tests
- Allure execution evidence
- stakeholder-facing assurance pack
- AI-assisted but human-led QA workflow pack

Together, those pieces show not only how tests were written and run, but also how coverage can be explained and defended.


## Lightweight code-level traceability

A small number of representative tests also include lightweight requirement tags in code via `utils/traceability.py`.

This is intentionally selective. The goal is to show how requirement IDs can be reflected in automated checks without turning the portfolio into a heavy framework exercise.
