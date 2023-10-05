import cv2
import os
# Opens the inbuilt camera of laptop to capture video.
def images():
    cap = cv2.VideoCapture(0)
    i = 1
    
    while(cap.isOpened()) and i<=30:
        ret, frame = cap.read()
        
        # This condition prevents from infinite looping
        # incase video ends.
        if ret == False:
            break
        
        # Save Frame by Frame into disk using imwrite method
        path = "insert dir"
        cv2.imwrite(os.path.join(path, "Frame"+str(i)+".jpg"), frame)
        i += 1
    
    cap.release()
    cv2.destroyAllWindows()
