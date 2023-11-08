import os
import sys
import requests
import bz2
from tqdm import tqdm

# Define model URLs
SHAPE_PREDICTOR_URL = "http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2"
FACE_RECOGNITION_MODEL_URL = "http://dlib.net/files/dlib_face_recognition_resnet_model_v1.dat.bz2"

# Function to download and extract bz2 files
def download_and_extract(url, filename):
    print(f"Downloading {filename}...")
    response = requests.get(url, stream=True)
    
    total_size_in_bytes = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    
    filepath = os.path.join('models', filename)
    
    with open(filepath, 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()
    
    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print("ERROR, something went wrong")
    
    print(f"Downloaded {filename}")

    # Extract the file
    with bz2.BZ2File(filepath) as file:
        decompressed_data = file.read()
        new_filepath = filepath[:-4]  # remove .bz2 from filename
        with open(new_filepath, 'wb') as new_file:
            new_file.write(decompressed_data)
    print(f"Extracted {filename} to {new_filepath}")

    # Remove the compressed file
    os.remove(filepath)

# Ensure the 'models' directory exists
def ensure_models_directory():
    if not os.path.exists('models'):
        os.makedirs('models')

# Downloading and extracting the files
def main():
    ensure_models_directory()
    download_and_extract(SHAPE_PREDICTOR_URL, "shape_predictor_68_face_landmarks.dat.bz2")
    download_and_extract(FACE_RECOGNITION_MODEL_URL, "dlib_face_recognition_resnet_model_v1.dat.bz2")

if __name__ == "__main__":
    main()
