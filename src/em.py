import keras
import cv2
from keras.models import model_from_json
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator

import numpy as np

model = model_from_json(open(r"model/facial_expression_model_structure.json", "r").read())
model.load_weights(r'model/facial_expression_model_weights.h5')  # load weights



face_cascade = cv2.CascadeClassifier(r'model/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)


emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')

def camclick(img):

    detected_face = img #crop detected face
    detected_face = cv2.cvtColor(detected_face, cv2.COLOR_BGR2GRAY) #transform to gray scale
    detected_face = cv2.resize(detected_face, (48, 48)) #resize to 48x48

    img_pixels = image.img_to_array(detected_face)
    img_pixels = np.expand_dims(img_pixels, axis = 0)

    img_pixels /= 255 #pixels are in scale of [0, 255]. normalize all pixels in scale of [0, 1]

    predictions = model.predict(img_pixels) #store probabilities of 7 expressions

    #find max indexed array 0: angry, 1:disgust, 2:fear, 3:happy, 4:sad, 5:surprise, 6:neutral
    max_index = np.argmax(predictions[0])

    emotion = emotions[max_index]

    print (emotion)
    return emotion
