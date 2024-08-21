from controller import Controller
from PySide6 import QtWidgets
import sys

if __name__ == "__main__":
    # Initialize the application and controller, then start the event loop
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    sys.exit(app.exec())
