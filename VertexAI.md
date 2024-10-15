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

 
 ![image](https://github.com/user-attachments/assets/30e743a5-b048-4608-a6b5-4424fd8d28ba)

- Kubeflow Pipelines is a Kubernetes-native, open source product, that has grown into the industry standard for running ML pipelines over the years.
  ![image](https://github.com/user-attachments/assets/4e907192-24eb-4e36-87d8-c122eea19f5a)
- Key Capabilities:
![image](https://github.com/user-attachments/assets/3d9e14b2-22a6-46e4-b2e2-303050fd3bdf)

- AI Hub is a repository for ML components.

# AutoML
- The downside of using pre-trained models like Vision API, the Speech-to-Text API etc. is that they only yield good predictions when your data is relatively common-place, as in social media images or customer reviews. 
- Vertex AI AutoML sits somewhere inbetween these two. A model is trained specific to your data but you don’t need any code to train it.
- Phases of AutoML:
![image](https://github.com/user-attachments/assets/1d2535a7-bf57-423c-9445-245ba2adba17)

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
