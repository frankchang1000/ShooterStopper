import numpy as np
import os
import tensorflow as tf
import cv2
from utils import label_map_util
from utils import visualization_utils as vis_util

cap = cv2.VideoCapture(0)

while True:
    # Read frame from camera
    ret, image_np = cap.read()
    # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
    image_np_expanded = np.expand_dims(image_np, axis=0)
# Display output
    cv2.imshow('Gun Detection', cv2.resize(image_np, (1200, 800)))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break