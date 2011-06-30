# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_confirmation_dialog.ui'
#
# Created: Thu Jun 30 23:21:40 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DeleteConfirmationDialog(object):
    def setupUi(self, DeleteConfirmationDialog):
        DeleteConfirmationDialog.setObjectName(_fromUtf8("DeleteConfirmationDialog"))
        DeleteConfirmationDialog.resize(350, 150)
        DeleteConfirmationDialog.setMinimumSize(QtCore.QSize(350, 150))
        DeleteConfirmationDialog.setMaximumSize(QtCore.QSize(350, 150))
        self.gridLayout = QtGui.QGridLayout(DeleteConfirmationDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(DeleteConfirmationDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.label = QtGui.QLabel(DeleteConfirmationDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.retranslateUi(DeleteConfirmationDialog)
        QtCore.QMetaObject.connectSlotsByName(DeleteConfirmationDialog)

    def retranslateUi(self, DeleteConfirmationDialog):
        DeleteConfirmationDialog.setWindowTitle(QtGui.QApplication.translate("DeleteConfirmationDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DeleteConfirmationDialog", "Are you sure ?", None, QtGui.QApplication.UnicodeUTF8))

