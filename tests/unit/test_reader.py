from src.handler.reader import Reader

WORDLIST_PATH = './data/wordlist.txt'
NUM_WORDLIST = 2315


class TestReader:
    reader = Reader(WORDLIST_PATH)

    def test_fetch_all(self):
        words = self.reader.fetch_all()
        assert len(words) == NUM_WORDLIST

    def test_fetch_one(self):
        assert self.reader.fetch_one(2294) == 'mercy'
        assert self.reader.fetch_one(1392) == 'snort'
        assert self.reader.fetch_one(289) == 'lowly'

    def test_contain(self):
        assert self.reader.contain('aaaaa') is False
        assert self.reader.contain('print') is True
