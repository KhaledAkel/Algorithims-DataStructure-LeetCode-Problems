class WordDictNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

class WordDictionary:
    def __init__(self):
        self.root = WordDictNode()
        
    def addWord(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.children:
                newNode = WordDictNode()
                node.children[word[i]] = newNode
            node = node.children[word[i]]
            if i == len(word)-1:
                node.is_word = True

    def search(self, word: str) -> bool:
        def dfs(subword, node):
            if len(subword) == 0:
                return node.is_word

            if subword[0] == ".":
                for letter in node.children:
                    if dfs(subword[1:], node.children[letter]):
                        return True
                return False
            elif subword[0] in node.children:
                return dfs(subword[1:], node.children[subword[0]])
            else:
                return False

        return dfs(word, self.root)

        

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
