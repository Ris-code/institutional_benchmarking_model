# MODULE STUFF
from modules.sales_module import *

# UI STUFF
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets, QtCore

QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

# counter for keeping in check the back and previous screen windows
sales_counter = -1

# parameters dictionary (needed in table)
sales_param_dict = dict()


# STARTING SCREEN
class starting_window(QMainWindow):
    def __init__(self):
        super(starting_window, self).__init__()
        uic.loadUi('ui_files/sales_module/sales_starting_screen.ui', self)

        self.nextButton.clicked.connect(self.nextScreen)

    def nextScreen(self):
        global sales_counter
        if sales_counter == -1:
            sales_counter += 1
            next_window = revenue_growth_screen()
            widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


# REVENUE GROWTH SCREEN
class revenue_growth_screen(QMainWindow):
    def __init__(self):
        super(revenue_growth_screen, self).__init__()
        uic.loadUi('ui_files/sales_module/revenue_growth_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            float(self.current_year_total_revenue.text())
            float(self.last_year_total_revenue.text())

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
        global current_year_total_revenue, last_year_total_revenue, RevenueGrowth
        current_year_total_revenue = float(self.current_year_total_revenue.text())
        last_year_total_revenue = float(self.last_year_total_revenue.text())

        RevenueGrowth = revenue_growth(current_year_total_revenue, last_year_total_revenue)
        print(f'Revenue Growth: {RevenueGrowth}')

        sales_param_dict['Revenue Growth'] = RevenueGrowth

        global sales_counter
        if sales_counter == 0:
            # sales_counter += 1
            # next_window = customer_retention_rate_ee_screen()
            sales_counter += 3
            next_window = number_of_sales_staff_screen()
            widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

''''
# CUSTOMER RETENTION RATE (EE)
class customer_retention_rate_ee_screen(QMainWindow):
    def __init__(self):
        super(customer_retention_rate_ee_screen, self).__init__()
        uic.loadUi('ui_files/sales_module/customer_retention_rate_ee.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            int(self.current_customers.text())
            int(self.lost_customers.text())
            int(self.prior_year_customers.text())

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
        global current_customers, lost_customers, prior_year_customers, CustomerRetentionRateEE
        current_customers = int(self.current_customers.text())
        lost_customers = int(self.lost_customers.text())
        prior_year_customers = int(self.prior_year_customers.text())

        CustomerRetentionRateEE = \
            customer_retention_rate(current_customers, lost_customers, prior_year_customers)
        print(f'Customer Retention Rate (EE): {CustomerRetentionRateEE}')

        sales_param_dict['Customer Retention Rate (EE)'] = CustomerRetentionRateEE

        global sales_counter
        if sales_counter == 1:
            sales_counter += 1
            next_window = renewal_rate_en_screen()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

# RENEWAL RATE (EN)
class renewal_rate_en_screen(QMainWindow):
    def __init__(self):
        super(renewal_rate_en_screen, self).__init__()
        uic.loadUi('ui_files/sales_module/renewal_rate_en_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            int(self.renewals_on_time.text())
            int(self.total_current_customers.text())

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
        global renewals_on_time, total_current_customers, RenewalRateEN
        renewals_on_time = int(self.renewals_on_time.text())
        total_current_customers = int(self.total_current_customers.text())

        RenewalRateEN = \
            renewal_rate_en(renewals_on_time, total_current_customers)
        print(f'Renewal Rate (EN): {RenewalRateEN}')

        sales_param_dict['Renewal Rate (EN)'] = RenewalRateEN

        global sales_counter
        if sales_counter == 2:
            sales_counter += 1
            next_window = number_of_sales_staff_screen()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)
'''

# NUMBER OF SALES STAFF
class number_of_sales_staff_screen(QMainWindow):
    def __init__(self):
        super(number_of_sales_staff_screen, self).__init__()
        uic.loadUi('ui_files/sales_module/number_of_sales_staff_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            int(self.num_ee.text())
            int(self.num_en.text())
            int(self.num_nn.text())

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
        global num_ee, num_en, num_nn
        num_ee = int(self.num_ee.text())
        num_en = int(self.num_en.text())
        num_nn = int(self.num_nn.text())

        sales_param_dict['Number of Sales Staff (EE)'] = num_ee
        sales_param_dict['Number of Sales Staff (EN)'] = num_en
        sales_param_dict['Number of Sales Staff (NN)'] = num_nn

        global sales_counter
        if sales_counter == 3:
            sales_counter += 1
            next_window = spends_cost_measures_screen()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# SPENDS / COSTS MEASURES SCREEN
class spends_cost_measures_screen(QMainWindow):
    def __init__(self):
        super(spends_cost_measures_screen, self).__init__()
        uic.loadUi('ui_files/sales_module/spends_cost_measures_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            int(self.marketing_spends.text())
            int(self.customer_success_support_spend.text())
            int(self.tech_and_ops_spends.text())
            int(self.support_enablement_cost.text())

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
        global marketing_spends, customer_success_support_spend, tech_and_ops_spends, support_enablement_cost
        marketing_spends = int(self.marketing_spends.text())
        customer_success_support_spend = int(self.customer_success_support_spend.text())
        tech_and_ops_spends = int(self.tech_and_ops_spends.text())
        support_enablement_cost = int(self.support_enablement_cost.text())

        print(f'Total Marketing spends: {marketing_spends}')
        print(f'Total Customer Success / support spend: {customer_success_support_spend}')
        print(f'Total Tech & Ops Spend on Sales: {tech_and_ops_spends}')
        print(f'Total Support / Enablement Cost: {support_enablement_cost}')

        sales_param_dict['Total Marketing Spends'] = marketing_spends
        sales_param_dict['Total Customer Sucess / Support Spend'] = customer_success_support_spend
        sales_param_dict['Total Tech & Ops Spend on Sales'] = tech_and_ops_spends
        sales_param_dict['Total Support / Enablement Cost'] = support_enablement_cost

        global sales_counter
        if sales_counter == 4:
            sales_counter += 1
            next_window = sales_staff_cost_screen()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# SALES STAFF COST SCREEN
class sales_staff_cost_screen(QMainWindow):
    def __init__(self):
        super(sales_staff_cost_screen, self).__init__()
        uic.loadUi('ui_files/sales_module/sales_staff_cost_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            int(self.total_sga_cost.text())
            int(self.total_staff_fte.text())

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
        global total_sga_cost, total_staff_fte, AverageCostToSalesStaff
        total_sga_cost = int(self.total_sga_cost.text())
        total_staff_fte = int(self.total_staff_fte.text())

        AverageCostToSalesStaff = avg_cost_of_sales_staff(total_sga_cost, total_staff_fte)

        print(f'Average Cost to Sales Staff: {AverageCostToSalesStaff}')

        sales_param_dict['Average Cost to Sales Staff'] = AverageCostToSalesStaff

        global sales_counter
        if sales_counter == 5:
            sales_counter += 1
            next_window = anticipated_ltv_screen()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# ANTICIPATED LTV SCREEN
class anticipated_ltv_screen(QMainWindow):
    def __init__(self):
        super(anticipated_ltv_screen, self).__init__()
        uic.loadUi('ui_files/sales_module/anticipated_ltv_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            float(self.ltv_ee.text())
            float(self.ltv_en.text())
            float(self.ltv_nn.text())

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
        global ltv_ee, ltv_en, ltv_nn
        ltv_ee = float(self.ltv_ee.text())
        ltv_en = float(self.ltv_en.text())
        ltv_nn = float(self.ltv_nn.text())

        print(f'Anticipated Life Time Value (EE): {ltv_ee}')
        print(f'Anticipated Life Time Value (EN): {ltv_en}')
        print(f'Anticipated Life Time Value (NN): {ltv_nn}')

        sales_param_dict['Anticipated Life Time Value (EE)'] = ltv_ee
        sales_param_dict['Anticipated Life Time Value (EN)'] = ltv_en
        sales_param_dict['Anticipated Life Time Value (NN)'] = ltv_nn

        global sales_counter
        if sales_counter == 6:
            sales_counter += 1
            next_window = renewal_rate_screen()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# RENEWAL RATE SCREEN
class renewal_rate_screen(QMainWindow):
    def __init__(self):
        super(renewal_rate_screen, self).__init__()
        uic.loadUi('ui_files/sales_module/renewal_rate_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            int(self.renewals_on_time.text())
            int(self.total_current_customers.text())

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
        global renewals_on_time, total_current_customers, RenewalRate
        renewals_on_time = int(self.renewals_on_time.text())
        total_current_customers = int(self.total_current_customers.text())

        RenewalRate = float(renewal_rate(renewals_on_time, total_current_customers))

        print(f'Renewal Rate: {RenewalRate}')

        sales_param_dict['Renewal Rate'] = RenewalRate

        global sales_counter
        if sales_counter == 7:
            sales_counter += 1
            next_window = retention_rate_screen()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# RETENTION RATE SCREEN
class retention_rate_screen(QMainWindow):
    def __init__(self):
        super(retention_rate_screen, self).__init__()
        uic.loadUi('ui_files/sales_module/retention_rate_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            int(self.current_customers.text())
            int(self.prior_year_customers.text())

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
        global current_customers, prior_year_customers, RetentionRate
        current_customers = int(self.current_customers.text())
        prior_year_customers = int(self.prior_year_customers.text())

        RetentionRate = float(retention_rate(current_customers, prior_year_customers))

        print(f'Retention Rate: {RetentionRate}')

        sales_param_dict['Retention Rate'] = RetentionRate

        global sales_counter
        if sales_counter == 8:
            sales_counter += 1
            next_window = churn_rate_screen()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# CHURN RATE SCREEN
class churn_rate_screen(QMainWindow):
    def __init__(self):
        super(churn_rate_screen, self).__init__()
        uic.loadUi('ui_files/sales_module/churn_rate_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            int(self.customers_lost.text())

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
        global customer_lost, ChurnRate
        customers_lost = int(self.customers_lost.text())

        ChurnRate = float(churn_rate(customers_lost, prior_year_customers))

        print(f'Churn Rate: {ChurnRate}')

        sales_param_dict['Churn Rate'] = ChurnRate

        global sales_counter
        if sales_counter == 9:
            sales_counter += 1
            next_window = win_rate_screen()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# WIN RATE SCREEN
class win_rate_screen(QMainWindow):
    def __init__(self):
        super(win_rate_screen, self).__init__()
        uic.loadUi('ui_files/sales_module/win_rate_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            int(self.bids_won.text())
            int(self.bids_submitted.text())

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
        global bids_won, bids_submitted, WinRate
        bids_won = int(self.bids_won.text())
        bids_submitted = int(self.bids_submitted.text())

        WinRate = float(win_rate(bids_won, bids_submitted))

        print(f'Win Rate: {WinRate}')

        sales_param_dict['Win Rate'] = WinRate

        global sales_counter
        if sales_counter == 10:
            sales_counter += 1
            next_window = revenue_conversion_rate_screen()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# REVENUE CONVERSION SCREEN
class revenue_conversion_rate_screen(QMainWindow):
    def __init__(self):
        super(revenue_conversion_rate_screen, self).__init__()
        uic.loadUi('ui_files/sales_module/revenue_conversion_rate_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            int(self.bookings.text())
            int(self.qualified_pipeline.text())

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
        global bookings, qualififed_pipeline, RevenueConversionRate
        bookings = int(self.bookings.text())
        qualififed_pipeline = int(self.qualified_pipeline.text())

        RevenueConversionRate = float(revenue_conversion_rate(bookings, qualififed_pipeline))

        print(f'Revenue Conversion Rate: {RevenueConversionRate}')

        sales_param_dict['Revenue Conversion Rate'] = RevenueConversionRate

        global sales_counter
        if sales_counter == 11:
            sales_counter += 1
            next_window = pipeline_quality_screen()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# PIPELINE QUALITY SCREEN
class pipeline_quality_screen(QMainWindow):
    def __init__(self):
        super(pipeline_quality_screen, self).__init__()
        uic.loadUi('ui_files/sales_module/pipeline_quality_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            int(self.qualified_pipeline.text())
            int(self.total_pipeline.text())

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
        global qualififed_pipeline, total_pipeline, PipelineQuality
        qualififed_pipeline = int(self.qualified_pipeline.text())
        total_pipeline = int(self.total_pipeline.text())

        PipelineQuality = float(pipeline_quality(qualififed_pipeline, total_pipeline))

        print(f'Pipeline Quality: {PipelineQuality}')

        sales_param_dict['Pipeline Quality'] = PipelineQuality

        global sales_counter
        if sales_counter == 12:
            sales_counter += 1
            next_window = bill_to_book_ratio_screen()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# BILL TO BOOK RATIO SCREEN
class bill_to_book_ratio_screen(QMainWindow):
    def __init__(self):
        super(bill_to_book_ratio_screen, self).__init__()
        uic.loadUi('ui_files/sales_module/bill_to_book_ratio_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            int(self.new_revenue_billed.text())
            int(self.new_revenue_booked.text())

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
        global new_revenue_billed, new_revenue_booked, BillToBookRatio
        new_revenue_billed = int(self.new_revenue_billed.text())
        new_revenue_booked = int(self.new_revenue_booked.text())

        BillToBookRatio = float(bill_to_book_ratio(new_revenue_billed, new_revenue_booked))

        print(f'Bill to Book Ratio: {BillToBookRatio}')

        sales_param_dict['Bill to Book Ratio'] = BillToBookRatio

        global sales_counter
        if sales_counter == 13:
            sales_counter += 1
            next_window = display_table_screen()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# DISPLAY TABLE
class display_table_screen(QMainWindow):
    def __init__(self):
        super(display_table_screen, self).__init__()
        uic.loadUi('ui_files/sales_module/sales_display_table_screen.ui', self)

        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 150)
        self.load_data()

        self.backButton.clicked.connect(self.backScreen)

    def load_data(self):
        idx = 0
        self.tableWidget.setRowCount(len(sales_param_dict))
        for param in sales_param_dict.keys():
            self.tableWidget.setItem(idx, 0, QtWidgets.QTableWidgetItem(param))
            self.tableWidget.setItem(idx, 1, QtWidgets.QTableWidgetItem(str(sales_param_dict[param])))
            idx += 1

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


if __name__ == '__main__':
    demoApp = QApplication([])

    widget = QtWidgets.QStackedWidget()
    first_window = starting_window()

    # debugging
    # first_window = name_of_window()

    widget.addWidget(first_window)
    widget.showMaximized()

    demoApp.exec_()
