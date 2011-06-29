#!/usr/bin/env/python

import platform
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from gui.library.dialogs import *
__version__ = '1.0.0'


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        fileImportAction = self.createAction('&Import data',
                self.fileImport, tip='Import a file')

        fileExportAction = self.createAction('&Export data',
                self.fileExport, tip='Export help text')

        fileQuitAction = self.createAction('&Quit', self.close, 'Ctrl + Q',
                'filequit', 'Close the application')

        toolsAddHealthCenterAction = self.createAction('&Add Health Center',
                self.addHealthCenter, tip='Add Health Center')

        toolsEditHealthCenterAction = self.createAction('&Edit Health Center',
                self.editHealthCenter, tip='Edit Health Center')

        toolsAddCriteriaAction = self.createAction('Add &Criteria',
                self.addCriteria, tip='Add Criteria')

        toolsEditCriteriaAction = self.createAction('E&dit Criteria',
                self.editCriteria, tip='Edit Criteria')

        helpAboutAction = self.createAction('&About', self.helpAbout,
                tip='About the application')

        fileMenu = self.menuBar().addMenu('&File')
        self.addActions(fileMenu, (fileImportAction, fileExportAction, None,
            fileQuitAction))

        toolsMenu = self.menuBar().addMenu('&Tools')
        self.addActions(toolsMenu, (toolsAddHealthCenterAction,
            toolsEditHealthCenterAction, None, toolsAddCriteriaAction,
            toolsEditCriteriaAction))

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
        #self.showMaximized()

    def fileImport(self):
        pass

    def fileExport(self):
        pass

    def addHealthCenter(self):
        form = HealthCenterDialog()
        self.infinite_loop(form)

    def infinite_loop(self, form):
        if form.exec_():
            if form.isValid() is not True:
                self.infinite_loop(form)
            return

    def editHealthCenter(self):
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
