import random
from collections import Counter
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

        # Compute counting dictionary
        counter = Counter(self.solution)

        result = []
        for guess_char, sol_char in zip(guess, self.solution):
            # Return GREEN if the character is identical and correct location
            if guess_char == sol_char:
                result.append(Color.GREEN)
                counter[guess_char] -= 1
            # Return YELLOW if the character is in the solution and has not been guessed yet
            elif guess_char in self.solution and counter[guess_char] > 0:
                result.append(Color.YELLOW)
                counter[guess_char] -= 1
            # Else, return GRAY
            else:
                result.append(Color.GRAY)

        return result
