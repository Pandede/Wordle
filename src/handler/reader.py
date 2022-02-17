from typing import List


class Reader:
    def __init__(self, filepath: str):
        self.wordlist = self.load_file(filepath)
        self.n_words = len(self.wordlist)

    @staticmethod
    def load_file(filepath: str) -> List[str]:
        """Load dictionary from txt file

        Args:
            filepath (str): path of txt file

        Returns:
            List[str]: all words in list
        """
        with open(filepath, 'r', encoding='utf-8') as streamer:
            return streamer.read().splitlines()

    def contain(self, word: str) -> bool:
        """Check if the dictionary contains the word

        Args:
            word (str): word

        Returns:
            bool: contains
        """
        return word in self.wordlist

    def fetch_all(self) -> List[str]:
        """Get all words in dictionary

        Returns:
            List[str]: word list
        """
        return self.wordlist

    def fetch_one(self, idx: int) -> str:
        """Get single word in dictionary by given index

        Args:
            idx (int): word index

        Returns:
            str: word
        """
        return self.wordlist[idx % self.n_words]
