# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_TabMainWidget2(object):
    def setupUi(self, TabMainWidget2):
        if not TabMainWidget2.objectName():
            TabMainWidget2.setObjectName(u"TabMainWidget2")
        TabMainWidget2.resize(1019, 625)
        self.horizontalLayout = QHBoxLayout(TabMainWidget2)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftSidebarContainer = QWidget(TabMainWidget2)
        self.leftSidebarContainer.setObjectName(u"leftSidebarContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftSidebarContainer.sizePolicy().hasHeightForWidth())
        self.leftSidebarContainer.setSizePolicy(sizePolicy)
        self.leftSidebarContainer.setMinimumSize(QSize(100, 0))
        self.verticalLayout = QVBoxLayout(self.leftSidebarContainer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.leftSidebarCloseButton = QPushButton(self.leftSidebarContainer)
        self.leftSidebarCloseButton.setObjectName(u"leftSidebarCloseButton")

        self.verticalLayout.addWidget(self.leftSidebarCloseButton)


        self.horizontalLayout.addWidget(self.leftSidebarContainer)

        self.centralContainer = QWidget(TabMainWidget2)
        self.centralContainer.setObjectName(u"centralContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(30)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralContainer.sizePolicy().hasHeightForWidth())
        self.centralContainer.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.centralContainer)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.commandLineEdit = QLineEdit(self.centralContainer)
        self.commandLineEdit.setObjectName(u"commandLineEdit")

        self.verticalLayout_3.addWidget(self.commandLineEdit)


        self.horizontalLayout.addWidget(self.centralContainer)

        self.rightSidebarContainer = QWidget(TabMainWidget2)
        self.rightSidebarContainer.setObjectName(u"rightSidebarContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(5)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.rightSidebarContainer.sizePolicy().hasHeightForWidth())
        self.rightSidebarContainer.setSizePolicy(sizePolicy2)
        self.rightSidebarContainer.setMinimumSize(QSize(100, 0))
        self.verticalLayout_2 = QVBoxLayout(self.rightSidebarContainer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.rightSidebarCloseButton = QPushButton(self.rightSidebarContainer)
        self.rightSidebarCloseButton.setObjectName(u"rightSidebarCloseButton")

        self.verticalLayout_2.addWidget(self.rightSidebarCloseButton)


        self.horizontalLayout.addWidget(self.rightSidebarContainer)


        self.retranslateUi(TabMainWidget2)

        QMetaObject.connectSlotsByName(TabMainWidget2)
    # setupUi

    def retranslateUi(self, TabMainWidget2):
        TabMainWidget2.setWindowTitle(QCoreApplication.translate("TabMainWidget2", u"Form", None))
        self.leftSidebarCloseButton.setText(QCoreApplication.translate("TabMainWidget2", u"<", None))
        self.rightSidebarCloseButton.setText(QCoreApplication.translate("TabMainWidget2", u">", None))
    # retranslateUi
