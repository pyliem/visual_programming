from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QLabel, QFormLayout, QComboBox


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Choose Pizza Toppings')
        self.resize(300, 100)

        self.form_layout = QFormLayout()
        self.setLayout(self.form_layout)

        self.add_cheese = QCheckBox('Add Cheese?')
        self.add_pepperoni = QCheckBox('Add Pepperoni')

        # connect toggled signal of the checkbox
        self.add_cheese.toggled.connect(self.show_cheese)
        self.add_pepperoni.toggled.connect(self.show_pepperoni)

        self.combobox = QComboBox()
        self.combobox.addItems(['Small', 'Medium', 'Large'])

        self.combobox.currentTextChanged.connect(self.show_size)

        self.label_result = QLabel('Your Pizza: ')
        self.size_text = QLabel('')
        self.cheese_text = QLabel('')
        self.pepperoni_text = QLabel('')

        self.form_layout.addRow(self.add_cheese, self.add_pepperoni)
        self.form_layout.addRow(self.combobox)
        self.form_layout.addRow(self.label_result)
        self.form_layout.addRow(self.size_text)
        self.form_layout.addRow(self.cheese_text)
        self.form_layout.addRow(self.pepperoni_text)

    def show_cheese(self):
        """ function to show if cheese is added to cheese_text """
        result = ''
        if self.add_cheese.isChecked():  # similar to radio button
            result = 'Cheese Added'
        self.cheese_text.setText(result)

    def show_pepperoni(self):
        """ function to show if pepperoni is added to pepperoni_text """
        result = ''
        if self.add_pepperoni.isChecked():  # similar to radio button
            result = 'Pepperoni Added'
        self.pepperoni_text.setText(result)

    def show_size(self):
        """ function to show combobox text to size_text """
        result = self.combobox.currentText()
        self.size_text.setText(result)


app = QApplication([])
window = Window()
window.show()
app.exec_()
