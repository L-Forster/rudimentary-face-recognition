from saveCam import *
from recog import *
j=0
while j<=3 :
    images()
    if check_faces():
        print("Success")
        break
    j +=1 