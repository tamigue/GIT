import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_excel("titanic3.xls")

data = data.drop(['pclass', 'survived', 'name', 'sex', 'sibsp', 'parch', 'ticket',
       'fare', 'cabin', 'embarked', 'boat', 'body', 'home.dest'], axis=1)
a = len(data)
data = data.dropna(axis=0)
b = len(data)
c = a-b


d = data[data["age"]<=20]
d = len(d)


e = data.loc[((data['age'] > 20) & (data['age'] <= 30))]
e = len(e)

f = data.loc[((data['age'] > 30) & (data['age'] <= 40))]
f = len(f)

g = data[data["age"]>40]
g = len(g)

h = c+d+e+f+g
df1 = pd.Series(["cat0", "cat1", "cat2", "cat3","Personne sans age"])
df = pd.DataFrame({"Nombre de personne":[d, e, f, g, c]}, index=df1)
print(df)
plt.figure()
df.plot.bar()

plt.show()