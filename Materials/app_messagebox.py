from PyQt5.QtWidgets import (
    QApplication, QWidget, QComboBox, QLabel, QFormLayout, QMessageBox,
    QLineEdit, QRadioButton, QPushButton
)


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Input Data')
        self.resize(300, 200)

        self.form_layout = QFormLayout()
        self.setLayout(self.form_layout)

        self.result_text = QLabel('')
        self.name_label = QLabel('Enter name')
        self.name_input = QLineEdit()
        self.age_label = QLabel('Enter age')
        self.age_input = QLineEdit()
        self.label_gender = QLabel('Choose your gender')
        self.male_gender = QRadioButton('Male')
        self.female_gender = QRadioButton('Female')
        self.button_result = QPushButton('Show Result')

        # connect the clicked signal to button
        self.button_result.clicked.connect(self.show_result)

        self.form_layout.addRow(self.name_label, self.name_input)
        self.form_layout.addRow(self.age_label, self.age_input)
        self.form_layout.addRow(self.label_gender)
        self.form_layout.addRow(self.male_gender, self.female_gender)
        self.form_layout.addRow(self.button_result)
        self.form_layout.addRow(self.result_text)

    def get_gender(self):
        """ function to get gender based on the radion button checked """
        gender = ''
        if self.male_gender.isChecked():  # if male is checked, use male text
            gender = self.male_gender.text()
        elif self.female_gender.isChecked():  # use female text if checked
            gender = self.female_gender.text()
        return gender

    def show_result(self):
        """ function to show all information in a message box """
        msg_box = QMessageBox()  # instantiate
        # add icon and resize
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.resize(100, 100)
        # create a string to contain all information
        result = """
            Name: %s
            Age: %s
            Gender: %s
        """ % (self.name_input.text(), self.age_input.text(), self.get_gender())
        # similar to label, setText accepts only string
        msg_box.setText(result)
        # always call exec_ to show the message box
        msg_box.exec_()


app = QApplication([])
window = Window()
window.show()
app.exec_()
