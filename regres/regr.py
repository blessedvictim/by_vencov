import csv
from os.path import dirname, join

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.utils import Bunch

lin_model = None
dirpath = dirname(__file__)


def load_csv_locally(filepath=join(dirpath, 'boston_house_prices.csv')):
    with open(filepath) as f:
        data_file = csv.reader(f)
        temp = next(data_file)
        n_samples = int(temp[0])
        n_features = int(temp[1])
        data = np.empty((n_samples, n_features))
        target = np.empty((n_samples,))
        temp = next(data_file)  # names of features
        feature_names = np.array(temp)

        for i, d in enumerate(data_file):
            data[i] = np.asarray(d[:-1], dtype=np.float64)
            target[i] = np.asarray(d[-1], dtype=np.float64)

        return Bunch(data=data,
                     target=target,
                     feature_names=feature_names[:-1])


def train():
    global lin_model
    print("train!!!")
    boston_dataset = load_csv_locally()
    boston = pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)
    boston['MEDV'] = boston_dataset.target
    boston.isnull().sum()

    X = pd.DataFrame(np.c_[boston['LSTAT'], boston['RM'], boston['NOX']],
                     columns=['LSTAT', 'RM', 'NOX'])
    Y = boston['MEDV']
    # X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=5)
    lin_model = LinearRegression()
    lin_model.fit(X, Y)


train()


# in the array the  number of parameters must be as many columns
def pred(a):
    print("pred()")
    global lin_model
    if isinstance(lin_model, LinearRegression):
        predicted = lin_model.predict(pd.np.array([a]))
        return predicted[0]
    else:
        return "-~+"
