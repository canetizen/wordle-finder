# -*- coding: utf-8 -*-

from model import Model
from view import View
from PySide6.QtWidgets import QTextEdit

class Controller:
    def __init__(self):
        self.view = View()
        self.model = Model()

        self.view.mainWindow.button_find.clicked.connect(self.find)
        self.view.mainWindow.radio_turkish.toggled.connect(lambda: self.changeLanguage("tr"))
        self.view.mainWindow.radio_english.toggled.connect(lambda: self.changeLanguage("en"))

        self.setupController()

    def setupController(self):
        self.changeLanguage("tr")
        self.view.mainWindow.show()

    def find(self):
        lineEdits = self.view.mainWindow.findChildren(QTextEdit)
        searchedWord = ''.join(
            letter.toPlainText() if letter.toPlainText() else '*'
            for letter in lineEdits
        )

        if all(char == '*' for char in searchedWord):
            self.view.showError("Lütfen tahmin için harf giriniz.")
            return
        
        if any(len(letter.toPlainText()) > 1 for letter in lineEdits):
            self.view.showError("Sadece harf giriniz.")
            return
        
        excludedLetters = self.view.mainWindow.input_notContain.toPlainText()

        if excludedLetters and not all(len(char.strip()) == 1 for char in excludedLetters.split(',')):
            self.view.showError("Bulmacada bulunmayan karakterler virgulle ayrılmalıdır (ör:'a,b' ya da 'a, b').")
            self.view.setPossibleWords("")
            return
        
        possibleWordList = self.model.findPossibleWords(searchedWord, excludedLetters)

        if len(possibleWordList) == 0:
            self.view.setPossibleWords("Olası kelime bulunamadı.")
        else:
            listToString = ', '.join(possibleWordList)
            self.view.setPossibleWords(listToString)


    def changeLanguage(self, lang):
        if self.model.readFromFile(lang):
            self.view.showError("Dil dosyası okunurken hata oluştu.")
        self.view.setPossibleWords("")
