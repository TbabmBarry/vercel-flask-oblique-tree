from sklearn.manifold import TSNE
from flask import Flask, jsonify
from numpy import reshape
import pandas as pd
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
    result = []
    train_X = pd.read_csv(os.getcwd()+'/static/'+'train_x.csv', header=None)
    train_y = pd.read_csv(os.getcwd()+'/static/'+'train_y.csv', header=None)
    row_num = train_X.shape[0]
    tsne = TSNE(perplexity=20, learning_rate=100, n_components=2, random_state=123)
    embeded_X = tsne.fit_transform(train_X)
    xyembed = embeded_X.reshape((row_num, 2))
    label_arr = train_y.iloc[:,0].tolist()
    for i in range(len(label_arr)):
        result.append({
            'id': i,
            'label': int(label_arr[i]),
            'position': xyembed[i].tolist()
        })
    return jsonify(result)