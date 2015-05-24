# Useful functions for writing twitter bots

import os
import nltk
import requests
import tempfile
import yaml

def get_all_pos(pos):
    """
    Get all the words with the given part of speech - from the penn treebank.
    Possible parts of speech:
    1.	CC	Coordinating conjunction
    2.	CD	Cardinal number
    3.	DT	Determiner
    4.	EX	Existential there
    5.	FW	Foreign word
    6.	IN	Preposition or subordinating conjunction
    7.	JJ	Adjective
    8.	JJR	Adjective, comparative
    9.	JJS	Adjective, superlative
    10.	LS	List item marker
    11.	MD	Modal
    12.	NN	Noun, singular or mass
    13.	NNS	Noun, plural
    14.	NNP	Proper noun, singular
    15.	NNPS	Proper noun, plural
    16.	PDT	Predeterminer
    17.	POS	Possessive ending
    18.	PRP	Personal pronoun
    19.	PRP$	Possessive pronoun
    20.	RB	Adverb
    21.	RBR	Adverb, comparative
    22.	RBS	Adverb, superlative
    23.	RP	Particle
    24.	SYM	Symbol
    25.	TO	to
    26.	UH	Interjection
    27.	VB	Verb, base form
    28.	VBD	Verb, past tense
    29.	VBG	Verb, gerund or present participle
    30.	VBN	Verb, past participle
    31.	VBP	Verb, non-3rd person singular present
    32.	VBZ	Verb, 3rd person singular present
    33.	WDT	Wh-determiner
    34.	WP	Wh-pronoun
    35.	WP$	Possessive wh-pronoun
    36.	WRB	Wh-adverb
    """

    return set([word[0] for word in nltk.corpus.treebank.tagged_words() if word[1] == pos])

def download_file(url):
    """download a file from a url, return the filename"""
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(local_filename, 'w') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
        f.flush()
    return local_filename

def first_image_for(query):
    """download the first image for a google image search for the query"""
    query_url = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=%s&start=0"%(query)
    res = requests.get(query_url)
    url = res.json()['responseData']['results'][0]['url']
    return download_file(url)

def get_twurl_profile(username):
    """read an auth profile from twurl"""
    data = yaml.load(open(os.path.expanduser("~/.twurlrc")).read())
    return data['profiles'][username].values()[0]
