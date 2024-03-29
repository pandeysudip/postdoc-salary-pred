import joblib
import numpy as np
import pandas as pd
import test
from sklearn.preprocessing import StandardScaler


def preprocess(variables=['Rating', 'Size', 'Type of ownership', 'Industry',
                          'Sector', 'Revenue', 'State', 'desc_length']):
    #dummies = pd.get_dummies(variables)
    #std = StandardScaler()
    test1 = test.test

    trained_model = joblib.load('model.pkl')
    prediction = trained_model.predict(test1)

    return prediction
