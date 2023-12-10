# MODULE STUFF
from modules.marketing_module import *

# UI STUFF
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets, QtCore

QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

# counter for keeping in check the back and previous screen windows
marketing_counter = 0

# parameters dictionary (needed in table)
marketing_param_dict = dict()

class web_traffic(QMainWindow):
    def __init__(self):
        super(web_traffic, self).__init__()
        uic.loadUi('ui_files/marketing_module/marketing_web_traffic.ui', self)

        self.nextButton.clicked.connect(self.checkInput)

    def checkInput(self):
        try:
            int(self.web_traffic_1.text())
            int(self.web_traffic_2.text())
            int(self.web_traffic_3.text())
            int(self.web_traffic_4.text())
            int(self.web_traffic_5.text())

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
        global Website_Traffic, Organic_Search, Direct_Traffic, Referral_Traffic, Social_Media_Traffic
        Website_Traffic = int(self.web_traffic_1.text())
        Organic_Search = int(self.web_traffic_2.text())
        Direct_Traffic = int(self.web_traffic_3.text())
        Referral_Traffic = int(self.web_traffic_4.text())
        Social_Media_Traffic = int(self.web_traffic_5.text())

        print('Website Traffic and Search measure:',
              Website_Traffic, Organic_Search, Direct_Traffic, Referral_Traffic)
        global marketing_counter
        if marketing_counter == 0:
            marketing_counter += 1
            next_window = new_vs_return_visitors()
            widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

        global total_traffic, organic_search_percentage, direct_traffic_percentage, referral_traffic_percentage, social_media_traffic_percentage

        total_traffic, organic_search_percentage, direct_traffic_percentage, referral_traffic_percentage, social_media_traffic_percentage=web_traffic_search(Organic_Search, Direct_Traffic, Referral_Traffic, Social_Media_Traffic)
        
        marketing_param_dict['Total Traffic']=total_traffic
        marketing_param_dict['Organic Search Percentage']=organic_search_percentage
        marketing_param_dict['Direct Traffic Percentage']=direct_traffic_percentage
        marketing_param_dict['Referral Traffic Percentage']=referral_traffic_percentage
        marketing_param_dict['Social Media Traffic Percentage']=social_media_traffic_percentage

class new_vs_return_visitors(QMainWindow):
    def __init__(self):
        super(new_vs_return_visitors, self).__init__()
        uic.loadUi('ui_files/marketing_module/marketing_new_vs_return_visitors.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            int(self.visitors_1.text())
            int(self.visitors_2.text())
            int(self.visitors_3.text())
            float(self.visitors_4.text())

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
        global New_Visitors, Returning_Visitors, Total_Sessions, Average_Session_Duration
        New_Visitors = int(self.visitors_1.text())
        Returning_Visitors = int(self.visitors_2.text())
        Total_Sessions = int(self.visitors_3.text())
        Average_Session_Duration = float(self.visitors_4.text())
        
        print('New Vs Return Visitors:',
              New_Visitors, Returning_Visitors, Total_Sessions,  Average_Session_Duration)
        global marketing_counter
        if marketing_counter == 1:
            marketing_counter += 1
            next_window = exit_and_bounce_rate()
            widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

        global sessions_per_visitor, new_visitors_percentage, returning_visitors_percentage
        sessions_per_visitor, new_visitors_percentage, returning_visitors_percentage=new_vs_return_visitor(New_Visitors, Returning_Visitors, Total_Sessions, Average_Session_Duration)

        marketing_param_dict['Sessions Per Visitor']=sessions_per_visitor
        marketing_param_dict['New Visitors Percentage']=new_visitors_percentage
        marketing_param_dict['Returning Visitors Percentage']=returning_visitors_percentage

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


class exit_and_bounce_rate(QMainWindow):
    def __init__(self):
        super(exit_and_bounce_rate, self).__init__()
        uic.loadUi('ui_files/marketing_module/marketing_exit_and_bounce_rate.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            int(self.exit_rate_1.text())
            float(self.exit_rate_3.text())
            float(self.exit_rate_4.text())

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
        global Page_Views, Exit_Rate, Bounce_Rate
        Page_Views = int(self.exit_rate_1.text())
        Exit_Rate = float(self.exit_rate_3.text())
        Bounce_Rate = float(self.exit_rate_4.text())
        
        print('Exit and Bounce Rate:',
              Page_Views,Exit_Rate, Bounce_Rate)
        global marketing_counter
        if marketing_counter == 2:
            marketing_counter += 1
            next_window = conversion_cost_per_click()
            widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

        global total_exits, total_bounces
        total_exits, total_bounces=exit_and_total_bounces(Page_Views, Exit_Rate, Bounce_Rate)

        marketing_param_dict['Total Exits']=total_exits
        marketing_param_dict['Total Bounces']=total_bounces
    
    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

class conversion_cost_per_click(QMainWindow):
    def __init__(self):
        super(conversion_cost_per_click, self).__init__()
        uic.loadUi('ui_files/marketing_module/marketing_conversion_cost_per_click.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            int(self.cost_per_click_1.text())
            int(self.cost_per_click_2.text())
          
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
        global Conversions, Cost_per_click
        Conversions = int(self.cost_per_click_1.text())
        Cost_per_click = int(self.cost_per_click_2.text())
        
        print('Conversion and cost per click:',
              Conversions, Cost_per_click)
        global marketing_counter
        if marketing_counter == 3:
            marketing_counter += 1
            next_window = email_opens_clicks_sents()
            widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

        global conversion_rate, cost_per_conversion, cost_per_acquisition        
        conversion_rate, cost_per_conversion, cost_per_acquisition=conversion_rate(Conversions, Cost_per_click, total_traffic)        
        
        marketing_param_dict['Conversion Rate']=conversion_rate    
        marketing_param_dict['Cost Per Conversion']=cost_per_conversion
        marketing_param_dict['Cost Per Acquisition']=cost_per_acquisition

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

class email_opens_clicks_sents(QMainWindow):
    def __init__(self):
        super(email_opens_clicks_sents, self).__init__()
        uic.loadUi('ui_files/marketing_module/marketing_email_opens_clicks_sents.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            int(self.email_open_1.text())
            int(self.email_open_2.text())
            int(self.email_open_3.text())

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
        global Email_Open, Email_Clicks, Email_Sent
        Email_Open = int(self.email_open_1.text())
        Email_Clicks = int(self.email_open_2.text())
        Email_Sent = float(self.email_open_3.text())
                
        print('Exit and Bounce Rate:',
               Email_Open, Email_Clicks, Email_Sent)
        global marketing_counter
        if marketing_counter == 4:
            marketing_counter += 1
            next_window = impression_social_engagements()
            widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

        global email_open_rate, email_click_through_rate
        email_open_rate, email_click_through_rate=email_open_rate(Email_Open, Email_Clicks, Email_Sent)

        marketing_param_dict['Email Open Rate']=email_open_rate
        marketing_param_dict['Email Click Through Rate']=email_click_through_rate
    
    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

class impression_social_engagements(QMainWindow):
    def __init__(self):
        super(impression_social_engagements, self).__init__()
        uic.loadUi('ui_files/marketing_module/marketing_impression_social_engagement.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            int(self.social_reach_1.text())
            int(self.social_reach_2.text())
          
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
        global Impression, Social_Engagement 
        Impression = int(self.social_reach_1.text())
        Social_Engagement = int(self.social_reach_2.text())
        
        print('Conversion and cost per click:',
              Impression, Social_Engagement)
        global marketing_counter
        if marketing_counter == 5:
            marketing_counter += 1
            next_window = display_table_screen()
            widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

        global engagement_rate
        engagement_rate=engagement_rate(Impression, Social_Engagement)

        marketing_param_dict['Engagement Rate']=engagement_rate
    
    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# DISPLAY TABLE
class display_table_screen(QMainWindow):
    def __init__(self):
        super(display_table_screen, self).__init__()
        uic.loadUi('ui_files/marketing_module/marketing_display_table_screen.ui', self)

        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 150)
        self.load_data()

        self.backButton.clicked.connect(self.backScreen)

    def load_data(self):
        idx = 0
        self.tableWidget.setRowCount(len(marketing_param_dict))
        for param in marketing_param_dict.keys():
            self.tableWidget.setItem(idx, 0, QtWidgets.QTableWidgetItem(param))
            self.tableWidget.setItem(idx, 1, QtWidgets.QTableWidgetItem(str(marketing_param_dict[param])))
            idx += 1

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

if __name__ == '__main__':
    demoApp = QApplication([])

    widget = QtWidgets.QStackedWidget()
    first_window = web_traffic()

    # debugging
    # first_window = name_of_window()

    widget.addWidget(first_window)
    widget.showMaximized()

    demoApp.exec_()