# Methods.

from typing import Any

from random import choice, choices, uniform

from questions import Question


class Random:
    """Random method."""

    @staticmethod
    def solve(questions: tuple[Question]) -> tuple[Any]:
        """Solve via random method."""
        return tuple([choice(question.variants) for question in questions])

class RandomWeights:
    """RandomWeights method."""

    @staticmethod
    def solve(questions: list[Question]) -> tuple[Any]:
        """Solve via random_weights method."""
        return tuple([choices(question.variants, weights=[uniform(0, 1) for _ in range(len(question.variants))], k=2)[0] for question in questions])

class EachNew:
    """EachNew method."""

    @staticmethod
    def solve(questions: tuple[Question]) -> tuple[Any]:
        """Solve via each_new method."""
        answers = []

        for question in questions:
            answers.append(question.variants[len(answers) % len(question.variants)])

        return tuple(answers)

class EachNewReversed:
    """EachNewReversed method."""

    @staticmethod
    def solve(questions: tuple[Question]) -> tuple[Any]:
        """Solve via each_new_reversed method."""
        answers = []

        for question in questions:
            answers.append(question.variants[::-1][len(answers) % len(question.variants)])

        return tuple(answers)

class EachOdd:
    """EachOdd method."""

    @staticmethod
    def solve(questions: tuple[Question]) -> tuple[Any]:
        """Solve via each_new_odd method."""
        return tuple([question.variants[question_index % len(question.variants)] if question_index % 2 == 1 else choice(question.variants) for question_index, question in enumerate(questions)])

class EachEven:
    """EachOdd method."""

    @staticmethod
    def solve(questions: tuple[Question]) -> tuple[Any]:
        """Solve via each_new_odd method."""
        return tuple([question.variants[question_index % len(question.variants)] if question_index % 2 == 0 else choice(question.variants) for question_index, question in enumerate(questions)])
