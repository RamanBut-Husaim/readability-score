from automatic_readability_evaluator import AutomaticReadabilityEvaluator
from dale_chall_readability_evaluator import DaleChallReadabilityEvaluator
from flesch_kincaid_readability_evaluator import FleschKincaidReadabilityEvaluator
from readability_tokenizer import ReadabilityTokenizer
from readability_evaluation_result import ReadabilityEvaluationResult


class ReadabilityEvaluator:
    _readability_score_age_lookup: dict[int, tuple[int, int]] = {
        1: (5, 6),
        2: (6, 7),
        3: (7, 8),
        4: (8, 9),
        5: (9, 10),
        6: (10, 11),
        7: (11, 12),
        8: (12, 13),
        9: (13, 14),
        10: (14, 15),
        11: (15, 16),
        12: (16, 17),
        13: (17, 18),
        14: (18, 22)
    }

    _tokenizer: ReadabilityTokenizer = None
    _automatic_readability_evaluator: AutomaticReadabilityEvaluator = None
    _flesch_kincaid_readability_evaluator: FleschKincaidReadabilityEvaluator = None
    _dale_chall_readability_evaluator: DaleChallReadabilityEvaluator = None

    def __init__(self, difficult_words: list[str]):
        self._tokenizer = ReadabilityTokenizer()
        self._automatic_readability_evaluator = AutomaticReadabilityEvaluator()
        self._flesch_kincaid_readability_evaluator = FleschKincaidReadabilityEvaluator()
        self._dale_chall_readability_evaluator = DaleChallReadabilityEvaluator(difficult_words)

    def initialize(self):
        self._tokenizer.initialize()

    def evaluate(self, text: str) -> ReadabilityEvaluationResult:
        tokenized_text = self._tokenizer.tokenize(text)

        total_number_of_words = tokenized_text.number_of_words
        total_number_of_sentences = tokenized_text.number_of_sentences

        automatic_score, total_number_of_characters = self._automatic_readability_evaluator.evaluate(tokenized_text)
        flesch_kincaid_score, total_number_of_syllables = self._flesch_kincaid_readability_evaluator.evaluate(
            tokenized_text)
        dale_chall_score, total_number_of_difficult_words = self._dale_chall_readability_evaluator.evaluate(
            tokenized_text)

        automatic_comprehension_age = self._find_comprehension_age(automatic_score)
        flesch_kincaid_comprehension_age = self._find_comprehension_age(flesch_kincaid_score)
        dale_chall_comprehension_age = self._find_comprehension_age(dale_chall_score)

        return ReadabilityEvaluationResult(total_number_of_words, total_number_of_sentences,
                                           total_characters=total_number_of_characters,
                                           automatic_readability_score=automatic_score,
                                           automatic_comprehension_age=automatic_comprehension_age,
                                           total_syllables=total_number_of_syllables,
                                           flesch_kincaid_readability_score=flesch_kincaid_score,
                                           flesch_kincaid_comprehension_age=flesch_kincaid_comprehension_age,
                                           total_difficult_words=total_number_of_difficult_words,
                                           dale_chall_readability_score=dale_chall_score,
                                           dale_chall_comprehension_age=dale_chall_comprehension_age)

    def _find_comprehension_age(self, readability_score: int) -> tuple[int, int]:
        min_readability_score = min(self._readability_score_age_lookup.keys())
        max_readability_score = max(self._readability_score_age_lookup.keys())

        adjusted_index = min(max_readability_score, max(min_readability_score, readability_score))

        return self._readability_score_age_lookup[adjusted_index]
