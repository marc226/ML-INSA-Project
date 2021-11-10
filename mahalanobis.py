import pandas as pd
import numpy as np
from numpy.linalg import inv
from scipy.spatial import distance
import ComputeAverages


mean_vector = ComputeAverages.get_data_mean("basedata.csv", 10)


# disassemble tuples and arrange vectors in new matrix
raw_vectors = []
for vector in mean_vector:
    (subject_id, subject_vector) = vector
    raw_vectors.append(subject_vector)
avg_matrix = np.array(raw_vectors)

# transpose resulting matrix
average_array_T = np.transpose(avg_matrix)

# compute covariance matrix
cov_matrix = np.cov(average_array_T)

# inverse of covariance matrix
inv_matrix = inv(cov_matrix)

# computes mahalanobis distance between each vectors in matrix and the observation vector
def mahalanobis(avg_matrix, observation, iv):
    distances = []
    for vector in avg_matrix:
        (subject_id,subject_vector) = vector
        distances.append(distance.mahalanobis(subject_vector,observation, iv))
    return(distances)
