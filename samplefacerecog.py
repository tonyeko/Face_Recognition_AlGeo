import cv2
import numpy as np
import scipy
import _pickle as pickle
import os   
import math
import extractor
from functools import partial
from tkinter import *

from PIL import ImageTk, Image

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

def next(subwindow):
    subwindow.quit()
    subwindow.update()

def show_img(path, similarity):
    img = cv2.imread(path)
    # # cv2.imshow('image', img)
    # # cv2.waitKey(0)

    b,g,r = cv2.split(img)
    img = cv2.merge((r,g,b))
    # A root window for displaying objects
    subwindow = Toplevel()
    subwindow.title("Result")
    name = os.path.basename(path)
    Label(subwindow, text=name).pack()
    
    sim = StringVar()
    string = "Similarity: "+ str(similarity) 
    sim.set(string)
    if (similarity != -9999) :
        Label(subwindow, textvariable=sim).pack()
    

    # Convert the Image object into a TkPhoto object
    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=im) 

    # Put it in the display window
    Label(subwindow, image=imgtk).pack() 
    Button(subwindow, text="Next", command=partial(next, subwindow)).pack()
    # subwindow.destroy()
    subwindow.mainloop() # Start the GUI
    
    
def main(method, T, sample):
    datauji_path = 'datauji/'
    files = [os.path.join(datauji_path, p) for p in sorted(os.listdir(datauji_path))]
    
    # extractor.batch_extractor(datauji_path)
    
    datauji = Matcher('datauji.pck')
    
    print ('Query image ==========================================')
    print(sample)
    sample = os.path.join(datauji_path, sample)
    show_img(sample, -9999)
    names, match = datauji.match(sample, method, topn=T)
    print ('Result images ========================================')
    for i in range(T):
        if method == 1: similarity = round(match[i], 5)
        else: similarity = round(1-(match[i]), 5) # PERLU DIGANTI 
        print("Similarity:", similarity, names[i]) 
        show_img(os.path.join(datauji_path, names[i]), similarity)
        # if i == T-1:
        #     cv2.destroyAllWindows()
        #     break
