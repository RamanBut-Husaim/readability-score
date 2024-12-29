from readability_evaluator import ReadabilityEvaluator
from readability_evaluation_result import ReadabilityEvaluationResult

import argparse


def read_file_content(path_to_file: str) -> str:
    with open(path_to_file) as f:
        return f.read()


def read_difficult_words(path_to_file: str) -> list[str]:
    file_content = read_file_content(path_to_file)

    difficult_words = str.split(file_content, '\n')
    return [word.lower() for word in difficult_words if word != '']


def create_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='A program to calculate the readability score of the provided text.')
    parser.add_argument('path_to_file', type=str, help='The path to the file with the provided text.')
    parser.add_argument('difficult_words_path_to_file', type=str, help='The path to the file with difficult words.')

    return parser


def display_results(text: str, result: ReadabilityEvaluationResult) -> None:
    automatic_min_age = min(result.automatic_comprehension_age)
    automatic_max_age = max(result.automatic_comprehension_age)

    flesh_kincaid_min_age = min(result.flesh_kincaid_comprehension_age)
    flesh_kincaid_max_age = max(result.flesh_kincaid_comprehension_age)

    dale_chall_min_age = min(result.dale_chall_comprehension_age)
    dale_chall_max_age = max(result.dale_chall_comprehension_age)

    print(f'Text: {text}')
    print(f'Characters: {result.total_characters}')
    print(f'Sentences: {result.total_sentences}')
    print(f'Words: {result.total_words}')
    print(f'Difficult words: {result.total_difficult_words}')
    print(f'Syllables: {result.total_syllables}')
    print('\n')
    print(
        f'Automated Readability Index: {result.automatic_readability_score} (The text can be understood by {automatic_min_age}-{automatic_max_age} year olds).')
    print(
        f'Flesch–Kincaid Readability Test: {result.flesch_kincaid_readability_score} (The text can be understood by {flesh_kincaid_min_age}-{flesh_kincaid_max_age} year olds).')
    print(
        f'Dale-Chall Readability Index: {result.dale_chall_readability_score} (The text can be understood by {dale_chall_min_age}-{dale_chall_max_age} year olds).')
    print(f'This text should be understood in average by {round(result.average_comprehension_age, 1)} year olds.')


if __name__ == '__main__':
    parser = create_argument_parser()
    args = parser.parse_args()
    path_to_file = args.path_to_file
    difficult_words_path_to_file = args.difficult_words_path_to_file

    text = read_file_content(path_to_file)
    difficult_words = read_difficult_words(difficult_words_path_to_file)

    readability_evaluator = ReadabilityEvaluator(difficult_words)
    readability_evaluator.initialize()

    result = readability_evaluator.evaluate(text)

    display_results(text, result)
