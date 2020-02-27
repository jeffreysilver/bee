import pickle
import requests

pickle_path = "save.p"

class Node(object):

    def __init__(self, char):
        self.char = char
        self.children = {}
        self.is_terminus = False

    def get_or_create_child(self, char):
        if char in self.children:
            return self.children[char]

        node = Node(char)
        self.children[char] = node
        return node

    def get_child(self, char):
        return self.children.get(char)


    def set_is_terminus(self):
        self.is_terminus = True


class Trie(object):

    def __init__(self):
        self.parent = Node("")

    def insert(self, word):
        print("inserting", word)
        node = self.parent

        for char in word:
            node = node.get_or_create_child(char)

        node.set_is_terminus()

    def get_prefix(self, word):
        node = self.parent

        for char in word:
            node = node.get_child(char)
            if not node:
                return False

        return node

    def word_exists(self, word):
        prefix_node = self.get_prefix(word)
        return prefix_node and prefix_node.is_terminus

    def seed_dictionary(self):
        with open("/usr/share/dict/words") as f:
            lines = f.readlines()
            for line in lines:
                self.insert(line.lower().strip())


    def pickle(self):
        self.__module__ = "trie"
        pickle.dump(self, open(pickle_path, "wb"))



def get_trie(use_pickle=True):
    try:
        return pickle.load(open(pickle_path, "rb"))
    except:
        print("Trie cache not found, creating new Trie")

    t = Trie()
    t.seed_dictionary()
    t.pickle()
    return t
