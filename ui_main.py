# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainHDlTlQ.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1168, 659)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_12 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.frame_10 = QFrame(self.tab)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_10)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.frame_10)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(500, 182))
        self.verticalLayout_14 = QVBoxLayout(self.groupBox)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_13.addWidget(self.label_3)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_13.addWidget(self.label_2)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.verticalLayout_13.addWidget(self.label)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_13.addWidget(self.label_4)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_13.addWidget(self.label_5)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_13.addWidget(self.label_6)


        self.verticalLayout_14.addLayout(self.verticalLayout_13)


        self.verticalLayout_37.addWidget(self.groupBox)


        self.verticalLayout_34.addWidget(self.frame_10, 0, Qt.AlignTop)

        self.groupBox_17 = QGroupBox(self.tab)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.verticalLayout_94 = QVBoxLayout(self.groupBox_17)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.verticalLayout_93 = QVBoxLayout()
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.label_37 = QLabel(self.groupBox_17)
        self.label_37.setObjectName(u"label_37")

        self.verticalLayout_93.addWidget(self.label_37)

        self.label_38 = QLabel(self.groupBox_17)
        self.label_38.setObjectName(u"label_38")

        self.verticalLayout_93.addWidget(self.label_38)

        self.label_36 = QLabel(self.groupBox_17)
        self.label_36.setObjectName(u"label_36")

        self.verticalLayout_93.addWidget(self.label_36)

        self.label_15 = QLabel(self.groupBox_17)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_93.addWidget(self.label_15)


        self.verticalLayout_94.addLayout(self.verticalLayout_93)

        self.horizontalLayout_73 = QHBoxLayout()
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.pushButton_19 = QPushButton(self.groupBox_17)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.horizontalLayout_73.addWidget(self.pushButton_19)

        self.pushButton_20 = QPushButton(self.groupBox_17)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.horizontalLayout_73.addWidget(self.pushButton_20)


        self.verticalLayout_94.addLayout(self.horizontalLayout_73)


        self.verticalLayout_34.addWidget(self.groupBox_17, 0, Qt.AlignTop)

        self.tableWidget_9 = QTableWidget(self.tab)
        if (self.tableWidget_9.columnCount() < 2):
            self.tableWidget_9.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget_9.setObjectName(u"tableWidget_9")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_9.sizePolicy().hasHeightForWidth())
        self.tableWidget_9.setSizePolicy(sizePolicy)
        self.tableWidget_9.setShowGrid(False)
        self.tableWidget_9.horizontalHeader().setVisible(False)
        self.tableWidget_9.horizontalHeader().setMinimumSectionSize(23)
        self.tableWidget_9.verticalHeader().setVisible(False)
        self.tableWidget_9.verticalHeader().setDefaultSectionSize(23)

        self.verticalLayout_34.addWidget(self.tableWidget_9)

        self.frame_11 = QFrame(self.tab)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_11)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)

        self.verticalLayout_38.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(1, 1, 1, 1)

        self.verticalLayout_38.addWidget(self.frame_13)


        self.verticalLayout_34.addWidget(self.frame_11, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.horizontalLayout_13.addLayout(self.verticalLayout_34)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_35 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.tableWidget_7 = QTableWidget(self.groupBox_2)
        if (self.tableWidget_7.columnCount() < 4):
            self.tableWidget_7.setColumnCount(4)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(3, __qtablewidgetitem5)
        self.tableWidget_7.setObjectName(u"tableWidget_7")
        self.tableWidget_7.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_7.verticalHeader().setVisible(False)
        self.tableWidget_7.verticalHeader().setDefaultSectionSize(23)

        self.verticalLayout_35.addWidget(self.tableWidget_7)


        self.verticalLayout_33.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_36 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.tableWidget_8 = QTableWidget(self.groupBox_3)
        if (self.tableWidget_8.columnCount() < 4):
            self.tableWidget_8.setColumnCount(4)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        self.tableWidget_8.setObjectName(u"tableWidget_8")
        self.tableWidget_8.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_8.verticalHeader().setVisible(False)
        self.tableWidget_8.verticalHeader().setDefaultSectionSize(23)

        self.verticalLayout_36.addWidget(self.tableWidget_8)


        self.verticalLayout_33.addWidget(self.groupBox_3)


        self.horizontalLayout_13.addLayout(self.verticalLayout_33)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)


        self.verticalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_3 = QFrame(self.tab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_3)
        self.verticalLayout_16.setSpacing(6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(9, -1, 9, -1)
        self.frame_14 = QFrame(self.frame_3)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_7 = QLabel(self.frame_14)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_15.addWidget(self.label_7)


        self.horizontalLayout_14.addLayout(self.verticalLayout_15)


        self.verticalLayout_16.addWidget(self.frame_14)


        self.verticalLayout_6.addWidget(self.frame_3)


        self.verticalLayout_4.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setStyleSheet(u";\n"
"border-color: rgb(0, 0, 0);")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(200, 30))
        self.pushButton.setBaseSize(QSize(0, 0))

        self.verticalLayout_10.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(200, 30))

        self.verticalLayout_10.addWidget(self.pushButton_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.progressBar = QProgressBar(self.frame_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet(u"background-color: rgb(218, 218, 218);")
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_11.addWidget(self.progressBar, 0, Qt.AlignBottom)

        self.progressBar_2 = QProgressBar(self.frame_2)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setKerning(False)
        self.progressBar_2.setFont(font1)
        self.progressBar_2.setMouseTracking(False)
        self.progressBar_2.setStyleSheet(u"background-color: rgb(218, 218, 218);")
        self.progressBar_2.setAlignment(Qt.AlignCenter)
        self.progressBar_2.setTextVisible(True)
        self.progressBar_2.setOrientation(Qt.Horizontal)
        self.progressBar_2.setInvertedAppearance(False)
        self.progressBar_2.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_11.addWidget(self.progressBar_2, 0, Qt.AlignBottom)


        self.horizontalLayout_4.addLayout(self.verticalLayout_11)


        self.horizontalLayout_5.addWidget(self.frame_2, 0, Qt.AlignBottom)


        self.verticalLayout_7.addWidget(self.frame)


        self.verticalLayout_4.addLayout(self.verticalLayout_7)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_18 = QVBoxLayout(self.tab_2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_74 = QHBoxLayout()
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.frame_4 = QFrame(self.tab_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lineEdit = QLineEdit(self.frame_4)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy2)
        self.lineEdit.setMinimumSize(QSize(200, 0))
        self.lineEdit.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_6.addWidget(self.lineEdit)

        self.pushButton_7 = QPushButton(self.frame_4)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_6.addWidget(self.pushButton_7)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_74.addWidget(self.frame_4, 0, Qt.AlignLeft)

        self.frame_30 = QFrame(self.tab_2)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.NoFrame)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_30)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.frame_30)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_8.addWidget(self.label_20, 0, Qt.AlignRight)


        self.horizontalLayout_74.addWidget(self.frame_30)


        self.verticalLayout_18.addLayout(self.horizontalLayout_74)

        self.horizontalLayout_83 = QHBoxLayout()
        self.horizontalLayout_83.setSpacing(0)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.pushButton_61 = QPushButton(self.tab_2)
        self.pushButton_61.setObjectName(u"pushButton_61")

        self.horizontalLayout_83.addWidget(self.pushButton_61)

        self.pushButton_60 = QPushButton(self.tab_2)
        self.pushButton_60.setObjectName(u"pushButton_60")
        self.pushButton_60.setMinimumSize(QSize(100, 0))
        self.pushButton_60.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_83.addWidget(self.pushButton_60)

        self.pushButton_59 = QPushButton(self.tab_2)
        self.pushButton_59.setObjectName(u"pushButton_59")
        self.pushButton_59.setMinimumSize(QSize(100, 0))
        self.pushButton_59.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_83.addWidget(self.pushButton_59)

        self.pushButton_62 = QPushButton(self.tab_2)
        self.pushButton_62.setObjectName(u"pushButton_62")
        self.pushButton_62.setMinimumSize(QSize(47, 0))
        self.pushButton_62.setMaximumSize(QSize(47, 16777215))
        self.pushButton_62.setFlat(True)

        self.horizontalLayout_83.addWidget(self.pushButton_62)


        self.verticalLayout_18.addLayout(self.horizontalLayout_83)

        self.tableWidget = QTableWidget(self.tab_2)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(16)

        self.verticalLayout_18.addWidget(self.tableWidget)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_23 = QVBoxLayout(self.tab_3)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalLayout_75 = QHBoxLayout()
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.frame_5 = QFrame(self.tab_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_5)
        self.verticalLayout_28.setSpacing(6)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lineEdit_2 = QLineEdit(self.frame_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy2.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy2)
        self.lineEdit_2.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_8.addWidget(self.lineEdit_2)

        self.pushButton_8 = QPushButton(self.frame_5)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_8.addWidget(self.pushButton_8)

        self.pushButton_22 = QPushButton(self.frame_5)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setFlat(True)

        self.horizontalLayout_8.addWidget(self.pushButton_22)


        self.verticalLayout_28.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_75.addWidget(self.frame_5, 0, Qt.AlignLeft)

        self.frame_31 = QFrame(self.tab_3)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.NoFrame)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.frame_31)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_76.addWidget(self.label_21, 0, Qt.AlignLeft)


        self.horizontalLayout_75.addWidget(self.frame_31, 0, Qt.AlignRight)


        self.verticalLayout_23.addLayout(self.horizontalLayout_75)

        self.horizontalLayout_82 = QHBoxLayout()
        self.horizontalLayout_82.setSpacing(0)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.pushButton_58 = QPushButton(self.tab_3)
        self.pushButton_58.setObjectName(u"pushButton_58")

        self.horizontalLayout_82.addWidget(self.pushButton_58)

        self.pushButton_57 = QPushButton(self.tab_3)
        self.pushButton_57.setObjectName(u"pushButton_57")
        self.pushButton_57.setMinimumSize(QSize(150, 0))
        self.pushButton_57.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_82.addWidget(self.pushButton_57)

        self.pushButton_56 = QPushButton(self.tab_3)
        self.pushButton_56.setObjectName(u"pushButton_56")
        self.pushButton_56.setMinimumSize(QSize(150, 0))
        self.pushButton_56.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_82.addWidget(self.pushButton_56)

        self.pushButton_55 = QPushButton(self.tab_3)
        self.pushButton_55.setObjectName(u"pushButton_55")
        self.pushButton_55.setMinimumSize(QSize(150, 0))
        self.pushButton_55.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_82.addWidget(self.pushButton_55)

        self.pushButton_54 = QPushButton(self.tab_3)
        self.pushButton_54.setObjectName(u"pushButton_54")
        self.pushButton_54.setMinimumSize(QSize(78, 0))
        self.pushButton_54.setMaximumSize(QSize(78, 16777215))
        self.pushButton_54.setFlat(True)

        self.horizontalLayout_82.addWidget(self.pushButton_54)


        self.verticalLayout_23.addLayout(self.horizontalLayout_82)

        self.tableWidget_2 = QTableWidget(self.tab_3)
        if (self.tableWidget_2.columnCount() < 6):
            self.tableWidget_2.setColumnCount(6)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem19)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(16)

        self.verticalLayout_23.addWidget(self.tableWidget_2)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_22 = QVBoxLayout(self.tab_4)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_77 = QHBoxLayout()
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.frame_6 = QFrame(self.tab_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_6)
        self.verticalLayout_29.setSpacing(6)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lineEdit_3 = QLineEdit(self.frame_6)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy2.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy2)
        self.lineEdit_3.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_9.addWidget(self.lineEdit_3)

        self.pushButton_9 = QPushButton(self.frame_6)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout_9.addWidget(self.pushButton_9)

        self.pushButton_26 = QPushButton(self.frame_6)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setFlat(True)

        self.horizontalLayout_9.addWidget(self.pushButton_26)


        self.verticalLayout_29.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_77.addWidget(self.frame_6, 0, Qt.AlignLeft)

        self.frame_32 = QFrame(self.tab_4)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.NoFrame)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_78 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.frame_32)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_78.addWidget(self.label_24)


        self.horizontalLayout_77.addWidget(self.frame_32, 0, Qt.AlignRight)


        self.verticalLayout_22.addLayout(self.horizontalLayout_77)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.pushButton_51 = QPushButton(self.tab_4)
        self.pushButton_51.setObjectName(u"pushButton_51")

        self.horizontalLayout_47.addWidget(self.pushButton_51)

        self.pushButton_50 = QPushButton(self.tab_4)
        self.pushButton_50.setObjectName(u"pushButton_50")
        self.pushButton_50.setMinimumSize(QSize(150, 0))
        self.pushButton_50.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_47.addWidget(self.pushButton_50)

        self.pushButton_49 = QPushButton(self.tab_4)
        self.pushButton_49.setObjectName(u"pushButton_49")
        self.pushButton_49.setMinimumSize(QSize(150, 0))
        self.pushButton_49.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_47.addWidget(self.pushButton_49)

        self.pushButton_48 = QPushButton(self.tab_4)
        self.pushButton_48.setObjectName(u"pushButton_48")
        self.pushButton_48.setMinimumSize(QSize(150, 0))
        self.pushButton_48.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_47.addWidget(self.pushButton_48)

        self.pushButton_53 = QPushButton(self.tab_4)
        self.pushButton_53.setObjectName(u"pushButton_53")
        self.pushButton_53.setMinimumSize(QSize(150, 0))
        self.pushButton_53.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_47.addWidget(self.pushButton_53)

        self.pushButton_52 = QPushButton(self.tab_4)
        self.pushButton_52.setObjectName(u"pushButton_52")
        self.pushButton_52.setMinimumSize(QSize(107, 0))
        self.pushButton_52.setMaximumSize(QSize(107, 16777215))
        self.pushButton_52.setFlat(True)

        self.horizontalLayout_47.addWidget(self.pushButton_52)


        self.verticalLayout_22.addLayout(self.horizontalLayout_47)

        self.tableWidget_3 = QTableWidget(self.tab_4)
        if (self.tableWidget_3.columnCount() < 8):
            self.tableWidget_3.setColumnCount(8)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, __qtablewidgetitem27)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.horizontalHeader().setVisible(False)
        self.tableWidget_3.horizontalHeader().setMinimumSectionSize(16)

        self.verticalLayout_22.addWidget(self.tableWidget_3)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_17 = QVBoxLayout(self.tab_5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_8 = QLabel(self.tab_5)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout.addWidget(self.label_8)

        self.pushButton_27 = QPushButton(self.tab_5)
        self.pushButton_27.setObjectName(u"pushButton_27")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_27.sizePolicy().hasHeightForWidth())
        self.pushButton_27.setSizePolicy(sizePolicy3)
        self.pushButton_27.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton_27)

        self.pushButton_4 = QPushButton(self.tab_5)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.tab_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.pushButton_3 = QPushButton(self.tab_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_3)


        self.verticalLayout_17.addLayout(self.horizontalLayout)

        self.tabWidget_2 = QTabWidget(self.tab_5)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.verticalLayout_21 = QVBoxLayout(self.tab_7)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_7 = QFrame(self.tab_7)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_7)
        self.verticalLayout_31.setSpacing(6)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lineEdit_4 = QLineEdit(self.frame_7)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_10.addWidget(self.lineEdit_4)

        self.pushButton_10 = QPushButton(self.frame_7)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout_10.addWidget(self.pushButton_10)


        self.verticalLayout_31.addLayout(self.horizontalLayout_10)


        self.verticalLayout_25.addWidget(self.frame_7, 0, Qt.AlignLeft)


        self.verticalLayout_21.addLayout(self.verticalLayout_25)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.pushButton_29 = QPushButton(self.tab_7)
        self.pushButton_29.setObjectName(u"pushButton_29")

        self.horizontalLayout_35.addWidget(self.pushButton_29)

        self.pushButton_28 = QPushButton(self.tab_7)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setMinimumSize(QSize(100, 0))
        self.pushButton_28.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_35.addWidget(self.pushButton_28)

        self.pushButton_24 = QPushButton(self.tab_7)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setMinimumSize(QSize(150, 0))
        self.pushButton_24.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_35.addWidget(self.pushButton_24)

        self.pushButton_32 = QPushButton(self.tab_7)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setMinimumSize(QSize(150, 0))
        self.pushButton_32.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_35.addWidget(self.pushButton_32)

        self.pushButton_31 = QPushButton(self.tab_7)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setMinimumSize(QSize(150, 0))
        self.pushButton_31.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_35.addWidget(self.pushButton_31)

        self.pushButton_30 = QPushButton(self.tab_7)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setMinimumSize(QSize(150, 0))
        self.pushButton_30.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_35.addWidget(self.pushButton_30)

        self.pushButton_33 = QPushButton(self.tab_7)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setMinimumSize(QSize(102, 0))
        self.pushButton_33.setMaximumSize(QSize(102, 16777215))
        self.pushButton_33.setFlat(True)

        self.horizontalLayout_35.addWidget(self.pushButton_33)


        self.verticalLayout_21.addLayout(self.horizontalLayout_35)

        self.tableWidget_4 = QTableWidget(self.tab_7)
        if (self.tableWidget_4.columnCount() < 9):
            self.tableWidget_4.setColumnCount(9)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(6, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(7, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(8, __qtablewidgetitem36)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.horizontalHeader().setVisible(False)
        self.tableWidget_4.horizontalHeader().setMinimumSectionSize(16)

        self.verticalLayout_21.addWidget(self.tableWidget_4)

        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.verticalLayout_20 = QVBoxLayout(self.tab_8)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.frame_8 = QFrame(self.tab_8)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_8)
        self.verticalLayout_32.setSpacing(6)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lineEdit_5 = QLineEdit(self.frame_8)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy2.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy2)
        self.lineEdit_5.setMinimumSize(QSize(200, 0))
        self.lineEdit_5.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_11.addWidget(self.lineEdit_5)

        self.pushButton_11 = QPushButton(self.frame_8)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_11.addWidget(self.pushButton_11)


        self.verticalLayout_32.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_48.addWidget(self.frame_8, 0, Qt.AlignLeft)

        self.frame_29 = QFrame(self.tab_8)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.pushButton_25 = QPushButton(self.frame_29)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_50.addWidget(self.pushButton_25, 0, Qt.AlignRight)


        self.horizontalLayout_48.addWidget(self.frame_29, 0, Qt.AlignRight)


        self.verticalLayout_20.addLayout(self.horizontalLayout_48)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.pushButton_37 = QPushButton(self.tab_8)
        self.pushButton_37.setObjectName(u"pushButton_37")

        self.horizontalLayout_36.addWidget(self.pushButton_37)

        self.pushButton_36 = QPushButton(self.tab_8)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setMinimumSize(QSize(100, 0))
        self.pushButton_36.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_36.addWidget(self.pushButton_36)

        self.pushButton_35 = QPushButton(self.tab_8)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setMinimumSize(QSize(150, 0))
        self.pushButton_35.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_36.addWidget(self.pushButton_35)

        self.pushButton_34 = QPushButton(self.tab_8)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setMinimumSize(QSize(150, 0))
        self.pushButton_34.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_36.addWidget(self.pushButton_34)

        self.pushButton_40 = QPushButton(self.tab_8)
        self.pushButton_40.setObjectName(u"pushButton_40")
        self.pushButton_40.setMinimumSize(QSize(150, 0))
        self.pushButton_40.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_36.addWidget(self.pushButton_40)

        self.pushButton_39 = QPushButton(self.tab_8)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setMinimumSize(QSize(150, 0))
        self.pushButton_39.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_36.addWidget(self.pushButton_39)

        self.pushButton_38 = QPushButton(self.tab_8)
        self.pushButton_38.setObjectName(u"pushButton_38")
        self.pushButton_38.setMinimumSize(QSize(102, 0))
        self.pushButton_38.setMaximumSize(QSize(102, 16777215))
        self.pushButton_38.setFlat(True)

        self.horizontalLayout_36.addWidget(self.pushButton_38)


        self.verticalLayout_20.addLayout(self.horizontalLayout_36)

        self.tableWidget_5 = QTableWidget(self.tab_8)
        if (self.tableWidget_5.columnCount() < 9):
            self.tableWidget_5.setColumnCount(9)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(5, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(6, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(7, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(8, __qtablewidgetitem45)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        self.tableWidget_5.horizontalHeader().setVisible(False)
        self.tableWidget_5.horizontalHeader().setMinimumSectionSize(16)

        self.verticalLayout_20.addWidget(self.tableWidget_5)

        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.verticalLayout_19 = QVBoxLayout(self.tab_9)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_9 = QFrame(self.tab_9)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_9)
        self.verticalLayout_30.setSpacing(6)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lineEdit_6 = QLineEdit(self.frame_9)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_12.addWidget(self.lineEdit_6)

        self.pushButton_12 = QPushButton(self.frame_9)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.horizontalLayout_12.addWidget(self.pushButton_12)


        self.verticalLayout_30.addLayout(self.horizontalLayout_12)


        self.verticalLayout_27.addWidget(self.frame_9, 0, Qt.AlignLeft)


        self.verticalLayout_19.addLayout(self.verticalLayout_27)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.pushButton_44 = QPushButton(self.tab_9)
        self.pushButton_44.setObjectName(u"pushButton_44")

        self.horizontalLayout_46.addWidget(self.pushButton_44)

        self.pushButton_43 = QPushButton(self.tab_9)
        self.pushButton_43.setObjectName(u"pushButton_43")
        self.pushButton_43.setMinimumSize(QSize(100, 0))
        self.pushButton_43.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_46.addWidget(self.pushButton_43)

        self.pushButton_42 = QPushButton(self.tab_9)
        self.pushButton_42.setObjectName(u"pushButton_42")
        self.pushButton_42.setMinimumSize(QSize(150, 0))
        self.pushButton_42.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_46.addWidget(self.pushButton_42)

        self.pushButton_41 = QPushButton(self.tab_9)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setMinimumSize(QSize(150, 0))
        self.pushButton_41.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_46.addWidget(self.pushButton_41)

        self.pushButton_47 = QPushButton(self.tab_9)
        self.pushButton_47.setObjectName(u"pushButton_47")
        self.pushButton_47.setMinimumSize(QSize(150, 0))
        self.pushButton_47.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_46.addWidget(self.pushButton_47)

        self.pushButton_46 = QPushButton(self.tab_9)
        self.pushButton_46.setObjectName(u"pushButton_46")
        self.pushButton_46.setMinimumSize(QSize(150, 0))
        self.pushButton_46.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_46.addWidget(self.pushButton_46)

        self.pushButton_45 = QPushButton(self.tab_9)
        self.pushButton_45.setObjectName(u"pushButton_45")
        self.pushButton_45.setMinimumSize(QSize(32, 0))
        self.pushButton_45.setMaximumSize(QSize(32, 16777215))
        self.pushButton_45.setFlat(True)

        self.horizontalLayout_46.addWidget(self.pushButton_45)


        self.verticalLayout_19.addLayout(self.horizontalLayout_46)

        self.tableWidget_6 = QTableWidget(self.tab_9)
        if (self.tableWidget_6.columnCount() < 7):
            self.tableWidget_6.setColumnCount(7)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(3, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(4, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(5, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(6, __qtablewidgetitem52)
        self.tableWidget_6.setObjectName(u"tableWidget_6")
        self.tableWidget_6.horizontalHeader().setVisible(False)
        self.tableWidget_6.horizontalHeader().setMinimumSectionSize(16)

        self.verticalLayout_19.addWidget(self.tableWidget_6)

        self.tabWidget_2.addTab(self.tab_9, "")

        self.verticalLayout_17.addWidget(self.tabWidget_2)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout = QVBoxLayout(self.tab_6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget_3 = QTabWidget(self.tab_6)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.verticalLayout_75 = QVBoxLayout(self.tab_10)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_74 = QVBoxLayout()
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.verticalLayout_77 = QVBoxLayout()
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.groupBox_13 = QGroupBox(self.tab_10)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.verticalLayout_81 = QVBoxLayout(self.groupBox_13)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.frame_20 = QFrame(self.groupBox_13)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_90 = QVBoxLayout(self.frame_20)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.verticalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_89 = QVBoxLayout()
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.label_33 = QLabel(self.frame_20)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_62.addWidget(self.label_33)

        self.lineEdit_17 = QLineEdit(self.frame_20)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        sizePolicy3.setHeightForWidth(self.lineEdit_17.sizePolicy().hasHeightForWidth())
        self.lineEdit_17.setSizePolicy(sizePolicy3)
        self.lineEdit_17.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_62.addWidget(self.lineEdit_17)


        self.verticalLayout_89.addLayout(self.horizontalLayout_62)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.label_31 = QLabel(self.frame_20)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_57.addWidget(self.label_31)

        self.lineEdit_15 = QLineEdit(self.frame_20)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        sizePolicy3.setHeightForWidth(self.lineEdit_15.sizePolicy().hasHeightForWidth())
        self.lineEdit_15.setSizePolicy(sizePolicy3)
        self.lineEdit_15.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_57.addWidget(self.lineEdit_15)


        self.verticalLayout_89.addLayout(self.horizontalLayout_57)

        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_32 = QLabel(self.frame_20)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_61.addWidget(self.label_32)

        self.lineEdit_16 = QLineEdit(self.frame_20)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        sizePolicy3.setHeightForWidth(self.lineEdit_16.sizePolicy().hasHeightForWidth())
        self.lineEdit_16.setSizePolicy(sizePolicy3)
        self.lineEdit_16.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_61.addWidget(self.lineEdit_16)


        self.verticalLayout_89.addLayout(self.horizontalLayout_61)

        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.label_34 = QLabel(self.frame_20)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_63.addWidget(self.label_34)

        self.lineEdit_18 = QLineEdit(self.frame_20)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        sizePolicy3.setHeightForWidth(self.lineEdit_18.sizePolicy().hasHeightForWidth())
        self.lineEdit_18.setSizePolicy(sizePolicy3)
        self.lineEdit_18.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_63.addWidget(self.lineEdit_18)


        self.verticalLayout_89.addLayout(self.horizontalLayout_63)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.label_35 = QLabel(self.frame_20)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_56.addWidget(self.label_35)

        self.lineEdit_13 = QLineEdit(self.frame_20)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        sizePolicy3.setHeightForWidth(self.lineEdit_13.sizePolicy().hasHeightForWidth())
        self.lineEdit_13.setSizePolicy(sizePolicy3)
        self.lineEdit_13.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_56.addWidget(self.lineEdit_13)


        self.verticalLayout_89.addLayout(self.horizontalLayout_56)

        self.verticalLayout_80 = QVBoxLayout()
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.label_30 = QLabel(self.frame_20)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_55.addWidget(self.label_30)

        self.lineEdit_14 = QLineEdit(self.frame_20)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        sizePolicy3.setHeightForWidth(self.lineEdit_14.sizePolicy().hasHeightForWidth())
        self.lineEdit_14.setSizePolicy(sizePolicy3)
        self.lineEdit_14.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_55.addWidget(self.lineEdit_14)


        self.verticalLayout_80.addLayout(self.horizontalLayout_55)


        self.verticalLayout_89.addLayout(self.verticalLayout_80)


        self.verticalLayout_90.addLayout(self.verticalLayout_89)


        self.verticalLayout_81.addWidget(self.frame_20, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_77.addWidget(self.groupBox_13)


        self.horizontalLayout_54.addLayout(self.verticalLayout_77)

        self.verticalLayout_76 = QVBoxLayout()
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.groupBox_16 = QGroupBox(self.tab_10)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.verticalLayout_86 = QVBoxLayout(self.groupBox_16)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.frame_21 = QFrame(self.groupBox_16)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_91 = QVBoxLayout(self.frame_21)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_83 = QVBoxLayout()
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.checkBox_4 = QCheckBox(self.frame_21)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_59.addWidget(self.checkBox_4)


        self.verticalLayout_83.addLayout(self.horizontalLayout_59)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.checkBox_5 = QCheckBox(self.frame_21)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_60.addWidget(self.checkBox_5)


        self.verticalLayout_83.addLayout(self.horizontalLayout_60)

        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.checkBox_6 = QCheckBox(self.frame_21)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_58.addWidget(self.checkBox_6)


        self.verticalLayout_83.addLayout(self.horizontalLayout_58)

        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.checkBox_7 = QCheckBox(self.frame_21)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_64.addWidget(self.checkBox_7)


        self.verticalLayout_83.addLayout(self.horizontalLayout_64)

        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.checkBox_8 = QCheckBox(self.frame_21)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_65.addWidget(self.checkBox_8)


        self.verticalLayout_83.addLayout(self.horizontalLayout_65)


        self.verticalLayout_91.addLayout(self.verticalLayout_83)


        self.verticalLayout_86.addWidget(self.frame_21, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_76.addWidget(self.groupBox_16)


        self.horizontalLayout_54.addLayout(self.verticalLayout_76)


        self.verticalLayout_74.addLayout(self.horizontalLayout_54)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.verticalLayout_79 = QVBoxLayout()
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.horizontalLayout_81 = QHBoxLayout()
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.groupBox_21 = QGroupBox(self.tab_10)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.horizontalLayout_80 = QHBoxLayout(self.groupBox_21)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.frame_23 = QFrame(self.groupBox_21)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_57 = QVBoxLayout()
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.frame_16 = QFrame(self.frame_23)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.frame_16)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(100, 0))
        self.label_22.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_43.addWidget(self.label_22)

        self.lineEdit_12 = QLineEdit(self.frame_16)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        sizePolicy3.setHeightForWidth(self.lineEdit_12.sizePolicy().hasHeightForWidth())
        self.lineEdit_12.setSizePolicy(sizePolicy3)
        self.lineEdit_12.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_43.addWidget(self.lineEdit_12)


        self.horizontalLayout_38.addWidget(self.frame_16, 0, Qt.AlignLeft)


        self.verticalLayout_57.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.frame_15 = QFrame(self.frame_23)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.frame_15)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(100, 0))
        self.label_23.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_42.addWidget(self.label_23)

        self.lineEdit_11 = QLineEdit(self.frame_15)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        sizePolicy3.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy3)
        self.lineEdit_11.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_42.addWidget(self.lineEdit_11)


        self.horizontalLayout_41.addWidget(self.frame_15, 0, Qt.AlignLeft)


        self.verticalLayout_57.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.frame_18 = QFrame(self.frame_23)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.checkBox_3 = QCheckBox(self.frame_18)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_44.addWidget(self.checkBox_3)


        self.horizontalLayout_40.addWidget(self.frame_18)


        self.verticalLayout_57.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.frame_17 = QFrame(self.frame_23)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.checkBox_2 = QCheckBox(self.frame_17)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_45.addWidget(self.checkBox_2)


        self.horizontalLayout_39.addWidget(self.frame_17, 0, Qt.AlignLeft)


        self.verticalLayout_57.addLayout(self.horizontalLayout_39)


        self.horizontalLayout_79.addLayout(self.verticalLayout_57)


        self.horizontalLayout_80.addWidget(self.frame_23, 0, Qt.AlignLeft)


        self.horizontalLayout_81.addWidget(self.groupBox_21)

        self.groupBox_8 = QGroupBox(self.tab_10)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_55 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_54 = QVBoxLayout()
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.horizontalLayout_84 = QHBoxLayout()
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.frame_33 = QFrame(self.groupBox_8)
        self.frame_33.setObjectName(u"frame_33")
        sizePolicy1.setHeightForWidth(self.frame_33.sizePolicy().hasHeightForWidth())
        self.frame_33.setSizePolicy(sizePolicy1)
        self.frame_33.setFrameShape(QFrame.NoFrame)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.label_39 = QLabel(self.frame_33)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(150, 0))
        self.label_39.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_88.addWidget(self.label_39)

        self.lineEdit_23 = QLineEdit(self.frame_33)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_88.addWidget(self.lineEdit_23)


        self.horizontalLayout_84.addWidget(self.frame_33, 0, Qt.AlignLeft)


        self.verticalLayout_54.addLayout(self.horizontalLayout_84)

        self.horizontalLayout_85 = QHBoxLayout()
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.frame_34 = QFrame(self.groupBox_8)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.NoFrame)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_89 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.label_40 = QLabel(self.frame_34)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(150, 0))
        self.label_40.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_89.addWidget(self.label_40)

        self.lineEdit_24 = QLineEdit(self.frame_34)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_89.addWidget(self.lineEdit_24)


        self.horizontalLayout_85.addWidget(self.frame_34, 0, Qt.AlignLeft)


        self.verticalLayout_54.addLayout(self.horizontalLayout_85)

        self.horizontalLayout_86 = QHBoxLayout()
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.frame_35 = QFrame(self.groupBox_8)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.NoFrame)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_90 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.label_45 = QLabel(self.frame_35)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setEnabled(True)
        self.label_45.setMinimumSize(QSize(150, 0))
        self.label_45.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_90.addWidget(self.label_45)

        self.lineEdit_25 = QLineEdit(self.frame_35)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setEnabled(False)
        self.lineEdit_25.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_90.addWidget(self.lineEdit_25)


        self.horizontalLayout_86.addWidget(self.frame_35, 0, Qt.AlignLeft)


        self.verticalLayout_54.addLayout(self.horizontalLayout_86)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.frame_36 = QFrame(self.groupBox_8)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.NoFrame)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_87 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.label_46 = QLabel(self.frame_36)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(150, 0))
        self.label_46.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_87.addWidget(self.label_46)

        self.lineEdit_26 = QLineEdit(self.frame_36)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setEnabled(False)
        self.lineEdit_26.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_87.addWidget(self.lineEdit_26)


        self.horizontalLayout_37.addWidget(self.frame_36, 0, Qt.AlignLeft)


        self.verticalLayout_54.addLayout(self.horizontalLayout_37)


        self.verticalLayout_55.addLayout(self.verticalLayout_54)


        self.horizontalLayout_81.addWidget(self.groupBox_8)


        self.verticalLayout_79.addLayout(self.horizontalLayout_81)

        self.groupBox_14 = QGroupBox(self.tab_10)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.verticalLayout_85 = QVBoxLayout(self.groupBox_14)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_82 = QVBoxLayout()
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.frame_22 = QFrame(self.groupBox_14)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_92 = QVBoxLayout(self.frame_22)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.pushButton_6 = QPushButton(self.frame_22)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(160, 30))

        self.horizontalLayout_72.addWidget(self.pushButton_6)

        self.pushButton_13 = QPushButton(self.frame_22)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(160, 30))
        self.pushButton_13.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_72.addWidget(self.pushButton_13)


        self.verticalLayout_92.addLayout(self.horizontalLayout_72)


        self.verticalLayout_82.addWidget(self.frame_22, 0, Qt.AlignBottom)

        self.progressBar_3 = QProgressBar(self.groupBox_14)
        self.progressBar_3.setObjectName(u"progressBar_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.progressBar_3.sizePolicy().hasHeightForWidth())
        self.progressBar_3.setSizePolicy(sizePolicy4)
        self.progressBar_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_82.addWidget(self.progressBar_3)


        self.verticalLayout_85.addLayout(self.verticalLayout_82)


        self.verticalLayout_79.addWidget(self.groupBox_14)


        self.horizontalLayout_53.addLayout(self.verticalLayout_79)

        self.verticalLayout_78 = QVBoxLayout()
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.groupBox_15 = QGroupBox(self.tab_10)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setEnabled(False)
        self.verticalLayout_87 = QVBoxLayout(self.groupBox_15)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.frame_19 = QFrame(self.groupBox_15)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.frame_19)
        self.verticalLayout_88.setSpacing(6)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_84 = QVBoxLayout()
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.label_41 = QLabel(self.frame_19)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(0, 0))
        self.label_41.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_67.addWidget(self.label_41)

        self.lineEdit_19 = QLineEdit(self.frame_19)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        sizePolicy3.setHeightForWidth(self.lineEdit_19.sizePolicy().hasHeightForWidth())
        self.lineEdit_19.setSizePolicy(sizePolicy3)
        self.lineEdit_19.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_67.addWidget(self.lineEdit_19)


        self.verticalLayout_84.addLayout(self.horizontalLayout_67)

        self.horizontalLayout_71 = QHBoxLayout()
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.label_42 = QLabel(self.frame_19)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(100, 0))
        self.label_42.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_71.addWidget(self.label_42)

        self.lineEdit_20 = QLineEdit(self.frame_19)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        sizePolicy3.setHeightForWidth(self.lineEdit_20.sizePolicy().hasHeightForWidth())
        self.lineEdit_20.setSizePolicy(sizePolicy3)
        self.lineEdit_20.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_71.addWidget(self.lineEdit_20)


        self.verticalLayout_84.addLayout(self.horizontalLayout_71)

        self.horizontalLayout_70 = QHBoxLayout()
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.label_43 = QLabel(self.frame_19)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(100, 0))
        self.label_43.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_70.addWidget(self.label_43)

        self.lineEdit_21 = QLineEdit(self.frame_19)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        sizePolicy3.setHeightForWidth(self.lineEdit_21.sizePolicy().hasHeightForWidth())
        self.lineEdit_21.setSizePolicy(sizePolicy3)
        self.lineEdit_21.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_70.addWidget(self.lineEdit_21)


        self.verticalLayout_84.addLayout(self.horizontalLayout_70)

        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.label_44 = QLabel(self.frame_19)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(100, 0))
        self.label_44.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_68.addWidget(self.label_44)

        self.lineEdit_22 = QLineEdit(self.frame_19)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        sizePolicy3.setHeightForWidth(self.lineEdit_22.sizePolicy().hasHeightForWidth())
        self.lineEdit_22.setSizePolicy(sizePolicy3)
        self.lineEdit_22.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_68.addWidget(self.lineEdit_22)


        self.verticalLayout_84.addLayout(self.horizontalLayout_68)

        self.horizontalLayout_69 = QHBoxLayout()
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.checkBox_10 = QCheckBox(self.frame_19)
        self.checkBox_10.setObjectName(u"checkBox_10")

        self.horizontalLayout_69.addWidget(self.checkBox_10)

        self.checkBox_9 = QCheckBox(self.frame_19)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.horizontalLayout_69.addWidget(self.checkBox_9)

        self.checkBox_11 = QCheckBox(self.frame_19)
        self.checkBox_11.setObjectName(u"checkBox_11")

        self.horizontalLayout_69.addWidget(self.checkBox_11)


        self.verticalLayout_84.addLayout(self.horizontalLayout_69)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")

        self.verticalLayout_84.addLayout(self.horizontalLayout_66)


        self.verticalLayout_88.addLayout(self.verticalLayout_84)


        self.verticalLayout_87.addWidget(self.frame_19, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_78.addWidget(self.groupBox_15)


        self.horizontalLayout_53.addLayout(self.verticalLayout_78)


        self.verticalLayout_74.addLayout(self.horizontalLayout_53)


        self.verticalLayout_75.addLayout(self.verticalLayout_74)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_27 = QLabel(self.tab_10)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_33.addWidget(self.label_27)

        self.pushButton_21 = QPushButton(self.tab_10)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_33.addWidget(self.pushButton_21)


        self.verticalLayout_75.addLayout(self.horizontalLayout_33)

        self.tabWidget_3.addTab(self.tab_10, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.verticalLayout_40 = QVBoxLayout(self.tab_12)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.groupBox_4 = QGroupBox(self.tab_12)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_46 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.frame_24 = QFrame(self.groupBox_4)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_96 = QVBoxLayout(self.frame_24)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.verticalLayout_45 = QVBoxLayout()
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.pushButton_18 = QPushButton(self.frame_24)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(210, 30))
        self.pushButton_18.setMaximumSize(QSize(210, 16777215))

        self.horizontalLayout_21.addWidget(self.pushButton_18)

        self.label_13 = QLabel(self.frame_24)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_21.addWidget(self.label_13)


        self.verticalLayout_45.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.pushButton_17 = QPushButton(self.frame_24)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(210, 30))
        self.pushButton_17.setMaximumSize(QSize(210, 16777215))

        self.horizontalLayout_20.addWidget(self.pushButton_17)

        self.label_12 = QLabel(self.frame_24)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_20.addWidget(self.label_12)


        self.verticalLayout_45.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.pushButton_16 = QPushButton(self.frame_24)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(210, 30))
        self.pushButton_16.setMaximumSize(QSize(210, 16777215))

        self.horizontalLayout_19.addWidget(self.pushButton_16)

        self.label_11 = QLabel(self.frame_24)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_19.addWidget(self.label_11)


        self.verticalLayout_45.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.pushButton_15 = QPushButton(self.frame_24)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(210, 30))
        self.pushButton_15.setMaximumSize(QSize(210, 16777215))

        self.horizontalLayout_18.addWidget(self.pushButton_15)

        self.label_10 = QLabel(self.frame_24)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_18.addWidget(self.label_10)


        self.verticalLayout_45.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.pushButton_14 = QPushButton(self.frame_24)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(210, 30))
        self.pushButton_14.setMaximumSize(QSize(210, 16777215))

        self.horizontalLayout_17.addWidget(self.pushButton_14)

        self.label_9 = QLabel(self.frame_24)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_17.addWidget(self.label_9)


        self.verticalLayout_45.addLayout(self.horizontalLayout_17)


        self.verticalLayout_96.addLayout(self.verticalLayout_45)


        self.verticalLayout_46.addWidget(self.frame_24, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_42.addWidget(self.groupBox_4)


        self.horizontalLayout_15.addLayout(self.verticalLayout_42)

        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.groupBox_7 = QGroupBox(self.tab_12)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_52 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.frame_26 = QFrame(self.groupBox_7)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_99 = QVBoxLayout(self.frame_26)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.verticalLayout_99.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_51 = QVBoxLayout()
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.checkBox = QCheckBox(self.frame_26)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_27.addWidget(self.checkBox)


        self.verticalLayout_51.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_16 = QLabel(self.frame_26)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_26.addWidget(self.label_16)

        self.lineEdit_7 = QLineEdit(self.frame_26)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy3.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy3)
        self.lineEdit_7.setMaximumSize(QSize(200, 20))

        self.horizontalLayout_26.addWidget(self.lineEdit_7)


        self.verticalLayout_51.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_17 = QLabel(self.frame_26)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_25.addWidget(self.label_17)

        self.lineEdit_8 = QLineEdit(self.frame_26)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        sizePolicy3.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy3)
        self.lineEdit_8.setMaximumSize(QSize(200, 20))

        self.horizontalLayout_25.addWidget(self.lineEdit_8)


        self.verticalLayout_51.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_18 = QLabel(self.frame_26)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_24.addWidget(self.label_18)

        self.lineEdit_9 = QLineEdit(self.frame_26)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        sizePolicy3.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy3)
        self.lineEdit_9.setMaximumSize(QSize(200, 20))

        self.horizontalLayout_24.addWidget(self.lineEdit_9)


        self.verticalLayout_51.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_19 = QLabel(self.frame_26)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_23.addWidget(self.label_19)

        self.lineEdit_10 = QLineEdit(self.frame_26)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        sizePolicy3.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy3)
        self.lineEdit_10.setMaximumSize(QSize(200, 20))

        self.horizontalLayout_23.addWidget(self.lineEdit_10)


        self.verticalLayout_51.addLayout(self.horizontalLayout_23)


        self.verticalLayout_99.addLayout(self.verticalLayout_51)


        self.verticalLayout_52.addWidget(self.frame_26, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_41.addWidget(self.groupBox_7)


        self.horizontalLayout_15.addLayout(self.verticalLayout_41)


        self.verticalLayout_39.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.verticalLayout_44 = QVBoxLayout()
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.groupBox_5 = QGroupBox(self.tab_12)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setEnabled(True)
        self.verticalLayout_50 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.frame_25 = QFrame(self.groupBox_5)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97 = QVBoxLayout(self.frame_25)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.verticalLayout_49 = QVBoxLayout()
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.checkBox_12 = QCheckBox(self.frame_25)
        self.checkBox_12.setObjectName(u"checkBox_12")
        self.checkBox_12.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_32.addWidget(self.checkBox_12)


        self.verticalLayout_49.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.checkBox_13 = QCheckBox(self.frame_25)
        self.checkBox_13.setObjectName(u"checkBox_13")
        self.checkBox_13.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_31.addWidget(self.checkBox_13)


        self.verticalLayout_49.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")

        self.verticalLayout_49.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")

        self.verticalLayout_49.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")

        self.verticalLayout_49.addLayout(self.horizontalLayout_28)


        self.verticalLayout_97.addLayout(self.verticalLayout_49)


        self.verticalLayout_50.addWidget(self.frame_25, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_44.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.tab_12)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setEnabled(False)
        self.verticalLayout_48 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.frame_27 = QFrame(self.groupBox_6)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(400, 0))
        self.frame_27.setFrameShape(QFrame.NoFrame)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_98 = QVBoxLayout(self.frame_27)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.verticalLayout_98.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_47 = QVBoxLayout()
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_14 = QLabel(self.frame_27)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_22.addWidget(self.label_14, 0, Qt.AlignHCenter)

        self.radioButton_2 = QRadioButton(self.frame_27)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_22.addWidget(self.radioButton_2, 0, Qt.AlignHCenter)

        self.radioButton = QRadioButton(self.frame_27)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_22.addWidget(self.radioButton, 0, Qt.AlignHCenter)


        self.verticalLayout_47.addLayout(self.horizontalLayout_22)


        self.verticalLayout_98.addLayout(self.verticalLayout_47)


        self.verticalLayout_48.addWidget(self.frame_27, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_44.addWidget(self.groupBox_6)


        self.horizontalLayout_16.addLayout(self.verticalLayout_44)

        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.groupBox_10 = QGroupBox(self.tab_12)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setEnabled(True)
        self.verticalLayout_70 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.frame_28 = QFrame(self.groupBox_10)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setEnabled(True)
        self.frame_28.setFrameShape(QFrame.NoFrame)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_100 = QVBoxLayout(self.frame_28)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.verticalLayout_66 = QVBoxLayout()
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.label_26 = QLabel(self.frame_28)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_51.addWidget(self.label_26)

        self.comboBox = QComboBox(self.frame_28)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_51.addWidget(self.comboBox)


        self.verticalLayout_66.addLayout(self.horizontalLayout_51)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_29 = QLabel(self.frame_28)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_52.addWidget(self.label_29)

        self.spinBox = QSpinBox(self.frame_28)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(1024)
        self.spinBox.setMaximum(8196)
        self.spinBox.setSingleStep(128)

        self.horizontalLayout_52.addWidget(self.spinBox)


        self.verticalLayout_66.addLayout(self.horizontalLayout_52)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_25 = QLabel(self.frame_28)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_49.addWidget(self.label_25)

        self.checkBox_14 = QCheckBox(self.frame_28)
        self.checkBox_14.setObjectName(u"checkBox_14")
        self.checkBox_14.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_49.addWidget(self.checkBox_14)


        self.verticalLayout_66.addLayout(self.horizontalLayout_49)


        self.verticalLayout_100.addLayout(self.verticalLayout_66)


        self.verticalLayout_70.addWidget(self.frame_28, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_43.addWidget(self.groupBox_10)


        self.horizontalLayout_16.addLayout(self.verticalLayout_43)


        self.verticalLayout_39.addLayout(self.horizontalLayout_16)


        self.verticalLayout_40.addLayout(self.verticalLayout_39)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_28 = QLabel(self.tab_12)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_34.addWidget(self.label_28)

        self.pushButton_23 = QPushButton(self.tab_12)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_34.addWidget(self.pushButton_23)


        self.verticalLayout_40.addLayout(self.horizontalLayout_34)

        self.tabWidget_3.addTab(self.tab_12, "")

        self.verticalLayout.addWidget(self.tabWidget_3)

        self.tabWidget.addTab(self.tab_6, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.verticalLayout_9 = QVBoxLayout(self.tab_11)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.tabWidget_4 = QTabWidget(self.tab_11)
        self.tabWidget_4.setObjectName(u"tabWidget_4")
        self.tab_15 = QWidget()
        self.tab_15.setObjectName(u"tab_15")
        self.verticalLayout_24 = QVBoxLayout(self.tab_15)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.textBrowser = QTextBrowser(self.tab_15)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy5)

        self.verticalLayout_24.addWidget(self.textBrowser)

        self.tabWidget_4.addTab(self.tab_15, "")
        self.tab_16 = QWidget()
        self.tab_16.setObjectName(u"tab_16")
        self.verticalLayout_53 = QVBoxLayout(self.tab_16)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.textBrowser_3 = QTextBrowser(self.tab_16)
        self.textBrowser_3.setObjectName(u"textBrowser_3")

        self.verticalLayout_53.addWidget(self.textBrowser_3)

        self.tabWidget_4.addTab(self.tab_16, "")
        self.tab_17 = QWidget()
        self.tab_17.setObjectName(u"tab_17")
        self.verticalLayout_26 = QVBoxLayout(self.tab_17)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.textBrowser_2 = QTextBrowser(self.tab_17)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        sizePolicy5.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy5)

        self.verticalLayout_26.addWidget(self.textBrowser_2)

        self.tabWidget_4.addTab(self.tab_17, "")

        self.verticalLayout_9.addWidget(self.tabWidget_4)

        self.tabWidget.addTab(self.tab_11, "")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.verticalLayout_59 = QVBoxLayout(self.tab_14)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.textEdit = QTextEdit(self.tab_14)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.verticalLayout_59.addWidget(self.textEdit)

        self.tabWidget.addTab(self.tab_14, "")

        self.verticalLayout_12.addWidget(self.tabWidget, 0, Qt.AlignTop)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1168, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"E-Trust CRL Parsing v1.0.0-beta.14", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f TSL E-Trust", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u0441\u0438\u044f \u0431\u0430\u0437\u044b:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0432\u044b\u043f\u0443\u0441\u043a\u0430 \u0431\u0430\u0437\u044b:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435\u0433\u043e \u0423\u0426:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435\u0433\u043e CRL:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0426 \u0434\u043b\u044f \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0438 \u043e\u0442\u043c\u0435\u0447\u0435\u043d\u043e:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"CRL \u0431\u0443\u0434\u0435\u0442 \u0437\u0430\u0433\u0440\u0443\u0436\u0435\u043d\u043e:", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f:", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0435\u0435 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435: ", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u0435 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435:", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u0432 \u0440\u0430\u0431\u043e\u0442\u0435:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0439\u043c\u0435\u0440:", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u043b\u043e\u0432\u043d\u043e\u0439 \u0423\u0434\u043e\u0441\u0442\u043e\u0432\u0435\u0440\u044f\u044e\u0449\u0438\u0439 \u0446\u0435\u043d\u0442\u0440", None))
        ___qtablewidgetitem = self.tableWidget_7.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u043b\u044e\u0447\u0430", None));
        ___qtablewidgetitem1 = self.tableWidget_7.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0435 \u0441\u043a\u0430\u0447\u0438\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem2 = self.tableWidget_7.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0435 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435", None));
        ___qtablewidgetitem3 = self.tableWidget_7.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u0435 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435", None));
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u043e\u0439 \u0423\u0426: ", None))
        ___qtablewidgetitem4 = self.tableWidget_8.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u043b\u044e\u0447\u0430", None));
        ___qtablewidgetitem5 = self.tableWidget_8.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0435 \u0441\u043a\u0430\u0447\u0438\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem6 = self.tableWidget_8.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0435 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438", None));
        ___qtablewidgetitem7 = self.tableWidget_8.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u0435 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435", None));
        self.label_7.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0438\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.label_20.setText("")
        self.pushButton_61.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.pushButton_60.setText(QCoreApplication.translate("MainWindow", u"\u0418\u041d\u041d", None))
        self.pushButton_59.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0413\u0420\u041d", None))
        self.pushButton_62.setText("")
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u0418\u041d\u041d", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0413\u0420\u041d", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0423\u0426", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.pushButton_22.setText("")
        self.label_21.setText("")
        self.pushButton_58.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.pushButton_57.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u043b\u044e\u0447\u0430", None))
        self.pushButton_56.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0435\u0447\u0430\u0442\u043e\u043a", None))
        self.pushButton_55.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u0438\u0439\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440", None))
        self.pushButton_54.setText("")
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem12 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u043b\u044e\u0447\u0430", None));
        ___qtablewidgetitem13 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0435\u0447\u0430\u0442\u043e\u043a", None));
        ___qtablewidgetitem14 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u0438\u0439\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0441\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0432", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.pushButton_26.setText("")
        self.label_24.setText("")
        self.pushButton_51.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.pushButton_50.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u043b\u044e\u0447\u0430", None))
        self.pushButton_49.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0435\u0447\u0430\u0442\u043e\u043a", None))
        self.pushButton_48.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u0438\u0439\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440", None))
        self.pushButton_53.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441 \u0432 \u0438\u043d\u0442\u0435\u0440\u043d\u0435\u0442\u0435", None))
        self.pushButton_52.setText("")
        ___qtablewidgetitem15 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem16 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u043b\u044e\u0447\u0430", None));
        ___qtablewidgetitem17 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0435\u0447\u0430\u0442\u043e\u043a", None));
        ___qtablewidgetitem18 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u0438\u0439\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440", None));
        ___qtablewidgetitem19 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441 \u0432 \u0438\u043d\u0442\u0435\u0440\u043d\u0435\u0442\u0435", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a CRL", None))
        self.label_8.setText("")
        self.pushButton_27.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0430\u0447\u0430\u0442\u044c \u0432\u0441\u0435 CRL'\u044b", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u0432\u0441\u0435 CRL", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c CRL \u0434\u043b\u044f \u0423\u0426", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0413\u0420\u041d", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u043b\u044e\u0447\u0430", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441 CRL", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0435 \u0441\u043a\u0430\u0447\u0438\u0432\u0430\u043d\u0438\u0435", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u0435 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.pushButton_33.setText("")
        ___qtablewidgetitem20 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem21 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0413\u0420\u041d", None));
        ___qtablewidgetitem22 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u043b\u044e\u0447\u0430", None));
        ___qtablewidgetitem23 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441 CRL", None));
        ___qtablewidgetitem24 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0435 \u0441\u043a\u0430\u0447\u0438\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem25 = self.tableWidget_4.horizontalHeaderItem(5)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"C\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u0435 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435", None));
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 CRL", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0413\u0420\u041d", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u043b\u044e\u0447\u0430", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441 CRL", None))
        self.pushButton_40.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0435 \u0441\u043a\u0430\u0447\u0438\u0432\u0430\u043d\u0438\u0435", None))
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u0435 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.pushButton_38.setText("")
        ___qtablewidgetitem26 = self.tableWidget_5.horizontalHeaderItem(0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem27 = self.tableWidget_5.horizontalHeaderItem(1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0413\u0420\u041d", None));
        ___qtablewidgetitem28 = self.tableWidget_5.horizontalHeaderItem(2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u043b\u044e\u0447\u0430", None));
        ___qtablewidgetitem29 = self.tableWidget_5.horizontalHeaderItem(3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441 CRL", None));
        ___qtablewidgetitem30 = self.tableWidget_5.horizontalHeaderItem(4)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0435 \u0441\u043a\u0430\u0447\u0438\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem31 = self.tableWidget_5.horizontalHeaderItem(5)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"C\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u0435 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435", None));
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"\u0421\u0432\u043e\u0438 CRL", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.pushButton_44.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.pushButton_43.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0413\u0420\u041d", None))
        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u043b\u044e\u0447\u0430", None))
        self.pushButton_41.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0435\u0447\u0430\u0442\u043e\u043a", None))
        self.pushButton_47.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u0438\u0439\u043d\u044b\u0435 \u043d\u043e\u043c\u0435\u0440", None))
        self.pushButton_46.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441 CRL", None))
        self.pushButton_45.setText("")
        ___qtablewidgetitem32 = self.tableWidget_6.horizontalHeaderItem(0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem33 = self.tableWidget_6.horizontalHeaderItem(1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0413\u0420\u041d", None));
        ___qtablewidgetitem34 = self.tableWidget_6.horizontalHeaderItem(2)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u043b\u044e\u0447\u0430", None));
        ___qtablewidgetitem35 = self.tableWidget_6.horizontalHeaderItem(3)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0435\u0447\u0430\u0442\u043e\u043a", None));
        ___qtablewidgetitem36 = self.tableWidget_6.horizontalHeaderItem(4)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u0438\u0439\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440", None));
        ___qtablewidgetitem37 = self.tableWidget_6.horizontalHeaderItem(5)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441 CRL", None));
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u044b\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0430\u0447\u0438\u0432\u0430\u0435\u043c\u044b\u0435 CRL", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0432\u043a\u043b\u0430\u0434\u043e\u043a", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0432\u044b\u0432\u043e\u0434\u0438\u043c\u044b\u0445 \u0441\u0442\u0440\u043e\u043a \u0432 \u0441\u043f\u0438\u0441\u043a\u0435 CRL", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0432\u044b\u0432\u043e\u0434\u0438\u043c\u044b\u0445 \u0441\u0442\u0440\u043e\u043a \u0432 \u0441\u0432\u043e\u0435\u043c \u0441\u043f\u0438\u0441\u043a\u0435 \u0441\u043a\u0430\u0447\u0438\u0432\u0430\u043d\u0438\u044f CRL", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0432\u044b\u0432\u043e\u0434\u0438\u043c\u044b\u0445 \u0441\u0442\u0440\u043e\u043a \u0432 \u043e\u0441\u043d\u043e\u0432\u043d\u043e\u043c \u0441\u043f\u0438\u0441\u043a\u0435 \u0441\u043a\u0430\u0447\u0438\u0432\u0430\u043d\u0438\u044f CRL", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0432\u044b\u0432\u043e\u0434\u0438\u043c\u044b\u0445 \u0441\u0442\u0440\u043e\u043a \u0432 \u0441\u043f\u0438\u0441\u043a\u0435 \u0421\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0432", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0432\u044b\u0432\u043e\u0434\u0438\u043c\u044b\u0445 \u0441\u0442\u0440\u043e\u043a \u0432 \u0441\u043f\u0438\u0441\u043a\u0435 \u0423\u0426", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0432\u044b\u0432\u043e\u0434\u0438\u043c\u044b\u0445 \u0441\u0442\u0440\u043e\u043a \u0432 \u0441\u043f\u0438\u0441\u043a\u0435 \u043e\u0442\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u044b\u0445 CRL", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u0438\u044f", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0440\u0435\u0448\u0438\u0442\u044c \u0438\u043c\u043f\u043e\u0440\u0442 CRL", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0440\u0435\u0448\u0438\u0442\u044c \u044d\u043a\u0441\u043f\u043e\u0440\u0442 CRL", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0440\u0435\u0448\u0438\u0442\u044c \u0443\u0434\u0430\u043b\u044f\u0442\u044c CRL \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430 \u0441\u043a\u0430\u0447\u0438\u0432\u0430\u0435\u043c\u044b\u0445", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u043a\u043d\u043e\u043f\u043a\u0443 \"\u0421\u043a\u0430\u0447\u0430\u0442\u044c \u0432\u0441\u0435 CRL\"", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u043a\u043d\u043e\u043f\u043a\u0443 \"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u0432\u0441\u0435 CRL\"", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0433\u043e \u043e\u043a\u043d\u0430", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u043e\u043a\u043d\u0430:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u0438\u043d\u0430 \u043e\u043a\u043d\u0430:", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0431\u043b\u043e\u043a\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0440\u0430\u0437\u043c\u0435\u0440\u0430 \u043e\u043a\u043d\u0430", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u044f\u0442\u044c \u0440\u0430\u0437\u043c\u0435\u0440 \u043e\u043a\u043d\u0430 \u043f\u0440\u0438 \u0432\u044b\u0445\u043e\u0434\u0435", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u043d\u0438\u0442\u043e\u0440\u0438\u043d\u0433", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0435\u0434\u0438\u0442\u044c \u0432 \u043f\u0440\u0435\u0434\u0435\u043b\u0430\u0445 \u0434\u043d\u0435\u0439", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u044f\u0442\u044c CRL \u0434\u043e \u0438\u0441\u0442\u0435\u0447\u0435\u043d\u0438\u044f", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0413\u0420\u041d \u0423\u0426 \u0421\u0432\u043e\u0439", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0413\u0420\u041d \u0423\u0426 \u041c\u0438\u043d\u043a\u043e\u043c\u0441\u0432\u044f\u0437\u044c", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442 / \u042d\u043a\u0441\u043f\u043e\u0440\u0442 CRL'\u043e\u0432", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a CRL", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c CRL \u043b\u0438\u0441\u0442", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u043e\u0432\u0435\u0449\u0435\u043d\u0438\u0435 \u043f\u043e XMPP", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u0432\u0435\u0440 XMPP", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u0443 \u043e\u0442\u0441\u044b\u043b\u0430\u0442\u044c", None))
        self.checkBox_10.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u043e\u0432\u0435\u0449\u0430\u0442\u044c \u043e\u0431 \u043e\u0448\u0438\u0431\u043a\u0430\u0445", None))
        self.checkBox_9.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u043e\u0432\u0435\u0449\u0430\u0442\u044c \u043e \u043d\u043e\u0432\u044b\u0445 CRL", None))
        self.checkBox_11.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u043e\u0432\u0435\u0449\u0430\u0442\u044c \u043e \u043d\u043e\u0432\u043e\u043c TSL", None))
        self.label_27.setText("")
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0435", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043f\u043a\u0438 \u0441\u043a\u0430\u0447\u0438\u0432\u0430\u043d\u0438\u044f", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0430\u043f\u043a\u0443 \u0434\u043b\u044f \u0421\u0410\u0421", None))
        self.label_13.setText("")
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0430\u043f\u043a\u0443 \u0434\u043b\u044f \u0421\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0432", None))
        self.label_12.setText("")
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0430\u043f\u043a\u0443 \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445 \u0444\u0430\u0439\u043b\u043e\u0432 \u0423\u0426", None))
        self.label_11.setText("")
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0430\u043f\u043a\u0443 \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445 \u0444\u0430\u0439\u043b\u043e\u0432", None))
        self.label_10.setText("")
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0430\u043f\u043a\u0443 \u0434\u043b\u044f \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438 \u0432 \u0423\u0426", None))
        self.label_9.setText("")
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u043f\u0440\u043e\u043a\u0441\u0438", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u043f\u0440\u043e\u043a\u0441\u0438?", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0440\u0442:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438 \u0437\u0430\u043f\u0443\u0441\u043a\u0435 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b (\u043c\u043e\u0436\u0435\u0442 \u0437\u0430\u043c\u0435\u0434\u043b\u0438\u0442\u044c \u0437\u0430\u043f\u0443\u0441\u043a \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b)", None))
        self.checkBox_12.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u044f\u0442\u044c CRL \u043d\u0430 \u0430\u043a\u0442\u0443\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0438 \u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u043e\u0441\u0442\u044c", None))
        self.checkBox_13.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u044f\u0442\u044c TSL \u043d\u0430 \u0430\u043a\u0442\u0443\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442 \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0438 CRL", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442 \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0438 CRL \u0432 \u0423\u0426", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u043e\u0438", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u043b\u043e\u0433\u043e\u0432", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c \u043b\u043e\u0433\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))

        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u043b\u043e\u0433\u043e\u0432 (\u041a\u0411)", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043b\u0438\u0442\u044c \u043b\u043e\u0433\u0438 \u043f\u043e \u0434\u043d\u044f\u043c", None))
        self.checkBox_14.setText("")
        self.label_28.setText("")
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_15), QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0442\u0430 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_16), QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0430\u0447\u0438\u0432\u0430\u043d\u0438\u0435", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_17), QCoreApplication.translate("MainWindow", u"\u041e\u0448\u0438\u0431\u043a\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">GitHub:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/MrSaerus/E-TrustCRLparsing\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">https://github.com/MrSaerus/E-TrustCRLparsing</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                        "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0423\u0440\u043e\u0432\u043d\u0438 \u043b\u043e\u0433\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  1 \u041a\u0440\u0438\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u043e\u0448\u0438\u0431\u043a\u0438</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  2 \u041e\u0448\u0438\u0431\u043a\u0438 \u0440\u0430\u0431\u043e\u0442\u044b</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  3 \u041f\u0440\u0435\u0434\u0443\u043f\u0440\u0435\u0436\u0434\u0435\u043d\u0438\u044f \u0440\u0430\u0431\u043e\u0442\u044b \u043c\u043e\u0434\u0443\u043b\u0435\u0439</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent"
                        ":0px;\">  4 \u041f\u0440\u0435\u0434\u0443\u043f\u0440\u0435\u0436\u0434\u0435\u043d\u0438\u044f \u0441\u043a\u0430\u0447\u0438\u0432\u0430\u043d\u0438\u044f \u0438 \u043f\u0440\u0435\u0432\u043e\u0440\u043e\u043a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  5 \u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0441\u043a\u0430\u0447\u0438\u0432\u0430\u043d\u0438\u0438 \u0438 \u043f\u0440\u043e\u0432\u0435\u0440\u043e\u043a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  6 \u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0440\u0430\u0431\u043e\u0442\u0435 \u043c\u043e\u0434\u0443\u043b\u0435\u0439</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  7 \u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043f\u0440\u043e"
                        "\u0447\u0430\u044f</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  8 \u0420\u0435\u0437\u0435\u0440\u0432</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  9 \u0412\u0441\u0451</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_14), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
    # retranslateUi

