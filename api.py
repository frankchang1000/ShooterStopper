import time
from flask import Flask, request
from efficientdet import test
from Video import photo
import numpy as np
import cv2

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

"""
@app.route("/predict", methods = ['GET','POST'])
def predict():
    while True:
        image_placeholder, label = test(photo, (512, 512), 0.3, 0.45)
        image_placeholder = np.array(image_placeholder)
        
        cv2.imshow(image_placeholder, channels="BGR")
"""