@portfolio @ui @login @risk-based @RQ-UI-001 @RQ-UI-002 @RQ-UI-003
Feature: Sauce Demo login access

  As a QA and delivery stakeholder
  I want login outcomes described in clear business-readable language
  So that access behaviour can be reviewed against expected user outcomes

  Background:
    Given the Sauce Demo login page is available

  @smoke @positive
  Scenario: Standard user can access the inventory page
    When the standard user signs in with valid credentials
    Then the inventory page should be displayed
    And available products should be visible

  @negative @access-control
  Scenario: Locked-out user receives a controlled error
    When the locked-out user signs in with valid credentials
    Then the user should remain on the login page
    And a locked-out user error message should be displayed
