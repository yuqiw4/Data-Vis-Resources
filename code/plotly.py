# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 18:16:24 2018

@author: 45336
"""

import plotly
plotly.tools.set_credentials_file(username='yw545', api_key='4cLtBnFZAahayYzX5d8u')

import plotly.plotly as py
import pandas as pd
import plotly.graph_objs as go


df = pd.read_csv('Statistics of U.S. Businesses (SUSB)/us_state_totals_emplchange_2014-2015.csv')
df.Employment2014 = df.Employment2014.str.replace(',','').astype(float)
df.EmploymentChange = df.EmploymentChange.str.replace(',','').astype(float)
df = df.loc[df.State != 'West Virginia',]
df = df.loc[df.State != 'United States',]

size = list(df.EmploymentChange)
trace0 = go.Scatter(
    x=df.State,
    y=df.Employment2014,
    mode='markers',
    marker=dict(
        size=size,
        sizemode='area',
        sizeref=2.*max(size)/(40.**2),
        sizemin=4
    )
)

data = [trace0]
py.iplot(data, filename='bubblechart-size-ref')
