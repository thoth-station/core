# Aggregating OpenSSF Scorecard metrics to compute software stack quality scores

* Status: proposed
* Date: 2022-August-1

Technical Story: Aggregate OpenSSF Scorecard metrics on a package release update to compute software stack quality scores.

## Context and Problem Statement

As part of advise output improvements mentioned in [](https://github.com/thoth-station/core/issues/434), we would like to aggregate Security Scorecards data on a new package release to provide software stack quality metrics with regards to the global quality of packages that can be found in Thoth's Database. These metrics would inform the user about the health of a project dependencies and provide a software stack score (on a 0-100 scale or A,B,C...) based on Scorecard data.

**Note:** The architecture diagram below supposes that the OSSF Scorecards dataset available on BigQuery will expose metrics by package release instead of repository head commit SHA as it is currently the case. However if this feature is not going to be implemented on the Scorecards project side, we will need to handle the head commit SHA to release association logic by ourselves and thus revisit the diagram to include appropriate calls to the GitHub API and additional computations.

The data aggregation and score computation logic would be implemented as follows:

* With each `package-releases-job` run, aggregate data about the latest package release and corresponding Scorecards data retrieved from BigQuery
* Update a new database table `package_scorecard_metrics` with columns for the package name and version and Scorecards Check (1 if the check passed, 0 otherwise). Eventually add a column for a global confidence computed from all Scorecards confidence for a project
* Schedule a job to compute a global package quality score from the previously aggregated data and store this score in the database
* Make this data available in prescriptions: update existing Scorecard prescriptions with the package version and create new prescriptions for other packages via `prescriptions-refresh-job`
* Implement the scoring logic available for relevant Thoth endpoints
* When a request is made to the relevant endpoint or a parameter is passed to ask for software stack scoring when computing an advise, output the computed metrics about the user's software stack quality

## Architectural diagram

![Scorecard metrics aggregation logic diagram](/images/Scorecards_metrics_ADR.png)
