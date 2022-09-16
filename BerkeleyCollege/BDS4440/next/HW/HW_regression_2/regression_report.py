import matplotlib.pyplot as plt
from scipy import stats
from best_regressor import best_regressor
from sklearn.metrics import r2_score,mean_squared_error
import numpy as np

class regression_report(best_regressor):
    def __init__(self,model,data,target,parameters,metric='r2',test_size=0.2,cv=5):
        super().__init__(model,data,target,parameters,metric,test_size,cv)
        super().run()
        self.best_model.fit(self.X_train,self.y_train)
        self.y_pred_test = self.best_model.predict(self.X_test)
        self.y_pred_train = self.best_model.predict(self.X_train)
        
    def string_report(self,y_pred,y_obs,label):
        r2 = r2_score(y_pred,y_obs)
        mse = mean_squared_error(y_pred,y_obs)
        rmse = np.sqrt(mse)
        
        metric_text = '''
        Metrics for {0}
        r2 score: {1}
        mse: {2}
        rmse: {3}
        '''.format(label,round(r2,4),round(mse,4),round(rmse,4))
        print(metric_text)
        return metric_text
    
    def plot_predictions_vs_observations(self,y_pred,y_obs,label):
        slope, intercept, r_value, p_value, std_err = stats.linregress(y_obs,y_pred)
        plt.title('predictions vs observations\n on {0} set \n r2 score: {1}'.format(label,round(r_value,4)))
        plt.scatter(y_obs,y_pred)
        plt.ylabel('predictions')
        plt.xlabel('observations')
        line = slope*y_obs+intercept
        plt.plot(y_obs,line,color='red',label='OLS line;\n y={0}*X+{1}'.format(round(slope,2),round(intercept,2)))
        plt.legend()
        
    def graphic_report(self,y_pred,y_obs,label):
        errors = y_pred-y_obs
        plt.subplot(1,3,1)
        self.plot_predictions_vs_observations(y_pred,y_obs,label)
        plt.subplot(1,3,2)
        plt.title('Histogram of {} errors'.format(label))
        plt.hist(errors)
        plt.subplot(1,3,3)
        stats.probplot(errors,plot=plt)
        plt.title('Q-Q plot of {} errors'.format(label))
        plt.ylabel('{} errors'.format(label))
        plt.xlabel('Gaussian Distribution')
        plt.subplots_adjust(wspace=0.5)
        plt.show()
        
    def report(self):
        figsize = (12,3)
        plt.figure(figsize=figsize)
        plt.subplot(2,1,1)
        self.string_report(self.y_pred_test,self.y_test,'test set')
        self.graphic_report(self.y_pred_test,self.y_test,'test set')
        plt.figure(figsize=figsize)
        plt.subplot(2,1,2)
        self.string_report(self.y_pred_train,self.y_train,'train set')
        self.graphic_report(self.y_pred_train,self.y_train,'train set')