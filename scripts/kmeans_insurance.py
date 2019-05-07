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

"kmeans_insurance.py" 84L, 2458C                              15,40         Top
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

                                                              84,4          Bot
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

                                                              77,1          Bot
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
