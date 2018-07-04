Feature: analyze Container Image

    Background: Test Environment
        Given I am using the TEST environement

    @wip
    Scenario Outline: Submitting a Container Image for analysis
        When I submit <a container image> to the User API for analysis by <analyzer image>
        Then I want to receive a analyzer Job ID
        And I wait for the analyzer Job to finish successful
        And the Analyzer Job Log should not be empty
        Then I query the Result API for the result of the latest analyzer
        And the list of analzer results should not be empty

        Examples: Container Image and analyzers
            | a container image | analyzer image               |
            | fedora:27         | fridex/thoth-package-extract |

    @wip
    Scenario: Query for currently available analyzer Results
        When I query the Result API for a list of analyzer results
        Then the list of results should not be empty
