Feature: Result API

As a container image maintainer,
I want to query Thoth for a stack analysis,
so that I get a complete dump of the stack including observations and recommendations.

    Scenario: Query for currently available Results
        Given I am using the TEST environement
        When I query the Result API for a list of analyser results
        Then the list of analyser results should not be empty

    Scenario: Get one of the for currently available Results
        Given I am using the TEST environement
        When I query the Result API for a list of analyser results
        And I get one of the results
        Then the analyser result should not be empty
        And the analyser should be "thoth-package-extract"
        And the analyser version should be "1.0.0"