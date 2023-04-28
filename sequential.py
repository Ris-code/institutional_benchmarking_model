# MODULE STUFF
from qualityModule import *
from managementModule import *
from riskModule import *
from effortModule import *
from salesModule import *
from marketingModule import *

# UI STUFF
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets, QtCore

QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

# for dependent comboboxes
from PyQt5.QtGui import QStandardItemModel, QStandardItem

# counter for keeping in check the back and previous screen windows
counter = 0

# parameters dictionary (needed in table)
sales_param_dict = dict()
marketing_param_dict = dict()

# MAIN START SCREEN
class main_start_screen(QMainWindow):
    def __init__(self):
        super(main_start_screen, self).__init__()
        uic.loadUi('ui_files/ultimate_start_screen.ui', self)

        self.startButton.clicked.connect(self.nextScreen)

    def nextScreen(self):
        global counter
        if counter == 0:
            counter += 1
            next_window = ability_scaling_window()
            widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


# ABILITY SCALING SCREEN
abilityEntry, abiltyIntermediate, abilityHigh, abilityExpert \
    = map(float, [1, 1, 1, 1])

class ability_scaling_window(QMainWindow):
    def __init__(self):
        super(ability_scaling_window, self).__init__()
        uic.loadUi('ui_files/ability_scaling_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            float(self.abilityEntry.text())
            float(self.abilityIntermediate.text())
            float(self.abilityHigh.text())
            float(self.abilityExpert.text())

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
        global abilityEntry, abilityIntermediate, abilityHigh, abilityExpert
        abilityEntry = float(self.abilityEntry.text())
        abilityIntermediate = float(self.abilityIntermediate.text())
        abilityHigh = float(self.abilityHigh.text())
        abilityExpert = float(self.abilityExpert.text())

        abilityEntry, abilityIntermediate, abilityHigh, abilityExpert \
            = map(lambda x: x/abilityEntry,
                  [abilityEntry,
                   abilityIntermediate,
                   abilityHigh,
                   abilityExpert])

        print('Ability scaling:',
              abilityEntry, abiltyIntermediate, abilityHigh, abilityExpert)
        
        global counter
        if counter == 1:
            counter += 1
            next_window = jobType_scaling_window()
            widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# JOB-TYPE SCALING SCREEN
jobSimple, jobMedium, jobHigh, jobComplex = map(float, [1, 1, 1, 1])

class jobType_scaling_window(QMainWindow):
    def __init__(self):
        super(jobType_scaling_window, self).__init__()
        uic.loadUi('ui_files/jobType_scaling_screen.ui', self)

        # adjusting label size
        self.heading.adjustSize()
        self.jobLabel.adjustSize()

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            float(self.jobSimple.text())
            float(self.jobMedium.text())
            float(self.jobHigh.text())
            float(self.jobComplex.text())

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
        global jobSimple, jobMedium, jobHigh, jobComplex
        jobSimple = float(self.jobSimple.text())
        jobMedium = float(self.jobMedium.text())
        jobHigh = float(self.jobHigh.text())
        jobComplex = float(self.jobComplex.text())

        jobSimple, jobMedium, jobHigh, jobComplex \
            = map(lambda x: x/jobSimple,
                  [jobSimple, jobMedium, jobHigh, jobComplex])

        print('JobType scaling:',
              jobSimple, jobMedium, jobHigh, jobComplex)

        global counter
        if counter == 2:
            counter += 1
            next_window = ability_jobType_window()
            widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# ABILITY JOB TYPE SCREEN
class ability_jobType_window(QMainWindow):
    def __init__(self):
        super(ability_jobType_window, self).__init__()
        uic.loadUi('ui_files/ability_jobType_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            int(self.s1.text())
            int(self.s2.text())
            int(self.s3.text())
            int(self.s4.text())

            int(self.m1.text())
            int(self.m2.text())
            int(self.m3.text())
            int(self.m4.text())

            int(self.h1.text())
            int(self.h2.text())
            int(self.h3.text())
            int(self.h4.text())

            int(self.c1.text())
            int(self.c2.text())
            int(self.c3.text())
            int(self.c4.text())

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
        global s1, s2, s3, s4
        s1 = self.s1.text()
        s2 = self.s2.text()
        s3 = self.s3.text()
        s4 = self.s4.text()

        global m1, m2, m3, m4
        m1 = self.m1.text()
        m2 = self.m2.text()
        m3 = self.m3.text()
        m4 = self.m4.text()

        global h1, h2, h3, h4
        h1 = self.h1.text()
        h2 = self.h2.text()
        h3 = self.h3.text()
        h4 = self.h4.text()

        global c1, c2, c3, c4
        c1 = self.c1.text()
        c2 = self.c2.text()
        c3 = self.c3.text()
        c4 = self.c4.text()

        s1, s2, s3, s4, m1, m2, m3, m4, h1, h2, h3, h4, c1, c2, c3, c4 \
            = map(int,
                  [s1, s2, s3, s4,
                   m1, m2, m3, m4,
                   h1, h2, h3, h4,
                   c1, c2, c3, c4])

        global E_Simple, E_Medium, E_High, E_Complex
        E_Simple = {
            "Entry": E(abilityEntry, jobSimple, s1),
            "Intermediate": E(abilityIntermediate, jobSimple, s2),
            "High": E(abilityHigh, jobSimple, s3),
            "Expert": E(abilityExpert, jobSimple, s4)
            }
        E_Medium = {
            "Entry": E(abilityEntry, jobMedium, m1),
            "Intermediate": E(abilityIntermediate, jobMedium, m2),
            "High": E(abilityHigh, jobMedium, m3),
            "Expert": E(abilityExpert, jobMedium, m4)
            }
        E_High = {
            "Entry": E(abilityEntry, jobHigh, h1),
            "Intermediate": E(abilityIntermediate, jobHigh, h2),
            "High": E(abilityHigh, jobHigh, h3),
            "Expert": E(abilityExpert, jobHigh, h4)
            }
        E_Complex = {
            "Entry": E(abilityEntry, jobComplex, c1),
            "Intermediate": E(abilityIntermediate, jobComplex, c2),
            "High": E(abilityHigh, jobComplex, c3),
            "Expert": E(abilityExpert, jobComplex, c4)
            }

        global Effort_Dict
        Effort_Dict = {
            'Simple': E_Simple,
            'Medium': E_Medium,
            'High': E_High,
            'Complex': E_Complex
            }

        global counter
        if counter == 3:
            counter += 1
            next_window = quality_window()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# QUALITY SCREEN
class quality_window(QMainWindow):
    def __init__(self):
        super(quality_window, self).__init__()
        uic.loadUi('ui_files/quality_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            float(self.paramA.text())
            float(self.paramB.text())
            float(self.paramC.text())
            float(self.paramD.text())

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
        A = self.paramA.text()
        B = self.paramB.text()
        C = self.paramC.text()
        D = self.paramD.text()
        A, B, C, D = map(float, [A, B, C, D])

        global Q_parameterArray
        Q_parameterArray = [A, B, C, D]

        print('Q_parameterArray:', Q_parameterArray)

        global counter
        if counter == 4:
            counter += 1
            next_window = quality_scaling_window()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# QUALITY SCALING SCREEN
class quality_scaling_window(QMainWindow):
    def __init__(self):
        super(quality_scaling_window, self).__init__()
        uic.loadUi('ui_files/quality_scaling_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            float(self.qualityBasic.text())
            float(self.qualityStandard.text())
            float(self.qualityHigh.text())
            float(self.qualityPremium.text())

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
        qualityBasic = self.qualityBasic.text()
        qualityStandard = self.qualityStandard.text()
        qualityHigh = self.qualityHigh.text()
        qualityPremium = self.qualityPremium.text()

        qualityBasic, qualityStandard, qualityHigh, qualityPremium \
            = map(float,
                  [qualityBasic, qualityStandard, qualityHigh, qualityPremium])
        qualityBasic, qualityStandard, qualityHigh, qualityPremium \
            = map(lambda x: x/qualityBasic,
                  [qualityBasic, qualityStandard, qualityHigh, qualityPremium])

        qualityScalingFactorsArray = [
            qualityBasic, qualityStandard, qualityHigh, qualityPremium
            ]

        print('qualityScalingFactorsArray:', qualityScalingFactorsArray)

        qualityFactorsInput(qualityScalingFactorsArray)

        # Quality Factors Mapping
        global Q_Simple, Q_Medium, Q_High, Q_Complex
        Q_Simple = {
            "Entry": Q(qualityBasic, s1, Q_parameterArray),
            "Intermediate": Q(0.75*qualityBasic, s2, Q_parameterArray),
            "High": Q(0.5*qualityBasic, s3, Q_parameterArray),
            "Expert": Q(0.25*qualityBasic, s4, Q_parameterArray)
            }
        Q_Medium = {
            "Entry": Q(qualityStandard, m1, Q_parameterArray),
            "Intermediate": Q(qualityStandard, m2, Q_parameterArray),
            "High": Q(qualityBasic, m3, Q_parameterArray),
            "Expert": Q(0.5*qualityBasic, m4, Q_parameterArray)
            }
        Q_High = {
            "Entry": Q(qualityHigh, h1, Q_parameterArray),
            "Intermediate": Q(qualityHigh, h2, Q_parameterArray),
            "High": Q(qualityStandard, h3, Q_parameterArray),
            "Expert": Q(qualityBasic, h4, Q_parameterArray)
            }
        Q_Complex = {
            "Entry": Q(qualityPremium, c1, Q_parameterArray),
            "Intermediate": Q(qualityPremium, c2, Q_parameterArray),
            "High": Q(qualityHigh, c3, Q_parameterArray),
            "Expert": Q(qualityStandard, c4, Q_parameterArray)
            }

        # Quality Output Dictionary
        global Quality_Dict
        Quality_Dict = {
            'Simple': Q_Simple,
            'Medium': Q_Medium,
            'High': Q_High,
            'Complex': Q_Complex
            }

        global counter
        if counter == 5:
            counter += 1
            next_window = management_window()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# MANAGEMENT SCREEN
class management_window(QMainWindow):
    def __init__(self):
        super(management_window, self).__init__()
        uic.loadUi('ui_files/management_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            float(self.paramE.text())
            float(self.paramF.text())
            float(self.paramG.text())
            float(self.paramH.text())
            float(self.paramI.text())

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
        E = self.paramE.text()
        F = self.paramF.text()
        G = self.paramG.text()
        H = self.paramH.text()
        I = self.paramI.text()
        E, F, G, H, I = map(float, [E, F, G, H, I])

        global M_parameterArray
        M_parameterArray = [E, F, G, H, I]

        print('M_parameterArray:', M_parameterArray)

        global counter
        if counter == 6:
            counter += 1
            next_window = management_scaling_window()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# MANAGEMENT SCALING SCREEN
class management_scaling_window(QMainWindow):
    def __init__(self):
        super(management_scaling_window, self).__init__()
        uic.loadUi('ui_files/management_scaling_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            float(self.managementLow.text())
            float(self.managementMedium.text())
            float(self.managementHigh.text())

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
        managementLow = self.managementLow.text()
        managementMedium = self.managementMedium.text()
        managementHigh = self.managementHigh.text()

        managementLow, managementMedium, managementHigh \
            = map(float,
                  [managementLow, managementMedium, managementHigh])
        managementLow, managementMedium, managementHigh \
            = map(lambda x: x/managementLow,
                  [managementLow, managementMedium, managementHigh])

        managementScalingFactorsArray \
            = [managementLow, managementMedium, managementHigh]

        print('managementScalingFactorsArray:', managementScalingFactorsArray)

        managementFactorsInput(managementScalingFactorsArray)

        # Management Factors Mapping
        global M_Simple, M_Medium, M_High, M_Complex
        M_Simple = {
            "Entry": M(managementLow, s1, M_parameterArray),
            "Intermediate": M(managementLow, s2, M_parameterArray)
            }
        M_Medium = {
            "Entry": M(managementMedium, m1, M_parameterArray),
            "Intermediate": M(managementMedium, m2, M_parameterArray),
            "High": M(managementLow, m3, M_parameterArray),
            "Expert": M(managementLow, m4, M_parameterArray)
            }
        M_High = {
            "Entry": M(managementHigh, h1, M_parameterArray),
            "Intermediate": M(managementHigh, h2, M_parameterArray),
            "High": M(managementMedium, h3, M_parameterArray),
            "Expert": M(managementLow, h4, M_parameterArray)
            }
        M_Complex = {
            "High": M(managementHigh, c3, M_parameterArray),
            "Expert": M(managementHigh, c4, M_parameterArray)
            }

        # Management Output Dictionary
        global Management_Dict
        Management_Dict = {
            'Simple': M_Simple,
            'Medium': M_Medium,
            'High': M_High,
            'Complex': M_Complex
            }

        global counter
        if counter == 7:
            counter += 1
            next_window = risk_window()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# RISK SCREEN
class risk_window(QMainWindow):
    def __init__(self):
        super(risk_window, self).__init__()
        uic.loadUi('ui_files/risk_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            float(self.paramJ.text())
            float(self.paramK.text())

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
        J = self.paramJ.text()
        K = self.paramK.text()
        J, K = map(float, [J, K])

        global R_parameterArray
        R_parameterArray = [J, K]

        print('R_parameterArray:', R_parameterArray)

        global counter
        if counter == 8:
            counter += 1
            next_window = risk_scaling_window()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# RISK SCALING SCREEN
class risk_scaling_window(QMainWindow):
    def __init__(self):
        super(risk_scaling_window, self).__init__()
        uic.loadUi('ui_files/risk_scaling_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

        self.viewButton.clicked.connect(self.viewLookupTable)

    def checkInput(self):
        try:
            float(self.riskLow.text())
            float(self.riskMedium.text())
            float(self.riskHigh.text())
            float(self.riskComplex.text())

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
        riskLow = self.riskLow.text()
        riskMedium = self.riskMedium.text()
        riskHigh = self.riskHigh.text()
        riskComplex = self.riskComplex.text()

        riskLow, riskMedium, riskHigh, riskComplex \
            = map(float,
                  [riskLow, riskMedium, riskHigh, riskComplex])
        riskLow, riskMedium, riskHigh, riskComplex \
            = map(lambda x: x/riskLow,
                  [riskLow, riskMedium, riskHigh, riskComplex])

        riskScalingFactorsArray = [riskLow, riskMedium, riskHigh, riskComplex]

        print('riskScalingFactorsArray:', riskScalingFactorsArray)

        riskFactorsInput(riskScalingFactorsArray)

        # Risk Factors Mapping
        global R_Low, R_Medium, R_High, R_NA
        R_Low = {
            "Simple": R(riskLow, R_parameterArray)
            }
        R_Medium = {
            "Simple": R(riskLow, R_parameterArray),
            "Medium": R(riskLow, R_parameterArray)
            }
        R_High = {
            "Simple": R(riskMedium, R_parameterArray),
            "Medium": R(riskMedium, R_parameterArray),
            "High": R(riskHigh, R_parameterArray)
            }
        R_NA = {
            "Simple": R(riskComplex, R_parameterArray),
            "Medium": R(riskComplex, R_parameterArray),
            "High": R(riskComplex, R_parameterArray),
            "NA": R(riskComplex, R_parameterArray)
            }

        # Risk Output Dictionary
        global Risk_Dict
        Risk_Dict = {
            'Low': R_Low,
            'Medium': R_Medium,
            'High': R_High,
            'NA': R_NA
            }

        global counter
        if counter == 9:
            counter += 1
            next_window = lookup_table_window()
            widget.addWidget(next_window)

        if counter == 10:
            counter += 1
            next_window = output_drop_down_window()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 2)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def viewLookupTable(self):
        global counter
        if counter == 9:
            counter += 1
            next_window = lookup_table_window()
            widget.addWidget(next_window)

        if counter == 10:
            counter += 1
            next_window = output_drop_down_window()
            widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


# BUSINESS IMPACT LOOKUP TABLE
class lookup_table_window(QMainWindow):
    def __init__(self):
        super(lookup_table_window, self).__init__()
        uic.loadUi('ui_files/risk_lookup_table.ui', self)
        self.returnButton.clicked.connect(self.returnBack)

    def returnBack(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# OUTPUT SCREEN
class output_drop_down_window(QMainWindow):
    def __init__(self):
        super(output_drop_down_window, self).__init__()
        uic.loadUi('ui_files/output_drop_down_screen.ui', self)
        self.show()

        self.model = QStandardItemModel(self)

        self.factors.setModel(self.model)
        self.parameters1.setModel(self.model)
        self.parameters2.setModel(self.model)

        self.nextButton.clicked.connect(self.nextScreen)
        self.backButton.clicked.connect(self.backScreen)

        for factor_key in dictionary.keys():
            FACTOR = QStandardItem(factor_key)
            self.model.appendRow(FACTOR)
            factor_key_dict = dictionary.get(factor_key)

            for param1_key in factor_key_dict.keys():
                PARAM1 = QStandardItem(param1_key)
                FACTOR.appendRow(PARAM1)

                param1_array = factor_key_dict.get(param1_key)

                for value in param1_array:
                    PARAM2 = QStandardItem(value)
                    PARAM1.appendRow(PARAM2)

        self.factors.currentIndexChanged.connect(self.updateParam1Combo)
        self.updateParam1Combo(0)
        self.factors.activated.connect(self.labelUpdate)

        # initial default values for labels
        self.paramLabel1.setText('Job Type')
        self.paramLabel2.setText('Ability')

        self.generateButton.clicked.connect(self.generateOutput)

        self.nextButton.clicked.connect(self.nextScreen)

    def labelUpdate(self):
        if self.factors.currentText() == "Quality" \
                or \
                self.factors.currentText() == "Management" \
                or \
                self.factors.currentText() == "Effort":
            self.paramLabel1.setText('Job Type')
            self.paramLabel2.setText('Ability')
        elif self.factors.currentText() == "Risk":
            self.paramLabel1.setText('Risk Impact')
            self.paramLabel2.setText('Mitigation Options')

    def updateParam1Combo(self, index):
        model_index = self.model.index(
            index, 0, self.factors.rootModelIndex()
            )
        self.parameters1.setRootModelIndex(model_index)
        self.parameters1.setCurrentIndex(0)
        self.parameters1.currentIndexChanged.connect(self.updateParam2Combo)
        self.updateParam2Combo(0)

    def updateParam2Combo(self, index):
        model_index = self.model.index(
            index, 0, self.parameters1.rootModelIndex()
            )
        self.parameters2.setRootModelIndex(model_index)
        self.parameters2.setCurrentIndex(0)

    def generateOutput(self):
        # output_text = self.factors.currentText() + " " \
        #   + self.parameters1.currentText() + " " \
        #   + self.parameters2.currentText()
        # self.outputDataLabel.setText(output_text)

        # OUTPUT DICTIONARY
        output_dictionary = {
            'Quality': Quality_Dict,
            'Management': Management_Dict,
            'Risk': Risk_Dict,
            'Effort': Effort_Dict
            }

        output_text \
            = output_dictionary\
            [self.factors.currentText()]\
            [self.parameters1.currentText()]\
            [self.parameters2.currentText()]

        self.outputDataLabel.setText(
            f'{output_text:.2f}' + " " \
                + str(self.factors.currentText()) + " units"
            )
        
    def nextScreen(self):
        global counter
        if counter == 11:
            counter += 1
            next_window = sales_starting_window()
            widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 2)


# FACTORS & PARAMETERS DICTIONARY
dictionary = {
    'Quality': {
        'Simple': ['Entry', 'Intermediate', 'High', 'Expert'],
        'Medium': ['Entry', 'Intermediate', 'High', 'Expert'],
        'High': ['Entry', 'Intermediate', 'High', 'Expert'],
        'Complex': ['Entry', 'Intermediate', 'High', 'Expert']
        },
    'Management': {
        'Simple': ['Entry', 'Intermediate'],
        'Medium': ['Entry', 'Intermediate', 'High', 'Expert'],
        'High': ['Entry', 'Intermediate', 'High', 'Expert'],
        'Complex': ['High', 'Expert']
        },
    'Risk': {
        'Low': ['Simple'],
        'Medium': ['Simple', 'Medium'],
        'High': ['Simple', 'Medium', 'High'],
        'NA': ['Simple', 'Medium', 'High', 'NA']
        },
    'Effort': {
        'Simple': ['Entry', 'Intermediate', 'High', 'Expert'],
        'Medium': ['Entry', 'Intermediate', 'High', 'Expert'],
        'High': ['Entry', 'Intermediate', 'High', 'Expert'],
        'Complex': ['Entry', 'Intermediate', 'High', 'Expert']
    }
}


# SALES STARTING SCREEN
class sales_starting_window(QMainWindow):
    def __init__(self):
        super(sales_starting_window, self).__init__()
        uic.loadUi('ui_files/sales_module/sales_starting_screen.ui', self)

        self.nextButton.clicked.connect(self.nextScreen)
        self.backButton.clicked.connect(self.backScreen)

    def nextScreen(self):
        global counter
        if counter == 12:
            counter += 1
            next_window = revenue_growth_screen()
            widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


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

        global counter
        if counter == 13:
            counter += 1
            next_window = number_of_sales_staff_screen()
            widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


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

        global counter
        if counter == 14:
            counter += 1
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

        global counter
        if counter == 15:
            counter += 1
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

        global counter
        if counter == 16:
            counter += 1
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

        global counter
        if counter == 17:
            counter += 1
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

        global counter
        if counter == 18:
            counter += 1
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

        global counter
        if counter == 19:
            counter += 1
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

        global counter
        if counter == 20:
            counter += 1
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

        global counter
        if counter == 21:
            counter += 1
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

        global counter
        if counter == 22:
            counter += 1
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

        global counter
        if counter == 23:
            counter += 1
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

        global counter
        if counter == 24:
            counter += 1
            next_window = sales_display_table_screen()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# DISPLAY TABLE
class sales_display_table_screen(QMainWindow):
    def __init__(self):
        super(sales_display_table_screen, self).__init__()
        uic.loadUi('ui_files/sales_module/sales_display_table_screen.ui', self)

        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 150)
        self.load_data()

        self.nextButton.clicked.connect(self.nextScreen)
        self.backButton.clicked.connect(self.backScreen)

    def load_data(self):
        idx = 0
        self.tableWidget.setRowCount(len(sales_param_dict))
        for param in sales_param_dict.keys():
            self.tableWidget.setItem(idx, 0, QtWidgets.QTableWidgetItem(param))
            self.tableWidget.setItem(idx, 1, QtWidgets.QTableWidgetItem(str(sales_param_dict[param])))
            idx += 1

    def nextScreen(self):
        global counter
        if counter == 25:
            counter += 1
            next_window = marketing_starting_window()
            widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# MARKETING STARTING SCREEN
class marketing_starting_window(QMainWindow):
    def __init__(self):
        super(marketing_starting_window, self).__init__()
        uic.loadUi('ui_files/marketing_module/marketing_starting_screen.ui', self)

        self.nextButton.clicked.connect(self.nextScreen)
        self.backButton.clicked.connect(self.backScreen)

    def nextScreen(self):
        global counter
        if counter == 26:
            counter += 1
            next_window = web_traffic()
            widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


class web_traffic(QMainWindow):
    def __init__(self):
        super(web_traffic, self).__init__()
        uic.loadUi('ui_files/marketing_module/marketing_web_traffic.ui', self)

        self.backButton.clicked.connect(self.backScreen)
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
        global counter
        if counter == 27:
            counter += 1
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

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


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
        global counter
        if counter == 28:
            counter += 1
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

        global total_exits, total_bounces
        total_exits, total_bounces = exit_and_total_bounces(Page_Views, Exit_Rate, Bounce_Rate)

        marketing_param_dict['Total Exits'] = total_exits
        marketing_param_dict['Total Bounces'] = total_bounces

        global counter
        if counter == 29:
            counter += 1
            next_window = conversion_cost_per_click()
            widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
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

        global ConversionTable, CostPerConversion, CostPerAcquisition     
        ConversionTable, CostPerConversion, CostPerAcquisition = conversion_rate(Conversions, Cost_per_click, total_traffic)        
        
        marketing_param_dict['Conversion Rate'] = ConversionTable
        marketing_param_dict['Cost Per Conversion'] = CostPerConversion
        marketing_param_dict['Cost Per Acquisition'] = CostPerAcquisition

        global counter
        if counter == 30:
            counter += 1
            next_window = email_opens_clicks_sents()
            widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

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

        global EmailOpenRate, EmailClickThroughRate
        EmailOpenRate, EmailClickThroughRate = email_open_rate(Email_Open, Email_Clicks, Email_Sent)

        marketing_param_dict['Email Open Rate'] = EmailOpenRate
        marketing_param_dict['Email Click Through Rate'] = EmailClickThroughRate

        global counter
        if counter == 31:
            counter += 1
            next_window = impression_social_engagements()
            widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
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

        global EngagementRate
        EngagementRate = engagement_rate(Impression, Social_Engagement)

        marketing_param_dict['Engagement Rate'] = EngagementRate

        global counter
        if counter == 32:
            counter += 1
            next_window = marketing_display_table_screen()
            widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# DISPLAY TABLE
class marketing_display_table_screen(QMainWindow):
    def __init__(self):
        super(marketing_display_table_screen, self).__init__()
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
    first_window = main_start_screen()

    # debugging
    # first_window = name_of_window()

    widget.addWidget(first_window)
    widget.show()

    demoApp.exec_()
