import json
import os
from flask import Flask, request, jsonify
from fbprophet import Prophet
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['POST'])
def calc():
    try:
        if request.args['key'] != os.environ['secret_key']:
            return jsonify(dict(message='invalid key')), 400
    except KeyError:
        return jsonify(dict(message='invalid key')), 400
    try:
        data = json.loads(request.data)
    except Exception:
        return jsonify(dict(message="invalid data format")), 400
    try:
        ds = data['ds']
        y = data['y']
    except KeyError:
        return jsonify(dict(message='invalid input')), 400
        
    periods = request.args.get('periods', 100)
    m = Prophet()
    df = pd.DataFrame(dict(ds=ds, y=y))
    m.fit(df)
    f = m.make_future_dataframe(periods=periods)
    forecast = m.predict(f)
    # only send back new dates
    f_df = forecast[forecast['ds'] > df['ds'].max()].to_dict()
    return jsonify(f_df)
