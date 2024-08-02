# -*- coding: utf-8 -*-
"""Classification_21BRS1682.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1s6ggo7uTkoVXlEMhTwPx8h4acyKoKOq9

# Classification ML - Beginners

![do.png](data:image/png;base64,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)

# Importing necessary libraries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

"""#Dataset loading
 > Initial data understanding
"""

df = pd.read_csv('/content/Categorical 2.csv')

df.head(10)

df.isnull().sum()

df.duplicated().sum()

df.info()

"""## Data Preprocessing"""

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

df['X1'] = le.fit_transform(df['X1'])
df['X2'] = le.fit_transform(df['X2'])
df['X3'] = le.fit_transform(df['X3'])
df['X4'] = le.fit_transform(df['X4'])
df['X5'] = le.fit_transform(df['X5'])
df['X6'] = le.fit_transform(df['X6'])
df['X7'] = le.fit_transform(df['X7'])
df['X8'] = le.fit_transform(df['X8'])

df.info()

df['Target'] = le.fit_transform(df['Target'])

df.describe().T

sns.pairplot(df)

"""# Data visulaization"""

df.info()

sns.histplot(x='X1',data=df,color='Yellow')
plt.show()

sns.histplot(x='X2',data=df,color='red')
plt.show()

sns.histplot(x='X3',data=df,color='blue')
plt.show()

sns.histplot(x='X4',data=df,color='green')
plt.show()

sns.histplot(x='X5',data=df,color='orange')
plt.show()

sns.histplot(x='X6',data=df,color='pink')
plt.show()

sns.histplot(x='X7',data=df,color='purple')
plt.show()

sns.histplot(x='X8',data=df,color='brown')
plt.show()

"""# Model Building  -- Bernouilli Naive Bayes"""

X= df.drop('Target',axis=1)
y= df['Target']

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=42)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.naive_bayes import BernoulliNB
bb = BernoulliNB()
bb.fit(X_train,y_train)

y_pred = bb.predict(X_test)

from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
print(accuracy_score(y_test,y_pred))

print(confusion_matrix(y_test,y_pred))

print(classification_report(y_test,y_pred))

"""# Model Building  -- Decision Tree"""

from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier()
dt.fit(X_train,y_train)

y_pred = dt.predict(X_test)

print(accuracy_score(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

"""#All ML Models"""

pip install lazypredict

import lazypredict

from lazypredict.Supervised import LazyClassifier

clf = LazyClassifier(verbose=0, ignore_warnings=True, custom_metric = None)

models,predictions = clf.fit(X_train, X_test, y_train, y_test)

print(models)

df['Target'].value_counts()