## App Engine

```bash
# Initialize your SDK
$ gcloud init

# Deploy your code to App Engine 
$ gcloud app deploy

# stream logs of your application
$ gcloud app logs tail -s default

# view your application - will provide URL for the browser
$ gcloud app browse
```
```
cd default-service
gcloud app deploy
gcloud app services list
gcloud app versions list
gcloud app instances list
gcloud app deploy --versio
n=v2
gcloud app versions list
gcloud app browse
gcloud app deploy --version=v3 --no-promote
gcloud app browse --version v3
gcloud app services set-traffic splits=v3=.5,v2=.5
watch curl https://melodic-furnace-304906.uc.r.appspot.com/
gcloud app services set-traffic --splits=v3=.5,v2=.5 --split-by=random
 
cd ../my-first-service/
gcloud app deploy
gcloud app browse --service=my-first-service
 
gcloud app services list
gcloud app regions list
```
