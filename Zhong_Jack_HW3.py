# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 18:48:25 2016

@author: Jack Zhong
"""
 
 
import urllib
import pandas as pd


url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

column = ['sepal length', 'sepal width', 'petal length',
          'petal width', 'class']

data = pd.read_csv(url, names = column)

data.head(10)
data.tail(10)



