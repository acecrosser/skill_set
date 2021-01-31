# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interFace.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(400, 620)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QSize(400, 620))
        mainWindow.setMaximumSize(QSize(400, 620))
        font = QFont()
        font.setFamily(u"Arial")
        mainWindow.setFont(font)
        icon = QIcon()
        iconThemeName = u"ico"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"../util_ico.png", QSize(), QIcon.Normal, QIcon.Off)
            icon.addFile(u"../util_ico.png", QSize(), QIcon.Normal, QIcon.On)
        
        mainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(11, 300, 369, 24))
        self.comboBox.setModelColumn(0)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 25, 371, 265))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_company = QLabel(self.layoutWidget)
        self.label_company.setObjectName(u"label_company")

        self.verticalLayout.addWidget(self.label_company)

        self.name_company = QLineEdit(self.layoutWidget)
        self.name_company.setObjectName(u"name_company")

        self.verticalLayout.addWidget(self.name_company)

        self.label_inn = QLabel(self.layoutWidget)
        self.label_inn.setObjectName(u"label_inn")

        self.verticalLayout.addWidget(self.label_inn)

        self.inn_company = QLineEdit(self.layoutWidget)
        self.inn_company.setObjectName(u"inn_company")

        self.verticalLayout.addWidget(self.inn_company)

        self.label_kpp = QLabel(self.layoutWidget)
        self.label_kpp.setObjectName(u"label_kpp")

        self.verticalLayout.addWidget(self.label_kpp)

        self.kpp_company = QLineEdit(self.layoutWidget)
        self.kpp_company.setObjectName(u"kpp_company")

        self.verticalLayout.addWidget(self.kpp_company)

        self.label_bill = QLabel(self.layoutWidget)
        self.label_bill.setObjectName(u"label_bill")

        self.verticalLayout.addWidget(self.label_bill)

        self.number_bill = QLineEdit(self.layoutWidget)
        self.number_bill.setObjectName(u"number_bill")

        self.verticalLayout.addWidget(self.number_bill)

        self.label_address = QLabel(self.layoutWidget)
        self.label_address.setObjectName(u"label_address")

        self.verticalLayout.addWidget(self.label_address)

        self.address_work = QLineEdit(self.layoutWidget)
        self.address_work.setObjectName(u"address_work")

        self.verticalLayout.addWidget(self.address_work)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 560, 371, 51))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.makeEmail = QPushButton(self.layoutWidget1)
        self.makeEmail.setObjectName(u"makeEmail")

        self.horizontalLayout.addWidget(self.makeEmail)

        self.printReestr = QPushButton(self.layoutWidget1)
        self.printReestr.setObjectName(u"printReestr")

        self.horizontalLayout.addWidget(self.printReestr)

        self.printRequest = QPushButton(self.layoutWidget1)
        self.printRequest.setObjectName(u"printRequest")

        self.horizontalLayout.addWidget(self.printRequest)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 342, 371, 211))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_kkt = QLabel(self.layoutWidget2)
        self.label_kkt.setObjectName(u"label_kkt")

        self.verticalLayout_2.addWidget(self.label_kkt)

        self.model_kkt = QLineEdit(self.layoutWidget2)
        self.model_kkt.setObjectName(u"model_kkt")

        self.verticalLayout_2.addWidget(self.model_kkt)

        self.label_kkt_serial = QLabel(self.layoutWidget2)
        self.label_kkt_serial.setObjectName(u"label_kkt_serial")

        self.verticalLayout_2.addWidget(self.label_kkt_serial)

        self.serial_kkt = QLineEdit(self.layoutWidget2)
        self.serial_kkt.setObjectName(u"serial_kkt")

        self.verticalLayout_2.addWidget(self.serial_kkt)

        self.label_fn = QLabel(self.layoutWidget2)
        self.label_fn.setObjectName(u"label_fn")

        self.verticalLayout_2.addWidget(self.label_fn)

        self.serial_fn = QLineEdit(self.layoutWidget2)
        self.serial_fn.setObjectName(u"serial_fn")

        self.verticalLayout_2.addWidget(self.serial_fn)

        self.label_name = QLabel(self.layoutWidget2)
        self.label_name.setObjectName(u"label_name")

        self.verticalLayout_2.addWidget(self.label_name)

        self.spec_name = QLineEdit(self.layoutWidget2)
        self.spec_name.setObjectName(u"spec_name")

        self.verticalLayout_2.addWidget(self.spec_name)

        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"\u0423\u0442\u0438\u043b\u0438\u0442\u0430 \u0432\u043d\u0435\u0434\u0440\u0435\u043d\u0438\u044f", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("mainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f \u0438 \u0444\u0438\u0441\u043a\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u043e\u0434\u043d\u043e\u0439 \u0435\u0434\u0438\u043d\u0438\u0446\u044b \u041a\u041a\u0422", u"first_"))
        self.comboBox.setItemText(1, QCoreApplication.translate("mainWindow", u"\u041a\u043e\u043c\u043f\u043b\u0435\u043a\u0441\u043d\u0430\u044f \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u041a\u043e\u043d\u0442\u0443\u0440.\u041c\u0430\u0440\u043a\u0435\u0442\u0430", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("mainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u041a\u043e\u043d\u0442\u0443\u0440.\u041c\u0430\u0440\u043a\u0435\u0442\u0430", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("mainWindow", u"\u041f\u0435\u0440\u0435\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f \u041a\u041a\u0422 \u0431\u0435\u0437 \u0437\u0430\u043c\u0435\u043d\u044b  \u0424\u041d", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("mainWindow", u"\u041f\u0435\u0440\u0435\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f \u041a\u041a\u0422 \u0441 \u0437\u0430\u043c\u0435\u043d\u043e\u0439  \u0424\u041d", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("mainWindow", u"\u0421\u043d\u044f\u0442\u0438\u0435 \u0441 \u0443\u0447\u0435\u0442\u0430 \u041a\u041a\u0422", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("mainWindow", u"\u041f\u0440\u043e\u0448\u0438\u0432\u043a\u0430 \u041a\u041a\u0422", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("mainWindow", u"\u041f\u0443\u0441\u0442\u043e\u0439 \u0431\u043b\u0430\u043d\u043a", None))

        self.label_company.setText(QCoreApplication.translate("mainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 ", None))
        self.label_inn.setText(QCoreApplication.translate("mainWindow", u"\u0418\u041d\u041d", None))
        self.label_kpp.setText(QCoreApplication.translate("mainWindow", u"\u041a\u041f\u041f", None))
        self.label_bill.setText(QCoreApplication.translate("mainWindow", u"\u2116 \u0441\u0447\u0435\u0442\u0430", None))
        self.label_address.setText(QCoreApplication.translate("mainWindow", u"\u0410\u0434\u0440\u0435\u0441", None))
        self.makeEmail.setText(QCoreApplication.translate("mainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043f\u0438\u0441\u044c\u043c\u043e", None))
        self.printReestr.setText(QCoreApplication.translate("mainWindow", u"\u041f\u0435\u0447\u0430\u0442\u044c \u0440\u0435\u0435\u0441\u0442\u0440\u0430", None))
        self.printRequest.setText(QCoreApplication.translate("mainWindow", u"\u041f\u0435\u0447\u0430\u0442\u044c \u0437\u0430\u044f\u0432\u043a\u0438", None))
        self.label_kkt.setText(QCoreApplication.translate("mainWindow", u"\u041c\u043e\u0434\u0435\u043b\u044c \u041a\u041a\u0422", None))
        self.label_kkt_serial.setText(QCoreApplication.translate("mainWindow", u"\u0417\u0430\u0432\u043e\u0434\u0441\u043a\u043e\u0439 \u043d\u043e\u043c\u0435\u0440 \u041a\u041a\u0422", None))
        self.label_fn.setText(QCoreApplication.translate("mainWindow", u"\u0417\u0430\u0432\u043e\u0434\u043a\u043e\u0439 \u043d\u043e\u043c\u0435\u0440 \u0424\u041d", None))
        self.label_name.setText(QCoreApplication.translate("mainWindow", u"\u0424\u0418\u041e \u0412\u043d\u0435\u0434\u0440\u0435\u043d\u0446\u0430", None))
        self.spec_name.setText("")
    # retranslateUi

