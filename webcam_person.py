
import tensorflow as tf

from utils import backbone
from api import object_counting_api

detection_graph, category_index = backbone.set_model('ssd_mobilenet_v1_coco_2018_01_28', 'mscoco_label_map.pbtxt')

is_color_recognition_enabled = False 

object_counting_api.object_counting_webcam(detection_graph, category_index, is_color_recognition_enabled)
