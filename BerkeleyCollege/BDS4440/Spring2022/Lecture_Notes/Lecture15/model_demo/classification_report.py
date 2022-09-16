from sklearn.metrics import confusion_matrix, classification_report,accuracy_score,f1_score,roc_curve,auc
from classification_model import classication_model
from plot_confusion_matrix import plot_confusion_matrix

class classification_report(classication_model):
	def __init__(self,model,parameters,data,training):
		self.training=training
		if training:
			super().__init__(model,parameters,data)
			super().fit()
		else:
			self.model = model
			self.X = data
	def report(self):
		y_pred = self.model.predict(self.X)
		y_prob = self.model.predict_proba(X)[:,1]
		if self.training:
			false_positive_rate, true_positive_rate, thresholds = roc_curve(self.y_test, y_prob)
			roc_auc = auc(false_positive_rate, true_positive_rate)
			plt.figure(figsize=(5,5))
			plt.title(str(model)+': \n Receiver Operating Characteristic\n Accuracy : {}'.format(accuracy_score(y_test,y_pred)))
			plt.plot(false_positive_rate,true_positive_rate, color='red',label = 'AUC = %0.2f' % roc_auc)
			plt.legend(loc = 'lower right')
			plt.plot([0, 1], [0, 1],linestyle='--')
			plt.axis('tight')
			plt.ylabel('True Positive Rate')
			plt.xlabel('False Positive Rate')
			plot_confusion_matrix(confusion_matrix(y_test, y_pred),target_names=['poisonous','edible'],normalize=True)
			plt.show()
		else:
			return y_pred,y_prob


