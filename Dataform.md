# Dataform 

- Dataform is a service for data analysts to develop, test, version control, and schedule complex SQL workflows for data transformation in BigQuery.
- Dataform lets you perform the following data transformation actions:
  - Develop and execute SQL workflows for data transformation.
  - Collaborate with team members on SQL workflow development through Git.
  - Manage a large number of tables and their dependencies.
  - Declare source data and manage table dependencies.
  - View a visualization of the dependency tree of your SQL workflow.
  - Manage data with SQL code in a central repository.
  - Reuse code with JavaScript.
  - Test data correctness with quality tests on source and output tables.
  - Version control SQL code.
  - Document data tables inside SQL code.

- Dataform has the following known limitations:
  - Dataform in Google Cloud runs on a plain V8 runtime and does not support additional capabilities and modules provided by Node.js. 
  - git+https:// URLs for dependencies in package.json are not supported.
  - Manually running unit tests is not available.
  - Searching for file content in development workspaces is not available.
