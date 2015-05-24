# how much wood could a wood chuck chuck if a wood chuck could chuck wood?
# how much/many X could an X Y Y if an X Y could Y X?
# x == noun, adjective
# y == verb

import random
import tweepy
from bot import *

# Read the authorization information for our bot
profile = get_twurl_profile("how_much_could")

# Log into the twitter api
auth = tweepy.OAuthHandler(profile['consumer_key'], profile['consumer_secret'])
auth.set_access_token(profile['token'], profile['secret'])
api = tweepy.API(auth)

# Get a list of nouns, adjectives and verbs
nouns = get_all_pos('NN')
adjectives = get_all_pos('JJ')
verbs = get_all_pos('VB')

# Xes must be a noun and an adjective
xs = nouns.intersection(adjectives)
# Yes must be a noun and a verb
ys = nouns.intersection(verbs)

# pick and X and Y
x = random.choice(list(xs))
y = random.choice(list(ys))

# Generate the sentence
sentence = "How much %s could a %s-%s %s if a %s-%s could %s %s?"%(
    x, x, y, y, x, y, y, x
)

# Get an image for the sentence, for extra weirdness
filename = first_image_for(sentence)

# Post it!
api.update_with_media(filename, status=sentence)

# cleanup
os.remove(filename)
