# Population segmentation with Amazon SageMaker

This project is about finding groupings in a dataset containing counties in the US. 

## Overview 

The following steps are taken in this project:

    1. Import the data
    2. Clean and prepare the data
    3. Perform PCA to reduce the dimensionality
    4. Train a K-means model (k=5) to see how everything works
    5. Perform hyperparameter optimization to find the best value for k
    6. Create a model with best k
    7. Look at natural groupings: which counties belong to the same cluster 

I am using Amazon SageMaker for this project. 

## Contents
The files in this repository contain the following information:

    1. Population_Segmentation.ipynb: Project Notebook    
    2. Population_Segmentation.html: A html file containing the project notebook and its outputs.
    3. utils.py: A function which return the inertia and silhouette scores (measures of K-means algorithm)
    4. Assumptions of K-means Test.ipynb: In this notebook, I tested the assumption of K-means. Also, I use a Gaussian Mixture Model and DBSCAN, which are other clustering algorithm which could potentially be used instead of K-means in the main project.
    5. TestNotebook.ipynb: A Test Notebook which I used to write the utils.py file
    
## Potential Improvements
Instead of using K-means, a Gaussian Mixture Model could be used. This is like a generalization of the K-means algorithm which also takes into account the variance of the data. 
