# Vertex AI

- It's a fully managed service for custom machine learning models, both training and serving predictions.
- VertexAI (your model, your data), AutoML ( our model, your data)
- It can scale from the experimentation stage all the way to production.
- A simple ML pipeline might do the following.
  - Load a dataset from a comma-separated value file.
  - Analyze the dataset to identify and remove outliers.
  - Split the cleaned dataset into a training and evaluation dataset.
  - Train a model on the training dataset.
  - Evaluate the model against the evaluation dataset.
- Vertex AI provides a service called Vertex AI Feature Store, which is a centralized repository to manage, serve, and share features. It aggregates the features from different sources in BigQuery and makes them available for both real-time (often called online) and batch (often called offline) serving. benefits of Vertex AI Feature Store:
  - features are shareable for training and serving. They are managed and served from a central repository, maintaining consistency across your organization.
  - features are reusable. This helps to save time and reduces duplicated efforts.
  - features are scalable. They automatically scale to provide low-latency serving, so you can focus on developing the logic to create them without worrying about deployment.
  - features are easy to use.
 
 ![image](https://github.com/user-attachments/assets/30e743a5-b048-4608-a6b5-4424fd8d28ba)

- Kubeflow Pipelines is a Kubernetes-native, open source product, that has grown into the industry standard for running ML pipelines over the years.
  ![image](https://github.com/user-attachments/assets/4e907192-24eb-4e36-87d8-c122eea19f5a)
- Key Capabilities:
![image](https://github.com/user-attachments/assets/3d9e14b2-22a6-46e4-b2e2-303050fd3bdf)

- AI Hub is a repository for ML components.
- In Vertex AI, feature importance is displayed through a bar chart to illustrate how each feature contributes to a prediction. The longer the bar, or the larger the numerical value associated with a feature, the more important it is. This information helps decide which features are included in a machine learning model to predict the goal. Feature importance is just one example of Vertex AI’s comprehensive machine learning functionality called Explainable AI. Explainable AI is a set of tools and frameworks to help understand and interpret predictions made by machine learning models.

# AutoML
- The downside of using pre-trained models like Vision API, the Speech-to-Text API etc. is that they only yield good predictions when your data is relatively common-place, as in social media images or customer reviews. 
- Vertex AI AutoML sits somewhere inbetween these two. A model is trained specific to your data but you don’t need any code to train it.
- AutoML supports four types of data: image, tabular, text, and video.
- Phases of AutoML:
![image](https://github.com/user-attachments/assets/1d2535a7-bf57-423c-9445-245ba2adba17)

![image](https://github.com/user-attachments/assets/9ecbf871-998f-4bfb-a2f4-5e502403f145)

- Phases
  - Phase one is data processing. After you upload a dataset, AutoML provides functions to automate part of the data preparation process. For example, it can covert numbers, datetime, text, categories, arrays of categories, and nested fields into a certain format of data so that it can be fed into an ML model.
  - Phase two includes searching the best models and tuning the parameters. Two critical technologies support this auto search.
    - neural architect search: which helps search the best models and tune the parameters automatically. The goal of neural architecture search is to find optimal models among many options.
    - transfer learning: Transfer learning is a powerful technique that lets people with smaller datasets or less computational power achieve great results by using pre-trained models trained on similar, larger datasets.
  - In phase three, the best models are assembled from phase 2 and prepared for prediction in phase 4. Note that AutoML does not rely on one single model, but on the top number of models. The number of models depends on the training budget, but is typically around 10.

- AutoML Vision specializes in training models for image classification.
  - Training supports several file formats including JPEG, GIF, PNG, BMP, and ICO.
  - The images can be up to 30 megabytes in size.
  - Prediction supports the following file formats up to 1.5 megabytes in size: JPEG, GIF, PNG, WEBP, BMP, TIFF, and ICO.
  - the Vertex AI API currently only supports sending base64-encoded image content to the predict method.
    
- AutoML Natural Language specializes in training models for text data.
  - Currently the documents must be standard text, and do not support Unico
  - The documents can be as small as one sentence or up to a maximum of 128 kilobytes.
  - You can have from two to 100 labels.
  - The custom model is evaluated on average precision. That is a value from 0.5 to 1.0. Its formal name is the area under the precision recall curve. A higher number indicates more accurate classification and prediction.
  - If a natural language custom model is not used for 60 days, it will be deleted. If a natural language custom model is being used, it will be deleted after 6 months. To reserve a model, you'll be required to retrain it.
  - High confusion and low average precision scores indicate that a prepared data set needs additional entries or that the labels are being used inconsistently.
 
- AutoML Tables for tabular data. Tabular data is what you might find in a spreadsheet for example.
  - The development of AutoML Table was a collaboration between Google Cloud and the Google Brain Team.
  - your data must have between 1,000 and 100 million rows, between two and 1,000 columns, and be 100 gigabytes or less in size.
  - You can make batch predictions on either BigQuery Tables or CSV files. However, the BigQuery data source tables must be no larger than 100 gigabytes. For CSV files, each data source file can be no larger than 10 gigabytes. And if you include multiple files, the sum of all files cannot exceed 100 gigabytes.

- To improve AutoML Vision and AutoML Natural Language models
  - Increase the diversity and complexity of data
  - Increase the amount of training data
  - Ensure consistent labeling
  
- How to choose ebtween Bigquery ML, AutoML abd a custom Model
![image](https://github.com/user-attachments/assets/f549910a-601c-4480-9cdb-280a9be174e9)


## Model Deployment
- You have two primary options:
  - Endpoint:
    -  Deploy the model to an endpoint for real-time predictions (or often called online predictions).
    -  This option is best when immediate results with low latency are needed, such as making instant recommendations based on a user’s browsing habits whenever they’re online.
  - Batch prediction:
    - This option is best when no immediate response is required. For example, sending out marketing campaigns every other week based on the user’s recent purchasing behavior and what’s currently popular on the market.
    - Batch prediction does not require deploying the model to an endpoint. You can deploy a model either using the UI on Vertex AI or using code by calling APIs.
- Vertex AI Pipelines
  - It automates, monitors, and governs machine learning systems by orchestrating the workflow in a serverless manner.
  - With Vertex AI Workbench, which is a notebook tool, you can define your own pipeline using SDKs. You can do this with prebuilt pipeline components, which means that you primarily need to specify how the pipeline is put together using components as building blocks.
- MLOps
  ![image](https://github.com/user-attachments/assets/e07514f5-9d2c-4c9a-ab19-d99b133373ad)

  - The backbone of MLOps on Vertex AI is a tool kit called Vertex AI Pipelines, which supports both Kubeflow Pipelines, or KFP, and TensorFlow Extended, or TFX.

![image](https://github.com/user-attachments/assets/5f2150a5-140f-4d62-9667-4063afa2a10a)


