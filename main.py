trainX2 = []
trainY2 = []
import os
import cv2
import numpy as np
import pyautogui

def averagecolor(image):
    return np.mean(image, axis=(0, 1))
path = "D:/Programming/CV_game_controller/Data/"
for label in ('Up','Straight'):
    print ("Loading training images for the label: "+label)
    
    #Load all images inside the subfolder                                                                                        
    for filename in os.listdir(path+label+"/"): 
        img = cv2.imread(path+label+"/"+filename)
        img_features = averagecolor(img)                                             
        trainX2.append(img_features)                              
        trainY2.append(label)
from sklearn.preprocessing import LabelEncoder  #encode labels into numerical  
encoder = LabelEncoder()                        #encode labels into numerical
encodedtrainY2 = encoder.fit_transform(trainY2) #encode labels into numerical

from sklearn import svm
model = svm.SVC(gamma="scale", decision_function_shape='ovr')
model.fit(trainX2, encodedtrainY2)

cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    img_features = averagecolor(frame)
    prediction = model.predict([img_features])[0]
    
    prediction = encoder.inverse_transform([prediction])[0]                                                   
    cv2.putText(frame,prediction,(100,100), cv2.FONT_HERSHEY_DUPLEX,1, (0,0,0), 2)
    cv2.imshow("Frame",frame)
    if prediction == "Up":
        pyautogui.press('Space')
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()