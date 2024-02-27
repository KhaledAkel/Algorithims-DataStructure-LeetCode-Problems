class TrieNode:
    def __init__(self):
        self.is_word = False  # to mark the end of the word
        self.children = {}    # letter: TrieNode


class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        node = self.root
        for i, char in enumerate(word):
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            if i == len(word) - 1:
                node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Test the Trie implementation
# obj = Trie()
# obj.insert("apple")
# print(obj.search("apple"))    # Output: True
# print(obj.search("app"))      # Output: False
# print(obj.startsWith("app"))  # Output: True
# obj.insert("app")
# print(obj.search("app"))      # Output: True
