import os

import flask
from flask import request, render_template, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import math

app = flask.Flask(__name__)

app.config['DEBUG'] == True

CORS(app)

# load model
model_dt = joblib.load('model/marriage_age_predict_dtr.ml')
model_rf = joblib.load('model/marriage_age_predict_rf.ml')


@app.route('/')
def home():
	return render_template('index.html')


@app.route('/predict', methods =['POST'])
def predict():
	int_features = [int(x) for x in request.form.values()]

	final_feature = np.array(int_features)

	
	if final_feature[-1] == 10:
		prediction = model_rf.predict(final_feature.reshape(1,-1)[:,:-1])
	else:
		prediction = model_dt.predict(final_feature.reshape(1,-1)[:,:-1])

	output = round(prediction[0])

	return render_template('index.html', prediction= math.ceil(output))


if __name__ == '__main__':
	main()