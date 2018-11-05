# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 18:01:00 2018

@author: joy
"""
#Import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from lifelines import KaplanMeierFitter

#Load data
url="https://archive.ics.uci.edu/ml/machine-learning-databases/haberman/haberman.data"
data=pd.read_csv(url,header=None)


#Inspect data
data.head()

#Find duration
time = data[1].apply(lambda x:70-x)
print(time)

#Fit data
kmf = KaplanMeierFitter() 
kmf.fit(durations = time, event_observed = data[3])
kmf.event_table

#Probabilities of survival
kmf.survival_function_

#Time to event
kmf._conditional_time_to_event_()
