###############################################################################
# Flask App
# Thomas Chia, Frank Chang, and other contributors
# MIT License
###############################################################################

import cv2
import pandas as pd
import numpy as np

from flask import Flask, render_template, Response, request, jsonify

import efficientdet as efficientdet

from database import database
from configs import *

app = Flask(__name__)

# Alter these values to match your environment
camera = cv2.VideoCapture(camera_number)


def run_inference(frame):
    """
    Runs object detection inference on a single frame.
    """
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame, _ = efficientdet.test(
        frame,
        model=MODEL,
        label_dict=LABEL_DICT,
        image_dims=IMAGE_DIMS,
        score_threshold=SCORE_THRESHOLD,
        iou_threshold=IOU_THRESHOLD)
    output_frame = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
    return output_frame


def gen_frames():
    """
    Grabs the frames and returns to the client.
    """
    while True:
        # print("Reading from camera")
        success, frame = camera.read()
        if not success:
            print("Not streaming.")
            break
        else:
            frame = run_inference(np.array(frame))
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """
    Returns a video feed with the detections to the frontend.
    """
    return Response(
        gen_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    return render_template('React_App.html')


@app.route('/database', methods=["GET"])
def db():
    """
    Provides database information to the frontend.
    """
    if request.method == "GET":
        connection = database(label='pistol')
        timestamps = pd.read_sql_query("SELECT b FROM timestamps", connection)
        data_pd = {}
        for index, col in timestamps.iterrows():
            data_pd[index] = str(
                dict(timestamps.loc[index])["b"].to_pydatetime())[0:-6]
        return jsonify(data_pd)


if __name__ == "__main__":
    print("Finished loading models.")
    print("Launching the app.")
    from gevent.pywsgi import WSGIServer

    http_server = WSGIServer(('0.0.0.0', 5000), app)

    print("The app will be run on localhost:{}. Press Ctrl+C to quit.".format(5000))
    http_server.serve_forever()
