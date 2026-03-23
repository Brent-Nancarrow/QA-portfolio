# AI Output Review Checklist

This checklist is used to review AI-assisted outputs before they are accepted into QA work.

The purpose is to avoid false confidence from plausible-sounding but incomplete, incorrect or low-value content.

---

## 1. Requirement alignment

- [ ] Does the output actually match the requirement or story?
- [ ] Has the AI introduced assumptions that were never stated?
- [ ] Are any important acceptance criteria missing?
- [ ] Is the output relevant to the actual feature scope?

---

## 2. Business realism

- [ ] Do the suggested tests reflect realistic user behaviour?
- [ ] Are business-critical scenarios covered?
- [ ] Are there any irrelevant or over-theoretical cases?
- [ ] Does the output reflect likely production usage?

---

## 3. Risk and priority

- [ ] Are the highest-risk scenarios clearly identified?
- [ ] Are the suggestions prioritised sensibly?
- [ ] Has the AI missed obvious failure paths?
- [ ] Would this output help improve release confidence?

---

## 4. Technical accuracy

- [ ] Are terms used correctly?
- [ ] Are API, UI or data assumptions technically sound?
- [ ] Are any validations or expected results incorrect?
- [ ] Would a developer or analyst challenge any part of this output?

---

## 5. Test quality

- [ ] Are the tests clear and unambiguous?
- [ ] Are expected results specific enough?
- [ ] Are duplicate or low-value cases removed?
- [ ] Are negative and edge cases included where needed?

---

## 6. Data and coverage quality

- [ ] Are useful data variations covered?
- [ ] Are null, empty, invalid and boundary inputs considered?
- [ ] Are permissions or role-based scenarios needed?
- [ ] Are reporting/output validation scenarios needed?

---

## 7. Accessibility / usability / non-functional considerations

- [ ] Has accessibility been considered where relevant?
- [ ] Are error messages and user feedback covered?
- [ ] Is there any obvious performance, resilience or compatibility risk?
- [ ] Are stakeholder-visible outputs considered?

---

## 8. Final decision

- [ ] Accept as useful with minor edits
- [ ] Use partially and rewrite
- [ ] Reject because too generic / inaccurate / low value

---

## Core rule

**AI-generated output is draft material, not trusted evidence.**