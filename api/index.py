from flask import Flask, jsonify, request
import pandas as pd
import json
import os
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/test')
def test():
    return 'Test'

@app.route('/api/get_dataset')
def get_dataset():
    train_X = pd.read_csv(os.getcwd()+'/static/'+'train_x.csv', header=None)
    train_y = pd.read_csv(os.getcwd()+'/static/'+'train_y.csv', header=None)
    
    result = {
        "trainingSet": train_X.values.tolist(),
        "labelSet": train_y.iloc[:,0].tolist()
    }
    return jsonify(result)

@app.route('/api/get_projection')
def get_projection():
    with open(os.getcwd()+'/static/' + 'projection.json', 'r') as f:
        result = json.load(f)
    return result

@app.route('/api/dataset_selected', methods=['POST'])
def dataset_selected():
    dataset_name = request.form.get('dataset_name')
