# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sub_main_addBrUchA.ui'
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


class Ui_Form_add(object):
    def setupUi(self, Form_add):
        if Form_add.objectName():
            Form_add.setObjectName(u"Form_add")
        Form_add.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form_add.sizePolicy().hasHeightForWidth())
        Form_add.setSizePolicy(sizePolicy)
        Form_add.setMinimumSize(QSize(800, 300))
        Form_add.setMaximumSize(QSize(800, 300))
        Form_add.setSizeIncrement(QSize(800, 300))
        Form_add.setBaseSize(QSize(800, 300))
        self.verticalLayout_2 = QVBoxLayout(Form_add)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(Form_add)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Panel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_4.addWidget(self.lineEdit)


        self.verticalLayout_4.addWidget(self.frame)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_4 = QFrame(Form_add)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.comboBox = QComboBox(self.frame_4)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QSize(385, 0))

        self.horizontalLayout.addWidget(self.comboBox)

        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(120, 0))

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_3.addWidget(self.frame_4, 0, Qt.AlignLeft)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.verticalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(Form_add)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.lineEdit_6 = QLineEdit(Form_add)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy1)
        self.lineEdit_6.setMinimumSize(QSize(250, 0))
        self.lineEdit_6.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_5.addWidget(self.lineEdit_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(Form_add)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.lineEdit_7 = QLineEdit(Form_add)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy1.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy1)
        self.lineEdit_7.setMinimumSize(QSize(250, 0))
        self.lineEdit_7.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_6.addWidget(self.lineEdit_7)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_6 = QLabel(Form_add)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_13.addWidget(self.label_6)

        self.lineEdit_2 = QLineEdit(Form_add)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy1.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy1)
        self.lineEdit_2.setMinimumSize(QSize(250, 0))
        self.lineEdit_2.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_13.addWidget(self.lineEdit_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(Form_add)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.lineEdit_3 = QLineEdit(Form_add)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy1.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy1)
        self.lineEdit_3.setMinimumSize(QSize(250, 0))
        self.lineEdit_3.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_7.addWidget(self.lineEdit_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_4 = QLabel(Form_add)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_9.addWidget(self.label_4)

        self.lineEdit_8 = QLineEdit(Form_add)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        sizePolicy1.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy1)
        self.lineEdit_8.setMinimumSize(QSize(250, 0))
        self.lineEdit_8.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_9.addWidget(self.lineEdit_8)


        self.verticalLayout_14.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_5 = QLabel(Form_add)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_14.addWidget(self.label_5)

        self.lineEdit_9 = QLineEdit(Form_add)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        sizePolicy1.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy1)
        self.lineEdit_9.setMinimumSize(QSize(250, 0))
        self.lineEdit_9.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_14.addWidget(self.lineEdit_9)


        self.verticalLayout_14.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_3.addLayout(self.verticalLayout_14)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_8 = QLabel(Form_add)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_10.addWidget(self.label_8)

        self.lineEdit_4 = QLineEdit(Form_add)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy1.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy1)
        self.lineEdit_4.setMinimumSize(QSize(250, 0))
        self.lineEdit_4.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_10.addWidget(self.lineEdit_4)


        self.verticalLayout_13.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_9 = QLabel(Form_add)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_11.addWidget(self.label_9)

        self.lineEdit_5 = QLineEdit(Form_add)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy1.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy1)
        self.lineEdit_5.setMinimumSize(QSize(250, 0))
        self.lineEdit_5.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_11.addWidget(self.lineEdit_5)


        self.verticalLayout_13.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_3.addLayout(self.verticalLayout_13)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.pushButton_2 = QPushButton(Form_add)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2, 0, Qt.AlignRight)


        self.retranslateUi(Form_add)

        QMetaObject.connectSlotsByName(Form_add)
    # setupUi

    def retranslateUi(self, Form_add):
        Form_add.setWindowTitle(QCoreApplication.translate("Form_add", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c CRL", None))
        self.label.setText(QCoreApplication.translate("Form_add", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u0432\u0441\u0435\u043c \u043f\u043e\u043b\u044f\u043c: ", None))
        self.pushButton.setText(QCoreApplication.translate("Form_add", u"\u041f\u043e\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u0432 \u043f\u043e\u043b\u044f", None))
        self.label_2.setText(QCoreApplication.translate("Form_add", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435: ", None))
        self.label_3.setText(QCoreApplication.translate("Form_add", u"\u0418\u041d\u041d: ", None))
        self.label_6.setText(QCoreApplication.translate("Form_add", u"\u041e\u0413\u0420\u041d: ", None))
        self.label_7.setText(QCoreApplication.translate("Form_add", u"\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u043b\u044e\u0447\u0430: ", None))
        self.label_4.setText(QCoreApplication.translate("Form_add", u"\u041e\u0442\u043f\u0435\u0447\u0430\u0442\u043e\u043a: ", None))
        self.label_5.setText(QCoreApplication.translate("Form_add", u"\u0410\u0434\u0440\u0435\u0441 CRL: ", None))
        self.label_8.setText(QCoreApplication.translate("Form_add", u"\u0421\u0435\u0440\u0438\u0439\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440: ", None))
        self.label_9.setText(QCoreApplication.translate("Form_add", u"TextLabel", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form_add", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

