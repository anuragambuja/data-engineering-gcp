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
- With Dataform, developers create and compile SQL workflows using SQL and JavaScript
  
- Dataform has the following known limitations:
  - Dataform in Google Cloud runs on a plain V8 runtime and does not support additional capabilities and modules provided by Node.js. 
  - git+https:// URLs for dependencies in package.json are not supported.
  - Manually running unit tests is not available.
  - Searching for file content in development workspaces is not available.

![image](https://github.com/user-attachments/assets/389afccc-bae7-4e87-8dd5-1b6fab71a6de)
- primary purpose of assertions in Dataform is to define data quality tests, ensuring data consistency and accuracy.
  
- Dataform provides two methods to manage dependencies:
  - implicit declaration: Implicit declaration is when you reference tables or views directly within your SQL using the ref() function. It is also possible to use the resolve() function to reference without creating a dependency.
    ```
    config {
      ...
    }
    SELECT ...
    FROM ${ref("customer_details")}
    ```
  - explicit declaration: Explicit declaration is when you list dependencies within a config block using the dependencies array.
    ```
    config {
      ...
      dependencies: ["customer_details"]
    }
    SELECT ...
    ```

![image](https://github.com/user-attachments/assets/f95cdf9e-f064-47fc-906c-ad565c49acf4)
