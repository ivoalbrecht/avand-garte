from tensorflow import keras
import numpy as np

genres_list = ['portrait', 'landscape', 'genre painting', 'abstract', 
'religious painting', 'cityscape', 'sketch and study', 'illustration', 'still life', 
'symbolic painting', 'nude painting (nu)', 'figurative', 'design', 
'mythological painting', 'marina', 'flower painting', 'animal painting', 'self-portrait', 
'allegorical painting', 'history painting']

def match_genre(score):
    """
    This u
    """
    decimals = 0
    genre_dict = {}

    for i, j in zip(score, genres_list):

        genre_dict[j] = round(i,decimals)

    return genre_dict

def predict_genre(file, num_pred: int, percentage: bool):
    """
    This 
    """
    model_path = "/Users/ivoalbrecht/projects/avand_garte/avand_garte/models/mobilenetV2"
    model = keras.models.load_model(model_path)

    pic = keras.preprocessing.image.load_img(file, target_size=(244,244))

    numpy_image = keras.preprocessing.image.img_to_array(pic)

    image_batch = np.expand_dims(numpy_image, axis=0)

    processed_image = keras.applications.mobilenet_v2.preprocess_input(image_batch)

    prediction = model.predict(processed_image).reshape(len(genres_list))

    prediction_list = prediction.tolist()

    if percentage == True:
        prediction_list = [element * 100 for element in prediction_list]

    results_dict = match_genre(prediction_list)

    sort_results = sorted(results_dict.items(), key=lambda x: x[1], reverse=True)

    return sort_results[:num_pred]
