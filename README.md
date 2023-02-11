
Set environment variable to point to your downloaded GCP keys:
   ```shell
   export GOOGLE_APPLICATION_CREDENTIALS="<path/to/your/service-account-authkeys>.json"
   
   # Refresh token/session, and verify authentication
   gcloud auth application-default login
   
   OR, gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS
   ```


> Get project id: `gcloud info --format='value(config.project)'`

### Dataflow
> Enable/Disable service: `gcloud services enable/disable dataflow.googleapis.com --force`

### Dataproc
> To locate the default Cloud Storage bucket used by Dataproc: `gcloud dataproc clusters describe sparktodp --region=us-central1 --format=json | jq -r '.config.configBucket'`

### Bigquery
> Install bigquery api in notebook:  `! pip install google-cloud-bigquery==1.25.0 --use-feature=2020-resolver`

### IAM
 > roles associated with the account: `gcloud projects get-iam-policy $PROJECT --format='table(bindings.role)' --flatten="bindings[].members" --filter="bindings.members:$USER_EMAIL"`
 
 > Add the Dataflow Admin role to the user account: `gcloud projects add-iam-policy-binding $PROJECT --member=user:$USER_EMAIL --role=roles/dataflow.admin`
