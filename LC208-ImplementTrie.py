class TrieNode:
    def __init__(self):
        self.children = {}  # child nodes hashmap (key=char, value=TrieNode)
        self.isEnd = False  # if it is an end of word


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True  # mark the end of the word in the last node

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Time Complexity: O(m) for insert, search, and startsWith, where m is the length of the word or prefix.
# Space Complexity: O(m) for insert in the worst case when all characters are new.

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
assert(obj.search("apple") == True)
assert(obj.search("app") == False)
assert(obj.startsWith("app") == True)
obj.insert("app")
assert(obj.search("app") == True)