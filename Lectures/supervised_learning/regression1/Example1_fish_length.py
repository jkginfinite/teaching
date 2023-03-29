import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from scipy import stats
from sklearn.metrics import r2_score,mean_squared_error

X,y = make_regression(n_samples=1000, n_features=1, n_informative=1, n_targets=1,noise=15,bias=0)
X = X+3
y = y+200
plt.figure(figsize=(7,7))
plt.scatter(X,y)
slope, intercept, r_value, p_value, std_err = stats.linregress(X.reshape(1,-1),y)
line = slope*X+intercept
if intercept>0:
    plusminus='+'
elif intercept<0:
    plusminus=' '
plt.plot(X,line,color='red',label='OLS line;\n y={0}*X{1}{2}'.format(round(slope,2),plusminus,round(intercept,2)))
r2 = round(r2_score(y,line),3)
mse = round(mean_squared_error(y,line),3)
plt.title('Fish length vs weight \n R2={}, MSE={}'.format(r2,mse),fontsize=20)
plt.ylabel('Y axis: Length (cm)',fontsize=20)
plt.xlabel('X Axis: Weight (kg)',fontsize=20)
plt.legend(fontsize=20)
plt.savefig('fish_length_weight.png')
plt.show()