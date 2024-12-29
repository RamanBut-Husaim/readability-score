class TokenizedSentence:
    _words: list[str] = []

    def __init__(self, words: list[str]):
        self._words = words

    @property
    def words(self) -> list[str]:
        return self._words

    @property
    def number_of_words(self) -> int:
        return len(self._words)