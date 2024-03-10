# ECE176Project
A classification project of landmarks using different Neural Networks. 

## Dataset

### Google Landmark Dataset V2

https://github.com/cvdfoundation/google-landmark

To download the dataset we created the Python file LandmarkFilterer.py which takes an input of Landmark ID's and iterates through the train.csv file (https://s3.amazonaws.com/google-landmark/metadata/train.csv) provided by the Google Landmark Dataset. This filtering file will download all of the images that match the Landmark ID's provided, download the image, and resize it to 128x128 pixels. 

Examples of our dataset's classes are provided below. 

![image](https://github.com/crae6/LandmarkClassifier/assets/122562172/41eb63d9-68bf-4d2a-ad46-57f300c7b07d)
