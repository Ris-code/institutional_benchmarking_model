# MODULE STUFF
from financeModule import *
import json

# UI STUFF
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets, QtCore

QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

# counter for keeping in check the back and previous screen windows
# finance_counter = -1

# years_flag = 0

# flags to check starting screen inputs change
prev_initial_year = None
prev_final_year = None


# STARTING SCREEN
class starting_window(QMainWindow):
    def __init__(self):
        super(starting_window, self).__init__()
        uic.loadUi('ui_files/finance_module/starting_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        # self.nextButton.clicked.connect(self.nextScreen)

    def checkInput(self):
        try:
            int(self.initial_year.text())
            int(self.final_year.text())
            float(self.discount_rate.text())

            if (int(self.initial_year.text()) < 1947) \
                or (int(self.final_year.text()) < 1947) \
                    or (int(self.initial_year.text()) > int(self.final_year.text())):
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
        global initial_year, final_year, discount_rate
        global prev_initial_year, prev_final_year

        initial_year = int(self.initial_year.text())
        final_year = int(self.final_year.text())
        discount_rate = float(self.discount_rate.text())/100


        # global finance_counter
        # if finance_counter == -1:
        #     finance_counter += 1
        #     for year in range(initial_year, final_year+1):
        #         widget.addWidget(finance_inputs_screen(year))
        #         widget.addWidget(finance_ratios_screen(year))
        #     widget.addWidget(finance_output_screen())
        # widget.setCurrentIndex(widget.currentIndex() + 1)

        if (prev_initial_year == None or prev_final_year == None) or (prev_initial_year != initial_year or prev_final_year != final_year):
            prev_initial_year = initial_year
            prev_final_year = final_year

            widget_count = widget.count()
            for index in range(widget_count - 1, 0, -1):
                _widget_ = widget.widget(index)
                widget.removeWidget(_widget_)
                _widget_.deleteLater()
            
            for year in range(initial_year, final_year+1):
                widget.addWidget(finance_inputs_screen(year))
                widget.addWidget(finance_ratios_screen(year))
            widget.addWidget(finance_output_screen())
        
        widget.setCurrentIndex(1)


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
            float(self.C.text())
            float(self.y.text())

            self.nextScreen()
        except Exception as e:
            print(e)
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
            int(self.N_fac.text())
            int(self.N_staff.text())
            int(self.N_stu.text())

            self.nextScreen()
        except Exception as e:
            print(e)
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
        N_fac = int(self.N_fac.text())
        N_staff = int(self.N_staff.text())
        N_stu = int(self.N_stu.text())

        r = discount_rate
        t = self.year - initial_year

        ProfitMarginPerStudent = \
            float(apply_discount_rate(r, t, R_inst, C, y, N_staff, N_fac, N_stu, S_fac, S_staff))
        print(f'Profit Margin Per Student in {self.year}: {ProfitMarginPerStudent}')

        def load_data(filename):
            try:
                with open(filename, 'r') as file:
                    data = json.load(file)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                data = {}
            return data

        def save_data(data, filename):
            with open(filename, 'w') as file:
                json.dump(data, file)

        data_filename = 'data.json'
        data = load_data(data_filename)

        data[f'{self.year}'] = ProfitMarginPerStudent

        data_keys = list(data.keys())
        data_keys.sort()
        data = {key: data[key] for key in data_keys}

        # Saving the updated dictionary to data.json
        save_data(data, data_filename)

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

        def load_data(filename):
            try:
                with open(filename, 'r') as file:
                    data = json.load(file)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                data = {}
            return data

        data_filename = 'data.json'
        data = load_data(data_filename)
        
        self.tableWidget.setRowCount(len(data))

        for param in data.keys():
            self.tableWidget.setItem(idx, 0, QtWidgets.QTableWidgetItem(str(param)))
            self.tableWidget.setItem(idx, 1, QtWidgets.QTableWidgetItem(str(data[param])))
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
