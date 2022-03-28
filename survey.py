# Importing
from fileinput import close
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
        self.display_widgets()
    
    # Create display_widgets method:
    def display_widgets(self):
        """
        Setup widgets using QHBoxLayout and QVBoxLayout.
        """
        # Create Label and button widgets
        title = QLabel("Restaurant Name")
        title.setFont(QFont("Tahoma", 18))
        question = QLabel("How would you rate your service today?")
        # Create horizontal layouts:
        title_h_bx = QHBoxLayout()
        title_h_bx.addStretch()
        title_h_bx.addWidget(title)
        
        ratings = ["Not Statisfied", "Average", "Statisfied"]
        # Create Checkboxes and put them to horizontal layouts, and add stretchable
        rating_h_bx = QHBoxLayout()
        rating_h_bx.setSpacing(60) #==> Set spacing between in widgets in horizontal layout.
        rating_h_bx.addStretch()
        for rat in ratings:
            rate_lbl = QLabel(rat,self)
            rating_h_bx.addWidget(rate_lbl)
        rating_h_bx.addStretch()
        checkbox_h_bx = QHBoxLayout()
        checkbox_h_bx.setSpacing(100)
        
        # Create button group to contain checkboxes
        scale_bg = QButtonGroup(self)
        checkbox_h_bx.addStretch()
        for cb in range(len(ratings)):
            scale_cb = QCheckBox(str(cb),self)
            checkbox_h_bx.addWidget(scale_cb)
            scale_bg.addButton(scale_cb)
        checkbox_h_bx.addStretch()
        
        # Check for signal when checkbox is clicked:
        scale_bg.buttonClicked.connect(self.check_box_clicked)
        close_btn = QPushButton('Close', self)
        close_btn.clicked.connect(self.close)
        
        # Create vertical layout and add widgets and h_box layouts:
        v_box = QVBoxLayout()
        v_box.addLayout(title_h_bx)
        v_box.addWidget(question)
        v_box.addStretch(1)
        v_box.addLayout(rating_h_bx)
        v_box.addLayout(checkbox_h_bx)
        v_box.addStretch(2)
        v_box.addWidget(close_btn)
        # Set main layout of the window
        self.setLayout(v_box)
    
    def check_box_clicked(self,cb):
        """
        print the text of checkbox selected
        """
        print(f"{cb.text()} Selected")
# execution code lines:
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mysurvey = DisplaySurvey()
    sys.exit(app.exec_())


