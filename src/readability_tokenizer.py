from tokenized_sentence import TokenizedSentence
from tokenized_text import TokenizedText

import re

import nltk

class ReadabilityTokenizer:
    _word_tokenize_pattern = None

    def __init__(self):
        self._word_tokenize_pattern = re.compile(r"[0-9A-z']+")

    def initialize(self):
        nltk.download('punkt')

    def tokenize(self, text: str) -> TokenizedText:
        raw_sentences = nltk.tokenize.sent_tokenize(text)

        tokenized_raw_sentences = [nltk.tokenize.regexp_tokenize(raw_sentence, self._word_tokenize_pattern) for
                                   raw_sentence in raw_sentences]

        tokenized_sentences = [TokenizedSentence(sentence) for sentence in tokenized_raw_sentences]

        return TokenizedText(tokenized_sentences, text)
