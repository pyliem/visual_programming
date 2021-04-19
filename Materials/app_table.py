from PyQt5.QtWidgets import (
    QApplication, QWidget, QTableWidget, QTableWidgetItem, QFormLayout
)


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.resize(300, 300)
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Col 1', 'Col 2'])
        for x in range(1, 11):
            row = self.table.rowCount()  # get the total row
            self.table.setRowCount(row + 1)  # set row count to add row
            itm1 = QTableWidgetItem(str(x))  # create item
            itm2 = QTableWidgetItem(str(x))
            self.table.setItem(x - 1, 0, itm1)  # set to row and column
            self.table.setItem(x - 1, 1, itm2)

        self.layout.addRow(self.table)


app = QApplication([])
window = Window()
window.show()
app.exec_()
