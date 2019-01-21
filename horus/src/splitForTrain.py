import os
import consts
import subprocess

# Time for MacBook Pro 2015, 2,7 GHz Intel Core i5, 8 GB 1867 MHz DDR3, Intel Iris Graphics 6100 1536 MB.
# 100 images -> 12 min.
for i, image in enumerate(os.listdir(consts.DIR_TRAIN_IMAGES)):
  path = os.path.join(consts.DIR_TRAIN_IMAGES, image)
  darknet = subprocess.call([
    "./darknet", 
    "detect", 
    "cfg/yolov2.cfg",
    "yolo.weights",
    path,
    "-thresh",
    "0.75",
    "-training", 
    "1"
    ])
  print(darknet)

# ./darknet detect cfg/yolov2.cfg yolo.weights ./teams/PSG/train/yes/5985f5da482ef.jpeg -thresh 0.6 -training