<p align="center">
  <img src='images/DlibCover.png' alt="Dlib Cover" height='300px'>
</p>

# FacialKey

FacialKey is a Python-based face recognition application that captures images via a webcam and uses machine learning models to perform face detection and recognition tasks.

## Installation

To get started with FacialKey, clone the repository to your local machine and install the required dependencies.

```bash
git clone https://github.com/StunsIO/FacialKey.git
cd FacialKey
pip3 install -r requirements.txt
```

## Usage

FacialKey can be operated in two modes:

1. **Saving face images**: Use this mode to save new face images for a person.

2. **Matching faces**: Use this mode to match captured faces with those that have been previously saved.

### Saving Face Images

To save face images associated with a name, run the script with the `--save-face` argument followed by the person's name:

```bash
python3 face_recognition.py --save-face Mohd
```

This will capture and save the images in the `faces` directory under a subdirectory named after the person.

### Matching Faces

To match a face with the saved faces, simply run the script with the `--match` argument:

```bash
python3 face_recognition.py --match
```

This will capture a temporary face image and attempt to match it with the saved faces in the `faces` directory.

Ensure that you have the necessary models downloaded by executing `download_models.py` before running the above commands.

### Downloading Models

Before running the face recognition script, ensure that the necessary models are downloaded:

```bash
python3 download_models.py
```

This will download and extract the models into the `models` directory.


# File Structure

The following is the structure of the project, outlining the main components and their purpose:

```
FacialKey/
│
├── download_models.py      # Script to download model files into the 'models' directory.
├── face_recognition.py     # Main application script for face recognition tasks.
├── requirements.txt        # Python dependencies for the project.
│
├── faces/                  # Directory where face images captured by the app are stored.
├── models/                 # Machine learning models for face detection and recognition.
└── tmp/                    # Directory for temporary images used for matching.
```

## Detailed Description:

- `download_models.py`: A Python script that automatically downloads the dlib models required for the face detection and recognition tasks and places them into the `models/` directory.

- `face_recognition.py`: This is the main Python script that handles face capturing from a webcam and face recognition. It uses the models downloaded by `download_models.py`.

- `requirements.txt`: Contains a list of all Python packages needed to run the application. To install them, run `pip3 install -r requirements.txt`.

- `faces/`: This directory is automatically created when the application runs. It stores the face images that are captured by the application.

- `models/`: Holds the face detection and recognition models that are downloaded by `download_models.py`. This directory is created automatically by the script if it does not exist.

- `tmp/`: A directory used by the application to store temporary images during the face recognition process. It's also automatically created when the application runs.

Please make sure to run `download_models.py` before using `face_recognition.py` to ensure that all necessary models are correctly set up in the `models/` directory. The `faces/` and `tmp/` directories are created and managed by the application scripts.

## Acknowledgments

- Dlib Library
- OpenCV

## License

This project is licensed under the GNU GENERAL PUBLIC License - see the [LICENSE](LICENSE) file for details.
