from keras.models import load_model
import tensorflow as tf
#from tensorflow.keras.preprocessing.image import load_img
import numpy as np
from keras.models import load_model
from keras.models import model_from_json
def detect_emotion(img_path):
    model = model_from_json(open("Model//emotion//model.json", "r").read())
    model.load_weights('Model//emotion//model.h5')
    image = tf.keras.utils.load_img(img_path, target_size=(224, 224))
    img = np.array(image)
    img = img / 255.0
    img = img.reshape(1,224,224,3)
    label = model.predict(img)
    labels={0:"Angry",1:"Disguist",2:"Fear",3:"Happy",4:"Neutral",5:"Sad",7:"Surprise"}
    label=label.tolist()[0]
    max_index=label.index(max(label))
    return labels[max_index]