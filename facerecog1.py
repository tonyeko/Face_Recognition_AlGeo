import cv2
import numpy as np
import scipy
import _pickle as pickle
import math
import os
import tkinter

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

def batch_extractor(images_path, pickled_db_path="features.pck"):
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

    result = {}
    for f in files:
        print ('Extracting features from image %s' % f)
        name = f.split('/')[-1].lower()
        result[name] = extract_features(f)
    
    # saving all our feature vectors in pickled file
    with open(pickled_db_path, 'wb') as fp:
        pickle.dump(result, fp)

class Matcher(object):
    def __init__(self, pickled_db_path="features.pck"):
        with open(pickled_db_path, 'rb') as fp:
            self.data = pickle.load(fp)
        self.names = []
        self.matrix = []
        print(self.data.items())
        for k, v in self.data.items():
            self.names.append(k)
            self.matrix.append(v)
        print(self.matrix)    
        self.matrix = np.array(self.matrix)
        self.names = np.array(self.names)

    def match(self, image_path, topn=5):
        features = extract_features(image_path)
        print(features); print("====================")
        
        img_distances = self.cos_cdist(features)
        print("Img Dist:", img_distances)
        print("Similarity:", 1-img_distances)
        # getting top 5 records
        nearest_ids = np.argsort(img_distances)[:topn].tolist()
        print(nearest_ids)
        nearest_img_paths = self.names[nearest_ids].tolist()
        print(nearest_img_paths)
        print(img_distances[nearest_ids].tolist())
        return nearest_img_paths, img_distances[nearest_ids].tolist()

# def sparse_vector(dense_vec):
#     sparse_vec = {“id”: [], “values”: []}
#     d = len(dense_vec)
#     for i in range(0, d):
#         if d[i] != 0:
#             sparse_vec["id"].append(i)
#             sparse_vec["values"].append(d[i])
#     return sparse_vec

def dotproduct(v1, v2):
    if len(v1) >= len(v2): length = len(v2)
    else: length = len(v1)
    return sum(v1[i] * v2[i] for i in range(length))
    # return sum((x1 * x2) for x1, x2 in zip(v1, v2))
    # return np.dot(v1, v2)

def norm(vector):
    return math.sqrt(sum(i**2 for i in vector))
    # return math.sqrt(dotproduct(vector, vector))

def unitvector(vector):
    return vector/norm(vector)

def euclidean_dist(sample_vector, test_data):
    # CARA 1
    # test_data_vector = extract_features(test_data)
    # vector_dist = norm(sample_vector - test_data_vector)

    # CARA 2
    # result_arr = []
    # for i in range(len(sample_vector)):
    #     result_arr.append(sample_vector[i] - test_data_vector[i])
    # vector_dist = norm(result_arr)

    # CARA 3
    cos_val = cos_sim(sample_vector, test_data)
    vector_dist = 2-(2*cos_val[1])
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

    if method == 1:
        # METODE COSINE SIMILARITY
        cos_sim_arr = []
        for i in datauji:
            cos_sim_arr.append(cos_sim(sample_vec, i))    
        cos_sim_arr.sort(key=lambda tup:tup[1], reverse=True)
        result = cos_sim_arr

    elif method == 2:
        # METODE EUCLIDEAN DISTANCE
        euclidean_dist_arr = []
        for i in datauji:
            euclidean_dist_arr.append(euclidean_dist(sample_vec, i))   
        euclidean_dist_arr.sort(key=lambda tup:tup[1])
        result = euclidean_dist_arr

    stop = timeit.default_timer()
    print('Time: ', stop - start)  
  
    for index, item in enumerate(result):
        if method == 1: similarity = round(item[1], 5)
        else: similarity = round(1-(item[1]), 5) # PERLU DIGANTI 
        print("Similarity:", similarity, item[0]) 
        img = cv2.imread(item[0])
        cv2.imshow('image', img)
        cv2.waitKey(0)
        if index == T-1:
            cv2.destroyAllWindows()
            break