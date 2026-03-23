# Example Defect Investigation Workflow

This example shows where AI may help during defect investigation without replacing evidence-based QA judgement.

---

## Scenario

A dashboard export shows completed revenue that does not match the value displayed on the dashboard.

---

## Human-led investigation steps

1. reproduce the issue
2. capture screenshots and exported file
3. compare dashboard figures against source data
4. run SQL checks to calculate expected totals
5. identify whether the issue is:
   - data issue
   - transformation issue
   - display issue
   - permissions/scope issue
6. raise a defect with evidence

---

## Where AI may assist

AI may help with:

- summarising rough notes into a clearer defect description
- drafting clearer expected vs actual wording
- suggesting additional questions for triage
- helping rewrite a stakeholder update in plain English
- identifying possible root-cause categories to investigate

---

## Where AI should not be trusted blindly

AI should not decide:

- whether the defect is valid without evidence
- whether the dashboard or SQL source is correct
- whether the defect severity is appropriate without context
- whether the release is safe

---

## Practical principle

AI can assist communication and idea generation.

Evidence, validation and release confidence decisions remain human responsibilities.