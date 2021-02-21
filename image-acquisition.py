import cv2
import os

import shutil
from os import path
from time import time
from datetime import datetime


# Defines how long to wait between captures
image_interval_ms = 5000

# Defines how long to capture images for. Set to 0 if
# you wish to capture images indefinitely (or until quit)
capture_elapsed_ms = 1;

# Defines the URIs to look for the streams on
camera_uris = ["192.168.1.37", "192.168.1.39"]

# Defines the extensions to pull image frames from
camera_stream_link = "/mjpg/video.mjpg"

# Defines the parent folder to save images under
save_folder = "img"


# Gets the current time in milliseconds, from epoch
def get_current_ms():
    return int(time() * 1000) 

# Defines a save directory local to the Jupyter Notebook
def get_save_directory(cam_num):
    return f"{save_folder}/cam{cam_num}"

# Returns a unique timestamp-based name for a file
def get_unique_image_id(cam_num):
    date_stamp = f"cam{cam_num}_img_{datetime.now()}"
    date_stamp = date_stamp.replace('-', '')
    date_stamp = date_stamp.replace(':', '')
    date_stamp = date_stamp.replace('.', '')
    date_stamp = date_stamp.replace(' ', '_')
    return date_stamp + '.jpg'

# Create new URI for an image
def get_new_image_uri(cam_num):
    return get_save_directory(cam_num) + '/' + get_unique_image_id(cam_num)

# Initialize by creating the paths as needed, and storing stream links. Returns the time
# that the program finished initializing, in milliseconds from the epoch, and the links
# to each stream
def initialize():
    stream_links = {}
    
    for index, ip in enumerate(camera_uris):
        stream_links[index] = f"http://{ip}{camera_stream_link}" 

        if not path.exists(get_save_directory(index)):
            os.makedirs(get_save_directory(index))
            
    return get_current_ms(), stream_links


if __name__ == "__main__":
    print(f'Beginning time lapse recording at an interval of {image_interval/1000} seconds/photo')
    print('Hold [Ctrl]+[C], or [Esc] to exit')
    start_time_ms, stream_links = initialize()
    
    while True if capture_elapsed_ms <= 0 else ((get_current_ms() - start_time_ms) > capture_elapsed_ms):
        for camera_id in stream_links.keys():
            stream = cv2.VideoCapture(stream_links[camera_id])
            ret, frame = stream.read()

            cv2.imwrite(get_new_image_uri(camera_id), frame) 
            
        if cv2.waitKey(image_interval_ms) == 27:
            sys.exit()