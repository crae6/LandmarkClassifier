# ECE176Project
A classification project of landmarks using different Neural Networks. 

## Dataset

### Google Landmark Dataset V2

https://github.com/cvdfoundation/google-landmark

To download the dataset we created the Python file LandmarkFilterer.py which takes an input of Landmark ID's and iterates through the train.csv file (https://s3.amazonaws.com/google-landmark/metadata/train.csv) provided by the Google Landmark Dataset. This filtering file will download all of the images that match the Landmark ID's provided, download the image, and resize it to 256x256 pixels. 

Examples of our dataset's classes are provided below. 

![image](https://github.com/crae6/LandmarkClassifier/assets/122562172/4250050b-f3f4-45c3-b3c1-4c339d3baf64)

## ResNet-10

## ResNet-34

## AlexNet

## VGG-16

## GUI
