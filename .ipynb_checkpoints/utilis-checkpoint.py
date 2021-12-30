import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


def preprocess(variables=['Rating', 'Size', 'Type of ownership', 'Industry',
                          'Sector', 'Revenue', 'State', 'desc_length']):
    dummies = pd.get_dummies(variables)
    std = StandardScaler()
    test = std.fit_transform(dummies)

    trained_model = joblib.load('model.pkl')
    prediction = trained_model.predict([test])

    return prediction
