import unittest

class Trie:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
    def insert(self, word: str):
        current = self
        for c in word:
            if c not in current.children:
                current.children[c] = Trie()
            current = current.children[c]
        current.is_word = True

    def search(self, word: str):
        nodes = [self]
        for c in word:
            m = len(nodes)
            while(m):
                node = nodes[0]
                nodes = nodes[1:]
                if c == '.':
                    nodes += list(node.children.values())
                elif c in node.children:
                    nodes.append(node.children[c])
                m -= 1

        for i in nodes:
            if i.is_word:
                return True
        return False

class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        return self.trie.search(word)

class Test(unittest.TestCase):

    def setUp(self):
        self.wd = WordDictionary()

    def test_1(self):
        self.wd.addWord("bad")
        self.wd.addWord("dad")
        self.wd.addWord("daddy")
        self.wd.addWord("mad")
        self.assertFalse(self.wd.search("pad"))
        self.assertTrue(self.wd.search("bad"))
        self.assertTrue(self.wd.search(".ad"))
        self.assertTrue(self.wd.search("b.."))
        self.assertFalse(self.wd.search("b."))
        self.assertTrue(self.wd.search("daddy"))

if __name__ == '__main__':
    unittest.main()
