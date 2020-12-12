from tensorflow import keras
import numpy as np



# def predict():
model_path = "/Users/ivoalbrecht/projects/avand_garte/avand_garte/models/MobileNetV2_10_testing=True"
picture_path = "/Users/ivoalbrecht/projects/avand_garte/avand_garte/pictures/mandelbrot.png"
model = keras.models.load_model(model_path)
model.summary()

pic = keras.preprocessing.image.load_img(picture_path,target_size=(224,224))
numpy_image = keras.preprocessing.image.img_to_array(pic)
image_batch = np.expand_dims(numpy_image, axis=0)
# stacked = np.stack(image_batch,image_batch)
print(image_batch.shape)
#print(stacked.shape)
processed_image = keras.applications.mobilenet_v2.preprocess_input(image_batch)
prediction = model.predict(processed_image)
# print(prediction)