# -*- coding: utf-8 -*-
import nltk
from nltk import word_tokenize
from nltk import trigrams
from nltk import bigrams
from collections import defaultdict

model = defaultdict(lambda: defaultdict(lambda: 0))  # Create a placeholder for model
model2 = defaultdict(lambda: defaultdict(lambda: 0))  # Create a placeholder for model


class Ngram:

    def __init__(self, sent):
        self.sent = sent

    def predict_trigram(self, first, second):
        # Tokenize the text
        tokenized_text = [list(map(str.lower, word_tokenize(sent)))
                          for sent in nltk.sent_tokenize(self.sent)]
        # Count frequency of co-occurrence
        for sentence in tokenized_text:
            for w1, w2, w3 in trigrams(sentence, pad_right=True, pad_left=True):
                model[(w1, w2)][w3] += 1
        # Let's transform the counts to probabilities
        for w1_w2 in model:
            total_count = float(sum(model[w1_w2].values()))
            for w3 in model[w1_w2]:
                model[w1_w2][w3] /= total_count

        # predict the next word
        print("probability of trigram:", dict(model[first, second]))

    def predict_bigram(self, word):
        # Tokenize the text
        tokenized_text2 = [list(map(str.lower, word_tokenize(sent)))
                           for sent in nltk.sent_tokenize(self.sent)]
        # Count frequency of co-occurrence
        for sentence in tokenized_text2:
            for w1, w2 in bigrams(sentence, pad_right=True, pad_left=True):
                model2[w1][w2] += 1
        # Let's transform the counts to probabilities
        for w1 in model2:
            total_count = float(sum(model2[w1].values()))
            for w2 in model2[w1]:
                model2[w1][w2] /= total_count
        # predict the next word
        print("probability of next word:", dict(model2[word]))


if __name__ == '__main__':
    text = Ngram('This is a foobar.This is a bee bar. This is a 7 day trial. this is the option you have')
    text.predict_trigram('this', 'is')
    text.predict_bigram('this')
