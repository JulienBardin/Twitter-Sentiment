# Imports
import sys
import csv
import json
import pickle
import twitter

# --- Training ---
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


# --- Which Twitter ? ---

config = json.load(open('config.json','r'))
	
api = twitter.Api(consumer_key=config['consumer_key'],
    consumer_secret=config['consumer_secret'],
    access_token_key=config['access_token'],
    access_token_secret=config['access_token_secret'])


csvFile = open("tweets_list.csv", 'w', encoding='utf-8')
csvWriter = csv.writer(csvFile)
csvWriter.writerow([
    "text", "created_at", "geo", "lang", "place", "coordinates",
    "user.favourites_count", "user.statuses_count", "user.description",
    "user.location", "user.id", "user.created_at", "user.verified",
    "user.following", "user.url", "user.listed_count",
    "user.followers_count", "user.default_profile_image",
    "user.utc_offset", "user.friends_count", "user.default_profile",
    "user.name", "user.lang", "user.screen_name", "user.geo_enabled",
    "user.profile_background_color", "user.profile_image_url",
    "user.time_zone", "id", "favorite_count", "retweeted", "source",
    "favorited", "retweet_count"
])

def createTestData(search_string):
    try:
        tweets_fetched=api.GetSearch(search_string, count=200)
        # This will return a list with twitter.Status objects. These have attributes for 
        # text, hashtags etc of the tweet that you are fetching. 
        # The full documentation again, you can see by typing pydoc twitter.Status at the 
        # command prompt of your terminal 
        print ("Great! We fetched "+str(len(tweets_fetched))+" tweets with the term "+search_string+"!!")
        # We will fetch only the text for each of the tweets, and since these don't have labels yet, 
        # we will keep the label empty 
        for status in tweets_fetched:
            csvWriter.writerow([
                    status.text, status.created_at, status.geo, status.lang,
                    status.place, status.coordinates,
                    status.user.favourites_count, status.user.statuses_count,
                    status.user.description, status.user.location,
                    status.user.id, status.user.created_at,
                    status.user.verified, status.user.following,
                    status.user.url, status.user.listed_count,
                    status.user.followers_count,
                    status.user.default_profile_image, status.user.utc_offset,
                    status.user.friends_count, status.user.default_profile,
                    status.user.name, status.user.lang,
                    status.user.screen_name, status.user.geo_enabled,
                    status.user.profile_background_color,
                    status.user.profile_image_url, status.user.time_zone,
                    status.id, status.favorite_count, status.retweeted,
                    status.source, status.favorited, status.retweet_count
                ])
    except:
        print ("Sorry there was an error!")
        return None
    

search_string=input("Bonjour, Que recherchons nous ? =>  ")
testData=createTestData(search_string)

# --- Clean Data ---

# --- Classifier avec tous les classificateur ---

# --- Centraliser le résultat ---

# --- Regrouper les résultats ---

# --- Afficher (Dashboard / graphique) ---

# --- Recommencer ---