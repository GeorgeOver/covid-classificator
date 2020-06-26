from tensorflow.keras.models import load_model
import numpy as np
import argparse
import cv2
from tensorflow.keras.preprocessing import image as kerasImage

"""
Загружаем обученную модель
"""

def loadModel(path):
    loaded_model = load_model(path)
    return loaded_model

"""
Классификация одного изображения
0 = covid
1 = normal
"""
def classifySingleImage(imgSrc, model):
    image = cv2.imread(imgSrc)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (224, 224))
    x = kerasImage.img_to_array(image)
    x = np.expand_dims(x, axis=0)
    x = x * 1./255 
    prediction = model.predict(x)
    prediction = np.argmax(prediction, axis=1)
    return prediction
