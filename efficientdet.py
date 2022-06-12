"""
ShooterStopper Object Detection Model.
"""
import os
import tensorflow as tf

from typing import Union

from configs import *
from utils.postprocess import FilterDetections
from utils.visualize import draw_boxes
from utils.file_reader import parse_label_file

def preprocess_image(image, 
                     image_dims: tuple) -> Union[tf.Tensor, tuple]:
    """Preprocesses an image.
        
    Parameters:
        image: numpy arr of the image
        image_dims: The dimensions to resize the image to
    Returns:
        A preprocessed image with range [0, 255]
        A Tuple of the original image shape (w, h)
    """
    image = tf.convert_to_tensor(image)
    original_shape = tf.shape(image)
    image = tf.image.resize(images=image,
                            size=image_dims,
                            method="bilinear")
    image = tf.expand_dims(image, axis=0)
    image = tf.cast(image, tf.float32)
    # Image is on scale [0-255]
    return image, (original_shape[1], original_shape[0])


def test(image: str, 
         image_dims: tuple = (512, 512), 
         score_threshold: float = 0.55, 
         iou_threshold: float = 0.3) -> None:
    """Preprocesses, Tests, and Postprocesses.
    
    Parameters:
        image_path: image frame, numpy array
        model: Model to test
        image_dims: Dimensions of image
        score_threshold: Threshold for score
        iou_threshold: Threshold for iou
    Returns:
        image, labels
    """
    image, original_shape = preprocess_image(
        image, image_dims)

    pred_cls, pred_box = MODEL(image, training=False)
    labels, bboxes, scores = FilterDetections(
        score_threshold=score_threshold,
        iou_threshold=iou_threshold,
        image_dims=image_dims)(
            labels=tf.cast(pred_cls, tf.float32),
            bboxes=tf.cast(pred_box, tf.float32))

    labels = [list(LABEL_DICT.keys())[int(l)]
              for l in labels[0]]
    bboxes = bboxes[0]
    scores = scores[0]

    image = draw_boxes(
        image=tf.squeeze(image, axis=0),
        original_shape=original_shape,
        resized_shape=image_dims,
        bboxes=bboxes,
        labels=labels,
        scores=scores,
        labels_dict=LABEL_DICT)

    return image, labels
