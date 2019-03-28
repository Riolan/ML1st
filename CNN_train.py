import PIL.ImageOps
import keras
import cv2
import numpy as np
from matplotlib import pyplot as plt
model = keras.models.load_model("MODEL")
model.compile(loss="categorical_crossentropy", optimizer="sgd", metrics=["accuracy"])


from keras.utils import to_categorical
from keras.datasets import mnist
def data_set():
	(x1, y1), (x2, y2) = mnist.load_data()

	x1 = x1.reshape((60000, 28, 28, 1))
	x1 = x1.astype('float32') / 255
	x2 = x2.reshape((10000, 28, 28, 1))
	x2 = x2.astype('float32') / 255

	y1 = to_categorical(y1)
	y2 = to_categorical(y2)

#model.fit(x1, y1, batch_size = 100, epochs = 5, verbose=1)
#model.save("MODEL")
	test_loss, test_acc = model.evaluate(x2, y2)
	print("TEST LOSS: ",test_loss, "TEST ACC: ", test_acc)
def run_test():
	img = keras.preprocessing.image.load_img("picture.png", target_size=(28, 28), color_mode="grayscale")
	img = PIL.ImageOps.invert(img)
	img = keras.preprocessing.image.img_to_array(img)
	#img = x1[0]
	#print(img.shape)
	#plt.figure()
	#plt.imshow(img.reshape((28, 28)), cmap="gray")
	#plt.show()
	img = img.reshape((1,) + img.shape)
	img = img.astype("float32") / 255
	classes = model.predict_classes(img)
	print(classes)
