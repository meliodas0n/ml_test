import catboost as cb
import pandas as pd

from flask import Flask, jsonify, request

model = cb.CatBoostClassifier()
model.load_model('loan_catboost_model.cbm')

app = Flask('default')

@app.route('/predict', methods = ['POST'])
def predict():
  x = request.get_json()
  preds = model.predict_proba(pd.DataFrame(x, index = [0]))[0, 1]
  result = {"default_probability" : preds}
  return jsonify(result)

if __name__ == "__main__":
  app.run(debug = True, host = "0.0.0.0", port = 8989)