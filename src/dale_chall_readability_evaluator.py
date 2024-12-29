from tokenized_text import TokenizedText

import math


class DaleChallReadabilityEvaluator:
    _difficult_words: set[str] = []

    def __init__(self, difficult_words: list[str]):
        self._difficult_words = set(difficult_words)

    def evaluate(self, text: TokenizedText) -> tuple[int, int]:
        total_number_of_words = text.number_of_words
        total_number_of_sentences = text.number_of_sentences
        total_number_of_difficult_words = self._calculate_number_of_difficult_words(text)

        dale_chall_readability_score = self._calculate_dale_chall_readability_score(
            total_number_of_words=total_number_of_words,
            total_number_of_sentences=total_number_of_sentences,
            total_number_of_difficult_words=total_number_of_difficult_words)

        return dale_chall_readability_score, total_number_of_difficult_words

    def _calculate_dale_chall_readability_score(self, total_number_of_words: int, total_number_of_sentences: int,
                                                total_number_of_difficult_words: int) -> int:
        difficult_words_percent = (total_number_of_difficult_words / total_number_of_words) * 100

        score = 0.1579 * difficult_words_percent + 0.0496 * (
                total_number_of_words / total_number_of_sentences)

        if difficult_words_percent > 5:
            score += 3.6365

        int_score = math.ceil(score)

        return int_score

    def _calculate_number_of_difficult_words(self, text: TokenizedText) -> int:
        difficult_words = 0

        for sentence in text.sentences:
            for word in sentence.words:
                if word not in self._difficult_words:
                    difficult_words += 1

        return difficult_words
