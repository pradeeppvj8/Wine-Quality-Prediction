# Project Name
* Wine Quality Prediction

#### Project Status: [Completed]

## Project Intro/Objective
The purpose of this project is to predict wine's quality based on attributes like fixed acidity, volatile acidity, citric acid etc.

### Methods Used
* ElasticNet
* Data Visualization

### Technologies
* Python
* Pandas, jupyter
* Sklearn
* Flask
* Dockers
* AWS ECR, AWS EC2
* Github runners
* MLFlow


## Project Description
* The purpose of this project is to predict wine's quality based on attributes like fixed acidity, volatile acidity, citric acid etc.
* The data has been taken from https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009
* After trying various learning algorithms, ElasticNet has been used to perform wine quality prediction in this project.
* This project has been dockorized and the settings are present in 'Dockerfile'.
* AWS ECR Repository was created to store our docker image.
* AWS EC2 Instance was created and was connected to the ECR repository.
* Github workflow and Github runner has been configured using main.yaml file. 
* The purpose of Github runner is to create a docker image for every push to git hub repository.
* Github runner and AWS EC2 instance are connected and whenever the github runner runs, the docker image is moved to ECR repository.
* MLFlow has been integerated into this project for model tracking purposes.
* Model evaluation component contains the MLFlow integeration.

## Getting Started

1. Raw Data is kept in [data\wine-quality.zip].

2. Data Ingestion scripts are kept in [src\wqpproject\components\data_ingestion.py]
    
3. Data transformation scripts are kept in [src\wqpproject\components\data_transformation.py]

4. Data validation scripts are kept in [src\wqpproject\components\data_validation.py]

5. Model training scripts are kept in [src\wqpproject\components\model_trainer.py]

6. Model evaluation scripts are kept in [src\wqpproject\components\model_evaluation.py]

7. Docker configuration is kept in [Dockerfile]

8. Github workflow & runner configuration is kept in [.github\workflows\main.yaml]

## Featured Notebooks/Analysis/Deliverables
* [src\wqpproject\pipeline\prediction.py] is the prediction pipeline that is responsible for performing model predictions.
* [main.py] is the training pipeline that is responsible for training the model.

## Contact
* Name :- Pradeep.P 
* Mobile :- 8197607412
* Email :- pradeep.pvj8@gmail.com