# AI Test Design Prompt Pack

This file contains example prompt patterns for using Generative AI in a QA workflow.

These are not intended to be trusted blindly. They are starting points to accelerate thinking, which must still be reviewed by the tester.

---

## 1. User story to test ideas

### Example prompt

You are assisting a senior QA analyst.

Review the following user story and acceptance criteria. Generate:
1. positive test scenarios
2. negative test scenarios
3. edge cases
4. data validation considerations
5. usability or accessibility considerations
6. questions or ambiguities that should be clarified before release

User story:
[insert story here]

Acceptance criteria:
[insert acceptance criteria here]

Return the output in a clear test-design format suitable for review by a human tester.

---

## 2. Exploratory testing charter support

### Example prompt

Act as an experienced QA test analyst.

Based on the feature below, propose an exploratory testing charter that includes:
- objective
- areas of focus
- likely risks
- suggested test ideas
- useful data variations
- possible failure patterns

Feature:
[insert feature description here]

Keep the output practical and realistic for a time-boxed exploratory session.

---

## 3. API test idea support

### Example prompt

Review the API details below and suggest practical QA test scenarios.

Include:
- happy path scenarios
- validation failures
- authentication/authorisation concerns
- boundary conditions
- missing-field scenarios
- invalid data format scenarios
- response structure checks

API details:
[insert endpoint, request, response, rules]

---

## 4. Requirement gap analysis

### Example prompt

Review the requirement below and identify:
- missing assumptions
- unclear business rules
- ambiguous wording
- possible edge cases
- dependency risks
- testability concerns

Requirement:
[insert requirement]

Return the output as a QA review checklist.

---

## 5. Defect write-up support

### Example prompt

Rewrite the following rough defect notes into a clearer defect report with:
- summary
- steps to reproduce
- actual result
- expected result
- risk / impact
- suggested evidence to attach

Rough notes:
[insert notes here]

Keep the wording factual and concise.

---

## Important usage note

These prompts are intended to support a tester's thinking, not replace it.

Before using any AI-generated test ideas:
- remove duplicates
- remove weak or generic cases
- check business realism
- confirm requirement alignment
- prioritise based on risk
- verify technical correctness