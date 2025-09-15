class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []  # save up to 3 words of minimum lexico order


class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        products.sort()  # sort first to secure lexico order

        # construct Trie
        root = TrieNode()
        for word in products:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                # keep the top 3
                if len(node.suggestions) < 3:
                    node.suggestions.append(word)

        # search prefix
        ret = []
        node = root
        for ch in searchWord:
            if node and ch in node.children:
                node = node.children[ch]
                ret.append(node.suggestions)
            else:
                # if the prefix doesn't exist, all subsequences are null.
                node = None
                ret.append([])

        return ret


# Trie solution, typical application for Trie.
# Time: O(m + nlogn), m is the total number of characters in products, n is the length of searchWord.
# Space: O(m), for the Trie.

s = Solution()
assert(s.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse") ==
         [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]])
assert(s.suggestedProducts(["havana"], "havana") ==
       [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]])