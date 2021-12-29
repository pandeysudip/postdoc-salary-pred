import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler


def preprocess(variables=['Rating', 'Size', 'Type of ownership', 'Industry',
                          'Sector', 'Revenue', 'State', 'desc_length']):
    trained_model = joblib.load('model.pkl')
    prediction = trained_model.predict(variables)

    return prediction
