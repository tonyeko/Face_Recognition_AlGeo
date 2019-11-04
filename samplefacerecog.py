import cv2
import numpy as np
import scipy
from scipy.misc import imread
import _pickle as pickle
import random
import os
import math

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

def batch_extractor(images_path, pickled_db_path="datauji.pck"):
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

    result = {}
    for f in files:
        print ('Extracting features from image %s' % f)
        name = f.split('/')[-1].lower()
        result[name] = extract_features(f)
    
    # saving all our feature vectors in pickled file
    with open(pickled_db_path, 'wb') as fp:
        pickle.dump(result, fp)

def dotproduct(v1, v2):
    # if len(v1) >= len(v2): length = len(v2)
    # else: length = len(v1)
    # return sum(v1[i] * v2[i] for i in range(length))
    return sum((x1 * x2) for x1, x2 in zip(v1, v2))

def norm(vector):
    # return math.sqrt(sum(i**2 for i in vector))
    return math.sqrt(dotproduct(vector, vector))

def unitvector(vector):
    return vector/norm(vector)

def euclidean_dist(sample_vector, test_data_vector):
    vector_dist = norm(sample_vector - test_data_vector)
    return vector_dist
    

def cos_sim(sample_vector, test_data_vector):
    cos_value = dotproduct(sample_vector, test_data_vector)/(norm(sample_vector)*norm(test_data_vector))
    return cos_value

class Matcher(object):
    def __init__(self, pickled_db_path="features.pck"):
        with open(pickled_db_path, 'rb') as fp:
            self.data = pickle.load(fp)
        self.names = []
        self.matrix = []
        for k, v in self.data.items():
            self.names.append(k)
            self.matrix.append(v)
        self.matrix = np.array(self.matrix)
        self.names = np.array(self.names)

    def match(self, image_path, method, topn):
        sample = extract_features(image_path)
        result = []
        for i in self.matrix:
            if method == 1:
                result.append(cos_sim(sample, i))
            elif method == 2:
                result.append(euclidean_dist(sample, i)) 
        topn_result = []
        if method == 1: nearest_ids = np.argsort(result)[::-1][:topn].tolist()
        else: nearest_ids = np.argsort(result)[:topn].tolist()
        for i in nearest_ids:
            topn_result.append(result[i])
        nearest_img_paths = self.names[nearest_ids].tolist()
        return nearest_img_paths, topn_result

def show_img(path):
    img = cv2.imread(path)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    
def main(method, T, sample):
    datauji_path = 'datauji/'
    files = [os.path.join(datauji_path, p) for p in sorted(os.listdir(datauji_path))]
    # batch_extractor(datauji_path)
    datauji = Matcher('datauji.pck')
    
    print ('Query image ==========================================')
    print(sample)
    sample = os.path.join(datauji_path, sample)
    show_img(sample)
    names, match = datauji.match(sample, method, topn=T)
    print ('Result images ========================================')
    for i in range(len(names)):
        if method == 1: similarity = round(match[i], 5)
        else: similarity = round(1-(match[i]), 5) # PERLU DIGANTI 
        print("Similarity:", similarity, names[i]) 
        show_img(os.path.join(datauji_path, names[i]))
        if i == T-1:
            cv2.destroyAllWindows()
            break
