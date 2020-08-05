import cv2
import os
import sys

from os import path
from datetime import datetime


image_interval = 200
camera_ips = [201, 202]
stream_links = {}


def get_save_directory(cam_num):
    return f"img/cam{cam_num}"


def get_unique_image_id(cam_num):
    date_stamp = f"cam{cam_num}_img_{datetime.now()}"
    date_stamp = date_stamp.replace('-', '')
    date_stamp = date_stamp.replace(':', '')
    date_stamp = date_stamp.replace('.', '')
    date_stamp = date_stamp.replace(' ', '_')
    return date_stamp + '.jpg'


def get_new_image_uri(cam_num):
    return get_save_directory(cam_num) + '/' + get_unique_image_id(cam_num)


def initialize():
    current_index = 0
    for ip in camera_ips:
        stream_links[current_index] = f"http://192.168.1.{ip}/mjpg/video.mjpg"

        if not path.exists(get_save_directory(current_index)):
            os.mkdir(get_save_directory(current_index))

        current_index += 1


if __name__ == "__main__":
    print(f'Beginning time lapse recording at an interval of {image_interval/1000} seconds/photo')
    print('Hold [Ctrl]+[C] to exit')
    initialize()

    while True:
        for camera_id in stream_links.keys():
            stream = cv2.VideoCapture(stream_links[camera_id])
            ret, frame = stream.read()

            cv2.imwrite(get_new_image_uri(camera_id), frame)

        if cv2.waitKey(image_interval) == 27:  # Esc
            sys.exit()
