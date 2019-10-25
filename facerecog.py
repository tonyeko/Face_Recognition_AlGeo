import cv2
import numpy as np
import scipy
from scipy.misc import imread
import _pickle as pickle
import math
import os

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

# def eucledian_dist():

#     return 

def cos_sim(sample, test_data):
    sample_vector = extract_features(sample)
    test_data_vector = extract_features(test_data)
    dotproduct = sum(sample_vector[i] * test_data_vector[i] for i in range(len(sample_vector)))
    result = dotproduct/(norm(sample_vector)*norm(test_data_vector))
    return test_data, result

def main():
    datauji_path = 'datauji/'
    datauji = [os.path.join(datauji_path, p) for p in sorted(os.listdir(datauji_path))]
    # sample = input("Masukkan nama file: ")
    # METODE COSINE SIMILARITY
    cos_sim_arr = []
    sample = os.path.join(datauji_path,"taylor swift4.jpg")
    for i in datauji:
        cos_sim_arr.append(cos_sim(sample, i))    
    cos_sim_arr.sort(key=lambda tup:tup[1], reverse=True)
    print(cos_sim_arr)