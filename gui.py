import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
import classificator
import time

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.model = classificator.loadModel('covid19.model')
        self.label = QLabel()
        self.resultLabel = QLabel()
        self.currentFname = ''
        self.button = QPushButton("Загрузить изображение")
        self.button.clicked.connect(self.getImage)
        self.button1 = QPushButton("Классифицировать")
        self.button1.clicked.connect(self.classifyImage)
        self.button2 = QPushButton("Очистить интерфейс")
        self.button2.clicked.connect(self.clearInterface)
        self.button3 = QPushButton("Обучить нейронную сеть")
        self.button3.clicked.connect(self.trainNeural)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.resultLabel)
        self.setLayout(self.layout)
        self.show()

    def getImage(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'd:\\',"Image files (*.jpg *.gif *.png *.jpeg)")
        pixmap = QPixmap(fname[0])
        self.label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        self.currentFname = fname[0]
        self.resultLabel.clear()

    def classifyImage(self):
        start_time = time.time()
        pred = classificator.classifySingleImage(self.currentFname, self.model)
        if pred[0] == 0:
            self.resultLabel.setText('Результат классификации: "COVID-19"')
        else:
            self.resultLabel.setText('Результат классификации: "Здоров"')
        print('Time: ' + str(time.time() - start_time))

    def clearInterface(self):
        self.label.clear()
        self.resultLabel.clear()

    def trainNeural(self):
        self.label.clear()
        self.resultLabel.setText('Нейронная сеть обучена')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.resize(800, 600)
    ex.show()
    sys.exit(app.exec_())