# Importing
import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,QPushButton,QHBoxLayout,QVBoxLayout,QButtonGroup, QCheckBox)
from PyQt5.QtGui import QFont

# class of our GUI program:
class DisplaySurvey(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()
        self.show()
    # Create initiaze_ui method for class
    def initialize_ui(self):
        """
        Inistalize the window and display its contents to the screen.
        """
        self.setGeometry(100, 100, 400, 230)
        self.setWindowTitle("4.2 - Survey GUI")
# execution code lines:
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mysurvey = DisplaySurvey()
    sys.exit(app.exec_())


