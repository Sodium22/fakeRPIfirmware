from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import time
import sys

app = QApplication(sys.argv)        #creates the instance

"""window = QWidget()                  #creates a specific window
window.show()                       #shows the window (hidden by default similar to TK)

windowButton = QPushButton("Test")
windowButton.show()"""

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")

        # Set the central widget of the Window.
        self.setCentralWidget(button)

window = MainWindow()
window.show()

app.exec()