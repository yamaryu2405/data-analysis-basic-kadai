import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib 

df = pd.read_csv('sample_pandas_6.csv')

category_df =pd.read_csv('category.csv')

df = pd.merge(df,category_df[['商品番号','カテゴリー']],how='inner',on='商品番号')

#print(df.head())

num =df['カテゴリー'].value_counts()

print(df.groupby('商品番号')['カテゴリー'].value_counts())

print(df.groupby('商品番号')['注文数'].describe())

num.plot(kind='bar')
plt.title('カテゴリー別頻度') # グラフのタイトルを追加
plt.xlabel('カテゴリー') # x軸のラベルを追加
plt.ylabel('頻度') # y軸のラベルを追加

plt.show()