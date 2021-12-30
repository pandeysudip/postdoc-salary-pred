import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler


def preprocess(variables=['Rating', 'Size', 'Type of ownership', 'Industry',
                          'Sector', 'Revenue', 'State', 'desc_length']):
    std_scaler = StandardScaler()
    test_data = std_scaler.fit_transform([variables])
    trained_model = joblib.load('model.pkl')
    prediction = trained_model.predict(test_data)

    return prediction
