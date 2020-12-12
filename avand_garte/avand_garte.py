# -*- coding: utf-8 -*-

"""Main module."""

from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


@app.route("/index")
@app.route("/")
def index():
    
    return render_template("index.html",)

# @app.route("/recommend")
# def recommend():

#     user_input = dict(request.args)
    
#     if MODEL == "NMF":
#         game_list = ml_models.nmf_recommender(user_input, NUMBER_OF_RECOM)
#     if MODEL == "CoSim":
#         game_list = ml_models.cosim_recommender(user_input, NUMBER_OF_RECOM)

#     image_list = get_images_from_game_list(game_list)

#     return render_template("recommendations.html", results_html = zip(game_list, image_list))


if __name__ == "__main__":

    app.run(debug=True, port=5000)