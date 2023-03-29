from itertools import combinations
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris(as_frame=True)
data = pd.concat([iris['data'],iris['target']],axis=1)
X = data.drop('target',axis=1)
y = data['target']

def compare_x_y_iris(data,x_axis,y_axis,legend=False):
    colors = {'setosa': (0,'red'), 'versicolor': (1,'green'), 'virginica': (2,'blue')}
    for key,values in colors.items():
        plt.scatter(x=data[data['target']==values[0]][x_axis], y=data[data['target']==values[0]][y_axis], c=values[1], label=key)
    plt.xlabel(x_axis,fontsize=15)
    plt.ylabel(y_axis,fontsize=15)
    if legend:
        plt.legend(fontsize=12)
    

cols = [j for j in list(data.columns) if j!='target']
combos = list(combinations(cols, 2))

n=1
plt.figure(figsize=(20,20*(2/3)))
for c in combos:
    plt.subplot(2,3,n)
    if n==1:
        legend=True
    else:
        legend=False
    compare_x_y_iris(data,c[0],c[1],legend)
    n=n+1
plt.savefig('iris_plots.png')
plt.show()