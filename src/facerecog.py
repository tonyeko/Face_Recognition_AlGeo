import numpy as np
import _pickle as pickle
import os   
import math
import extractor
from imgshow import *

def dotproduct(v1, v2):
    return np.dot(v1, v2)

def norm(vector):
    return math.sqrt(dotproduct(vector, vector))

def unitvector(vector):
    return vector/norm(vector)

def euclidean_dist(sample_vector, test_data_vector):
    vector_dist = norm(sample_vector - test_data_vector)
    return vector_dist
    
def cos_sim(sample_vector, test_data_vector):
    cos_value = dotproduct(sample_vector/norm(sample_vector), test_data_vector/norm(test_data_vector))
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
        sample = extractor.extract_features(image_path)
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

def main(method, T, sample):
    database_path = '../test/database'
    datauji_path = '../test/datauji'
    files = [os.path.join(database_path, p) for p in sorted(os.listdir(database_path))]
    database = Matcher('../test/database.pck')
    print ('Sample image:', end=" ")
    print(sample)
    sample = os.path.join(datauji_path, sample)
    names, match = database.match(sample, method, topn=T)
    print ('Database images:')
    for i in range(T):
        similarity = round(match[i], 5)
        if method == 1: 
            print("Similarity:", similarity, names[i]) 
        else: 
            print("Distance:", similarity, names[i]) 
        
        show_img(os.path.join(database_path, names[i]), similarity, i+1, method)