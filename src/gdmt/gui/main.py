#!/usr/bin/env/python

import platform
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from gui.library.dialogs import *
from utils.config import session

__version__ = '1.0.0'

def getHealthCenters():
    hc_list = []
    for hc in session.query(HealthCenter).order_by(HealthCenter.name):
        hc_list.append(hc)
    return hc_list

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.health_centers = getHealthCenters()

        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)

        fileImportAction = self.createAction('&Import data',
                self.fileImport, tip='Import a file')

        fileExportAction = self.createAction('&Export data',
                self.fileExport, tip='Export help text')

        fileQuitAction = self.createAction('&Quit', self.close, 'Ctrl + Q',
                'filequit', 'Close the application')

        toolsManageHealthCentersAction = self.createAction(
                'Manage &Health Centers', self.manageHealthCenters,
                tip='Manage Health Centers')

        toolsManageCriteriasAction = self.createAction('Manage &Criterias',
                self.manageCriterias, tip='Manage Criterias')

        helpAboutAction = self.createAction('&About', self.helpAbout,
                tip='About the application')

        fileMenu = self.menuBar().addMenu('&File')
        self.addActions(fileMenu, (fileImportAction, fileExportAction, None,
            fileQuitAction))

        toolsMenu = self.menuBar().addMenu('&Tools')
        self.addActions(toolsMenu, (toolsManageHealthCentersAction, None,
            toolsManageCriteriasAction))

        reportsMenu = self.menuBar().addMenu('&Reports')

        helpMenu = self.menuBar().addMenu('&Help')
        self.addActions(helpMenu, (helpAboutAction, ))

        settings = QSettings()
        size = settings.value('MainWindow/Size',
                QVariant(QSize(900, 600))).toSize()

        self.resize(size)
        position = settings.value('MainWindow/Position',
                QVariant(QPoint(0,0))).toPoint()

        self.move(position)
        self.restoreState(
                settings.value('MainWindow/Restore').toByteArray())

        self.setWindowTitle('GIS Data Monitoring Tool')
        self.showMaximized()

    def fileImport(self):
        pass

    def fileExport(self):
        pass

    def manageHealthCenters(self):
        manageHealthCentersToolBar = QToolBar('Manage Health Centers')
        manageHealthCentersToolBar.addAction('Add Health Center',
                self.addHealthCenter)
        manageHealthCentersToolBar.addAction('Edit Health Center',
                self.editHealthCenter)
        manageHealthCentersToolBar.addAction('Delete Health Center',
                self.deleteHealthCenter)

        self.removeToolBar(self.toolbar)
        self.toolbar = manageHealthCentersToolBar
        self.addToolBar(self.toolbar)

        self.showHealthCenters()

    def addHealthCenter(self):
        form = HealthCenterDialog()
        if form.exec_():
            if form.success:
                self.health_centers = getHealthCenters()
                self.showHealthCenters()
                self.table.setCurrentCell(-1,-1)

    def editHealthCenter(self):
        current_row = self.table.currentRow()
        if current_row == -1:
            QMessageBox.warning(self, 'Error', 'Please select a row.')
            self.table.setCurrentCell(-1,-1)
            return
        hc = self.health_centers[current_row]
        form = HealthCenterDialog(health_center=hc)
        if form.exec_():
            if form.success:
                self.health_centers = getHealthCenters()
                self.showHealthCenters()

    def deleteHealthCenter(self):
        current_row = self.table.currentRow()
        if current_row == -1:
            QMessageBox.warning(self, 'Error', 'Please select a row.')
            self.table.setCurrentCell(-1,-1)
            return
        hc =  self.health_centers[current_row]
        form = DeleteHealthCenterDialog(health_center=hc)
        if form.exec_():
            if form.success:
               self.health_centers.remove(hc)
               self.table.removeRow(current_row)
               self.table.setCurrentCell(-1,-1)


    def showHealthCenters(self):
        table = QTableWidget()
        self.table = table
        self.setCentralWidget(table)

        self.connect(table,
                SIGNAL("itemDoubleClicked(QTableWidgetItem*)"),
                self.editHealthCenter)

        table.setRowCount(len(self.health_centers))
        table.setColumnCount(8)
        table.setHorizontalHeaderLabels(['Name', 'Type', 'Description',
            'Latitude', 'Longitude', 'Responsible Person', 'Phone Number', 
            'Email Address'])
        table.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        table.setAlternatingRowColors(True)
        table.setEditTriggers(QTableWidget.NoEditTriggers)
        table.setSelectionBehavior(QTableWidget.SelectRows)
        table.setSelectionMode(QTableWidget.SingleSelection)
        selected = None
        for row, hc in enumerate(self.health_centers):
            table.setItem(row, 0, QTableWidgetItem(QString(hc.name)))
            table.setItem(row, 1, QTableWidgetItem(QString(hc.type.name)))
            table.setItem(row, 2, QTableWidgetItem(QString(hc.description)))
            table.setItem(row, 3, QTableWidgetItem(QString(hc.latitude)))
            table.setItem(row, 4, QTableWidgetItem(QString(hc.longitude)))
            table.setItem(row, 5, QTableWidgetItem(QString(hc.responsible_person)))
            table.setItem(row, 6, QTableWidgetItem(QString(hc.phone_number)))
            table.setItem(row, 7, QTableWidgetItem(QString(hc.email_address)))

    def manageCriterias(self):
        pass

    def addCriteria(self):
        pass

    def editCriteria(self):
        pass

    def createAction(self, text, slot=None, shortcut=None, icon=None,
           tip=None, checkable=False, signal="triggered()"):
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon(":/%s.png" % icon))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            self.connect(action, SIGNAL(signal), slot)
        if checkable:
            action.setCheckable(True)
        return action


    def addActions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    def helpAbout(self):
        QMessageBox.about(self, 'GIS Data Monitoring Tool - About',
                '''
                <b>GIS Data Monitoring Tool</b> v %s
                <p>Copyright &copy; 2011  Policy Innovations Pvt. Ltd.
                All rights reserved.
                <p>This application can be used to monitor quality of health
                centers across state.
                <p>Python %s - Qt %s - Pyqt %s on %s''' %(
                    __version__, platform.python_version(),
                    QT_VERSION_STR, PYQT_VERSION_STR, platform.system()))

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec_()

if __name__ == '__main__':
    #someone is launching this file directly
    main()
