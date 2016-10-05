# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 18:48:25 2016

@author: Jack Zhong
"""
##Prof G - Nice work!
#-----------------------------Question 1--------------------------------------- 
'''
Search for the IRIS dataset on the internet. You should quickly find the 
UCI Machine Learning repository. Instead of downloading the files, figure out 
how to directly load the files from the internet into Python and add the column
names using Python code instead of an editor.
'''

import pandas as pd # we need this for everything below

url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

column = ['sepal length', 'sepal width', 'petal length',
          'petal width', 'class'] # column names

data = pd.read_csv(url, names = column)


#-----------------------------Question 2---------------------------------------
'''
Using	Pandas, display	the first ten and the last ten rows of the data.
'''
data.head(10) # first ten
data.tail(10) # last ten


#-----------------------------Question 3---------------------------------------
'''
Using Pandas, print simple location statistics (Count, Mean, STD, Min, 25%, 
50%, 75%, MAX). There is a single method call that will accomplish this.
'''
print(data.describe()) # print statistics


#-----------------------------Question 4---------------------------------------
def hist(list1):
    '''
    Write a function that accepts a list of numbers that represent numbers of 
    bins and, using Pandas, plots a histogram for each of the numeric columns 
    at each bin size. For example, if I call your function with [10, 50, 100] 
    as bin sizes, the function should plot 12 histograms (3 for each numeric 
    variable). Group the histograms by the column name.
    
    Parameter:
    a list of bin sizes
    
    Returns:
    histograms grouped by the column name
    '''

        
    for col in column[0:4]: # for each of the first 4 columns (grouping by col)
        for i in list1: # then for each bin size
            data.hist(column = col, bins = i) # print a histogram
        
        
hist([10,50,100])


#-----------------------------Question 5---------------------------------------
'''
Plot a box plot for each of the numeric column.
'''
import matplotlib.pyplot as plt
for i in column[0:4]:# for each of the first 4 columns
    plt.figure() # make a new plot
    data[i].plot.box() # use only the data on 1 column
    
    
#-----------------------------Question 6---------------------------------------
'''
Plot a bar chart for the nominal column.
'''
nominal_count = data['class'].value_counts() # make a frequency dataframe
nominal_count.plot.bar() # print the bar plot

