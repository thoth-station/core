# Changelog for the Sesheta's Bot Cohort


## [0.2.0] - 2018-04-19 - goern

### Added

**approve.py** now checks if all commits have successful CI status, CI context used is 'continuous-integration/jenkins/pr-merge'.

if 'needs-rebase' label is present, but GitHub thinks the PR is mergable, the label is removed.

'work-in-progress' label is a NOGO: the PR will be left alone.

**merge_pr.py** will merge any PR that has the 'approved' label, if one of 'needs-rebase' or 'work-in-progress' label is present, it will take precedence and no merge will happen.

**check_if_labels_present.py** will make sure that the labels we depend on are present.

**config.yaml** is selfexplanatory ;)