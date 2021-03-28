from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QFormLayout


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Choose Language')
        self.resize(300, 200)

        self.form_layout = QFormLayout()
        self.setLayout(self.form_layout)

        self.label_result = QLabel('Result: ')
        self.result_text = QLabel('')
        self.label_combobox = QLabel('Choose your programming language')

        self.combobox = QComboBox()
        # add exactly 1 item
        self.combobox.addItem('Python')
        # add list of items
        self.combobox.addItems(['C', 'Java', 'C#', 'Ruby'])

        # set result_text with the first selected text of combobox
        self.result_text.setText(self.combobox.currentText())
        # send currentTextChanged signal of combobox
        self.combobox.currentTextChanged.connect(self.on_change)

        self.form_layout.addRow(self.label_combobox, self.combobox)
        self.form_layout.addRow(self.label_result, self.result_text)

    def on_change(self):
        """ on_change function to set result_text based on combobox text """
        self.result_text.setText(self.combobox.currentText())


app = QApplication([])
window = Window()
window.show()
app.exec_()
