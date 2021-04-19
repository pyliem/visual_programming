from PyQt5.QtWidgets import (
    QApplication, QWidget, QTableWidget, QTableWidgetItem, QFormLayout, QPushButton,
    QLabel
)


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.resize(300, 300)
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        self.label = QLabel('')
        self.button_add = QPushButton('Add Line')
        self.button_total = QPushButton('Total Second Column')

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Name', 'Score'])

        self.layout.addRow(self.button_add)
        self.layout.addRow(self.button_total)
        self.layout.addRow(self.table)
        self.layout.addRow(self.label)

        self.button_add.clicked.connect(self.add_row)
        self.button_total.clicked.connect(self.total_row)
        self.table.itemChanged.connect(self.on_change)

    def total_row(self):
        total = 0
        for row in range(0, self.table.rowCount()):
            data = self.table.item(row, 1)
            if data:
                total += float(data.text())
        self.label.setText('Total: %d' % total)

    def add_row(self):
        row_count = self.table.rowCount()  # get row number
        self.table.insertRow(row_count)  # add new row

    def on_change(self, item):
        row = item.row()
        col = item.column()
        # validate the second column to contain only number
        if col == 1 and not item.text().isnumeric():
            item.setText('')  # empty cell


app = QApplication([])
window = Window()
window.show()
app.exec_()
