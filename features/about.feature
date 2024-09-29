@after-feature
Feature: Example selenium test 2

    Scenario: Example CMS Test
        When I get the index page
        Then I should be on home

    Scenario: Console Log check
        Given I get the index page
        When I check the console logs
        Then there should be no severe console log errors
