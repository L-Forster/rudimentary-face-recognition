import face_recognition
import os
import cv2
from face_recognition.api import face_locations




def check_faces():
    KNOWN_FACES_DIR = "put dir here"
    UNKNOWN_FACES_DIR = "put other dir here"
    TOLERANCE = 0.6
    FRAME_THICKNESS = 3
    FONT_THICKNESS = 2
    MODEL = "hog" #hog for pi cnn for gpu
    match_count = 0
    total_count = 0
    known_faces = []
    known_names = []

    print("Loading known faces..")
    for name in os.listdir(KNOWN_FACES_DIR):
        for filename in os.listdir(f"{KNOWN_FACES_DIR}/{name}"):
            image = face_recognition.load_image_file(f"{KNOWN_FACES_DIR}/{name}/{filename}")
            encoding = face_recognition.face_encodings(image)[0]
            known_faces.append(encoding)
            known_names.append(name)    

    for filename in os.listdir(UNKNOWN_FACES_DIR):
        print(filename)
        image = face_recognition.load_image_file(f"{UNKNOWN_FACES_DIR}/{filename}")
        locations = face_recognition.face_locations(image, model = MODEL)
        encodings = face_recognition.face_encodings(image, locations)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        for face_encoding, face_location in zip(encodings, locations):
            results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
            match = None
            if True in results:
                match = known_names[results.index(True)]
                print("Match found: {match}")
                
                top_left = (face_location[3], face_location[0])
                bottom_right = (face_location[1], face_location[2])
                color = [0, 255, 0]
                cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)
    
                top_left = (face_location[3], face_location[2])
                bottom_right = (face_location[1], face_location[2]+22)
                cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
                cv2.putText(image, match, (face_location[3]+10, face_location[2]+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200,200,200), FONT_THICKNESS)
                match_count += 1
            total_count += 1    
        print(total_count)
        print(match_count)
        
    if total_count == 30 and match_count/total_count > 0.9 and total_count >0:
        return True
        
        
        
        
