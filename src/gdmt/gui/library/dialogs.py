from PyQt4.QtCore import *
from PyQt4.QtGui import *
from gui.dialogs.health_center_dialog_ui import Ui_HealthCenterDialog
from gui.library.models import *
from utils.config import session

MAC = "qt_mac_set_native_menubar" in dir()

types = []
for hct in session.query(HealthCenterType).order_by(HealthCenterType.name):
    types.append(QString(hct.name))

class HealthCenterDialog(QDialog, Ui_HealthCenterDialog):
    def __init__(self, new=False, parent=None):
        super(HealthCenterDialog, self).__init__(parent)
        self.setupUi(self)
        self.typeComboBox.addItems(types)
        if not MAC:
            self.buttonBox.setFocusPolicy(Qt.NoFocus)
        #self.connect(self.buttonBox.button(QDialogButtonBox.Ok),
        #            SIGNAL('clicked()'), self.isValid)
    def save(self):
        name = unicode(self.nameLineEdit.text())
        type_id = session.query(HealthCenterType).filter_by(
                name=unicode(self.typeComboBox.currentText())).one().id
        latitude = unicode(self.latitudeLineEdit.text())
        longitude = unicode(self.longitudeLineEdit.text())
        description = unicode(self.descriptionTextEdit.toPlainText())
        responsible_person = unicode(self.nameResponsibleLineEdit.text())
        phone_number = unicode(self.phoneNumberLineEdit.text())
        email_address = unicode(self.emailAddressLineEdit.text())

        hc = HealthCenter(name, type_id, latitude, longitude, responsible_person,
                phone_number, email_address, description)
        session.add(hc)
        session.commit()
        return

    def isValid(self):
        if self.nameLineEdit.text() == '':
            QMessageBox.warning(self, 'Errors in Form', "Name can't be empty.")
            self.exec_()
            self.nameLineEdit.setFocus()
            return
        if self.nameResponsibleLineEdit.text() == '':
            QMessageBox.warning(self, 'Errors in Form',
                    "Name of Responsible Person can't be empty.")
            self.nameResponsibleLineEdit.setFocus()
            return
        if self.phoneNumberLineEdit.text() == '':
            QMessageBox.warning(self, 'Errors in Form', "Phone Number can't be empty.")
            self.phoneNumberLineEdit.setFocus()
            return
        self.save()
        return True

