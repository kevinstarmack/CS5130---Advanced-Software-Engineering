import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics


# Read the data from the reformatted CSV file with Requirements in them
data_set = pd.read_csv("Data.csv")

# Divide data into attributes and labels
# X variable contains all columns from data set except Class column
# y variable contains the values from the Class column
X = data_set.drop('Class', axis=1)
y = data_set['Class']

# Divide data into training and test sets
# Data is split the following way: 90% for training, 10% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10)

# Train the data
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)

# Make predictions the test data
y_pred = classifier.predict(X_test)


####################################################################
# Part 3
####################################################################
count = 0
matrix = pd.DataFrame(columns=('X', 'Y'))
for x in range(1, 111): #111 requirements
    for y in range(1, 900): #some 700+ PoS tags
        matrix.loc[count] = x, y
        count += 1

pred = classifier.predict(matrix)
matrix['Class'] = pred
matrix.to_csv('Output_File')
