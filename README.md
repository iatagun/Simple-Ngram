# Simple-Ngram
An n-gram model models sequences, notably natural languages, using the statistical properties of n-grams.

#Simple useage after the download this to your project file
import ngram

# then call the functions and write some sentences like below
ng = ngram.Ngram('Yvette had only to pass the fig tree and she could slip into the house without Dr Melrose knowing '
                 'she had arrived. His habit, though, was to call her without looking up from the ground just when '
                 'she thought she was screened by the tree. Yesterday he had talked to her for long enough to exhaust '
                 'her arms, but not for so long that she might drop the linen. He gauged such things very precisely.')
# this function predict next word that given
ng.predict_bigram('he')
# this function predict third word that given
ng.predict_trigram('he', 'had')
