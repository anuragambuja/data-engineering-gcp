# Machine Learning
- [Overview](#overview)
- [ML in GCP](#ml-in-gcp)

### Overview
- ML Types
  - Supervised Learning
    - Label has been given. Goal is to predict category ot value.
    - Examples
      - Regression
      - Classification
  - Unsupervised Learning
    - No labels. Try to draw inference from data from previously undetected patterns
    - Find Structure within data
    - Examples
      - Clustering
      - Anomaly Detection
      - Principal COmponent Analysis
  - Reinforcement Learning
    - Learn from environment
    - Maximize reward
    - Does not require examples
    - Combination of exploration and exploitation
 
  ![image](https://user-images.githubusercontent.com/19702456/226649438-f53178f3-e102-48f7-8752-eda4cfac92ef.png)

- Features - describes characterstics of an entity, act as an input variable. eg. height, length of an entity
- Labels - An attribute that is predicted or categorized. eg, selling price, income, Fraud/Non Fraud 
- Feature Engineering - Identifying useful features
- Stages of Model Building
  - Define Problem
  - Collect Data
  - Define Evaluation method
  - Prepare the data
  - Split data into training, validating and test
  - Execute algorithm on the data to build
  - Validate model
  - Test Model
- Model Evaluation
  - How well does the model perform
  - Commonly used metrices 
    - Accuracy - Number of correctly predicted data points. (TP+TN)/(TP+FP+TN+FN)
    - precision - percent of positive data points correctly classified. TP/(TP+FP)
    - Recall - Percent of Actual positive data points identified. TP /(TP+FN)
    - Mean Squared Error (Regression)
    
    ![image](https://user-images.githubusercontent.com/19702456/226649600-045a0da0-c2c4-4807-8435-852c6a0008f2.png)
    
- Model troubleshooting
  - Underfitting - Model performs poorly on training and validation data. Increase complexity of model to correct it
  - Overfitting - Model performs well on trianing data and poorly on validation data. regularization can be used for correcting it
  - Bias - Model did not sufficiently generalize from training data 
  - Variance error is due to sensitivity in small fluctuations in training data

- Regression
  - Output prediction is continuous in nature
  - Example
    - House Price prediction
  - Regression ML Algorithm :
    - Linear Regression
    - SVR
    - Decision Tree Regressor

- Classification
  - Output prediction is discrete in nature
  - Example
    - Sentiment analysis of review : +ve/-ve
      - This product is very much helpful. +ve
    - Is it Orange?
      - Yes/No
  - Classification Algorithm :
    - Logistic Regression
    - SVM
    - KNN
    - Decision Tree Classification

### ML in GCP

   ![image](https://user-images.githubusercontent.com/19702456/225668516-b06ef0ce-c313-4b1d-823f-1e9748846cbc.png)

- DataPrep

  - Intelligent Data Preparation tool
  - Visually explore, clean, and prepare data for analysis and machine learning
  - Build by Trifacta – Third Party tool, not cloud native one
  - Play with this tool without any code, with just click
  - Dataprep is serverless and works at any scale
  - Automatically detect schema, anomalies
  - Concern – Need to share data with Trifacta
  - Run the Job in Dataflow or Trifacta Photon environment

    ![image](https://user-images.githubusercontent.com/19702456/225673995-ebebe006-6511-4a8d-82b8-8ec39f3123b9.png)

- Pre-Trained ML
  - No Training required from customer
  - For generic use case like
    - Object recognition/detection – Vision API
      - Detect printed and handwritten text
      - Detect objects
      - Identify popular places and product logos
      - Moderate content
      - Celebrity recognition
    - OCR
    - Speech to Text
      - Accurately convert speech into text using an API powered by Google’s AI technologies.
      - 125 languages support
      - Streaming speech recognition
      - Content filtering
      - Automatic punctuation
    - Text to Speech API
      - Convert text into natural-sounding speech using an API powered by Google’s AI technologies.
      - 32 Voices
    - Language Translation
    - Dialogue Flow
    - NLP API – to get insight from natural language
       - Identify entities within documents
       - Sentiment analysis
       - Content classification

- Auto ML
  - Throw your data & GCP will create best model for you
  - Each time you train with a prepared data set, it creates a new custom model. Custom models are temporary. They are eventually deleted, and they cannot be exported or saved externally. So you will need to train a new custom model periodically to continue predicting and classifying.
  - Transfer learning technology
  - Example Use cases:
    - Flower species recognition
    - Text Classification 

  ![image](https://user-images.githubusercontent.com/19702456/226640484-f769cae3-3b28-4867-aab3-c59d78642f8e.png)


- Custom Model
  - Have your own data and train your model

- BigQuery ML
  - Create ML Model in SQL
  - Model support
    - Linear Regression
    - Multiclass Logistic Regression
    - K-Means Clustering
    - TIme series forecast
    - Matrix factorization
    - Boosted Tree and XGBoost
    - Tensorflow (imported)
    - AutoML Tables
  - BigQuery Function
    - Create MODEL
      - Model Type – Linear Reg, Logistic
      - Label Column
      - Learning Rate etc…
      ```
      CREATE OR REPLACE MODEL `bqml_tutorial.irisdata_model`
      OPTIONS
        ( model_type='LOGISTIC_REG',
          auto_class_weights=TRUE,
          data_split_method='NO_SPLIT',
          input_label_cols=['species'],
          max_iterations=10) AS
      SELECT * FROM `bigquery-public-data.ml_datasets.iris`
      ```
    - Evaluate Model
      - ML.Evaluate
      - Provide Model & Test Data
      - Determine how good model performance on Test data
      ```
      SELECT * 
      FROM ML.EVALUATE(MODEL bqml_tutorial.irisdata_model,
                (SELECT * FROM `bigquery-public-data.ml_datasets.iris`))
      ```
    - Prediction
      - ML.Prediction
      - Apply Live data to Model to get prediction
      ```
      select * from ML.PREDICT(MODEL bqml_tutorial.irisdata_model, 
                        (SELECT 5.1 as sepal_length,
                                2.5 as petal_length,
                                3.0 as petal_width,
                                1.1 as sepal_width))
       ```
- Kubeflow
  - Kubeflow is a platform that provides the tools and scalable services required to develop and deploy ML workloads all the way from distributed training to scalable serving to notebooks with JupyterHub and workflow orchestration. Kubeflow services are built on top of Kubernetes. 
  - Packages models like applications. This adds an element of portability since you can then move your ML pipelines even between cloud providers. AI Hub is a repository for ML components. Among the assets stored on AI Hub are entire Kubeflow pipelines, Jupyter notebooks, TensorFlow modules, fully trained models, services, and VM images. Public assets are available to all AI Hub users. Restricted scope assets contain AI components you have uploaded and those that have been shared with you.
  - compose, deploy and manage ML workflows

- GPUs and TPUs
  - Graphical Processing Unit (GPU)
    - Highlyparallel processing
    - Local memory
    - Arithematic logic Units (ALUs)
    - Matrix Multiplication
    - Available on other cloud and on premises
    - Cost more than TPUs
    - Need to install NVIDIA drivers
  - Tensor Processing Unit (TPU)
    - To do training faster Google created ASIC based in-house dedicated computing for Tensor Processing
    - Speed up training by 20x to 30x
    - Work with VM, GKE, AI Platform
    - Useful for training large training needs
    - Cost less than GPUs

- Monitoring ML Model Best Practices
  - Monitor for data skew
  - Watch for changes in dependencies
  - Models are refreshed as needed
  - Test for Unfairness
  - Access model prediction quality using different metrices


### Vertex AI
- Vertex AI is the unified AI platform on Google Cloud to train and deploy a ML model. Vertex AI offers two options on one platform to build a ML model: a codeless solution with AutoML and a code-based solution with Custom Training using Vertex Workbench

    ![image](https://user-images.githubusercontent.com/19702456/226648437-3c7930c6-0ec7-41a0-a271-de9b0780d2cb.png)

- Benefits
  - Features are sharable for training or serving tasks
  - Features are reusable
  - Features are scalable
  - Features are easy to use
  - 
