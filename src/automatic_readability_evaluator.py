from tokenized_text import TokenizedText

import math


class AutomaticReadabilityEvaluator:
    def evaluate(self, text: TokenizedText) -> tuple[int, int]:
        total_number_of_words = text.number_of_words
        total_number_of_sentences = text.number_of_sentences
        total_number_of_characters = self._calculate_characters(text.text)

        readability_index = self._calculate_automatic_readability_score(total_number_of_words,
                                                                        total_number_of_sentences,
                                                                        total_number_of_characters)

        return readability_index, total_number_of_characters

    def _calculate_characters(self, text: str) -> int:
        visible_characters = 0

        for character in text:
            if self._is_visible_character(character):
                visible_characters += 1

        return visible_characters

    @staticmethod
    def _calculate_automatic_readability_score(total_number_of_words: int, total_number_of_sentences: int,
                                               total_number_of_characters: int) -> int:
        score = 4.71 * (total_number_of_characters / total_number_of_words) + 0.5 * (
                total_number_of_words / total_number_of_sentences) - 21.43

        int_score = math.ceil(score)

        return int_score

    @staticmethod
    # according to the task description, a visible character is any character
    # that is not space, new line and tabulation
    def _is_visible_character(character: str) -> bool:
        if character == ' ':
            return False
        if character == '\n':
            return False
        if character == '\t':
            return False

        return True
