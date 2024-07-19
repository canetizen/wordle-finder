class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word.strip():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True

    def searchWordWithRegex(self, regex):
        results = []
        self._searchRecursive(self.root, "", regex, results)
        return results

    def _searchRecursive(self, node, current_word, regex, results):
        if node.isEndOfWord and regex.fullmatch(current_word):
            results.append(current_word)
        
        for char, child_node in node.children.items():
            self._searchRecursive(child_node, current_word + char, regex, results)
