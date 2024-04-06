# -*- coding: utf-8 -*-
"""Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rMkxJsfS1UwpTRF1767QXGaNThDLODGb
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing()

housing_df = pd.DataFrame(housing.data, columns=housing.feature_names)
housing_df.head()
housing_df.info()
housing_df.describe()
housing_df.isnull().sum()

"""Data Analysis"""

corr_matrix = housing_df.corr().round(2)
corr_matrix
x1 = housing_df['Longitude']
x2 = housing_df['Latitude']
y = housing_df['Population']
plt.figure(figsize=(10, 6))
plt.scatter(x1, y)
plt.xlabel('Longitude')
plt.ylabel('Population')
plt.figure(figsize=(10, 6))
plt.scatter(x2, y)
plt.xlabel('Latitude')
plt.ylabel('Population')

"""Special features"""

X = housing_df[['HouseAge', 'AveRooms', 'Population', 'AveOccup', 'Latitude', 'Longitude']]
y = housing_df['MedInc']
print(type(X), type(y))


from sklearn.model_selection import train_test_split


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

"""Linear Regression"""

from sklearn.linear_model import LinearRegression


model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)


from sklearn import metrics


print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
# You can also use:
print('R2:', np.round(metrics.r2_score(y_test, y_pred), 2))
