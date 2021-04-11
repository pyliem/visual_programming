from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QTextEdit, QStatusBar, QMenuBar,
    QGridLayout, QAction, QMenu, QFileDialog, QMessageBox
)


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.file_name = ''

        # add status bar
        self.statusbar = QStatusBar()

        # add menubar, but don't let it use the native menubar style
        self.menubar = QMenuBar()
        self.menubar.setNativeMenuBar(False)

        # show menubar
        self.menubar.show()

        # add menus
        self.file_menu = self.menubar.addMenu('File')
        self.help_menu = self.menubar.addMenu('Help')

        self.action_open = QAction('Open', self)
        self.action_open.setShortcut('Ctrl+O')
        self.action_save = QAction('Save', self)
        self.action_save.setShortcut('Ctrl+S')
        self.action_quit = QAction('Quit', self)
        self.action_quit.setShortcut('Ctrl+Q')
        self.action_about = QAction('About', self)

        self.file_menu.addAction(self.action_open)
        self.file_menu.addAction(self.action_save)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.action_quit)
        self.help_menu.addAction(self.action_about)

        self.editor = QTextEdit()
        self.layout.addWidget(self.menubar)
        self.layout.addWidget(self.editor)
        self.layout.addWidget(self.statusbar)

        self.action_save.triggered.connect(self.save_text)
        self.action_open.triggered.connect(self.open_text)
        self.action_quit.triggered.connect(self.quit)
        self.action_about.triggered.connect(self.about)
        self.editor.textChanged.connect(self.show_lines)

    def show_lines(self):
        text = self.editor.toPlainText()
        len_text = len(text.split('\n'))
        self.statusbar.showMessage('Lines: %s' % str(len_text))

    def save_text(self):
        # open file and save
        name, _ = QFileDialog.getSaveFileName(self, 'Save', self.file_name, 'TXT(*.txt)')
        if name:
            self.file_name = name
            file = open(name, 'w')
            text = self.editor.toPlainText()
            file.write(text)
            file.close()

    def open_text(self):
        # open file and load
        name, _ = QFileDialog.getOpenFileName(self, 'Open', '', 'TXT(*.txt)')
        if name:
            self.file_name = name
            file = open(name, 'r')
            with file:
                data = file.read()
                self.editor.setPlainText('')
                self.editor.setPlainText(data)
            file.close()

    def quit(self):
        # quit application
        QApplication.quit()

    def about(self):
        # show message in message box
        msg = QMessageBox()
        msg.setText('This is a simple text app')
        msg.exec_()


app = QApplication([])
window = Window()
window.show()
app.exec_()
