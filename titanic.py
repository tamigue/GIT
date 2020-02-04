import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_excel("titanic3.xls")

data = data.drop(['pclass', 'survived', 'name', 'sex', 'sibsp', 'parch', 'ticket',
       'fare', 'cabin', 'embarked', 'boat', 'body', 'home.dest'], axis=1)
print(data)