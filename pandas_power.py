import matplotlib.pyplot as plt
import pandas as pd

data = {'names': ['Jonah', 'Alex', 'Sam', 'China'],
        'jan_ir': [122, 52, 155, 20],
        'feb_ir': [150, 60, 120, 50],
        'mar_ir': [15, 2, 33, 70]
        }

df = pd.DataFrame(data, columns=['names', 'jan_ir', 'feb_ir', 'mar_ir'])
# create a new column
df['total_ir'] = df['jan_ir'] + df['feb_ir'] + df['mar_ir']

print(df)

color = [(.1, .3, 1), (.0, .5, .8), (.8, .2, .1), (.2, .2, .7)]

plt.pie(df['total_ir'], labels=df['names'], colors=color)
plt.show()
