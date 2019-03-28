import keras
import numpy as np
import cv2
import time
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('hello.log')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)


class NN():
	def __init__(self):
		self.model = keras.models.load_model("MODEL")
	def decision(self):
		img = keras.preprocessing.image.load_img("picture.png", target_size=(28 ,28))

		print(img)
#		cv2.imshow("img", cv2.imread("picture.png", 0))
#		cv2.waitKey(0)
#		cv2.destroyAllWindows()
		#convert img to grey scale
		img = img.convert("L")
		x = keras.preprocessing.image.img_to_array(img)
		logger.info((x))
		x = np.expand_dims(x, axis=0)
		logger.info((x))
		classes = self.model.predict(x)
		print(classes[0])

#X = NN()
#X.decision()
NN().decision()
