Feature: Naming Service

    Background: Test Environment
        Given I am using the TEST environement
    @wip
    Scenario: I query for solver image
        When I query the naming service for solver image
        Then I want will get at least the following results:
            | name          | image                                                           |
            | solver-26-job | docker-registry.default.svc:5000/thoth-test-core/solver-f26-job |
            | solver-27-job | docker-registry.default.svc:5000/thoth-test-core/solver-f27-job |

# TODO query for all analyzers

# TODO query for the default analyzer