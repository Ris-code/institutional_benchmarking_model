# MODULE STUFF
from financeModule import *

# UI STUFF
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets, QtCore

QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

# counter for keeping in check the back and previous screen windows
finance_counter = -1


# STARTING SCREEN
class starting_window(QMainWindow):
    def __init__(self):
        super(starting_window, self).__init__()
        uic.loadUi('ui_files/finance_module/starting_screen.ui', self)

        self.nextButton.clicked.connect(self.nextScreen)

    def nextScreen(self):
        global finance_counter
        if finance_counter == -1:
            finance_counter += 1
            next_window = finance_inputs_screen()
            widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


# FINANCE INPUTS SCREEN
class finance_inputs_screen(QMainWindow):
    def __init__(self):
        super(finance_inputs_screen, self).__init__()
        uic.loadUi('ui_files/finance_module/finance_inputs_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            float(self.R_inst.text())
            float(self.S_fac.text())
            float(self.S_staff.text())
            float(self.N.text())
            float(self.C.text())
            float(self.y.text())

            self.nextScreen()
        except:
            msg = QMessageBox()
            msg.setWindowTitle('ERROR')
            msg.setIcon(QMessageBox.Critical)
            error_text = 'Error detected in user input. '\
                'Ensure that the input is decimal or integer '\
                'value and there are no blank spaces '\
                'or other characters/symbols used.'
            msg.setText(error_text)
            msg.exec_()

    def nextScreen(self):
        global R_inst, S_fac, S_staff, N, C, y
        R_inst = float(self.R_inst.text())
        S_fac = float(self.S_fac.text())
        S_staff = float(self.S_staff.text())
        N = float(self.N.text())
        C = float(self.C.text())
        y = float(self.y.text())

        global finance_counter
        if finance_counter == 0:
            finance_counter += 1
            next_window = finance_ratios_screen()
            widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# FINANCE RATIOS SCREEN
class finance_ratios_screen(QMainWindow):
    def __init__(self):
        super(finance_ratios_screen, self).__init__()
        uic.loadUi('ui_files/finance_module/finance_ratios_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            float(self.N_fac.text())
            float(self.N_staff.text())
            float(self.N_stu.text())

            self.nextScreen()
        except:
            msg = QMessageBox()
            msg.setWindowTitle('ERROR')
            msg.setIcon(QMessageBox.Critical)
            error_text = 'Error detected in user input. '\
                'Ensure that the input is an integer '\
                'value and there are no blank spaces '\
                'or other characters/symbols used.'
            msg.setText(error_text)
            msg.exec_()

    def nextScreen(self):
        global N_fac, N_staff, N_stu, ProfitMarginPerStudent
        N_fac = float(self.N_fac.text())
        N_staff = float(self.N_staff.text())
        N_stu = float(self.N_stu.text())

        ProfitMarginPerStudent = \
            float(profit_margin_per_student(R_inst, C, y, N, N_staff, N_fac, N_stu, S_fac, S_staff))
        print(f'Profit Margin Per Student: {ProfitMarginPerStudent}')

        global finance_counter
        if finance_counter == 1:
            finance_counter += 1
            next_window = finance_output_screen()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# FINANCE OUTPUT SCREEN
class finance_output_screen(QMainWindow):
    def __init__(self):
        super(finance_output_screen, self).__init__()
        uic.loadUi('ui_files/finance_module/finance_output_screen.ui', self)
        
        self.generateButton.clicked.connect(self.generateOutput)
        self.backButton.clicked.connect(self.backScreen)

    def generateOutput(self):
        global ProfitMarginPerStudent
        self.output.setText(str(ProfitMarginPerStudent))

    def backScreen(self):
        self.output.setText("")
        widget.setCurrentIndex(widget.currentIndex() - 1)


if __name__ == '__main__':
    demoApp = QApplication([])

    widget = QtWidgets.QStackedWidget()
    first_window = starting_window()

    # debugging
    # first_window = name_of_window()

    widget.addWidget(first_window)
    widget.show()

    demoApp.exec_()
