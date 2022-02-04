from typing import List


class Reader:
    def __init__(self, filepath: str):
        self.wordlist = self.__load_file(filepath)
        self.n_words = len(self.wordlist)

    def __load_file(self, filepath: str) -> List[str]:
        with open(filepath, 'r') as streamer:
            return streamer.read().splitlines()

    def contain(self, word: str) -> bool:
        return word in self.wordlist

    def fetch_all(self) -> List[str]:
        return self.wordlist

    def fetch_one(self, idx: int) -> str:
        return self.wordlist[idx % self.n_words]
