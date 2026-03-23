# Test Scope and Risks

## Test scope included

The following areas are in scope within this portfolio:

### Functional UI scope
- authentication journey checks
- inventory page validation
- cart interaction feedback
- responsive viewport behaviour

### API scope
- endpoint availability
- status code validation
- response body checks
- response key validation
- simple negative path coverage

### Data / reporting scope
- SQL-backed validation against seeded reporting data
- total and revenue reconciliation
- export content validation
- status integrity checks
- duplicate and invalid-value detection

### Evidence / reporting scope
- failure artifacts
- Allure output
- CI execution visibility

---

## Out of scope

The following areas are intentionally out of scope for this public portfolio:

- performance testing
- load testing
- penetration/security testing
- browser matrix at scale
- complex service virtualisation
- enterprise-scale integration orchestration
- production-like release management controls

These exclusions are deliberate to keep the portfolio commercially credible without over-engineering it.

---

## Key risks considered

### 1. Functional regression risk
Basic user journeys may fail if login, inventory or cart behaviour changes unexpectedly.

### 2. API contract/content risk
API responses may change structure or content in ways that affect downstream consumers.

### 3. Reporting/data integrity risk
Dashboard or export outputs may not match source data, reducing business trust.

### 4. Stakeholder visibility risk
Without evidence capture and clear reporting, teams may struggle to understand true quality status.

---

## Residual risks

Residual risks remain in areas not covered by this portfolio, such as:

- non-functional performance behaviour
- security vulnerabilities
- full dependency-chain failures
- release coordination across multiple integrated systems

---

## QA interpretation

The portfolio shows how risk can be reduced through layered validation and evidence, while still being honest about what has not been covered.