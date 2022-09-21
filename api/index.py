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

@app.route('/api/projection_selected', methods=['POST'])
def projection_selected():
    data = request.json
    dataset_name = data["dataset_name"]
    with open(os.getcwd()+'/static/' + 'projection_' + dataset_name + '.json', 'r') as f:
        result = json.load(f)
    return result

@app.route('/api/dataset_selected', methods=['POST'])
def dataset_selected():
    data = request.json
    dataset_name = data["dataset_name"]
    X = pd.read_csv(os.getcwd()+'/static/'+'x_' + dataset_name + '_scaled.csv', header=None)
    y = pd.read_csv(os.getcwd()+'/static/'+'y_' + dataset_name + '.csv', header=None)
    
    result = {
        "trainingSet": X.values.tolist(),
        "labelSet": y.iloc[:,0].tolist()
    }
    return jsonify(result)

@app.route('/api/unscaled_dataset_selected', methods=['POST'])
def unscaled_dataset_selected():
    data = request.json
    dataset_name = data["dataset_name"]
    X = pd.read_csv(os.getcwd()+'/static/'+'x_' + dataset_name + '.csv', header=None)
    y = pd.read_csv(os.getcwd()+'/static/'+'y_' + dataset_name + '.csv', header=None)

    result = {
        "trainingSet": X.values.tolist(),
        "labelSet": y.iloc[:,0].tolist()
    }
    return jsonify(result)
