from tensorflow import keras
import numpy as np
#from PIL import image

# def predict():
model_path = "/Users/ivoalbrecht/projects/avand_garte/avand_garte/models/mobilenetV2"
picture_path = "/Users/ivoalbrecht/projects/avand_garte/avand_garte/pictures/mandelbrot.png"
model = keras.models.load_model(model_path)
model.summary()

# pic = keras.preprocessing.image.load_img(picture_path,target_size=(224,224))
# numpy_image = keras.preprocessing.image.img_to_array(pic)
# image_batch = np.expand_dims(numpy_image, axis=0)
# processed_image = keras.applications.mobilenet_v2.preprocess_input(image_batch)
# prediction = model.predict(processed_image)
# print(prediction)