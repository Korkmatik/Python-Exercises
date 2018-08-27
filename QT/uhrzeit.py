from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
import time, sys

class TimeOfDay(QWidget):
    def __init__(self):
        super().__init__()

        self.lblTime = QLabel()
        self.font = QFont('Arial', 100)
        self.font.setBold(True)
        self.font.setStretch(120)
        self.lblTime.setFont(self.font)
        self.timer = QTimer()
        self.timer.timeout.connect(self.__updateTime)
        self.timer.start(100)

        self.setStyleSheet("background: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 white, stop: 1 blue)")
        self.lblTime.setStyleSheet("background: transparent; color: white")
        self.showFullScreen()
        self.lblTime.setAlignment(Qt.AlignCenter)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.lblTime)
        self.setLayout(self.vbox)

        self.__updateTime()

        self.show()

    def __updateTime(self):
        currentTime = time.asctime().split()

        self.lblTime.setText(currentTime[3])

    def keyPressEvent(self, e):
        self.showNormal()

app = QApplication(sys.argv)
t = TimeOfDay()
sys.exit(app.exec_())