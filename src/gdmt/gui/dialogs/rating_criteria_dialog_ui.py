# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rating_criteria_dialog.ui'
#
# Created: Thu Jun 30 23:36:27 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_RatingCriteriaDialog(object):
    def setupUi(self, RatingCriteriaDialog):
        RatingCriteriaDialog.setObjectName(_fromUtf8("RatingCriteriaDialog"))
        RatingCriteriaDialog.resize(600, 400)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RatingCriteriaDialog.sizePolicy().hasHeightForWidth())
        RatingCriteriaDialog.setSizePolicy(sizePolicy)
        RatingCriteriaDialog.setMinimumSize(QtCore.QSize(600, 400))
        RatingCriteriaDialog.setMaximumSize(QtCore.QSize(600, 400))
        self.formLayout = QtGui.QFormLayout(RatingCriteriaDialog)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.nameLabel = QtGui.QLabel(RatingCriteriaDialog)
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtGui.QLineEdit(RatingCriteriaDialog)
        self.nameLineEdit.setObjectName(_fromUtf8("nameLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.nameLineEdit)
        self.minValueLabel = QtGui.QLabel(RatingCriteriaDialog)
        self.minValueLabel.setObjectName(_fromUtf8("minValueLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.minValueLabel)
        self.minValueLineEdit = QtGui.QLineEdit(RatingCriteriaDialog)
        self.minValueLineEdit.setObjectName(_fromUtf8("minValueLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.minValueLineEdit)
        self.maxValueLabel = QtGui.QLabel(RatingCriteriaDialog)
        self.maxValueLabel.setObjectName(_fromUtf8("maxValueLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.maxValueLabel)
        self.maxValueLineEdit = QtGui.QLineEdit(RatingCriteriaDialog)
        self.maxValueLineEdit.setObjectName(_fromUtf8("maxValueLineEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.maxValueLineEdit)
        self.descriptionLabel = QtGui.QLabel(RatingCriteriaDialog)
        self.descriptionLabel.setObjectName(_fromUtf8("descriptionLabel"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.descriptionLabel)
        self.descriptionTextEdit = QtGui.QTextEdit(RatingCriteriaDialog)
        self.descriptionTextEdit.setObjectName(_fromUtf8("descriptionTextEdit"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.descriptionTextEdit)
        self.dateLabel = QtGui.QLabel(RatingCriteriaDialog)
        self.dateLabel.setObjectName(_fromUtf8("dateLabel"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.dateLabel)
        self.dateEdit = QtGui.QDateEdit(RatingCriteriaDialog)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 4), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.dateEdit)
        self.buttonBox = QtGui.QDialogButtonBox(RatingCriteriaDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.buttonBox)
        self.nameLabel.setBuddy(self.nameLineEdit)
        self.minValueLabel.setBuddy(self.minValueLineEdit)
        self.maxValueLabel.setBuddy(self.maxValueLineEdit)
        self.descriptionLabel.setBuddy(self.descriptionTextEdit)
        self.dateLabel.setBuddy(self.dateEdit)

        self.retranslateUi(RatingCriteriaDialog)
        QtCore.QMetaObject.connectSlotsByName(RatingCriteriaDialog)
        RatingCriteriaDialog.setTabOrder(self.nameLineEdit, self.minValueLineEdit)
        RatingCriteriaDialog.setTabOrder(self.minValueLineEdit, self.maxValueLineEdit)
        RatingCriteriaDialog.setTabOrder(self.maxValueLineEdit, self.descriptionTextEdit)
        RatingCriteriaDialog.setTabOrder(self.descriptionTextEdit, self.dateEdit)
        RatingCriteriaDialog.setTabOrder(self.dateEdit, self.buttonBox)

    def retranslateUi(self, RatingCriteriaDialog):
        RatingCriteriaDialog.setWindowTitle(QtGui.QApplication.translate("RatingCriteriaDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.nameLabel.setText(QtGui.QApplication.translate("RatingCriteriaDialog", "&Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.minValueLabel.setText(QtGui.QApplication.translate("RatingCriteriaDialog", "&Minimum Value:", None, QtGui.QApplication.UnicodeUTF8))
        self.maxValueLabel.setText(QtGui.QApplication.translate("RatingCriteriaDialog", "Ma&ximum Value:", None, QtGui.QApplication.UnicodeUTF8))
        self.descriptionLabel.setText(QtGui.QApplication.translate("RatingCriteriaDialog", "&Description:", None, QtGui.QApplication.UnicodeUTF8))
        self.dateLabel.setText(QtGui.QApplication.translate("RatingCriteriaDialog", "&Valid from:", None, QtGui.QApplication.UnicodeUTF8))
        self.dateEdit.setDisplayFormat(QtGui.QApplication.translate("RatingCriteriaDialog", "dd/MM/yyyy", None, QtGui.QApplication.UnicodeUTF8))

