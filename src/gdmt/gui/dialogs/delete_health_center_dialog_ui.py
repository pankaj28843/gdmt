# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_health_center_dialog.ui'
#
# Created: Thu Jun 30 19:13:15 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DeleteHealthCenterDialog(object):
    def setupUi(self, DeleteHealthCenterDialog):
        DeleteHealthCenterDialog.setObjectName(_fromUtf8("DeleteHealthCenterDialog"))
        DeleteHealthCenterDialog.resize(350, 150)
        DeleteHealthCenterDialog.setMinimumSize(QtCore.QSize(350, 150))
        DeleteHealthCenterDialog.setMaximumSize(QtCore.QSize(350, 150))
        self.gridLayout = QtGui.QGridLayout(DeleteHealthCenterDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(DeleteHealthCenterDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.label = QtGui.QLabel(DeleteHealthCenterDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.retranslateUi(DeleteHealthCenterDialog)
        QtCore.QMetaObject.connectSlotsByName(DeleteHealthCenterDialog)

    def retranslateUi(self, DeleteHealthCenterDialog):
        DeleteHealthCenterDialog.setWindowTitle(QtGui.QApplication.translate("DeleteHealthCenterDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DeleteHealthCenterDialog", "Are you sure ?", None, QtGui.QApplication.UnicodeUTF8))

