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
            # Create a new node if the character is not present
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True

    def searchWordWithPattern(self, searchedWord, excludedLettersSet, includedLettersSet):
        results = []
        self._searchWithPattern(self.root, "", searchedWord, 0, excludedLettersSet, results, includedLettersSet)
        return results

    def _searchWithPattern(self, node, currentWord, searchedWord, wordIdx, excludedLettersSet, results, includedLettersSet):
        if wordIdx == len(searchedWord):
            if node.isEndOfWord and all(char in currentWord for char in includedLettersSet):
                results.append(currentWord)
            return
        
        char = searchedWord[wordIdx]

        # If the character is a wildcard (*), try all letters except those in excludedLettersSet
        if char == '*':
            for childChar, childNode in node.children.items():
                if childChar not in excludedLettersSet:
                    self._searchWithPattern(childNode, currentWord + childChar, searchedWord, wordIdx + 1, excludedLettersSet, results, includedLettersSet)
        else:
            # For a specific letter: Check that letter against excludedLettersSet
            if char in node.children and char not in excludedLettersSet:
                self._searchWithPattern(node.children[char], currentWord + char, searchedWord, wordIdx + 1, excludedLettersSet, results, includedLettersSet)
