import pandas as pd
titanic=pd.read_csv('titanic2.csv',encoding="shift-jis")
titanic=titanic.drop(['Name','PassengerId'],axis=1)
mean=round(titanic['Age'].mean(),2)
titanic['Age'].fillna(mean,inplace=True)
titanic.fillna("",inplace=True)

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
for i in titanic.columns.values.tolist():
 if (i=='Age'):
  pass
 else:
  titanic[i] = le.fit_transform(titanic[i])

from sklearn.model_selection import train_test_split
titanic_target = titanic['Survived']
titanic_data=titanic.drop(['Survived'],axis=1)
yX=titanic_target
yX=pd.concat([yX,titanic_data],axis=1)
yX.to_csv('temp.csv',encoding='utf-8')
X_train,X_test,y_train,y_test=train_test_split(titanic_data,titanic_target,test_size=0.2,random_state=54,shuffle=True)
from sklearn.ensemble import RandomForestClassifier
clf=RandomForestClassifier(n_estimators=382, max_depth=None,min_samples_split=2,random_state=8)
clf.fit(X_train,y_train)
print(clf.score(X_test,y_test))
dic=dict(zip(titanic_data.columns,clf.feature_importances_))
for item in sorted(dic.items(), key=lambda x: x[1], reverse=True):
    print(item[0],round(item[1],4))
