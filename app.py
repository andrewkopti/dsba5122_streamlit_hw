import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd

st.header('DSBA 5122 Streamlit Homework - IRS 990 Non-profit Organization Tax Data')

st.markdown(
"The IRS 990 dataset contains nonprofit tax information filed annually with the IRS covering finances, program statements, governance employment, and other topics from 2010-2017. It includes tax exempt organizations, nonexempt charitable trusts, and political organizations"
)

st.markdown(""
)

data = pd.read_csv('IRS 990 Data.csv')


data = data[['TOTEMPLOYEE', 'TOTVOLUNTEERS','SALARIESCURRENT', 'TOTALREVCURRENT', 'TOTALREVPRIOR']]
data = data.dropna()
column_names = ['Employees', 'Volunteers', 'Current Year Salaries', 'Current Year Revenue', 'Prior Year Revenue']
data.columns = column_names
st.write(data.head())

st.sidebar.header('Pick two variables for your scatterplot')

x_val = st.sidebar.selectbox('Pick your x-axis:', data.columns.to_list())
y_val = st.sidebar.selectbox('Pick your y-axis:', data.columns.to_list())

scatter = alt.Chart(data, title=f'Correlation between {x_val} and {y_val}').mark_point().encode(
    alt.X(x_val, title=f'{x_val}'),
    alt.Y(y_val, title=f'{y_val}'),
    tooltip=[x_val, y_val]
)


st.altair_chart(scatter, use_container_width=True)

corr = round(data[x_val].corr(data[y_val]), 2)
st.write(f"The correlation between {x_val} and {y_val} is {corr}")
