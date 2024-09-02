from trie import Trie

class Model:
    def __init__(self):
        self.trie = Trie()

    def readFromFile(self, lang):
        self.clearTrie()
        try:
            # Attempt to read the words from the specified language file
            with open(f"lang/{lang}.txt", "r") as file:
                for line in file:
                    self.trie.insert(line.strip())
            return 0
        except FileNotFoundError:
            print(f"File {lang}.txt not found.")
            return 1
        except Exception as e:
            print(f"An error occurred: {e}")
            return 1

    def findPossibleWords(self, searchedWord, excludedLetters, includedLetters):
        # Convert excluded letters to a set for easier comparison
        excludedLettersSet = set(char.strip() for char in excludedLetters.lower().split(',')) if excludedLetters else set()
        includedLettersSet = set(char.strip() for char in includedLetters.lower().split(',')) if includedLetters else set()
        return self.trie.searchWordWithPattern(searchedWord.lower(), excludedLettersSet, includedLettersSet)
    
    def clearTrie(self):
        # Clear the Trie before loading new data
        self.trie = Trie()
