class PrefixTree:

    def __init__(self):
        # each trie node has these characteristics
        self.children = {}
        self.isEnd = False

    def insert(self, word: str) -> None:
        curr = self
        # for every character in the word
        # if character is not one of curr's children
        # create a new child node
        # move curr to that child
        # after the loop is done mark curr as the end of word
        for char in word:
            if char not in curr.children:
                curr.children[char] = PrefixTree()
            
            curr = curr.children[char]
        
        curr.isEnd = True


    def search(self, word: str) -> bool:
        curr = self
        # for every character in the word
        for char in word:
        # if character is not one of curr's children return false
            if char not in curr.children:
                return False
        # else move curr to that child
            curr = curr.children[char]
        # after the loop is done check that curr is set to isEnd
        return curr.isEnd


    def startsWith(self, prefix: str) -> bool:
        curr = self
        # for every char in the prefix
        for char in prefix:
        # if char is not one of curr's children return false
            if char not in curr.children:
                return False
        # else move curr to that child
            curr = curr.children[char]
        # if loop completes, return true
        return True
        