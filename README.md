# Marriage-age-prediction

This prject is about predicting  your marriage age.

### Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model), joblib (to load model) and Flask.

### Project Structure
The project major parts are:

- app.py - This contains main file that receives age prediction details through GUI and computes the precited value based on our model and returns it.
- index.html - This file contain code for front end.
- data - Contain the cleaned data
- train-model/Marriage-age-prediction.ipynb - This file contain all the code about EDA, Feature selection, Model evaluation etc and finally save the model.
- model - This folder contains all the train model ready to use

### Running the project
- Download the zip file
- Go to project folder and run `pip install -r requirements.txt`
- `flask run`
