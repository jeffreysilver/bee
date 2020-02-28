from trie import get_trie, Trie
from copy import copy
import click



class Solver():

    def __init__(self, puzzle_letters, center_letter):
        self.letters = set()
        self.letters.update(puzzle_letters)
        self.letters.add(center_letter)
        self.center_letter = center_letter
        self.trie = get_trie()

    def solve(self):
        prefixes = copy(self.letters)
        found_words = set()
        while prefixes:
            prefix = prefixes.pop()
            if self.trie.word_exists(prefix) and self.center_letter in prefix and len(prefix) > 4:
                found_words.add(prefix)

            for letter in self.letters:
                new_prefix = prefix + letter
                if self.trie.get_prefix(new_prefix):
                    prefixes.add(new_prefix)

        print(sorted(found_words, key=len, reverse=True))


@click.command()
@click.argument("letters")
@click.argument("center")
def cli(letters, center):

    center = center.lower()
    letters = [l for l in letters.lower()]

    click.echo("Spelling Bee")
    click.echo(f"Letters: {letters}")
    click.echo(f"Center: {center}")

    Solver(letters, center).solve()

if __name__ == '__main__':
    cli()