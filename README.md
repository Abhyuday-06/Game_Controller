# Computer Vision Game Controller

This project uses computer vision to control a game based on the average color of the webcam feed. The script captures video from a webcam, calculates the average color of each frame, and uses a trained Support Vector Machine (SVM) model to predict the user's intended action.

## Dependencies

The following dependencies are required to run this project:

- `opencv-python`: For capturing video from the webcam and image processing.
- `numpy`: For numerical operations, especially for calculating the average color of an image.
- `pyautogui`: For simulating keyboard presses to control the game.
- `scikit-learn`: For training and using the SVM model.

You can install these dependencies using pip:

```bash
pip install opencv-python numpy pyautogui scikit-learn
```

## How to Use

### 1. Structure the Training Data

Create a `Data` directory in the same directory as the `main.py` script. Inside the `Data` directory, create subdirectories for each label you want to train the model on. For example, if you want to train the model to recognize "Up" and "Straight", you would create the following directory structure:

```
.
├── main.py
└── Data
    ├── Up
    │   ├── image1.jpg
    │   ├── image2.jpg
    │   └── ...
    └── Straight
        ├── imageA.jpg
        ├── imageB.jpg
        └── ...
```

Place the training images for each label in the corresponding subdirectory.

### 2. Run the Script

Once you have structured the training data, you can run the `main.py` script:

```bash
python main.py
```

The script will:

1.  Load the training images from the `Data` directory.
2.  Train an SVM model on the training images.
3.  Open a webcam feed.
4.  For each frame in the webcam feed, it will predict the user's action based on the average color of the frame.
5.  If the predicted action is "Up", it will simulate a "Space" key press.
6.  The script will display the webcam feed with the predicted action overlaid on the image.

To quit the script, press the "q" key.

## How it Works

The script works by calculating the average color of each frame in the webcam feed. The average color is then used as a feature to train an SVM model. The SVM model learns to classify the average color of a frame into one of the labels defined in the `Data` directory.

When the script is running, it continuously captures frames from the webcam, calculates the average color of each frame, and uses the trained SVM model to predict the user's action. The predicted action is then used to control the game by simulating keyboard presses.
