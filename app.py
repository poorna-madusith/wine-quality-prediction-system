from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model
with open('wine_quality_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        data = [
            float(request.form.get('a', 0)),
            float(request.form.get('b', 0)),
            float(request.form.get('c', 0)),
            float(request.form.get('d', 0)),
            float(request.form.get('e', 0)),
            float(request.form.get('f', 0)),
            float(request.form.get('g', 0)),
            float(request.form.get('h', 0)),
            float(request.form.get('i', 0)),
            float(request.form.get('j', 0)),
            float(request.form.get('k', 0))
        ]

        # Prepare input data for prediction
        input_data_nparray = np.asarray(data)
        input_data_reshaped = input_data_nparray.reshape(1, -1)

        # Make prediction
        prediction = model.predict(input_data_reshaped)[0]

        # Determine quality label
        if prediction >= 7:
            quality_label = "best"
        elif 4 <= prediction <= 6:
            quality_label = "good"
        else:
            quality_label = "bad"

        return render_template('home.html', prediction=quality_label)

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
