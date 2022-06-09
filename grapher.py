import plotly.express as px
import pandas as pd


df = pd.read_csv('results.csv', sep=',')

# print(df)
fig = px.box(df, x='msgLen', y='ber')
fig.show()
#fig = px.box(df, x='packets_misteakes')
#fig = px.box(df, x = 'packets_mistakes', y = 'numberOfIterations', title='bledy')
#fig.show()


# df2 = pd.read_csv('results2.csv', sep=',')
# print(df2)