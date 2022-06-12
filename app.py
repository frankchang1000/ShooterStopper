
import streamlit as st
import cv2
import pandas as pd
import numpy as np
import time

from main import database
from efficientdet import test


st.set_page_config(page_icon = ".docs/logo.png", layout="wide")
col1, col2, col3 = st.columns(3)

with col2: 
    st.image("./docs/logo.png", width = 500)

col1, col2, col3 = st.columns(3)
with col2:
    if st.button('start camera'):
        video = cv2.VideoCapture(0)
        video.set(cv2.CAP_PROP_FPS, 25)

        frame = st.empty()

        while True:
            success, image = video.read()
            
            image_placeholder, label = test(image, (512, 512))
            image_placeholder = np.array(image_placeholder)

            if not success:
                break

            frame.image(image_placeholder, channels="BGR")
            time.sleep(0.01)

            #connection = database(label = label)
            # timestamps = pd.read_sql_query("SELECT * FROM timestamps", connection)
            
        #st.dataframe(timestamps)


