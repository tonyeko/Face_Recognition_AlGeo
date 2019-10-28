import cv2
import numpy as np
import scipy
import _pickle as pickle
import math
import os
import tkinter
from annoy import AnnoyIndex

import timeit

# Feature extractor
def extract_features(image_path, vector_size=32):
    image = cv2.imread(image_path)
    try:
        # Using KAZE, cause SIFT, ORB and other was moved to additional module
        # which is adding addtional pain during install
        alg = cv2.KAZE_create()
        # Dinding image keypoints
        kps = alg.detect(image)
        # Getting first 32 of them. 
        # Number of keypoints is varies depend on image size and color pallet
        # Sorting them based on keypoint response value(bigger is better)
        kps = sorted(kps, key=lambda x: -x.response)[:vector_size]
        # computing descriptors vector
        kps, dsc = alg.compute(image, kps)
        # Flatten all of them in one big vector - our feature vector
        dsc = dsc.flatten()
        # Making descriptor of same size
        # Descriptor vector size is 64
        needed_size = (vector_size * 64)
        if dsc.size < needed_size:
            # if we have less the 32 descriptors then just adding zeros at the
            # end of our feature vector
            dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])
    except cv2.error as e:
        print ('Error: ', e)
        return None

    return dsc

# def sparse_vector(dense_vec):
#     sparse_vec = {“id”: [], “values”: []}
#     d = len(dense_vec)
#     for i in range(0, d):
#         if d[i] != 0:
#             sparse_vec["id"].append(i)
#             sparse_vec["values"].append(d[i])
#     return sparse_vec

def dotproduct(v1, v2):
    # if len(v1) >= len(v2): length = len(v2)
    # else: length = len(v1)
    # return sum(v1[i] * v2[i] for i in range(length))
    return sum((x1 * x2) for x1, x2 in zip(v1, v2))

def norm(vector):
    # return math.sqrt(sum(i**2 for i in vector))
    return math.sqrt(dotproduct(vector, vector))

def euclidean_dist(sample_vector, test_data):
    test_data_vector = extract_features(test_data)
    result_arr = []
    for i in range(len(sample_vector)):
        result_arr.append(sample_vector[i] - test_data_vector[i])
    vector_dist = norm(result_arr)
    return test_data, vector_dist

def cos_sim(sample_vector, test_data):
    test_data_vector = extract_features(test_data)
    cos_value = dotproduct(sample_vector, test_data_vector)/(norm(sample_vector)*norm(test_data_vector))
    # cos_value = dotproduct(sample_vector/norm(sample_vector), test_data_vector/norm(test_data_vector))
    return test_data, cos_value

def main(method, T, sample):
    start = timeit.default_timer()

    datauji_path = 'datauji/'
    datauji = [os.path.join(datauji_path, p) for p in sorted(os.listdir(datauji_path))]
    sample = os.path.join(datauji_path, sample)
    sample_vec = extract_features(sample)

    # if method == 1:
    #     # METODE COSINE SIMILARITY
    #     cos_sim_arr = AnnoyIndex(2, 'euclidean')
    #     for i in range (len(datauji)):
    #         v = cos_sim(sample_vec, datauji[i])
    #         cos_sim_arr.add_item(i, v)    
    #     cos_sim_arr.sort(key=lambda tup:tup[1], reverse=True)
    #     result = cos_sim_arr

    # elif method == 2:
    #     # METODE EUCLIDEAN DISTANCE
    #     euclidean_dist_arr = []
    #     for i in datauji:
    #         euclidean_dist_arr.append(euclidean_dist(sample_vec, i))   
    #     euclidean_dist_arr.sort(key=lambda tup:tup[1])
    #     result = euclidean_dist_arr
    test_data_arr = AnnoyIndex(2048, 'euclidean')
    test_data_arr.add_item(0, sample_vec)
    for i in range (1, len(datauji)):
        test_data_arr.add_item(i, extract_features(datauji[i]))
    test_data_arr.build(10000)
    result = test_data_arr.get_nns_by_item(0,9)

    stop = timeit.default_timer()
    print('Time: ', stop - start)
    print(result)
    for i in result:
        print(datauji[i])
        img = cv2.imread(datauji[i])
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
  
  
    # for index, item in enumerate(result):
    #     if method == 1: similarity = round(item[1], 5)
    #     else: similarity = round(1-(item[1]), 5) # PERLU DIGANTI 
    #     print("Similarity:", similarity, item[0]) 
    #     img = cv2.imread(item[0])
    #     cv2.imshow('image', img)
    #     cv2.waitKey(0)
    #     if index == T-1:
    #         cv2.destroyAllWindows()
    #         break