from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.metrics import r2_score,mean_squared_error,make_scorer

class best_regressor:
    def __init__(self,model,data,target,parameters,metric='r2',test_size=0.2,cv=5):
        self.model = model
        self.data = data
        self.target = target
        self.metric = metric.lower()
        if parameters == None:
            parameters = {}
        self.parameters = parameters
        self.test_size=test_size
        self.cv=cv
        
    def split(self):
        self.X_train,self.X_test,self.y_train,self.y_test=train_test_split(self.data,self.target,test_size=self.test_size)
    
    def run(self):
        self.split()
        d = {'r2':r2_score,'mse':mean_squared_error}
        if self.metric=='r2':
            greater_is_better=True
        else:
            greater_is_better=False
        scorer = make_scorer(d[self.metric],greater_is_better=greater_is_better)
        gs = GridSearchCV(estimator=self.model,param_grid=self.parameters,cv=self.cv,scoring=scorer)
        gs.fit(self.X_train,self.y_train)
        self.best_model = gs.best_estimator_
        self.best_score = gs.best_score_
        self.best_params = gs.best_params_
        print('Best Model: {}'.format(self.best_model))
        print('Best parameters: ',str(self.best_params))
        print('Best score: {}'.format(self.best_score))
        return