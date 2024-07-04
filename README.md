# Face Recognition Lock

This project utilizes OpenCV to implement a face recognition system that locks the laptop if an unknown face or no face is detected for a certain period.

## Features

- Face Dataset Creation: Captures face images and saves them to a dataset for training.
- Model Training: Trains an LBPH (Local Binary Pattern Histogram) face recognizer model using the captured dataset.
- Face Recognition and Lock: Recognizes faces in real-time and locks the laptop if an unknown face or no face is detected.

## Requirements

- Python 3.x
- OpenCV
- NumPy
- Pillow (PIL)

 Setup

 Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/face-recognition-lock.git
    cd face-recognition-lock
    ```

2. Install the required packages:

    ```bash
    pip install opencv-python opencv-contrib-python numpy Pillow
    ```

### Preparing Dataset

1. Run the `create_dataset.py` script to capture face images:

   
## Usage

1. **Create Dataset**: Run the `create_dataset.py` script to capture images of your face and save them in the dataset directory.
2. **Train Model**: Run the `training_model.py` script to train the face recognizer model.
3. **Run Face Recognition**: Run the `recognition.py` script to start the face recognition process. The laptop will lock if an unknown face or no face is detected for more than 8 seconds.

## Acknowledgments

- [OpenCV](https://opencv.org/) for providing the tools for computer vision tasks.
- The [Pillow](https://python-pillow.org/) library for image processing.
