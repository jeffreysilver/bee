from trie import get_trie, Trie
from copy import copy

center_letter = "h"
puzzle_letters = {"a", "i", "r", "l", "g", "c"}

class Solver():

    def __init__(self, puzzle_letters, center_letter):
        self.letters = set()
        self.letters.update(puzzle_letters)
        self.letters.add(center_letter)

        self.prefixes = copy(self.letters)
        self.found_words = set()
        self.center_letter = center_letter
        self.trie = get_trie()


    def extend_prefixes(self):
        new_prefixes = set()
        for prefix in self.prefixes:
            for letter in self.letters:
                new_prefix = prefix + letter
                if self.trie.get_prefix(new_prefix):
                    new_prefixes.add(new_prefix)

        self.prefixes.update(new_prefixes)

    def extract_words(self):
        for word in self.prefixes:
            if self.trie.word_exists(word) and self.center_letter in word and len(word) > 4:
                self.found_words.add(word)


    def clean_prefixes(self, n):
        self.prefixes = set([p for p in self.prefixes if len(p) > n])

    def iterate(self, n):
        self.extend_prefixes()
        self.extract_words()
        self.clean_prefixes(n)


    def solve(self):
        n = 1
        while self.prefixes:
            self.iterate(n)
            n += 1

        self.print_found_words()

    def print_found_words(self):
        print(sorted(self.found_words, key=len, reverse=True))


s = Solver(puzzle_letters, center_letter)
s.solve()