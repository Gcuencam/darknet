import os
import consts
import shutil

if not os.path.exists(consts.DIR_TRAIN_IMAGES):
  os.makedirs(consts.DIR_TRAIN_IMAGES)

for root, dirs, files in os.walk(consts.DIR_TEAMS_IMAGES):  # replace the . with your starting directory
  for file in files:
    path_file = os.path.join(root,file)
    try:
      shutil.copy2(path_file, consts.DIR_TRAIN_IMAGES) # change you destination dir
    except shutil.Error:
      pass

for i, image in enumerate(os.listdir(consts.DIR_TRAIN_IMAGES)):
    path = os.path.join(consts.DIR_TRAIN_IMAGES, image)
    if (image[-4:] == ".JPG" or image[-4:] == ".jpg" or image[-5:] == ".jpeg") and image[:5] != "train":
      target = os.path.join(consts.DIR_TRAIN_IMAGES, "train_" + str(i).zfill(2) +  ".jpg")
      os.rename(path, target)
    elif image[-4:] == ".png" and image[:5] != "train":
      target = os.path.join(consts.DIR_TRAIN_IMAGES, "train_" + str(i).zfill(2) +  ".png")
      os.rename(path, target)

