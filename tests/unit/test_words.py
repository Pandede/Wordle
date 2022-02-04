from src.handler.words import Color, WordAgent

WORDLIST_PATH = './data/wordlist.txt'


class TestWordAgent:
    wa = WordAgent(WORDLIST_PATH)
    wa.solution = 'yeast'

    def test_inspect(self):
        assert self.wa.inspect('aeiou') is None
        assert self.wa.inspect('yeast') == [Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN]
        assert self.wa.inspect('yyyyy') is None
        assert self.wa.inspect('tsaey') is None
        assert self.wa.inspect('envoy') == [Color.YELLOW, Color.GRAY, Color.GRAY, Color.GRAY, Color.YELLOW]
        assert self.wa.inspect('yearn') == [Color.GREEN, Color.GREEN, Color.GREEN, Color.GRAY, Color.GRAY]
