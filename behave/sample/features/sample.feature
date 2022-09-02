Feature: Show sample behave project struct

  Scenario: Run single scenario
    Given fetch data from "https://google.com"
    Then response status code is 200

  Scenario: Run single scenario with failure
    Given fetch data from "https://google.com"
    Then response status code is 400