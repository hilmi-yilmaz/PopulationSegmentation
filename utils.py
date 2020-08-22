from sklearn import metrics
from scipy.spatial.distance import cdist
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score, silhouette_samples
        
def inertia_silhouette_score(X, K, cluster_centers):
    
    """
    X the data (counties_transformed which has 7 columns)
    K should be a range()
    cluster_centers: a 2D numpy array containing the cluster centers 
    """
    
    #print("\n----------------------------------------------------------------------------------------------")

    print("\nK = {}".format(K))

    #Calculate the distances from each point to the cluster center
    distance = cdist(X, cluster_centers, "euclidean")
    print("\ndistance = \n{}".format(distance))
    #Note: The first column in distance represents the distance of the all datapoints to the first cluster center and so on.  

    #Determine the minimum distance. This takes the minimum 
    min_distance = np.min(distance, axis=1)
    print("\nmin_distance = \n{}".format(min_distance))
    #Note: These are the distances of each datapoint to the closest cluster

    #Calculate the inertia, which is the sum of squared distances (from the datapoint to closest cluster center) divided by the total datapoints
    inertia = sum(np.square(min_distance)) #/ X.shape[0]
    print("\nInertia = {}".format(inertia))

    #To calculate the silhouette score we need the clusters to which the datapoints are assigned
    cluster = np.argmin(distance, axis=1)
    print("\nClusters = \n{}".format(cluster))

    #Calculate the average silhouette score, This gives a perspective into the density and separation 
    #of the formed clusters. Because the silhouette score only works for k=2 or more, we introduce and if statement 
    if K >= 2: 
        sil_avg = silhouette_score(X, cluster)
        print("\nFor k = {} , The average silhouette_score is : {}".format(K, sil_avg))

        #Compute the silhouette score for each of the samples
        sample_sil_values = silhouette_samples(X, cluster)

    else:
        print("Number of clusters is one. No silhouette score available.")

    print("\n----------------------------------------------------------------------------------------------\n")
    
    return inertia, sil_avg