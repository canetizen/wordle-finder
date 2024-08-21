from trie import Trie

class Model:
    def __init__(self):
        self.trie = Trie()

    def readFromFile(self, lang):
        self.clearTrie()
        try: 
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

    def findPossibleWords(self, searchedWord, excludedLetters):
        excludedLettersSet = set(excludedLetters.lower().split(',')) if excludedLetters else set()
        return self.trie.searchWordWithPattern(searchedWord.lower(), excludedLettersSet)
    
    def clearTrie(self):
        self.trie = Trie()
