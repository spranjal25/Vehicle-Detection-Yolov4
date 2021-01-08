# Vehicle Detection using Yolov4

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

This Repository walks you through building, training and running your own YOLOv4 object detector. This application deals with a vehicle dataset and vehicle detection which is used in other applications as well.

  - Obtain dataset according to your needs
  - Prepare the data for training (Darknet Compatibility)
  - Train and test custom detection model

### Key features of YOLOv4!

  - Incorporation of Data-Augmentation.
  - Bag of freebies
    - Focal Loss
    - IOU Loss
    - Label Smoothing
 - Mish Activation - Bag of speacials

#### Lets start with the implementation!

#### Preparing the training data
- **Bounding boxes List**
    We need a .txt-file for each .jpg-image-file - in the same directory and with the same name, but with .txt-extension, and put to file: object number and object coordinates on this image, for each object in new line:

    `<object-class> <x_center> <y_center> <width> <height>`
    Where:
    - `<object-class>` - integer object number from 0 to (classes-1)
    - `<x_center>` `<y_center>` `<width>` `<height>` - float values relative to width and height of image, it can be equal from (0.0 to 1.0]
    - for example: `<x>` = `<absolute_x>` / `<image_width>` or `<height>` = `<absolute_height>` / `<image_height>`
    - atention: `<x_center>` `<y_center>` - are center of rectangle (are not top-left corner)

>We are using the [IDD Dataset](https://idd.insaan.iiit.ac.in/) released by IIIT-Hyderabad in colaboration with Intel.
>The dataset is provided with csv file with the coordinates of bounding boxes of each object in each image 

- **List of Objects - NAMES File**
      Create a list of all the objects that need to be detected, one in each line. Name it as *obj.names*

- **Training List**
    Create a list of training files with the paths of each training file in a line, .txt extension
    Use the given python file for the generation.

- **DATA File**
    Create a file - Obj.data with the contents:

        classes = <num of classes to be detected>
        train  = data/train.txt
        valid  = 
        names = data/obj.names
        backup = /mydrive/Yolov4/backup

#### Steps to proceed
1. Clone the repository from [AlexeyAB's Darknet](https://github.com/AlexeyAB/darknet)
2. Change the *.cfg* file accordingly to get a *yolov4_custom.cfg* 
    -  change line batch to `batch=64`
    - change line subdivisions to `subdivisions=16`
    - change line max_batches to (`classes*2000` but not less than number of training images, but not less than number of training images and not less than 6000), f.e. `max_batches=6000` if you train for 3 classes
    - change line steps to `80% and 90% of max_batches`, f.e. steps=4800,5400
    - set network size width=416 height=416 or any value multiple of 32 (i have used 608)
    - change line classes=80 to your number of objects in each of 3 `[yolo]`-layers
    - change [filters=255] to `filters=(classes + 5)x3` in the 3 `[convolutional]` before each `[yolo]` layer, keep in mind that it only has to be the last `[convolutional]` before each of the `[yolo]` layers
    - when using [Gaussian_yolo] layers, change `[filters=57]` filters=(classes + 9)x3 in the 3 `[convolutional]` before each `[Gaussian_yolo]` layer
    - save this *`yolov4_custom.cfg`*

##### Create a folder in google drive - `'Yolov4'`
Upload all these files - `obj.data`, `obj.names`, `train.txt`, `yolov4_custom.cfg` in it.

### Next up - Follow the jupyter notebook!
