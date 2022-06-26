from flask import Flask, jsonify
import os
import pandas as pd
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/test')
def test():
    return 'Test'

@app.route('/api/get_dataset')
def get_dataset():
    train_X = pd.read_csv(os.getcwd()+'\\static\\'+'\\train_x.csv', header=None)
    train_y = pd.read_csv(os.getcwd()+'\\static\\'+'\\train_y.csv', header=None)
    
    result = {
        "trainingSet": train_X,
        "labelSet": train_y
    }
    return jsonify(result)