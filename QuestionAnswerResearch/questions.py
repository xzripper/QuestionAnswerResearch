# Questions.

from typing import Any


class Question:
    """Question class."""

    title: str = None
    """Question title."""

    correct: Any = None
    """Correct answer."""

    variants: tuple[Any] = None
    """Answer variants."""
 
    def __init__(self, title: str, correct: Any, variants: tuple[Any]) -> None:
        """Initialize question."""
        self.title = title

        self.correct = correct

        self.variants = variants

    def check(self, answer: Any) -> None:
        """Is answer correct?"""
        return answer == self.correct

    def __repr__(self) -> None:
        """Represent question."""
        return f'{self.title}?: {self.correct} {str(self.variants)}'

questions: tuple[Question] = (
    Question('1+1', 2, (1, 2, 3, 4)),
    Question('8+8', 16, (4, 16, 8, 9)),
    Question('98*45', 4410, (4410, 30, 50, 1)),
    Question('| -10 | (abs)', 10, (-10, 10, 0, 1)),
    Question('100-200', -100, (100, -100, 200, 300)),
    Question('8*0', 0, (1, 2, 3, 0)),
    Question('5**2', 25, (25, 45, 78, 90)),
    Question('3>>8', 0, (3, 8, 4, 0)),
    Question('98789^654564', 556289, (0, 556289, 879846, 123564897)),
    Question('Hamburger', 'Cheeseburger', ('Cheeseburger', 'Hamburger', '???', 45)),
    Question('15+25', 40, (35, 40, 55, 30)),
    Question('12*7', 84, (56, 72, 84, 90)),
    Question('120/4', 30, (25, 30, 40, 20)),
    Question('2**5', 32, (16, 32, 64, 8)),
    Question('55-37', 18, (22, 18, 15, 25)),
    Question('9*9', 81, (72, 81, 90, 64)),
    Question('30/5', 6, (5, 6, 10, 3)),
    Question('4**3', 64, (16, 64, 32, 81)),
    Question('180/6', 30, (25, 30, 20, 35)),
    Question('7+14', 21, (18, 21, 25, 15)),
    Question('50*2', 100, (75, 100, 125, 50)),
    Question('40/8', 5, (4, 5, 6, 8)),
    Question('3**4', 81, (64, 81, 27, 16)),
    Question('98-64', 34, (22, 34, 42, 28)),
    Question('11*6', 66, (72, 66, 54, 60)),
    Question('25/5', 5, (4, 5, 6, 7)),
    Question('6**2', 36, (30, 36, 42, 49)),
    Question('85-19', 66, (44, 66, 78, 54)),
    Question('13*3', 39, (45, 39, 52, 27)),
    Question('120/3', 40, (35, 40, 30, 45)),
    Question('9+16', 25, (20, 25, 30, 15)),
    Question('14*5', 70, (65, 70, 80, 60)),
    Question('75/3', 25, (20, 25, 30, 15)),
    Question('2**6', 64, (32, 64, 128, 16)),
    Question('49-27', 22, (18, 22, 25, 20)),
    Question('10*8', 80, (72, 80, 90, 100)),
    Question('48/6', 8, (6, 8, 10, 12)),
    Question('5**3', 125, (100, 125, 150, 75)),
    Question('240/8', 30, (25, 30, 35, 40)),
    Question('6+9', 15, (12, 15, 18, 20)),
    Question('60*3', 180, (150, 180, 200, 160)),
    Question('45/5', 9, (8, 9, 10, 12)),
    Question('4**4', 256, (128, 256, 512, 64)),
    Question('73-49', 24, (22, 24, 28, 20)),
    Question('12*5', 60, (55, 60, 65, 70)),
    Question('36/6', 6, (5, 6, 7, 8)),
    Question('7**2', 49, (36, 49, 64, 81)),
    Question('92-37', 55, (44, 55, 66, 48)),
    Question('17*4', 68, (60, 68, 72, 80)),
    Question('135/5', 27, (25, 27, 30, 22)),
    Question('8+12', 20, (18, 20, 22, 16)),
    Question('16*6', 96, (90, 96, 100, 84)),
    Question('80/4', 20, (15, 20, 25, 30)),
    Question('3**7', 2187, (2048, 2187, 2401, 1923)),
    Question('64-29', 35, (28, 35, 40, 25)),
    Question('11*9', 99, (90, 99, 110, 88)),
    Question('54/6', 9, (8, 9, 10, 12)),
    Question('2**8', 256, (128, 256, 512, 64)),
    Question('312/8', 39, (30, 39, 45, 52)),
    Question('4+13', 17, (15, 17, 20, 13)),
    Question('77*2', 154, (140, 154, 168, 132)),
    Question('60/5', 12, (10, 12, 15, 8)),
    Question('5**5', 3125, (2500, 3125, 3750, 2000)),
    Question('93-47', 46, (44, 46, 50, 42)),
    Question('15*6', 90, (80, 90, 100, 75)),
    Question('48/8', 6, (5, 6, 7, 8)),
    Question('6**3', 216, (150, 216, 250, 125)),
    Question('101-57', 44, (40, 44, 48, 42)),
    Question('19*5', 95, (85, 95, 105, 90)),
    Question('150/5', 30, (25, 30, 35, 40)),
    Question('7+18', 25, (20, 25, 30, 22)),
    Question('17*8', 136, (128, 136, 144, 120)),
    Question('120/6', 20, (15, 20, 25, 30)),
    Question('2**9', 512, (256, 512, 1024, 128)),
    Question('79-43', 36, (32, 36, 40, 28)),
    Question('14*7', 98, (84, 98, 112, 105)),
    Question('63/7', 9, (8, 9, 10, 12)),
    Question('3**6', 729, (648, 729, 800, 512)),
    Question('256/8', 32, (30, 32, 35, 40)),
    Question('5+16', 21, (18, 21, 24, 17)),
    Question('88*2', 176, (160, 176, 192, 150)),
    Question('72/6', 12, (10, 12, 14, 15)),
    Question('6**4', 1296, (1024, 1296, 1600, 729)),
    Question('88-43', 45, (40, 45, 50, 38)),
    Question('16*9', 144, (126, 144, 162, 135)),
    Question('64/8', 8, (7, 8, 9, 10)),
    Question('7**3', 343, (280, 343, 400, 315)),
    Question('101-49', 52, (48, 52, 55, 45)),
    Question('22*6', 132, (120, 132, 144, 110)),
    Question('180/6', 30, (25, 30, 35, 40)),
    Question('9+23', 32, (28, 32, 36, 30)),
    Question('25*4', 100, (85, 100, 115, 95)),
    Question('120/5', 24, (20, 24, 28, 30)),
    Question('3**8', 6561, (6400, 6561, 6724, 6250)),
    Question('91-45', 46, (42, 46, 50, 40)),
    Question('15*8', 120, (112, 120, 128, 110)),
    Question('36/9', 4, (3, 4, 5, 6)),
    Question('4**5', 1024, (800, 1024, 1250, 729)),
    Question('128-64', 64, (60, 64, 68, 58)),
    Question('12*8', 96, (88, 96, 104, 90)),
    Question('48/6', 8, (7, 8, 9, 10)),
    Question('8**3', 512, (400, 512, 625, 729)),
    Question('75-39', 36, (32, 36, 40, 30)),
    Question('13*7', 91, (84, 91, 98, 105)),
    Question('54/9', 6, (5, 6, 7, 8)),
    Question('2**10', 1024, (512, 1024, 2048, 256)),
    Question('160/8', 20, (15, 20, 25, 30)),
    Question('14+19', 33, (28, 33, 38, 30)),
    Question('16*10', 160, (150, 160, 170, 140)),
    Question('80/5', 16, (14, 16, 18, 20)),
    Question('5**4', 625, (500, 625, 750, 560)),
    Question('89-47', 42, (38, 42, 46, 36)),
    Question('18*5', 90, (85, 90, 95, 100)),
    Question('240/12', 20, (15, 20, 25, 30)),
    Question('7+16', 23, (20, 23, 26, 18)),
    Question('17*7', 119, (105, 119, 133, 126)),
    Question('140/7', 20, (18, 20, 22, 24)),
    Question('2**11', 2048, (1024, 2048, 4096, 512)),
    Question('63-28', 35, (30, 35, 40, 25)),
    Question('13*8', 104, (96, 104, 112, 120)),
    Question('72/8', 9, (8, 9, 10, 11)),
    Question('6**5', 7776, (6250, 7776, 9375, 4665)),
    Question('99-53', 46, (42, 46, 50, 38)),
    Question('15*9', 135, (126, 135, 144, 120)),
    Question('0*0', 0, (4, 8, 3, 0))
)

def correct(_questions: tuple[Question], answers: tuple[Any]) -> tuple[list, int]:
    """Is answers correct?"""
    correct_answers = []

    for question, answer in zip(_questions, answers):
        correct_answers.append(question.check(answer))

    return correct_answers, correct_answers.count(True)
