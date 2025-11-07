from flask import Flask, request, jsonify

# Create the Flask app
app = Flask(__name__)

@app.route("/")
def hello():
    # A simple "homepage" to show it's working
    return "Hello! This is your ML Prediction API."

@app.route("/predict", methods=["GET"])
def predict():
    # In a real app, you would get data from the request
    # and run it through a model.
    # For our test, we'll just return a fake prediction.

    # Example of getting data: args = request.args
    # Example: data_point = args.get("data")

    # Fake prediction
    prediction = {"sleep_stage": 2, "confidence": 0.95}

    # Return the prediction as JSON
    return jsonify(prediction)

if __name__ == "__main__":
    # Run the app on host 0.0.0.0 so it's accessible
    # from outside the container.
    app.run(host="0.0.0.0", port=5000)