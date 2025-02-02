from speedml import Speedml
import pandas as pd

sml = Speedml('trainTitanic.csv', 
              'testTitanic.csv', 
              target = 'Survived',
              uid = 'PassengerId')*2
sml.shape()

sml.configure('overfit_threshold', 
              sml.np.sqrt(sml.train.shape[0]) / sml.train.shape[0])

sml.eda()

sml.plot.correlate()

sml.plot.distribute()

sml.plot.continuous('Age')

sml.plot.continuous('Fare')


sml.feature.outliers('Fare', upper=98)

sml.plot.continuous('Fare')

sml.plot.strip('Pclass', 'Fare')

sml.plot.ordinal('SibSp')
print(sml.feature.outliers('SibSp', upper=99))
sml.plot.ordinal('SibSp')
sml.plot.strip('SibSp', 'Age')

sml.eda()

sml.feature.density('Age')
sml.train[['Age', 'Age_density']].head()

sml.feature.density('Ticket')
sml.train[['Ticket', 'Ticket_density']].head()


sml.feature.drop(['Ticket'])

sml.plot.crosstab('Survived', 'SibSp')

sml.plot.crosstab('Survived', 'Parch')


sml.feature.fillna(a='Cabin', new='Z')
sml.feature.extract(new='Deck', a='Cabin', regex='([A-Z]){1}')
sml.feature.drop(['Cabin'])
sml.feature.mapping('Sex', {'male': 0, 'female': 1})
sml.feature.sum(new='FamilySize', a='Parch', b='SibSp')
sml.feature.add('FamilySize', 1)

sml.plot.bar('FamilySize', 'Survived')


sml.plot.bar('Deck', 'Survived')

sml.feature.drop(['Parch', 'SibSp'])

sml.feature.impute()


sml.info()

sml.plot.importance()
sml.train.head()

sml.feature.extract(new='Title', a='Name', regex=' ([A-Za-z]+)\.')
sml.plot.crosstab('Title', 'Sex')

sml.feature.replace(a='Title', match=['Lady', 'Countess','Capt', 'Col',\
'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], new='Rare')
sml.feature.replace('Title', 'Mlle', 'Miss')
sml.feature.replace('Title', 'Ms', 'Miss')
sml.feature.replace('Title', 'Mme', 'Mrs')

sml.train[['Name', 'Title']].head()


sml.feature.drop(['Name'])
sml.feature.labels(['Title', 'Embarked', 'Deck'])
sml.train.head()

sml.plot.importance()

sml.plot.correlate()

sml.plot.distribute()

sml.eda()

sml.model.data()

select_params = {'max_depth': [3,5,7], 'min_child_weight': [1,3,5]}
fixed_params = {'learning_rate': 0.1, 'subsample': 0.8, 
                'colsample_bytree': 0.8, 'seed':0, 
                'objective': 'binary:logistic'}

sml.xgb.hyper(select_params, fixed_params)

select_params = {'learning_rate': [0.3, 0.1, 0.01], 'subsample': [0.7,0.8,0.9]}
fixed_params = {'max_depth': 3, 'min_child_weight': 1, 
                'colsample_bytree': 0.8, 'seed':0, 
                'objective': 'binary:logistic'}

sml.xgb.hyper(select_params, fixed_params)

tuned_params = {'learning_rate': 0.1, 'subsample': 0.8, 
                'max_depth': 3, 'min_child_weight': 1,
                'seed':0, 'colsample_bytree': 0.8, 
                'objective': 'binary:logistic'}
sml.xgb.cv(tuned_params)

sml.xgb.cv_results.tail(5)

tuned_params['n_estimators'] = sml.xgb.cv_results.shape[0] - 1
sml.xgb.params(tuned_params)

sml.xgb.classifier()


sml.model.evaluate()
sml.plot.model_ranks()


sml.model.ranks()



# Buuild model
sml.xgb.fit()
sml.xgb.predict()

sml.xgb.feature_selection()

sml.xgb.sample_accuracy()

sml.save_results(
    columns={ 'PassengerId': sml.uid,
             'Survived': sml.xgb.predictions }, 
    file_path='output/titanic-speedml-{}.csv'.format(sml.slug()))
sml.slug()

# submission = pd.DataFrame({
#         "PassengerId": sml.uid ,
#         "Survived": sml.xgb.predictions
#     })
submission.to_csv('submission.csv', index=False)

print(sml.uid)