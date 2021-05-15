from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/predict_sentiment', methods=['GET', 'POST'])
def predict_sentiment():
    review = request.form['review']

    response = jsonify({
        'predicted_sentiment': util.get_predicted_sentiment(review)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server")
    util.load_saved_artifacts()
    app.run()