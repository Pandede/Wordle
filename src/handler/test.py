from reader import Reader
r = Reader('../../data/validGuess.txt')
print(f'wordlist: {len(r.wordlist)}')
print(type(r.wordlist))
