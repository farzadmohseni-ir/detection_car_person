
import tensorflow as tf

from utils import backbone
from api import object_counting_api

input_video = "./input_images_and_videos/detection_car.mp4"

detection_graph, category_index = backbone.set_model('ssd_mobilenet_v1_coco_2018_01_28', 'mscoco_label_map.pbtxt')

is_color_recognition_enabled = False 
roi = 0 
deviation = 4.5 
custom_object_name = '' 
targeted_objects_name = "car, truck"

object_counting_api.cumulative_object_counting_y_axis(input_video, detection_graph, category_index, is_color_recognition_enabled, roi, deviation, custom_object_name, targeted_objects_name) # counting all the objects
