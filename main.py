# Imports
import sys
import pickle


# Reload or not the classifier training : 
# add -reload=1 to reload

classificateur = {
    "NLTK Naive Bayes": "data/pickles/original_naive_bayes.pickle",
    "Multinomial Naive Bayes": "data/pickles/multinomial_naive_bayes.pickle",
    "Bernoulli Naive Bayes": "data/pickles/bernoulli_naive_bayes.pickle",
    "Logistic Regression": "data/pickles/logistic_regression.pickle",
    "LinearSVC": "data/pickles/linear_svc.pickle",
    "SVC": "data/pickles/svc.pickle",
    "SGDClassifier": "data/pickles/sgd.pickle"
}

if "reload" in sys.argv :
    print("ça cherche")
else : 
    print("c'est deja good")
    trained_classificateur = []
    for classifier in classificateur.values():
        with open(classifier, "rb") as file:
            trained_classificateur.append(pickle.load(file))