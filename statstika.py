import os
os.mkdir('archive')

import pandas as pd
df = pd.read_csv('/Cartoon_datasets.csv')
df.head()
df.describe()