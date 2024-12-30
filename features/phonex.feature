Feature: Phonex phone number searching
  As a user of phonex
  I want to provide phone numbers with an international prefix (+ or 00)
  So that phonex will generate variants and open Google Dork searches

  @happy_path
  Scenario: User provides a valid phone number with '+' prefix
    Given I have the phone number "+491701234567"
    When I run phonex with this phone number
    Then it should generate multiple search variants
    And it should not show an error

  @no_prefix
  Scenario: User provides a number without prefix
    Given I have the phone number "1701234567"
    When I run phonex with this phone number
    Then it should reject the phone number
    And it should print an error that a prefix is required

  @invalid_number
  Scenario: User provides an invalid phone number
    Given I have the phone number "+123"
    When I run phonex with this phone number
    Then it should print an error that the phone number is invalid

  @double_zero
  Scenario: User provides a valid phone number with "00" prefix
    Given I have the phone number "00491701234567"
    When I run phonex with this phone number
    Then it should generate multiple search variants
    And it should not show an error

  @help_option
  Scenario: User requests help with '-h'
    Given I run phonex with the '-h' option
    Then it should print usage information

