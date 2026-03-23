# Sample Requirements and Acceptance Criteria

This is a lightweight sample requirement set created specifically for portfolio traceability demonstration.

It is intentionally small and realistic enough to support requirement-to-test mapping without pretending to represent a full production backlog.

---

## UI requirements

### RQ-UI-001 — Login page availability
**Requirement**  
The login page should load successfully and present the core controls needed for a user to attempt sign-in.

**Acceptance criteria**
- AC-UI-001.1: The login page title is shown correctly
- AC-UI-001.2: The username field is visible
- AC-UI-001.3: The password field is visible
- AC-UI-001.4: The login button is visible and usable

### RQ-UI-002 — Valid user login
**Requirement**  
A valid standard user should be able to log in and reach the inventory page.

**Acceptance criteria**
- AC-UI-002.1: A standard user can submit valid credentials
- AC-UI-002.2: After login, the inventory page loads successfully
- AC-UI-002.3: At least one product is displayed on the inventory page

### RQ-UI-003 — Locked-out user handling
**Requirement**  
A locked-out user should be prevented from logging in and should see a clear error message.

**Acceptance criteria**
- AC-UI-003.1: A locked-out user cannot access the inventory page
- AC-UI-003.2: A meaningful locked-out error message is displayed

### RQ-UI-004 — Cart badge updates
**Requirement**  
The cart badge should reflect item add/remove activity for the selected product.

**Acceptance criteria**
- AC-UI-004.1: Adding the backpack shows a cart badge value of 1
- AC-UI-004.2: Removing the backpack hides the cart badge again

### RQ-UI-005 — Basic mobile usability
**Requirement**  
The login page should remain usable on a mobile-sized viewport.

**Acceptance criteria**
- AC-UI-005.1: Core login controls remain visible at mobile viewport size
- AC-UI-005.2: The page title still loads correctly on mobile viewport size

---

## API requirements

### RQ-API-001 — Posts endpoint availability
**Requirement**  
The posts endpoint should be reachable and return a successful response.

**Acceptance criteria**
- AC-API-001.1: `GET /posts` returns HTTP 200
- AC-API-001.2: `GET /posts` returns a non-empty list
- AC-API-001.3: A returned post contains the expected core fields

### RQ-API-002 — Missing post handling
**Requirement**  
Requesting a non-existent post should return the expected error response.

**Acceptance criteria**
- AC-API-002.1: `GET /posts/999999` returns HTTP 404
- AC-API-002.2: The response body is empty as expected for this test target

### RQ-API-003 — Post creation response
**Requirement**  
Creating a post should return the expected status and echo the submitted payload fields.

**Acceptance criteria**
- AC-API-003.1: `POST /posts` returns HTTP 201
- AC-API-003.2: The response echoes the submitted title/body/userId values

### RQ-API-004 — Users endpoint structure
**Requirement**  
The users endpoint should return a list of users with expected structure and usable email data.

**Acceptance criteria**
- AC-API-004.1: `GET /users` returns HTTP 200
- AC-API-004.2: `GET /users` returns a list
- AC-API-004.3: The first user contains expected fields
- AC-API-004.4: The first user email looks valid

---

## Data / reporting requirements

### RQ-DATA-001 — Dashboard totals align with source data
**Requirement**  
Dashboard totals should match the underlying SQLite source data.

**Acceptance criteria**
- AC-DATA-001.1: Total orders match source data
- AC-DATA-001.2: Completed orders match source data
- AC-DATA-001.3: Pending orders match source data
- AC-DATA-001.4: Cancelled orders match source data
- AC-DATA-001.5: Completed-order revenue matches source data

### RQ-DATA-002 — Order data quality checks
**Requirement**  
The local orders dataset should meet basic integrity expectations before being relied upon for reporting.

**Acceptance criteria**
- AC-DATA-002.1: Only valid order statuses are present
- AC-DATA-002.2: No duplicate order IDs exist
- AC-DATA-002.3: No negative order amounts exist

### RQ-DATA-003 — Dashboard export validation
**Requirement**  
The exported dashboard JSON should match SQL-derived figures and contain expected metadata.

**Acceptance criteria**
- AC-DATA-003.1: Exported dashboard metrics match SQL query results
- AC-DATA-003.2: The report name is present and correct
- AC-DATA-003.3: The intended audience/context field is present and correct
- AC-DATA-003.4: The data source field is present and correct
- AC-DATA-003.5: A metrics section is present

### RQ-DATA-004 — Dashboard mock display
**Requirement**  
The reporting dashboard mock should display the expected headline values.

**Acceptance criteria**
- AC-DATA-004.1: Dashboard title and metadata are visible
- AC-DATA-004.2: Total orders value is displayed correctly
- AC-DATA-004.3: Completed, pending and cancelled values are displayed correctly
- AC-DATA-004.4: Completed-order revenue is displayed correctly
