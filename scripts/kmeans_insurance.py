from copy import deepcopy
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from operator import itemgetter
from collections import Counter
import json

kmeans_global = None

def hit_the_nuke_button(new_point):
    X  = intialize_data()
    kmeans = kmeans_on_insurance_data(X)
    cluster_number = predict_new_point(kmeans, new_point)
    range = get_cluster_range_of_point(cluster_number[0])
    return range

def get_cluster_range_of_point(cluster_label):
    dict = create_dictionary()
    range = dict[cluster_label] 
    return range
 
def intialize_data():
    data = pd.read_csv("/html/databases/InsuranceUserData.csv")
    headers = list(data.columns)
    # NumPy representation of the Series object
    num_prescriptions_col = data['NumPrescriptions'].values
    age_range_col = data["AgeRange"].values
    average_income_col = data["AvgIncome"].values
    X = np.array(list(zip(num_prescriptions_col, age_range_col, average_income_col)))
    return X

def kmeans_on_insurance_data(X):
    k = 18
    # Number of clusters
    kmeans = KMeans(n_clusters=18)
    #Fitting the input data
    kmeans = kmeans.fit(X)
    # Getting the cluster labels 
    labels = kmeans.predict(X)
    # Centroid values 
    centroids = kmeans.cluster_centers_ 
    # What cluster each point belongs to.  Array of the cluster assignment for each training vector
    labels = kmeans.labels_
    return kmeans

def create_dictionary():

    x = {}

    x[0] = (147.84, 205.30)
    x[1] = (205.31, 262.76)
    x[2] = (262.77, 320.22)
    x[3] = (320.23, 377.68)
    x[4] = (377.69, 435.14)
    x[5] = (435.15, 492.60)
    x[6] = (492.61, 550.06)
    x[7] = (550.07, 607.52)
    x[8] = (607.53, 664.98)
    x[9] = (664.99, 722.04)
    x[10] = (722.05, 779.90)
    x[11] = (779.91, 837.06)
    x[12] = (837.07, 894.82)
    x[13] = (894.83, 952.28)
    x[14] = (952.29, 1009.74)
    x[15] = (1009.75, 1057.20)
    x[16] = (1057.21, 1124.66)
    x[17] = (1124.67, 1182.10)

    return x

# [prescriptions, AgeRange, AvgIncome]
def predict_new_point(kmeans, new_point):
    # predict new point
    new_point = [5, 25, 55000]
    # get cluster it is in
    print(np.array(new_point))
    new_point_label = kmeans.predict(np.array((new_point)).reshape(1, -1))
    print(new_point_label)
    print("The point belongs to cluster", new_point_label)
    return new_point_label
    
