import os
import dlib
import cv2
import argparse
import random
import string
import numpy as np
from tqdm import tqdm

if not os.path.exists('faces'):
    os.makedirs('faces')

if not os.path.exists('tmp'):
    os.makedirs('tmp')

def generate_random_string(length=5):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))

def capture_image():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return None

    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to capture frame.")
        return None

    cap.release()
    cv2.destroyAllWindows()

    return frame

def save_face_images(name):
    save_dir = os.path.join('faces', f'{name}_{generate_random_string()}')
    os.makedirs(save_dir, exist_ok=True)

    for i in range(5):
        input("Press Enter to capture image...")
        frame = capture_image()
        if frame is not None:
            cv2.imwrite(os.path.join(save_dir, f'{name}_{i+1}.jpg'), frame)
            print(f"Image {i+1} saved successfully.")
        else:
            print(f"Error: Unable to capture image {i+1}.")

def save_tmp_images():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    for i in range(5):
        ret, frame = cap.read()
        if not ret:
            print(f"Error: Unable to capture frame {i+1}.")
            continue

        cv2.imwrite(os.path.join('tmp', f'tmp_{i+1}.jpg'), frame)

    cap.release()
    cv2.destroyAllWindows()


def load_saved_faces():
    faces_dir = 'faces'
    saved_faces = []
    if not os.path.exists(faces_dir):
        print("Error: 'faces' directory does not exist.")
        return None

    for root, dirs, files in os.walk(faces_dir):
        for file in files:
            if file.endswith(".jpg"):
                face_path = os.path.join(root, file)
                saved_face = cv2.imread(face_path)
                saved_faces.append(saved_face)
    return saved_faces

def match_face(face, saved_faces):
    face_detector = dlib.get_frontal_face_detector()
    matched_images = []
    for saved_face in saved_faces:
        saved_face_gray = cv2.cvtColor(saved_face, cv2.COLOR_BGR2GRAY)
        detected_faces = face_detector(saved_face_gray, 1)

        if len(detected_faces) > 0:
            shape = sp(saved_face_gray, detected_faces[0])
            face_descriptor_saved = facerec.compute_face_descriptor(saved_face, shape)
            face_descriptor_tmp = facerec.compute_face_descriptor(face, shape)

            distance = np.linalg.norm(np.array(face_descriptor_saved) - np.array(face_descriptor_tmp))

            if distance < 0.6:
                matched_images.append(saved_face)
                return True
    return False



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Face Capture and Match CLI")
    parser.add_argument('--save-face', metavar='NAME', help="Name for saving face images")
    parser.add_argument('--match', action='store_true', help="Match face with saved faces")

    args = parser.parse_args()

    if args.save_face:
        name = args.save_face
        save_face_images(name)
    elif args.match:
        save_tmp_images()
        saved_faces = load_saved_faces()
        if saved_faces is not None:
            predictor_path = "./models/shape_predictor_68_face_landmarks.dat"
            facerec_path = "./models/dlib_face_recognition_resnet_model_v1.dat"

            detector = dlib.get_frontal_face_detector()
            sp = dlib.shape_predictor(predictor_path)
            facerec = dlib.face_recognition_model_v1(facerec_path)

            successful_matches = 0

            for i in tqdm(range(5), desc="Matching Progress"):
                tmp_face_path = os.path.join('tmp', f'tmp_{i+1}.jpg')
                tmp_face = cv2.imread(tmp_face_path)

                if tmp_face is not None:
                    if match_face(tmp_face, saved_faces):
                        successful_matches += 1

            success_percentage = (successful_matches / 5) * 100
            print(f"Success rate: {success_percentage}%")
    else:
        print("Error: Please provide a valid command.")
