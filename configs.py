# Global environment variables for the project

import tensorflow as tf

from utils.file_reader import parse_label_file

# AI/ML environment variables
labels_file = "docs/labels.txt"
models_file = "models/efficientdet-d0-shooterstopper-ep10"

MODEL = tf.keras.models.load_model(models_file)
LABEL_DICT = parse_label_file(labels_file)

IMAGE_DIMS = (512, 512)
SCORE_THRESHOLD = 0.55
IOU_THRESHOLD = 0.3

# Deployment options
server_port = 5000
camera_number = 0 # Alter to change which camera is used, IP Cameras can also be configured