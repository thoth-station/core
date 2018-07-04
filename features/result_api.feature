Feature: Result API

As a container image maintainer,
I want to query Thoth for a stack analysis,
so that I get a complete dump of the stack including observations and recommendations.

    Scenario: Query for currently available analyzer Results
        Given I am using the TEST environement
        When I query the Result API for a list of analyzer results
        Then the list of results should not be empty

    Scenario: Get one of the for currently available analyzer Results
        Given I am using the TEST environement
        When I query the Result API for a list of analyzer results
        And I get one of the analyzer results
        Then the result should not be empty
        And the analyzer should be "thoth-package-extract"
        And the analyzer version should not be empty

    Scenario: Query for currently available Solver Results
        Given I am using the TEST environement
        When I query the Solver API for a list of solver results
        Then the list of results should not be empty

    Scenario: Get one of the for currently available Solver Results
        Given I am using the TEST environement
        When I query the Solver API for a list of solver results
        And I get one of the solver results
        Then the result should not be empty
        And the solver should be "thoth-solver"
        And the solver version should not be empty
