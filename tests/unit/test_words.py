from src.handler.words import Color, WordAgent

WORDLIST_PATH = './data/wordlist.txt'


class TestWordAgent:
    wa = WordAgent(WORDLIST_PATH)
    wa.solution = 'yeast'

    def test_word_not_in_list(self):
        assert self.wa.inspect('aeiou') is None
        assert self.wa.inspect('yyyyy') is None
        assert self.wa.inspect('tsaey') is None

    def test_word_is_solution(self):
        assert self.wa.inspect('yeast') == [Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN]

    def test_word_with_unique_character(self):
        assert self.wa.inspect('yearn') == [Color.GREEN, Color.GREEN, Color.GREEN, Color.GRAY, Color.GRAY]
        assert self.wa.inspect('envoy') == [Color.YELLOW, Color.GRAY, Color.GRAY, Color.GRAY, Color.YELLOW]
        assert self.wa.inspect('crust') == [Color.GRAY, Color.GRAY, Color.GRAY, Color.GREEN, Color.GREEN]

    def test_word_with_duplicate_characters(self):
        assert self.wa.inspect('seedy') == [Color.YELLOW, Color.GREEN, Color.GRAY, Color.GRAY, Color.YELLOW]
        assert self.wa.inspect('ritts') == [Color.GRAY, Color.GRAY, Color.YELLOW, Color.GRAY, Color.YELLOW]
        assert self.wa.inspect('weeds') == [Color.GRAY, Color.GREEN, Color.GRAY, Color.GRAY, Color.YELLOW]
