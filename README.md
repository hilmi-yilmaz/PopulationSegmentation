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