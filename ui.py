import sys
from editor import read_image
from editor import brUp, brDown, ctUp, ctDown
import PIL.Image
from PIL.ImageQt import ImageQt

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton, QSizePolicy, QFileDialog
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
import PyQt5

class EditorGui:
    def __init__(self):
        # Create window
        self.__window = QWidget()
        self.__window.setWindowTitle("Photo Editor")
        self.__window.setGeometry(100, 100, 1000, 600)

        # Create widgets
        self.__label = QLabel()
        self.__label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.__label.setScaledContents(True)

        self.__buttons = []
        self.__buttons.append(QPushButton("Load file"))
        self.__buttons.append(QPushButton("Brightness up"))
        self.__buttons.append(QPushButton("Brightness down"))
        self.__buttons.append(QPushButton("Contrast up"))
        self.__buttons.append(QPushButton("Contrast down"))

        # Create layouts
        self.__masterLayout = QHBoxLayout()
        self.__buttonLayout = QVBoxLayout()
        self.__masterLayout.addLayout(self.__buttonLayout)

        # Add widgets to layout
        self.__masterLayout.addWidget(self.__label)
        for i in range(0,len(self.__buttons)):
            self.__buttonLayout.addWidget(self.__buttons[i])
        self.__window.setLayout(self.__masterLayout)

        # Connect signals to slots
        self.__buttons[1].clicked.connect(self.brup)
        self.__buttons[2].clicked.connect(self.brdown)
        self.__buttons[3].clicked.connect(self.ctup)
        self.__buttons[4].clicked.connect(self.ctdown)

        # Show window
        self.__window.show()

    def set_image(self):
        qtimage = ImageQt(self.__image)
        self.__pixmap = QPixmap.fromImage(qtimage)
        self.__label.setPixmap(self.__pixmap)
        self.__label.repaint()

    def load_picture(self):
        dialog = QFileDialog(caption="Select a file")
        filename = dialog.getOpenFileName()[0]
        filename = filename.split("/")[-1]
        self.__image = read_image(filename)
        self.set_image()

    def brup(self):
        self.__image = brUp(self.__image)
        self.__label.repaint()
        self.set_image()

    def brdown(self):
        self.__image = brDown(self.__image)
        self.__label.repaint()
        self.set_image()

    def ctup(self):
        self.__image = ctUp(self.__image)
        self.__label.repaint()
        self.set_image()

    def ctdown(self):
        self.__image = ctDown(self.__image)
        self.__label.repaint()
        self.set_image()


app = QApplication(sys.argv)

editorgui = EditorGui()
editorgui.load_picture()

sys.exit(app.exec_())