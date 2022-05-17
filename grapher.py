import plotly.express as px
import pandas as pd


df = pd.read_csv('results.csv')
fig = px.box(df, x = 'msgLen', y = 'resendNum', title='bledy')
fig.show()