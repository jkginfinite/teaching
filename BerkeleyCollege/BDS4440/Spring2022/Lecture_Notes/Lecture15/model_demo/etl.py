import pandas as pd
from sklearn.model_selection import train_test_split

class etl:
	def __init__(self,training=False):
		self.training=training
		self.drop_base_columns = ['veil-type']
		self.drop_dummy_columns = ['cap-shape_c', 'cap-shape_f', 'cap-surface_g', 'stalk-root_b']
		self.target = 'class'

	def extract(self):
		return pd.read_csv('source/data.csv')

	def transform(self,data):
		data.drop(self.drop_base_columns,axis=1,inplace=True)
		data2 = pd.DataFrame()
		for col in data.columns:
			if col!=self.target:
				df2 = pd.get_dummies(data[col])
       			df2.drop(df2.columns[-1],axis=1,inplace=True)
        		df2.columns = [col+'_'+i for i in df2.columns]
        		data2 = pd.concat([data2,df2],axis=1)
		data2[self.target]=data[self.target]
		data = data2
		data.drop(self.drop_dummy_columns,axis=1,inplace=True)
		return data

	def load(self):
		data = self.extract()
		data = self.transform(data)

		if (self.target in data.columns) and self.training:
			X = data.drop(self.target,axis=1)
			y = data[self.target]

		else:
			X = data
			y = None

		if self.training:
			X = data.drop(self.target,axis=1)
			y = data[self.target]
			X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)
			return X_train, X_test, y_train, y_test
		else:
			return X


