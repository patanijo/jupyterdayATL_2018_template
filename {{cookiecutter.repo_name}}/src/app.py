from flask import Flask, request, jsonify
import 

from sklearn.metrics import log_loss
from sklearn.externals import joblib

app = Flask(__name__)

@app.route('/predict',methods=['POST'])
def predict():
  json_ = request.json
  query = pd.DataFrame(json_).values
  prediction = clf.predict(query)
  return jsonify({'prediction': list(prediction)})

@app.route('/monitor',methods=['GET'])
def monitor():
  return {'Not Implemented'}

if __name__ == '__main__':
  clf = joblib.load('_model.pkl')
  app.run(debug=False, host="0.0.0.0")
