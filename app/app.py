
import streamlit as st
import cv2
import pandas as pd
import numpy as np

from main import database


st.title("Webcam Live Feed")

connection = database()
timestamps = pd.read_sql_query("SELECT * FROM timestamps", connection)

st.dataframe(timestamps)