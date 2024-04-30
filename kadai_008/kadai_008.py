from sklearn.datasets import load_wine
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import numpy as np

dataset =load_wine()

df= pd.DataFrame(data=dataset.data,columns=dataset.feature_names)

x = dataset.data
y = dataset.target

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=5)

model = RandomForestClassifier()

model.fit(x_train,y_train)

y_pred = model.predict(x_test)

print(accuracy_score(y_test,y_pred))