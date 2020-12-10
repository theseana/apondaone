import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('persons.csv')

plt.hist([df['age']], orientation='horizontal', range=(1, 15), color='r')
plt.show()
print(df)
