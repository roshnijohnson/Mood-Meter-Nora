import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
import pickle

col_names = ['Pleasantness', 'Energy', 'Mood']
# load dataset
pima = pd.read_csv("dataset.csv", header=1, names=col_names)

pima.head()

#split dataset in features and target variable
feature_cols = ['Energy', 'Pleasantness']
X = pima[feature_cols] # Features
y = pima.Mood # Target variable

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test


# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
y_pred1=clf.predict([[15,0]])	
print(y_pred1[0])

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))



filename = 'finalized_model.sav'
pickle.dump(clf, open(filename, 'wb'))
