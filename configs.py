# Global environment variables for the project

import tensorflow as tf

from utils.file_reader import parse_label_file

labels_file = "docs/labels.txt"
models_file = "models/efficientdet-d0-shooterstopper-ep10"

MODEL = tf.keras.models.load_model(models_file)
LABEL_DICT = parse_label_file(labels_file)
