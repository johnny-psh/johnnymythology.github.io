import numpy 
import pandas
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold

scores=[]
dataset = pandas.read_csv('total-foreign-reserves-annual.csv')

X = dataset['year'].values.reshape(-1,1)
y = dataset['total_foreign_reserve_usd'].values.reshape(-1,1)
  
clf = LinearRegression()
kf = KFold(n_splits=2, shuffle=True, random_state=None)
for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    clf.fit(X_train, y_train)
    scores.append(clf.score(X_test, y_test))

print("The R2 Score for this model is: "+str(numpy.mean(scores)))

print("="*10)
print("Bonus")
print("="*10)
# Bonus 
predict_years = numpy.array([[2015],[2016],[2017],[2018]], numpy.int32)
actual_years = numpy.array([[247747.4],[246575.3],[279899.7],[287673.1]], numpy.float_)

prediction = clf.predict(predict_years)

df = pandas.DataFrame({'Years': predict_years.flatten(),'Actual': actual_years.flatten(), 'Predicted': prediction.flatten()})
print(df)
