"""
important links for pyqt
https://doc.qt.io/archives/qt-5.15/widget-classes.html#basic-widget-classes (has all widgets with short examples)
https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/      (full guide for the entire library)
"""

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import time
import sys




app = QApplication(sys.argv)        #creates the instance

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)
        self.setMinimumSize(150, 200)

        self.setCentralWidget(button)        # puts the widget in the center of the window

    def the_button_was_clicked(self):
        print("Clicked")

    def the_button_was_toggled(self, checked):
        print("Checked?", checked)

window = MainWindow()
window.show()

app.exec()