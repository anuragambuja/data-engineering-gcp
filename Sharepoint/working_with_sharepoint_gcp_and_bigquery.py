# Import Libraries
import io
import logging as logger
import pandas as pd
from office365.sharepoint.files.file import File
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
# from office365.runtime.auth.client_credential import ClientCredential
from google.oauth2 import service_account
from google.cloud import storage
from google.cloud import bigquery

# Import configurations
from config import config


def sharepoint_auth(sharepoint_site, username, password):
    """
    Authorize sharepoint

    Return: Sharepoint connection object
    """
    # conn = ClientContext(sharepoint_site).with_credentials(ClientCredential('client_id','client_secret'))
    conn = ClientContext(sharepoint_site).with_credentials(UserCredential(username,password))
    logger.info("Sharepoint Connection Created.")
    return conn


def gcs_auth(sa_json):
    """
    Authorize gcs

    Return: GCS credential object
    """
    cred = service_account.Credentials.from_service_account_file(sa_json)
    logger.info("GCS Authorized.")
    return cred


def bq_auth(sa_json):
    """
    Authorize bigquery

    Return" bigquery client
    """
    client = bigquery.Client.from_service_account_json(json_credentials_path=sa_json)
    logger.info("Bigquery Client Created.")
    return client


def delete_gcs_file(project, bucket, directory, filename, cred):
    """
    Delete GCS file

    Return: deleted filename
    """
    filename = f"{directory}/{filename}"
    storage_client = storage.Client(project=project, credentials=cred)
    source_bucket = storage_client.bucket(bucket)
    blob = source_bucket.blob(filename)
    blob.delete()
    logger.info("Blob gs://%s/%s deleted.", bucket, filename)
    return filename


def delete_sharepoint_file(sharepoint_directory, filename, conn):
    """
    Delete sharepoint filename

    Return: deleted filename
    """
    file_url = f'/{sharepoint_directory}/{filename}'
    conn.web.get_file_by_server_relative_url(file_url).delete_object().execute_query()
    return filename


def download_from_sharepoint_as_file(sharepoint_directory, filename, conn):
    """
    Download file from sharepoint

    Return: downloaded filename
    """
    file_url = f'/{sharepoint_directory}/{filename}'
    file = File.open_binary(conn, file_url)
    with open(f"./{filename}", "wb") as fh:
        fh.write(file.content)
    logger.info("File %s downloaded from Sharepoint.", filename)
    return filename


def download_from_sharepoint_as_string(sharepoint_directory, filename, conn):
    """
    Read file from sharepoint

    Return: file content as string
    """
    file_url = f'/{sharepoint_directory}/{filename}'
    file = File.open_binary(conn, file_url)
    logger.info("File %s read from Sharepoint.", file_url)
    return file.content


def export_bq_table_to_gcs(client, project, dataset, table, destination):
    """
    Export Table to GCS as CSV

    Return: None
    """
    dataset_ref = bigquery.DatasetReference(project, dataset)
    table_ref = dataset_ref.table(table)
    extract_job = client.extract_table(
        table_ref,
        destination)
    extract_job.result()
    logger.info("Table Export Complete.")


def export_sql_as_bq_table(client, table, sql):
    """
    Export output to bigquery table

    Return: bigquery table name
    """
    job_config = bigquery.QueryJobConfig(allow_large_results=True, destination=table, use_legacy_sql=False, write_disposition="write_truncate")
    query_job = client.query(sql, job_config=job_config)
    query_job.result()
    logger.info("Output saved to table %s", table)
    return table


def read_gcs_file(project, bucket, directory, filename, cred):
    """
    Read the file from gcs

    Return: file content as string
    """
    filename = f"{directory}/{filename}"
    storage_client = storage.Client(project=project, credentials=cred)
    source_bucket = storage_client.bucket(bucket)
    blob = source_bucket.blob(filename)
    logger.info("File %s Read from GCS.", filename)
    return blob.download_as_string()


def string_to_pandas(data):
    """
    convert string content to pandas df

    Return: pandas dataframe
    """
    bytes_obj = io.BytesIO()
    bytes_obj.write(data)
    bytes_obj.seek(0)
    logger.info("Content converted to Pandas Dataframe")
    return pd.read_excel(bytes_obj)


def upload_to_sharepoint_from_string(sharepoint_directory, filename, conn, data):
    """
    Upload file to sharepoint

    Return: uploaded filename
    """
    conn.web.get_folder_by_server_relative_url(sharepoint_directory).upload_file(filename, data).execute_query()
    logger.info("File %s Uploaded.", filename)
    return filename


def upload_to_gcs_from_string(project, bucket, directory, filename, cred, data):
    """
    Upload file to GCS

    Return: Uploaded filename
    """
    filename = directory+"/"+filename
    storage_client = storage.Client(project=project, credentials=cred)
    source_bucket = storage_client.bucket(bucket)
    blob = source_bucket.blob(filename)
    df = string_to_pandas(data)
    blob.upload_from_string(df.to_csv(index=False, header=True), 'text/csv')
    logger.info("File %s successfully uploaded to GCS.", filename)
    return filename


def process():
    """
    1. copy xlsx from sharepoint to GCS as csv
    2. Read the CSV using bigqeury and join with exiting table to publish csv in GCS
    3. Copy the CSV from GCS to Sharepoint
    """
    logger.basicConfig(level=logger.INFO)
    # Sharepoint Credentials
    username = config["USERNAME"]
    password = config["PASSWORD"]
    sharepoint_site = config["SHAREPOINT_SITE"]
    sharepoint_directory = config["SHAREPOINT_DIRECTORY"]
    sharepoint_doc = config["SHAREPOINT_DOC"]

    # GCP Credentials
    sa_json = config["SA_JSON"]
    project = config["PROJECT"]
    gcs_bucket = config["GCS_BUCKET"]
    gcs_dir = config["GCS_DIR"]
    gcs_doc = config["GCS_DOC"]
    gcs_doc_ext = config["GCS_DOC_EXT"]
    bq_dataset = config["BQ_DATASET"]
    bq_table = config["BQ_TABLE"]
    sql = config["SQL"]
    dest_uri = config["DEST_URI"]
    tmp_table = config["TMP_TABLE"]

    # Create connections
    sp_conn = sharepoint_auth(sharepoint_site, username, password)
    gcs_cred = gcs_auth(sa_json)
    bq_client = bq_auth(sa_json)

    # 1. copy xlsx from sharepoint to GCS as csv
    sp_content = download_from_sharepoint_as_string(sharepoint_directory=sharepoint_directory, filename=sharepoint_doc, conn=sp_conn)
    upload_to_gcs_from_string(project=project, bucket=gcs_bucket, directory=gcs_dir, filename=gcs_doc_ext, cred=gcs_cred, data=sp_content)

    # 2. Read the CSV using bigquery and join with exiting table to publish csv in GCS
    export_sql_as_bq_table(client=bq_client, table=tmp_table, sql=sql)
    export_bq_table_to_gcs(client=bq_client, project=project, dataset=bq_dataset, table=bq_table, destination=dest_uri)

    # 3. Copy the CSV from GCS to Sharepoint as xlsx
    gcs_content = read_gcs_file(project=project, bucket=gcs_bucket, directory=gcs_dir, filename=gcs_doc, cred=gcs_cred)
    upload_to_sharepoint_from_string(sharepoint_directory=sharepoint_directory, filename=gcs_doc, conn=sp_conn, data=gcs_content)

    # Delete the GCS blob
    delete_gcs_file(project=project, bucket=gcs_bucket, directory=gcs_dir, filename=gcs_doc, cred=gcs_cred)
    delete_sharepoint_file(sharepoint_directory=sharepoint_directory, filename=sharepoint_doc, conn=sp_conn)


if __name__ == "__main__":
    process()
