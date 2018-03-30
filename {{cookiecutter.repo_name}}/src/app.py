from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
fromm sklearn.externals import joblib
model = joblib.load('logmodel.pkl')

@app.route('/predict',methods=['GET'])
def predict():
  answer = model.predict(sonuclar)

    
if __name__ == '__main__':
	app.run(debug=False, host="0.0.0.0")
