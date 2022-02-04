import random
from enum import Enum
from typing import List

from .reader import Reader


class Color(Enum):
    GREEN = 0
    YELLOW = 1
    GRAY = 2


class WordAgent:
    def __init__(self, wordlist: str):
        self.reader = Reader(wordlist)
        self.solution = self.choice()

    def choice(self) -> str:
        rnd_idx = random.randint(0, self.reader.n_words)
        return self.reader.fetch_one(rnd_idx)

    def solution(self) -> str:
        return self.solution

    def is_solution(self, guess: str) -> bool:
        return guess == self.solution

    def inspect(self, guess: str) -> List[Color]:
        # Check if the length of guess word does not match
        if len(self.solution) != len(guess):
            raise ValueError(f'expected length of word {len(self.solution)}, got {len(guess)}')

        # Check if the guess word does not in the dictionary
        if not self.reader.contain(guess):
            return None

        return [
            self.__get_color(guess_char, sol_char)
            for guess_char, sol_char in zip(guess, self.solution)
        ]

    def __get_color(self, guess_char: str, sol_char: str) -> Color:
        if guess_char == sol_char:
            return Color.GREEN

        if guess_char in self.solution:
            return Color.YELLOW

        return Color.GRAY
