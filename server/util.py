import json
import numpy as np
import ktrain

__model = None

def get_predicted_sentiment(review):
    data = [review]
    return __model.predict(data)


def load_saved_artifacts():
    print("loading saved artifacts...start")

    global __model
    if __model is None:
        __model = ktrain.load_predictor('./artifacts')
    print("loading saved artifacts...done")


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_predicted_sentiment('wonderful'))
