import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data = pd.read_csv('results.csv', sep=',')
#print(data)
fig = plt.figure(figsize=(10,7))
plt.boxplot(data['ber'])
plt.show()