# Machine Learning

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
  - COmmonly used metrices 
    - Accuracy - Number of correctly predicted data points. (TP+TN)/(TP+FP+TN+FN)
    - precision - percent of positive data points correctly classified. TP/(TP+FP)
    - Recall - Percent of Actual positive data points identified. TP /(TP+FN)
    - Mean Squared Error (Regression)
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

- ML in GCP

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
    - Language Translation
    - NLP API – to get insight from natural language
       - Identify entities within documents
       - Sentiment analysis
       - Content classification

- Auto ML
  - Throw your data & GCP will create best model for you
  - Transfer learning technology
  - Example Use cases:
    - Flower species recognition
    - Text Classification 

- Custom Model


