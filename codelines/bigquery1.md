
# Machine Learning with BigQuery

## Introduction to BigQuery ML

_[Video source](https://www.youtube.com/watch?v=B-WtpB0PuG4&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=29)_

***BigQuery ML*** is a BQ feature which allows us to create and execute Machine Learning models using standard SQL queries, without additional knowledge of Python nor any other programming languages and without the need to export data into a different system.

The pricing for BigQuery ML is slightly different and more complex than regular BigQuery. Some resources are free of charge up to a specific limit as part of the [Google Cloud Free Tier](https://cloud.google.com/free). You may check the current pricing [in this link](https://cloud.google.com/bigquery-ml/pricing).

BQ ML offers a variety of ML models depending on the use case, as the image below shows:

![image](https://user-images.githubusercontent.com/19702456/218378512-8c8c3242-155a-4159-8291-c0aa15a9b9bf.png)

We will now create a few example queries to show how BQ ML works. Let's begin with creating a custom table:

```sql
CREATE OR REPLACE TABLE `taxi-rides-ny.nytaxi.yellow_tripdata_ml` (
  `passenger_count` INTEGER,
  `trip_distance` FLOAT64,
  `PULocationID` STRING,
  `DOLocationID` STRING,
  `payment_type` STRING,
  `fare_amount` FLOAT64,
  `tolls_amount` FLOAT64,
  `tip_amount` FLOAT64
) AS (
  SELECT passenger_count, trip_distance, CAST(PULocationID AS STRING), CAST(DOLocationID AS STRING), CAST(payment_type AS STRING), fare_amount, tolls_amount, tip_amount
  FROM `taxi-rides-ny.nytaxi.yellow_tripdata_partitoned`
  WHERE fare_amount != 0
);
```
* BQ supports [***feature preprocessing***](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-preprocess-overview), both ***manual*** and ***automatic***.
* A few columns such as `PULocationID` are categorical in nature but are represented with integer numbers in the original table. We ***cast*** them as strings in order to get BQ to automatically preprocess them as categorical features that will be one-hot encoded.
* Our target feature for the model will be `tip_amount`. We drop all records where `tip_amount` equals zero in order to improve training.

Let's now create a simple linear regression model with default settings:

```sql
CREATE OR REPLACE MODEL `taxi-rides-ny.nytaxi.tip_model`
OPTIONS (
  model_type='linear_reg',
  input_label_cols=['tip_amount'],
  DATA_SPLIT_METHOD='AUTO_SPLIT'
) AS
SELECT
  *
FROM
  `taxi-rides-ny.nytaxi.yellow_tripdata_ml`
WHERE
  tip_amount IS NOT NULL;
```
* The `CREATE MODEL` clause will create the `taxi-rides-ny.nytaxi.tip_model` model
* The `OPTIONS()` clause contains all of the necessary arguments to create our model/
  * `model_type='linear_reg'` is for specifying that we will create a linear regression model.
  * `input_label_cols=['tip_amount']` lets BQ know that our target feature is `tip_amount`. For linear regression models, target features must be real numbers.
  * `DATA_SPLIT_METHOD='AUTO_SPLIT'` is for automatically splitting the dataset into train/test datasets.
* The `SELECT` statement indicates which features need to be considered for training the model.
  * Since we already created a dedicated table with all of the needed features, we simply select them all.
* Running this query may take several minutes.
* After the query runs successfully, the BQ explorer in the side panel will show all available models (just one in our case) with a special icon. Selecting a model will open a new tab with additional info such as model details, training graphs and evaluation metrics.

We can also get a description of the features with the following query:

```sql
SELECT * FROM ML.FEATURE_INFO(MODEL `taxi-rides-ny.nytaxi.tip_model`);
```
* The output will be similar to `describe()` in Pandas.

Model evaluation against a separate dataset is as follows:

```sql
SELECT
  *
FROM
ML.EVALUATE(
  MODEL `taxi-rides-ny.nytaxi.tip_model`, (
    SELECT
      *
    FROM
      `taxi-rides-ny.nytaxi.yellow_tripdata_ml`
    WHERE
      tip_amount IS NOT NULL
  )
);
```
* This will output similar metrics to those shown in the model info tab but with the updated values for the evaluation against the provided dataset.
* In this example we evaluate with the same dataset we used for training the model, so this is a silly example for illustration purposes.

The main purpose of a ML model is to make predictions. A `ML.PREDICT` statement is used for doing them:
```sql
SELECT
  *
FROM
ML.PREDICT(
  MODEL `taxi-rides-ny.nytaxi.tip_model`, (
    SELECT
      *
    FROM
      `taxi-rides-ny.nytaxi.yellow_tripdata_ml`
    WHERE
      tip_amount IS NOT NULL
  )
);
```
* The `SELECT` statement within `ML.PREDICT` provides the records for which we want to make predictions.
* Once again, we're using the same dataset we used for training to calculate predictions, so we already know the actual tips for the trips, but this is just an example.

Additionally, BQ ML has a special `ML.EXPLAIN_PREDICT` statement that will return the prediction along with the most important features that were involved in calculating the prediction for each of the records we want predicted.
```sql
SELECT
  *
FROM
ML.EXPLAIN_PREDICT(
  MODEL `taxi-rides-ny.nytaxi.tip_model`,(
    SELECT
      *
    FROM
      `taxi-rides-ny.nytaxi.yellow_tripdata_ml`
    WHERE
      tip_amount IS NOT NULL
  ), STRUCT(3 as top_k_features)
);
```
* This will return a similar output to the previous query but for each prediction, 3 additional rows will be provided with the most significant features along with the assigned weights for each feature.

Just like in regular ML models, BQ ML models can be improved with ***hyperparameter tuning***. Here's an example query for tuning:
```sql
CREATE OR REPLACE MODEL `taxi-rides-ny.nytaxi.tip_hyperparam_model`
OPTIONS (
  model_type='linear_reg',
  input_label_cols=['tip_amount'],
  DATA_SPLIT_METHOD='AUTO_SPLIT',
  num_trials=5,
  max_parallel_trials=2,
  l1_reg=hparam_range(0, 20),
  l2_reg=hparam_candidates([0, 0.1, 1, 10])
) AS
SELECT
*
FROM
`taxi-rides-ny.nytaxi.yellow_tripdata_ml`
WHERE
tip_amount IS NOT NULL;
```
* We create a new model as normal but we add the `num_trials` option as an argument.
* All of the regular arguments used for creating a model are available for tuning. In this example we opt to tune the L1 and L2 regularizations.

All of the necessary reference documentation is available [in this link](https://cloud.google.com/bigquery-ml/docs/reference).

_[Back to the top](#table-of-contents)_

## BigQuery ML deployment

_[Video source](https://www.youtube.com/watch?v=BjARzEWaznU&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=30)_

ML models created within BQ can be exported and deployed to Docker containers running TensorFlow Serving.

The following steps are based on [this official tutorial](https://cloud.google.com/bigquery-ml/docs/export-model-tutorial). All of these commands are to be run from a terminal and the gcloud sdk must be installed.

1. Authenticate to your GCP project.
    ```sh
    gcloud auth login
    ```
1. Export the model to a Cloud Storage bucket.
    ```sh
    bq --project_id taxi-rides-ny extract -m nytaxi.tip_model gs://taxi_ml_model/tip_model
    ```
1. Download the exported model files to a temporary directory.
    ```sh
    mkdir /tmp/model

    gsutil cp -r gs://taxi_ml_model/tip_model /tmp/model
    ```
1. Create a version subdirectory
    ```sh
    mkdir -p serving_dir/tip_model/1

    cp -r /tmp/model/tip_model/* serving_dir/tip_model/1

    # Optionally you may erase the temporary directoy
    rm -r /tmp/model
    ```
1. Pull the TensorFlow Serving Docker image
    ```sh
    docker pull tensorflow/serving
    ```
1. Run the Docker image. Mount the version subdirectory as a volume and provide a value for the `MODEL_NAME` environment variable.
    ```sh
    # Make sure you don't mess up the spaces!
    docker run \
      -p 8501:8501 \
      --mount type=bind,source=`pwd`/serving_dir/tip_model,target=/models/tip_model \
      -e MODEL_NAME=tip_model \
      -t tensorflow/serving &
    ```
1. With the image running, run a prediction with curl, providing values for the features used for the predictions.
    ```sh
    curl \
      -d '{"instances": [{"passenger_count":1, "trip_distance":12.2, "PULocationID":"193", "DOLocationID":"264", "payment_type":"2","fare_amount":20.4,"tolls_amount":0.0}]}' \
      -X POST http://localhost:8501/v1/models/tip_model:predict
    ```

_[Back to the top](#table-of-contents)_

# Integrating BigQuery with Airflow

We will now use Airflow to automate the creation of BQ tables, both normal and partitioned, from the files we stored in our Data Lake [in lesson 2](2_data_ingestion.md#airflow-in-action).

## Airflow setup

You may use the same working directory we used for Lesson 2 or you may create a new one for this lesson. In that case, make sure you have the following components:
* The `docker-compose.yaml` file for deploying Airflow.
  * You may use either the [default YAML file](2_data_ingestion#setup-full-version) or the [no-frills file](2_data_ingestion#setup-lite-version).
* The `.env` file with the `AIRFLOW_UID` and any additional environment variables you may need.
* The `dags`, `logs` and `plugins` folders.
* The `Dockerfile` for creating a custom Airflow image with the gcloud sdk.
* Optionally, you may include a `scripts` folder and place within an `entrypoint.sh` bash script in order to customize the intialization of Airflow. You may download an example script [from this link](https://github.com/DataTalksClub/data-engineering-zoomcamp/raw/main/week_3_data_warehouse/airflow/scripts/entrypoint.sh). You may learn more aboutthe Airflow entrypoint [in the official docs](https://airflow.apache.org/docs/docker-stack/entrypoint.html).

You may now deploy Airflow [with Docker-compose](2_data_ingestion.md#execution).

## Creating a Cloud Storage to BigQuery DAG

We will now create a new DAG inside the `dags` folder. In this example we will call it `gcs_2_bq_dag.py`.

1. Based on [the original DAG file we used in lesson 2](../2_data_ingestion/airflow/dags/data_ingestion_gcs_dag.py), we will copy the necessary imports and additional code.
    * We won't be using `BashOperator` nor `PythonOperator` because we will use the official Google-provided operators. We won't use PyArrow either because we will only deal with the files in our Data Lake.
    * Add the `default_args` dict and the DAG declaration.
    * Copy the `BigQueryCreateExternalTableOperator` block.
1. Define the task dependencies at the end of the DAG. We will use the following structure:
    ```python
    gcs_2_gcs >> gcs_2_bq_ext >> bq_ext_2_part
    ```
    * The DAG will contain 3 tasks: reorganizing the files within the Data Lake for easier processing, creating the external tables based on the Data Lake files, and creatng a partitioned table from the external tables.
1. Modify the imports slightly to import the corret operators we will use:
    ```python
    from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateExternalTableOperator, BigQueryInsertJobOperator
    from airflow.providers.google.cloud.transfers.gcs_to_gcs import GCStoGCSOperator
    ```
    * We already used the `BigQueryCreateExternalTableOperator` in the previous lesson. We also import `BigQueryInsertJobOperator` in order to be able to create partitioned tables.
    * `GCStoGCSOperator` is used to organize the files within the Data Lake.
1. Parametrize the filenames so that we can loop through all of the filenames. Wrap all tasks within the DAG in a `for` loop and loop through the taxi types.
1. Create the `gcs_2_gcs` task.
    * Use the `GCStoGCSOperator` operator. [Link to the official documentation](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/transfers/gcs_to_gcs/index.html).
    * We want to ***move*** multiple files. We will need to define the source bucket and objects as well as the destination bucket and objects.
        * Both the source and destination buckets will be the same bucket we defined in lesson 2.
        * Use f strings to change the source and destination object names on each loop.
        * You may use the wildcard `*` in the source object filename, but be aware that _every character **before** the wildcard_ will be removed from the destination object filename.
        * The destination object filename can be thought of as the prefix to be added to the source object filename.
1. Create the `gcs_2_bq_ext` task.
    * Modify the `BigQueryCreateExternalTableOperator` block. [Link to the official documentation](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/bigquery/index.html#airflow.providers.google.cloud.operators.bigquery.BigQueryCreateExternalTableOperator).
    * The original code block let BQ decide the schema of the external table by infering from the input file with the `externalDataConfiguration` dict. It's possible to provide a schema if you know it beforehand; check the documentation for more info.
    * Other than the `task_id`, this task is essentially the same code as last session's.
1. Create the `bq_ext_2_part` task.
    * Use the `BigQueryInsertJobOperator` operator. [Link to the official documentation](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/bigquery/index.html#airflow.providers.google.cloud.operators.bigquery.BigQueryInsertJobOperator).
    * The operator needs a dict for the `configuration` parameter which needs to contain a SQL query. We will use a very similar query to the one we used in the [partitions section](#partitions) to create a table.

The finalized `gcs_2_bq_dag.py` can be downloaded [from this link](../3_data_warehouse/airflow/dags/gcs_2_bq_dag.py).

>Previous: [Data Ingestion](2_data_ingestion.md)

>[Back to index](README.md)

>Next: [Analytics Engineering](4_analytics.md)
