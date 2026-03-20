from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

data = pd.read_csv("laptops.csv")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    budget = int(request.form['budget'])
    usage = request.form['usage'].lower()

    data['usage'] = data['usage'].str.lower()

    result = data[(data['price'] <= budget) & (data['usage'] == usage)]

    return render_template('result.html', laptops=result.to_dict(orient='records'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
