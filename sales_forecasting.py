# -*- coding: utf-8 -*-
"""SALES FORECASTING.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PYjsz5s86g_nRy_d-1tmmlvfGoy_fUwK
"""

import warnings;
warnings.simplefilter('ignore')

"""INSTALLING NECCESSARY LIBRARY FUNCTIONS"""

!pip install prophet

pip install plotly

pip install matplotlib

pip install statsmodels

pip install pandas

pip install scikit-learn

import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly

import plotly.graph_objects as go

"""READING THE CSV FILE AND EXTRACTING THE FILE"""

path="/content/drive/MyDrive/Colab Notebooks/Retails.csv"
data = pd.read_csv(path)
data

"""RENAMING THE COLUMNS ACCORDING TO MY CONVINIENCE"""

column_names = ["Date","Retails Sale"]
data.columns=column_names
data

"""DATA CLEANING(DROPPING THE NaN VALUES)"""

data.dropna(inplace=True)
data.reset_index(drop=True,inplace=True)
data.head()

"""RENAMING THE COLUMNS ACCORDING TO FBPROPHET"""

data.columns=['ds','y']
data['ds']=pd.to_datetime(data['ds'])
data

"""PLOTTING THE GRAPH"""

data.plot(x='ds',y='y',figsize=(18,6))

"""FINDING THE LENGTH OF THE DATA"""

len(data)

"""TRAINING AND TESTING THE DATASET"""

train=data.iloc[:len(data)-365]
test=data.iloc[len(data)-365:]

"""PREDICTING THE FUTURE SALES OF RETAIL BUSINESS(SALES FORECASTING)"""

m=Prophet()
m.fit(train)
future=m.make_future_dataframe(periods=1825)
forecast=m.predict(future)

"""FORECASTING THE DATA END"""

forecast.tail()

forecast[['ds','yhat','yhat_lower','yhat_upper']].tail()

test.tail()

"""FORECASTING THE DATA IN THE FORM OF GRAPH"""

plot_plotly(m,forecast)

plot_components_plotly(m,forecast)

"""FINDING THE MEAN VALUE AND ROOT MEAN SQUARE"""

from statsmodels.tools.eval_measures import rmse

predictions=forecast.iloc[-365:]['yhat']
print("Root Mean Square Eroor between predicted value and actual values : ",rmse(predictions,test['y']))
print("Mean Value of Test Dataset : ",test['y'].mean())