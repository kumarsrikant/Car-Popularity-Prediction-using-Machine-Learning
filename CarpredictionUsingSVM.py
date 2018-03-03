import pandas as pd
from sklearn import svm

# Reading the data
train = pd.read_csv(r'train.csv')
test = pd.read_csv(r'test.csv')

#prediction
train_y = train.popularity
predictor_cols = ['buying_price', 'maintainence_cost', 'number_of_doors', 'number_of_seats','luggage_boot_size','safety_rating']

#Training Data
train_X = train[predictor_cols]

#model
my_model = svm.SVC()
my_model.fit(train_X, train_y)

#Test Data
test_X = test[predictor_cols]
#Predicting
predicted_prices = my_model.predict(test_X)
y=train_y[1:101]

my_submission = pd.DataFrame({'Popularity': predicted_prices})

#Cerating seperate data
my_submission.to_csv('submissionSVM.csv', index=False)

