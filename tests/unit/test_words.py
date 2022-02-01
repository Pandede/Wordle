from src.handler.words import Color, WordAgent

WORDLIST_PATH = './data/wordlist.txt'


class TestWordAgent:
    wa = WordAgent(WORDLIST_PATH)
    wa.solution = 'yeast'

    def test_inspect(self):
        assert self.wa.inspect('aeiou') == [Color.YELLOW, Color.GREEN, Color.GRAY, Color.GRAY, Color.GRAY]
        assert self.wa.inspect('yeast') == [Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN]
        assert self.wa.inspect('yyyyy') == [Color.GREEN, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW]
        assert self.wa.inspect('tsaey') == [Color.YELLOW, Color.YELLOW, Color.GREEN, Color.YELLOW, Color.YELLOW]
