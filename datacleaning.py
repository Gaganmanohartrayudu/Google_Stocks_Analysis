#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 14:58:00 2019

@author: gaganmanohart
"""

import pandas as pd
import numpy as np

data = pd.read_csv("Google1.csv")


#number of  null values in the dataset
data.isnull().sum()


#finding mean of each attribute
k = data['Open'].mean(skipna = True)
z = data['High'].mean(skipna = True)
c = data['Low'].mean(skipna = True)
d = data['Close'].mean(skipna = True)
e = data['Adj. Open'].mean(skipna = True)
f = data['Adj. Close'].mean(skipna = True)
g = data['Adj. High'].mean(skipna = True)
h = data['Adj. Low'].mean(skipna = True)
b = data['Adj. Volume'].mean(skipna = True)



#replacing nan values with the mean of respective attribute
l = data['Open']=data['Open'].fillna(k)
m = data['High']=data['High'].fillna(z)
n = data['Low']=data['Low'].fillna(c)
o = data['Close']=data['Close'].fillna(d)

#normalization of the data
sample_data = data[['Open','High','Low','Close','Volume','Ex-Dividend','Split Ratio','Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]

v = sample_data.head()

normalized_data = (sample_data - sample_data.mean())/sample_data.std()
x = normalized_data.head()


#plotting graphs
data = pd.read_csv('Google1.csv', names=(['Open','High','Low','Close','Volume','Ex-Dividend','Split Ratio','Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume'])


q = data.drop(['Open'], axis=1).plot.line(title='Google Dataset')

