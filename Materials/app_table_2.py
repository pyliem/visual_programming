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
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Name', 'Major', 'GPA'])
        students = [
            ('John', 'IT', '3.4'),
            ('Mary', 'IS', '3.5'),
            ('Smith', 'IS', '3.2')
        ]
        for student in students:
            row = self.table.rowCount()  # get the total row
            self.table.setRowCount(row + 1)  # set row count to add row
            name = QTableWidgetItem(student[0])  # create item
            major = QTableWidgetItem(student[1])
            gpa = QTableWidgetItem(student[2])
            self.table.setItem(row, 0, name)  # set to row and column
            self.table.setItem(row, 1, major)
            self.table.setItem(row, 2, gpa)

        self.layout.addRow(self.table)


app = QApplication([])
window = Window()
window.show()
app.exec_()
