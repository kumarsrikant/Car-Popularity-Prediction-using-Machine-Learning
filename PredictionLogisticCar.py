import pandas as pd
from sklearn.linear_model import LogisticRegression

# Reading the data
train = pd.read_csv(r'train.csv')
test = pd.read_csv(r'test.csv')

#prediction
train_y = train.popularity
predictor_cols = ['buying_price', 'maintainence_cost', 'number_of_doors', 'number_of_seats','luggage_boot_size','safety_rating']

#Training Data
train_X = train[predictor_cols]

#model
logisticRegr= LogisticRegression()
logisticRegr.fit(train_X, train_y)

#Test Data
test_X = test[predictor_cols]
#Predicting
predicted_prices = logisticRegr.predict(test_X)
y=train_y[1:101]
accuracy=logisticRegr.score(train_X, train_y)
print(accuracy)

my_submission = pd.DataFrame({'Popularity': predicted_prices})

#Cerating seperate data
my_submission.to_csv('submissionLogisticRegression.csv', index=False)