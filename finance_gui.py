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

financial_years_dict = dict()
years_flag = 0

# STARTING SCREEN
class starting_window(QMainWindow):
    def __init__(self):
        super(starting_window, self).__init__()
        uic.loadUi('ui_files/finance_module/starting_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)

    def checkInput(self):
        try:
            int(self.initial_year.text())
            int(self.final_year.text())
            float(self.discount_rate.text())

            if (int(self.initial_year.text()) < 1947) \
                or (int(self.final_year.text()) < 1947) \
                    or (int(self.initial_year.text()) >= int(self.final_year.text())):
                raise Exception

            self.nextScreen()
        except:
            msg = QMessageBox()
            msg.setWindowTitle('ERROR')
            msg.setIcon(QMessageBox.Critical)
            error_text = 'Error detected in user input. '\
                'Make sure that the years entered and discount rate are valid.'
            msg.setText(error_text)
            msg.exec_()

    def nextScreen(self):
        global initial_year, discount_rate

        initial_year = int(self.initial_year.text())
        final_year = int(self.final_year.text())
        discount_rate = float(self.discount_rate.text())

        global years_flag
        if years_flag == 0:
            years_flag = 1
            for year in range(initial_year, final_year+1):
                financial_years_dict[year] = 0


        global finance_counter
        if finance_counter == -1:
            finance_counter += 1
            for year in range(initial_year, final_year+1):
                widget.addWidget(finance_inputs_screen(year))
                widget.addWidget(finance_ratios_screen(year))
            widget.addWidget(finance_output_screen())
        widget.setCurrentIndex(widget.currentIndex() + 1)


# FINANCE INPUTS SCREEN
class finance_inputs_screen(QMainWindow):
    def __init__(self, year):
        self.year = int(year)
        super(finance_inputs_screen, self).__init__()
        uic.loadUi('ui_files/finance_module/finance_inputs_screen.ui', self)

        self.heading.setText(f'Financial Year: {year}')
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

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# FINANCE RATIOS SCREEN
class finance_ratios_screen(QMainWindow):
    def __init__(self, year):
        self.year = int(year)
        super(finance_ratios_screen, self).__init__()
        uic.loadUi('ui_files/finance_module/finance_ratios_screen.ui', self)

        self.heading.setText(f'Financial Year: {year}')
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
        global N_fac, N_staff, N_stu, initial_year, discount_rate
        N_fac = float(self.N_fac.text())
        N_staff = float(self.N_staff.text())
        N_stu = float(self.N_stu.text())

        r = discount_rate
        t = self.year - initial_year

        ProfitMarginPerStudent = \
            float(apply_discount_rate(r,t,R_inst, C, y, N, N_staff, N_fac, N_stu, S_fac, S_staff))
        print(f'Profit Margin Per Student in {self.year}: {ProfitMarginPerStudent}')

        financial_years_dict[self.year] = ProfitMarginPerStudent

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# FINANCE OUTPUT SCREEN
class finance_output_screen(QMainWindow):
    def __init__(self):
        super(finance_output_screen, self).__init__()
        uic.loadUi('ui_files/finance_module/finance_output_screen.ui', self)
        
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 200)

        self.generateButton.clicked.connect(self.load_data)
        self.backButton.clicked.connect(self.backScreen)

    def load_data(self):   
        idx = 0
        self.tableWidget.setRowCount(len(financial_years_dict))
        for param in financial_years_dict.keys():
            self.tableWidget.setItem(idx, 0, QtWidgets.QTableWidgetItem(str(param)))
            self.tableWidget.setItem(idx, 1, QtWidgets.QTableWidgetItem(str(financial_years_dict[param])))
            idx += 1

    def backScreen(self):
        self.tableWidget.setRowCount(0)
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
