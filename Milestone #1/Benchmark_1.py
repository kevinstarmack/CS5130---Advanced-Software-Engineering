import numpy as np
import re
import nltk
from sklearn.datasets import load_files
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
nltk.download('stopwords')
nltk.download('wordnet')temporal_data = load_files(r"txt_sentoken")
X, y = temporal_data.data, temporal_data.targetdocuments = []
stemmer = WordNetLemmatizer()# Pre-processing tasks
for sen in range(0, len(X)):
    # Remove all the special characters
    document = re.sub(r'\W', ' ', str(X[sen]))    # remove all single characters
    document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)    # Remove single characters from the start
    document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)    # Substituting multiple spaces with single space
    document = re.sub(r'\s+', ' ', document, flags=re.I)    # Removing prefixed 'b'
    document = re.sub(r'^b\s+', '', document)    # Converting to Lowercase
    document = document.lower()    # Lemmatization
    document = document.split()    document = [stemmer.lemmatize(word) for word in document]
    document = ' '.join(document)    documents.append(document)# Bag of Words model to convert text documents into numerical features
vectorizer = CountVectorizer(max_features=1500, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))
X = vectorizer.fit_transform(documents).toarray()# Training and testing splits
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
classifier = RandomForestClassifier(n_estimators=1000, random_state=0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)# Evaluating the model
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))
