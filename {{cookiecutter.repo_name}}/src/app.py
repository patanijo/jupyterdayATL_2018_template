from flask import Flask, request, render_template
import pickle
import numpy as np

from sklearn.metrics import log_loss

app = Flask(__name__)
from sklearn.externals import joblib
model = joblib.load('logmodel.pkl')

@app.route('/predict',methods=['GET'])
def predict():
#  X =
  answer = model.predict()

@app.route('/monitor',methods=['GET'])
def monitor():
#  X = 
#  y_true =
#  y_pred = model.predict(X)
    
if __name__ == '__main__':
	app.run(debug=False, host="0.0.0.0")
