
import streamlit as st
import cv2
import pandas as pd
import numpy as np
import imutils
import argparse
import time

from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, RTCConfiguration
import av
import threading

from main import database
from efficientdet import test



st.title("Webcam Live Feed")




st.dataframe(timestamps)


if st.button('Start'):
    video = cv2.VideoCapture(0)
    video.set(cv2.CAP_PROP_FPS, 25)

    frame = st.empty()

    while True:
        success, image = video.read()
        
        image_placeholder, label = test(image, (512, 512), 0.3, 0.45)
        image_placeholder = np.array(image_placeholder)

        if not success:
            break
        frame.image(image_placeholder, channels="BGR")
        time.sleep(0.01)

        connection = database(label = label)
        timestamps = pd.read_sql_query("SELECT * FROM timestamps", connection)





