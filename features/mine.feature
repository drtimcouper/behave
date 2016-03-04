
Feature: Validate the static elements on mine.html

    A basic test to ensure that static components
    exist appropriately

    Scenario: Check home page title is correct
        Given I am logged in
        When I go to the root page
        Then I see the title "Achtung Minen"
