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
    def __init__(self, health_center=None, parent=None):
        super(HealthCenterDialog, self).__init__(parent)

        self.setupUi(self)
        self.typeComboBox.addItems(types)

        if health_center is not None:
            self.nameLineEdit.setText(QString(health_center.name))
            self.latitudeLineEdit.setText(QString(health_center.latitude))
            self.longitudeLineEdit.setText(QString(health_center.longitude))
            self.descriptionTextEdit.setText(
                    QString(health_center.description))
            self.nameResponsibleLineEdit.setText(
                    QString(health_center.responsible_person))
            self.phoneNumberLineEdit.setText(
                    QString(health_center.phone_number))
            self.emailAddressLineEdit.setText(
                    QString(health_center.email_address))

        if not MAC:
            self.buttonBox.setFocusPolicy(Qt.NoFocus)
        self.connect(self.buttonBox.button(QDialogButtonBox.Ok),
                    SIGNAL('clicked()'), self.save)
        self.connect(self.buttonBox.button(QDialogButtonBox.Cancel),
                    SIGNAL('clicked()'), self.reject)
        self.connect(self, SIGNAL('rejected()'), self.reject)
    def save(self):
        if not self.isValid():
            return
        name = unicode(self.nameLineEdit.text())
        type_id = session.query(HealthCenterType).filter_by(
                name=unicode(self.typeComboBox.currentText())).one().id
        latitude = unicode(self.latitudeLineEdit.text())
        longitude = unicode(self.longitudeLineEdit.text())
        description = unicode(self.descriptionTextEdit.toPlainText())
        responsible_person = unicode(self.nameResponsibleLineEdit.text())
        phone_number = unicode(self.phoneNumberLineEdit.text())
        email_address = unicode(self.emailAddressLineEdit.text())

        if health_center is not None:
            session.query(HealthCenter).filter(
                    HealthCenter.id == health_center.id).update(values=dict(
                        name=name, type_id=type_id, latitude=latitude,
                        longitude=longitude, description=description,
                        responsible_person=responsible_person,
                        phone_number=phone_number, email_address=email_address
                        ))
        else:
            hc = HealthCenter(name, type_id, latitude, longitude, responsible_person,
                    phone_number, email_address, description)
            session.add(hc)

        session.commit()
        self.accept()
        return

    def isValid(self):
        if self.nameLineEdit.text() == '':
            QMessageBox.warning(self, 'Errors in Form', "Name can't be empty.")
            self.exec_()
            self.nameLineEdit.setFocus()
            return False
        if self.nameResponsibleLineEdit.text() == '':
            QMessageBox.warning(self, 'Errors in Form',
                    "Name of Responsible Person can't be empty.")
            self.nameResponsibleLineEdit.setFocus()
            return False
        if self.phoneNumberLineEdit.text() == '':
            QMessageBox.warning(self, 'Errors in Form', "Phone Number can't be empty.")
            self.phoneNumberLineEdit.setFocus()
            return False
        return True
