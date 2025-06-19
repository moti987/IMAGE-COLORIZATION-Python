import numpy as np
import cv2
import imutils
def colorizer(img_path):
    proto='Model\color\colorization_deploy_v2.prototxt'
    model='Model\color\colorization_release_v2.caffemodel'
    hull_pts='Model\color\pts_in_hull.npy'
    network=cv2.dnn.readNetFromCaffe(proto,model)
    kernel=np.load(hull_pts)
    image=cv2.imread(img_path)
    scaled=image.astype("float32")/255.0
    lab=cv2.cvtColor(scaled,cv2.COLOR_BGR2LAB)
    class8 = network.getLayerId("class8_ab")
    conv8 = network.getLayerId("conv8_313_rh")
    pts = kernel.transpose().reshape(2, 313, 1, 1)
    network.getLayer(class8).blobs = [pts.astype("float32")]
    network.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]
    resize=cv2.resize(lab,(244,244))
    L=cv2.split(resize)[0]
    L=L-50
    network.setInput(cv2.dnn.blobFromImage(L))
    ab_channel = network.forward()[0, :, :, :].transpose((1, 2, 0))
    ab_channel = cv2.resize(ab_channel, (image.shape[1], image.shape[0]))
    L = cv2.split(lab)[0]
    colorize = np.concatenate((L[:, :, np.newaxis], ab_channel), axis=2)
    colorize = cv2.cvtColor(colorize, cv2.COLOR_LAB2BGR)
    colorize = np.clip(colorize, 0, 1)
    colorize = (255 * colorize).astype("uint8")
    #colorize=cv2.resize(colorize,(1280,720))
    #colorize = imutils.resize(colorize, width=480)
    return colorize

img='C:/Users/afzal/Documents/Studies/Stuff/cs351p/image/postprocessed/postprocessed.png'
img='postprocessed.'+img.split('.')[1]
