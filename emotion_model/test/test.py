from keras.models import load_model
from keras.preprocessing.image import load_img
import numpy as np
from keras.models import load_model
from keras.models import model_from_json
model = model_from_json(open("model.json", "r").read())
model.load_weights('model.h5')
image = load_img('sad.jpg', target_size=(224, 224))
img = np.array(image)
img = img / 255.0
img = img.reshape(1,224,224,3)
label = model.predict(img)
labels={0:"Angry",1:"Disguist",2:"Fear",3:"Happy",4:"Neutral",5:"Sad",7:"Surprise"}
label=label.tolist()[0]
max=label.index(max(label))
print(labels[5])