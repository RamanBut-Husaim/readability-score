class ReadabilityEvaluationResult:
    _total_words: int = 0
    _total_sentences: int = 0

    _total_characters: int = 0
    _automatic_readability_score: int = 0
    _automatic_comprehension_age: tuple[int, int] = (0, 0)

    _total_syllables: int = 0
    _flesch_kincaid_readability_score: int = 0
    _flesch_kincaid_comprehension_age: tuple[int, int] = (0, 0)

    _total_difficult_words: int = 0
    _dale_chall_readability_score: int = 0
    _dale_chall_comprehension_age: tuple[int, int] = (0, 0)

    def __init__(self, total_words: int, total_sentences: int,
                 total_characters: int, automatic_readability_score: int, automatic_comprehension_age: tuple[int, int],
                 total_syllables: int, flesch_kincaid_readability_score: int,
                 flesch_kincaid_comprehension_age: tuple[int, int],
                 total_difficult_words: int,
                 dale_chall_readability_score: int,
                 dale_chall_comprehension_age: tuple[int, int]):
        self._total_words = total_words
        self._total_sentences = total_sentences

        self._total_characters = total_characters
        self._automatic_readability_score = automatic_readability_score
        self._automatic_comprehension_age = automatic_comprehension_age

        self._total_syllables = total_syllables
        self._flesch_kincaid_readability_score = flesch_kincaid_readability_score
        self._flesch_kincaid_comprehension_age = flesch_kincaid_comprehension_age

        self._total_difficult_words = total_difficult_words
        self._dale_chall_readability_score = dale_chall_readability_score
        self._dale_chall_comprehension_age = dale_chall_comprehension_age

    @property
    def total_words(self) -> int:
        return self._total_words

    @property
    def total_sentences(self) -> int:
        return self._total_sentences

    @property
    def total_characters(self) -> int:
        return self._total_characters

    @property
    def automatic_readability_score(self) -> int:
        return self._automatic_readability_score

    @property
    def automatic_comprehension_age(self) -> tuple[int, int]:
        return self._automatic_comprehension_age

    @property
    def total_syllables(self) -> int:
        return self._total_syllables

    @property
    def flesch_kincaid_readability_score(self) -> int:
        return self._flesch_kincaid_readability_score

    @property
    def flesh_kincaid_comprehension_age(self) -> tuple[int, int]:
        return self._flesch_kincaid_comprehension_age

    @property
    def total_difficult_words(self) -> int:
        return self._total_difficult_words

    @property
    def dale_chall_readability_score(self) -> int:
        return self._dale_chall_readability_score

    @property
    def dale_chall_comprehension_age(self) -> tuple[int, int]:
        return self._dale_chall_comprehension_age

    @property
    def average_comprehension_age(self) -> float:
        average_age = (self._automatic_comprehension_age[0] + self._automatic_comprehension_age[1] +
                       self._flesch_kincaid_comprehension_age[0] + self._flesch_kincaid_comprehension_age[1] +
                       self._dale_chall_comprehension_age[0] + self._dale_chall_comprehension_age[1]) / 6
        return average_age
