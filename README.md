# ECE176Project
A classification project of landmarks using different Neural Networks. 

## Dataset

### Google Landmark Dataset V2

https://github.com/cvdfoundation/google-landmark

To download the dataset, we created the Python file LandmarkFilterer.py, which takes an input of Landmark IDs and iterates through the train.csv file (https://s3.amazonaws.com/google-landmark/metadata/train.csv) provided by the Google Landmark Dataset. This filtering file will download all of the images that match the Landmark IDs provided, download the image, and resize it to 256x256 pixels. 

Examples of our dataset's classes are provided below. 

![image](https://github.com/crae6/LandmarkClassifier/assets/122562172/4250050b-f3f4-45c3-b3c1-4c339d3baf64)

## Models
In this project, we explore the classification performance of various CCN networks and tailor them to best fit our data.

### ResNet-10
- Description: This was our first model and came from the homework implementation. We adjusted the padding to get higher accuracies with our classes, but, overall, we found this to be a very fitting network.
- Training Details: batch size: 64, optimizer: SGD, learning rate: 0.002, weight decay: 0.0001, momentum: 0.9
- Accuracy: 87% Validation Accuracy

### ResNet-34
- Description: A deeper version of ResNet that provides higher accuracy at the cost of increased computational complexity.
- Training Details: batch size: 64, optimizer: SGD, learning rate: 0.002, weight decay: 0.0001, momentum: 0.9
- Accuracy: 

### AlexNet
- Description:
- Training Details: batch size: 64, optimizer: SGD, learning rate: 0.002, weight decay: 0.0001, momentum: 0.9
- Accuracy: 

### VGG-16
- Description: A deep convolutional network known for its simplicity and depth.
- Training Details: batch size: 32, optimizer: SGD, learning rate: 0.002, weight decay: 0.0001, momentum: 0.9
- Accuracy: 

## GUI
- Our graphical user interface allows the user to input an image from their computer, and each model will display its individual result.

## GUI Usage
### Requirements
- Python 3.7 or newer

### Installation
1. **Download**
- First, download the zip file and unzip it
2. **Create a Virtual Environment (Optional)**
- python -m venv LandmarkClasGUI
- Activate the virtual environment:
    - On Windows:
    `.\LandmarkClasGUI\Scripts\activate`
    - On macOS and Linux:
    `source LandmarkClasGUI/bin/activate`
3. **Install Dependencies**
- Install the required packages using 
`pip install -r requirements.txt`
