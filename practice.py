import pandas as pd

import data_df

f = open ('WhatsApp Chat with Mechanical 3rd Year Offic (1).txt','r', encoding = 'utf-8')
Data = f.read()
df = preprocessor.preprocess(Data)

x = df['user'].value_counts()
print(x)
