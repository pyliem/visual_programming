# NOTE this could be used, but will provide confusion if your application is
# getting more complex
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QFormLayout


def show_result(result_text, combobox_text):
    result_text.setText(combobox_text)


def main():
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle('Choose Language')
    window.resize(300, 200)

    form_layout = QFormLayout()

    label_result = QLabel('Result: ')
    result_text = QLabel('')
    label_combobox = QLabel('Choose your programming language')
    combobox = QComboBox()
    combobox.addItem('Python')
    combobox.addItems(['C', 'Java', 'C#', 'Ruby'])

    result_text.setText(combobox.currentText())
    combobox.currentTextChanged.connect(lambda : show_result(result_text, combobox.currentText()))

    form_layout.addRow(label_combobox, combobox)
    form_layout.addRow(label_result, result_text)

    window.setLayout(form_layout)
    window.show()
    app.exec_()


main()
