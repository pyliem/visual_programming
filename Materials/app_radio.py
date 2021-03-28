from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QFormLayout


class Window(QWidget):
    def __init__(self):
        """ constructor for Window """
        # inherit from QWidget, call the constructor
        QWidget.__init__(self)
        # set title and resize
        self.setWindowTitle('Choose Gender')
        self.resize(300, 100)

        # add layout, set window layout to current layout
        self.form_layout = QFormLayout()
        self.setLayout(self.form_layout)

        # initiate widgets
        self.label_result = QLabel('Result: ')
        self.result_text = QLabel('')
        self.label_gender = QLabel('Choose your gender')
        self.male_gender = QRadioButton('Male')
        self.female_gender = QRadioButton('Female')

        # connect toggled signal of radio button to a function
        self.male_gender.toggled.connect(self.on_click)
        self.female_gender.toggled.connect(self.on_click)

        # add widget
        self.form_layout.addRow(self.label_gender)
        self.form_layout.addRow(self.male_gender, self.female_gender)
        self.form_layout.addRow(self.result_text)

    def on_click(self):
        """ function to show radio button signal on result_text """
        button = self.sender()  # this is the sender of the signal (radio)
        if button.isChecked():  # radio button is checked, show text
            self.result_text.setText(button.text())


app = QApplication([])
window = Window()
window.show()
app.exec_()
