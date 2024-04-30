import pandas as pd
import seaborn as sns
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt
import japanize_matplotlib

dataset = fetch_california_housing()

df = pd.DataFrame(data=dataset.data,columns=dataset.feature_names)

df['価格']=dataset.target

feature_names_JPN = ['所得', '築年数', '部屋数', '寝室数', '地域人口', '世帯人数', '緯度', '経度', '住宅価格']
df.columns = feature_names_JPN

#print(df.query('築年数==52').shape)
df = df[df['住宅価格']!=5.000010]

df['世帯数']= df['地域人口']/df['世帯人数']

df['全部屋数'] = df['部屋数']*df['世帯数']
df['全寝室数'] = df['寝室数']*df['世帯数']

df['部屋数/人']= df['全部屋数']/df['地域人口']
df['寝室数/人']= df['全寝室数']/df['地域人口']

#sns.scatterplot(x='部屋数/人',y='寝室数/人',data=df)
df = df.drop(columns = ['部屋数', '寝室数', '世帯人数', '世帯数', '全部屋数', '全寝室数'])

df.to_csv('california_housing_cleansing.csv',encoding='cp932')