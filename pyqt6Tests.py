"""
important links for pyqt
https://doc.qt.io/archives/qt-5.15/widget-classes.html#basic-widget-classes (has all widgets with short examples)
https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/      (full guide for the entire library)
"""

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import time
import sys

app = QApplication(sys.argv)        #creates the instance

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")

        #puts the widget in the center of the window
        self.setCentralWidget(button)

window = MainWindow()
window.show()

app.exec()