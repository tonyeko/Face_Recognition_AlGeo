import cv2
import numpy as np
import scipy
import _pickle as pickle
import math
import os
import time

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

def norm(vector):
    norm = math.sqrt(sum(i**2 for i in vector))
    return norm

def eucledian_dist(sample, test_data):
    sample_vector = extract_features(sample)
    test_data_vector = extract_features(test_data)
    result_arr = []
    for i in range(len(sample_vector)):
        result_arr.append(sample_vector[i] - test_data_vector[i])
    vector_dist = norm(result_arr)
    return test_data, vector_dist


def cos_sim(sample, test_data):
    sample_vector = extract_features(sample)
    test_data_vector = extract_features(test_data)
    dotproduct = sum(sample_vector[i] * test_data_vector[i] for i in range(len(sample_vector)))
    result = dotproduct/(norm(sample_vector)*norm(test_data_vector))
    return test_data, result

def main(namafile,jumlahfoto):
    datauji_path = 'datauji/'
    datauji = [os.path.join(datauji_path, p) for p in sorted(os.listdir(datauji_path))]
    # sample = input("Masukkan nama file: ")
    # METODE COSINE SIMILARITY
    cos_sim_arr = []
    sample = os.path.join(datauji_path,namafile)
    for i in datauji:
        cos_sim_arr.append(cos_sim(sample, i))    
    cos_sim_arr.sort(key=lambda tup:tup[1], reverse=True)
    j = 0
    for i in cos_sim_arr:
        j = j+1
        if(j>jumlahfoto):
            break
        print("Similarity:", round(i[1], 5))
        img = cv2.imread(i[0])
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    # print(cos_sim_arr)
def main2(namafile,jumlahfoto):
    datauji_path = 'datauji/'
    datauji = [os.path.join(datauji_path, p) for p in sorted(os.listdir(datauji_path))]
    eucledian_dist_arr = []
    sample = os.path.join(datauji_path,namafile)
    for i in datauji:
        eucledian_dist_arr.append(eucledian_dist(sample, i))    
    eucledian_dist_arr.sort(key=lambda tup:tup[1])
    j = 0
    for i in eucledian_dist_arr:
        j = j+1
        if(j>jumlahfoto):
            break
        print("Similarity:", 1-round(i[1], 5))
        img = cv2.imread(i[0])
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
