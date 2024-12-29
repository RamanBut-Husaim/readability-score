from tokenized_sentence import TokenizedSentence

class TokenizedText:
    _text: str = ""
    _total_words: int = 0
    _sentences: list[TokenizedSentence] = []

    def __init__(self, sentences: list[TokenizedSentence], text: str):
        self._sentences = sentences
        self._text = text
        self._total_words = sum([sentence.number_of_words for sentence in sentences])

    @property
    def sentences(self) -> list[TokenizedSentence]:
        return self._sentences

    @property
    def number_of_sentences(self) -> int:
        return len(self.sentences)

    @property
    def number_of_words(self) -> int:
        return self._total_words

    @property
    def text(self) -> str:
        return self._text
