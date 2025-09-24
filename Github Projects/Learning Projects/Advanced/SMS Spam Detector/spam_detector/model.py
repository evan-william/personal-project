from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import numpy as np
from typing import List

class SpamDetector: # ts module contains the core machine learning logic for the spam detector.
    def __init__(self):
        # initializes scikit pipelines...
        self.model = Pipeline([
            ('vectorizer', CountVectorizer()),
            ('classifier', MultinomialNB()),
        ])

    def train(self, X_train: np.ndarray, y_train: np.ndarray) -> None:
        # trains on provided data with (x_train is the training features) , 
        #   and (y_train is the training labels of ham or spam)
        self.model.fit(X_train, y_train)

    def predict(self, X_new: List[str]) -> np.ndarray:
        # this for predicting on new unseen before data, x_new (list[str]) for new msgs to classify,
            # np.ndarray is array for spam and ham
        return self.model.predict(X_new)

    def predict_proba(self, X_new: List[str]) -> np.ndarray:
        # predict the probability of each clss for the new data , with the 2nd args for list of new msg 
        return self.model.predict_proba(X_new)

