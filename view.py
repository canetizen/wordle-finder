from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class View:
    def __init__(self):
        self.mainWindow = None
        self.errorWindow = None
        self.setupView()

    def setupView(self):
        loader = QUiLoader()
        ui_mainFile = QFile("ui/window.ui")
        ui_mainFile.open(QFile.ReadOnly)
        self.mainWindow = loader.load(ui_mainFile)
        ui_mainFile.close()

        ui_errorFile = QFile("ui/error.ui")
        ui_errorFile.open(QFile.ReadOnly)
        self.errorWindow = loader.load(ui_errorFile)
        ui_errorFile.close()

    def showError(self, error):
        # Display the error message in the error window
        self.errorWindow.label_error.setText(error)
        self.errorWindow.show()

    def setPossibleWords(self, wordList):
        # Display the possible word list in the main window
        self.mainWindow.label_result.setPlainText(wordList)
