# N-Gram Language Model
This project is a simple implementation of an N-Gram Language Model using the Natural Language Toolkit (NLTK) in Python.

## Features
The project allows users to predict the next word of a given sentence using either a trigram or bigram model. The following features are included in the project:

- Tokenization of text
- Calculation of frequency of co-occurrence of words
- Transformation of counts to probabilities
- Prediction of next word

## Installation and Usage

1. Clone the repository to your local machine.
2. Install the required dependencies using the command pip install -r requirements.txt.
3. To use the N-Gram Language Model, simply import the Ngram class from the ngram.py file and create an instance of it with a text string as a parameter.
4. To predict the next word using the trigram model, call the predict_trigram() method with two words as parameters.
5. To predict the next word using the bigram model, call the predict_bigram() method with one word as a parameter.

```python

from ngram import Ngram

# create an instance of the Ngram class with a text string as a parameter
text = Ngram("This is a foobar.This is a bee bar. This is a 7 day trial. this is the option you have")

# predict the next word using the trigram model
text.predict_trigram('this', 'is') # output: probability of trigram: {'a': 0.6666666666666666, 'the': 0.3333333333333333}

# predict the next word using the bigram model
text.predict_bigram('this') # output: probability of next word: {'is': 0.6666666666666666, 'a': 0.3333333333333333}


```

## Known Issues and Limitations
The N-Gram Language Model implemented in this project has the following known issues and limitations:

- It is based on a small corpus, so its accuracy may be limited.

## Contributions
Contributions to this project are welcome! If you find any bugs or want to add new features, feel free to submit a pull request.


## License
Concordance is released under the [MIT License](https://choosealicense.com/licenses/mit/). See LICENSE.txt for more information.

