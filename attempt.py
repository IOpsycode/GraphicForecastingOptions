# -*- coding: utf-8 -*-
"""
Created on Fri May 18 13:00:50 2018

@author: auracoll

Goal for now is to show site level and country level. Maybe an example by Grade

"""
import pandas as pd
import numpy as np
from fbprophet import Prophet


# Data import and cleaning
data = pd.read_csv('Data/April18.csv', skiprows=1)

grouped = data.groupby('Report Date').sum()

# something weird happened here, but just del for now
grouped.loc['10/17/2017',] = np.nan

def forecast(column, pd='M', n_pds=12):
    # forecast a given column with pd=period unit and n_pds=future pds to forecast 
    
    newdf = grouped[column].reset_index()
    newdf.columns = ['ds', 'y']
    m = Prophet().fit(newdf)
    future = m.make_future_dataframe(freq=pd, periods=n_pds)
    fcst = m.predict(future)
    grph = m.plot(fcst)
    return grph
    
column = 'Headcount'
grouped[column].reset_index()
forecast('Headcount')
forecast('Leavers Voluntary')
forecast('Leavers Involuntary')
forecast('New Openings')
