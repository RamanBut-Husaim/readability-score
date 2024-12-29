from tokenized_text import TokenizedText

import math
import re


class FleschKincaidReadabilityEvaluator:
    _vowels_pattern = None

    def __init__(self):
        self._vowels_pattern = re.compile(r'[aeiou]+')

    def evaluate(self, text: TokenizedText) -> tuple[int, int]:
        total_number_of_words = text.number_of_words
        total_number_of_sentences = text.number_of_sentences
        total_number_of_syllables = self._calculate_total_syllables(text)

        flesch_kincaid_score = self._calculate_flesch_kincaid_score(total_number_of_words, total_number_of_sentences,
                                                                    total_number_of_syllables)

        return flesch_kincaid_score, total_number_of_syllables

    @staticmethod
    def _calculate_flesch_kincaid_score(total_number_of_words: int, total_number_of_sentences: int,
                                        total_number_of_syllables: int) -> int:
        score = 0.39 * (total_number_of_words / total_number_of_sentences) + 11.8 * (
                total_number_of_syllables / total_number_of_words) - 15.59

        int_score = math.ceil(score)

        return int_score

    def _calculate_total_syllables(self, text: TokenizedText) -> int:
        total_syllables = 0

        for sentence in text.sentences:
            for word in sentence.words:
                number_of_syllables = self._count_syllables_in_word(word)
                total_syllables += number_of_syllables

        return total_syllables

    # calculate the number of syllables in a word according to
    # Flesch-Kincaid readability test
    def _count_syllables_in_word(self, word: str) -> int:
        word = word.lower()

        vowel_matches = re.findall(self._vowels_pattern, word)

        syllable_count = 0

        for match in vowel_matches:
            if len(match) == 1:
                syllable_count += 1
            elif len(match) == 2:
                syllable_count += 1
            elif len(match) == 3:
                syllable_count += 2

        if word.endswith('e'):
            syllable_count -= 1

        if syllable_count == 0:
            syllable_count = 1

        return syllable_count
