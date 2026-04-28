@portfolio @data @dashboard @reporting @RQ-DATA-001 @RQ-DATA-003 @RQ-DATA-004
Feature: Orders reporting dashboard assurance

  As a reporting stakeholder
  I want dashboard values to be checked against trusted source data
  So that business users can have confidence in reported totals and status breakdowns

  Background:
    Given the orders reporting dataset is available

  @data-validation @source-to-report
  Scenario: Dashboard totals align with source data
    When the dashboard totals are calculated from the orders dataset
    Then the total order count should match the expected dashboard value
    And the completed order revenue should match the expected dashboard value

  @output-assurance @metadata
  Scenario: Dashboard export includes expected reporting metadata
    When the dashboard export is reviewed
    Then the export should identify the reporting period
    And the export should identify the source system used for validation

  @ui-output-check
  Scenario: Dashboard mock displays stakeholder-visible values
    When the reporting dashboard mock is opened
    Then the dashboard title should be visible
    And the stakeholder-visible card totals should match the validated data values
