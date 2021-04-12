from PyQt5.QtWidgets import (
    QApplication, QWidget, QGridLayout, QLabel, QPushButton, QLineEdit
)


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.resize(400, 400)
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.button = QPushButton('Show Second Window')
        self.result_label = QLabel('Result')
        self.label = QLabel('')

        self.layout.addWidget(self.button)
        self.layout.addWidget(self.result_label, 1, 0)
        self.layout.addWidget(self.label, 1, 1)

        self.button.clicked.connect(self.show_second_window)

    def show_second_window(self):
        self.second_window = SecondWindow(self)
        self.second_window.show()


class SecondWindow(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)
        self.resize(200, 200)
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.parent = parent

        self.input = QLineEdit('')
        self.button = QPushButton('Submit')

        self.layout.addWidget(self.input)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.submit)

    def submit(self):
        input_text = self.input.text()
        self.parent.label.setText(input_text)
        self.close()


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
