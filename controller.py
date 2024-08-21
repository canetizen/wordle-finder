# -*- coding: utf-8 -*-

from model import Model
from view import View
from PySide6.QtWidgets import QTextEdit

class Controller:
    def __init__(self):
        self.view = View()
        self.model = Model()

        # Connects the button click event to the find function
        self.view.mainWindow.button_find.clicked.connect(self.find)
        
        # Connects radio button toggles to change the language
        self.view.mainWindow.radio_turkish.toggled.connect(lambda: self.changeLanguage("tr"))
        self.view.mainWindow.radio_english.toggled.connect(lambda: self.changeLanguage("en"))

        self.setupController()

    def setupController(self):
        # Set the default language to Turkish and display the main window
        self.changeLanguage("tr")
        self.view.mainWindow.show()

    def find(self):
        lineEdits = self.view.mainWindow.findChildren(QTextEdit)
        
        # Combine the letters entered by the user, use '*' for missing letters
        searchedWord = ''.join(
            letter.toPlainText() if letter.toPlainText() else '*'
            for letter in lineEdits
        )

        # Show an error if no letters are entered
        if all(char == '*' for char in searchedWord):
            self.view.showError("Please enter a letter for the guess.")
            return
        
        # Show an error if more than one letter is entered in any text box
        if any(len(letter.toPlainText()) > 1 for letter in lineEdits):
            self.view.showError("Please enter only one letter.")
            return
        
        excludedLetters = self.view.mainWindow.input_notContain.toPlainText()

        # Show an error if excluded letters are not separated by commas
        if excludedLetters and not all(len(char.strip()) == 1 for char in excludedLetters.split(',')):
            self.view.showError("Characters not in the puzzle should be separated by commas (e.g., 'a,b' or 'a, b').")
            self.view.setPossibleWords("")
            return
        
        possibleWordList = self.model.findPossibleWords(searchedWord, excludedLetters)

        # Display an appropriate message if no words are found
        if len(possibleWordList) == 0:
            self.view.setPossibleWords("No possible words found.")
        else:
            listToString = ', '.join(possibleWordList)
            self.view.setPossibleWords(listToString)


    def changeLanguage(self, lang):
        # Attempt to read the language file, show an error if unsuccessful
        if self.model.readFromFile(lang):
            self.view.showError("An error occurred while reading the language file.")
        self.view.setPossibleWords("")
