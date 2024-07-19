from trie import Trie
import re

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

    def generateRegex(self, searchedWord, excludedLetters):

        searchedWord = searchedWord.lower()
        excludedLetters = excludedLetters.lower()

        excludedLettersSet = set(excludedLetters.split(',')) if excludedLetters else set()
        
        excludedPattern = ''.join(excludedLettersSet)

        regexPattern = searchedWord.replace('*', '[a-zA-Z]')
        
        if excludedPattern:
            finalPattern = f'^(?!.*[{excludedPattern}]){regexPattern}$'
        else:
            finalPattern = f'^{regexPattern}$'
        
        regex = re.compile(finalPattern)

        return regex

    def findPossibleWords(self, regex):
        return self.trie.searchWordWithRegex(regex)
    
    def clearTrie(self):
        self.trie = Trie()