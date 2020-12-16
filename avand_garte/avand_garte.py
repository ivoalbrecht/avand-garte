# -*- coding: utf-8 -*-

"""Main module."""

import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from predict import predict_genre, match_genre

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        if 'file' not in request.files:
            return render_template('index.html')

        file = request.files['file']

        if file.filename == '':
            return render_template('index.html')

        scores, genres = predict_genre(file, 5, percentage=True)

        return render_template('index.html', scores_html = scores, genres_html = genres, anchor="results")
        
    return render_template('index.html')

if __name__ == "__main__":

    app.run(debug=True, port=5000)
