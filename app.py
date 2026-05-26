from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load model
with open("mini_project_2.pkl", "rb") as f:
    model = pickle.load(f)

# 🔥 Home → opens HTML when you click link
@app.route('/')
def home():
    return render_template('index.html')


# 🔥 Predict (form submission)
@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        final_features = np.array([features])

        prediction = model.predict(final_features)[0]

        result = f"Estimated Car Price: ₹ {round(prediction, 2)}"

        return render_template('index.html', prediction_text=result)

    except:
        return render_template('index.html', prediction_text="Invalid Input")


if __name__ == "__main__":
    app.run(debug=True)