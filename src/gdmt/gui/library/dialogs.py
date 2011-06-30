import datetime
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from gui.dialogs.health_center_dialog_ui import Ui_HealthCenterDialog
from gui.dialogs.rating_criteria_dialog_ui import Ui_RatingCriteriaDialog
from gui.dialogs.delete_confirmation_dialog_ui import Ui_DeleteConfirmationDialog
from gui.library.models import *
from utils.config import session

MAC = "qt_mac_set_native_menubar" in dir()

class HealthCenterDialog(QDialog, Ui_HealthCenterDialog):
    def __init__(self, health_center=None, parent=None):
        super(HealthCenterDialog, self).__init__(parent)

        self.success = False
        self.health_center = health_center
        self.setupUi(self)

        health_center_types = []
        for hct in session.query(HealthCenterType).order_by(HealthCenterType.name):
            health_center_types.append(QString(hct.name))
        self.typeComboBox.addItems(health_center_types)

        if self.health_center is not None:
            self.nameLineEdit.setText(QString(self.health_center.name))
            self.latitudeLineEdit.setText(QString(self.health_center.latitude))
            self.longitudeLineEdit.setText(
                    QString(self.health_center.longitude))
            self.descriptionTextEdit.setText(
                    QString(self.health_center.description))
            self.nameResponsibleLineEdit.setText(
                    QString(self.health_center.responsible_person))
            self.phoneNumberLineEdit.setText(
                    QString(self.health_center.phone_number))
            self.emailAddressLineEdit.setText(
                    QString(self.health_center.email_address))

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

        if self.health_center is not None:
            session.query(HealthCenter).filter(
                    HealthCenter.id == self.health_center.id).update(
                            values=dict(
                            name=self.name, type_id=self.type_id,
                            latitude=self.latitude, longitude=self.longitude,
                            description=self.description,
                            responsible_person=self.responsible_person,
                            phone_number=self.phone_number,
                            email_address=self.email_address
                            ))
        else:
            hc = HealthCenter(self.name, self.type_id, self.latitude,
                    self.longitude, self.responsible_person, self.phone_number,
                    self.email_address, self.description)
            session.add(hc)

        session.commit()
        self.success = True
        self.accept()

    def isValid(self):

        self.name = unicode(self.nameLineEdit.text())
        if self.name == '':
            QMessageBox.warning(self, 'Errors in form', 'Name can\'t be empty.')
            self.nameLineEdit.setFocus()
            return False

        self.type_id = session.query(HealthCenterType).filter_by(
                name=unicode(self.typeComboBox.currentText())).one().id

        self.latitude = unicode(self.latitudeLineEdit.text())
        try:
            float(self.latitude)
        except:
            QMessageBox.warning(self, 'Errors in form',
                    'Latitude should be numeric.')
            self.latitudeLineEdit.setFocus()
            return False

        self.longitude = unicode(self.longitudeLineEdit.text())
        try:
            float(self.longitude)
        except:
            QMessageBox.warning(self, 'Errors in form',
                    'Longitude should be numeric.')
            self.longitudeLineEdit.setFocus()
            return False

        self.description = unicode(self.descriptionTextEdit.toPlainText())

        self.responsible_person = unicode(self.nameResponsibleLineEdit.text())
        if self.responsible_person == '':
            QMessageBox.warning(self, 'Errors in form',
                    'Name of Responsible Person can\'t be empty.')
            self.nameResponsibleLineEdit.setFocus()
            return False

        self.phone_number = unicode(self.phoneNumberLineEdit.text())
        if self.phone_number == '':
            QMessageBox.warning(self, 'Errors in form',
                    'Phone Number can\'t be empty.')
            self.phoneNumberLineEdit.setFocus()
            return False

        self.email_address = unicode(self.emailAddressLineEdit.text())

        return True

class DeleteHealthCenterDialog(QDialog, Ui_DeleteConfirmationDialog):
    def __init__(self, health_center=None, parent=None):
        super(DeleteHealthCenterDialog, self).__init__(parent)

        self.success = False
        self.health_center = health_center
        self.setupUi(self)

        self.label.setText(QString('Are you sure to delete Health Center '
            '- "%s"' % self.health_center.name))
        self.buttonBox.button(QDialogButtonBox.Cancel).setFocus()

        if not MAC:
            self.buttonBox.setFocusPolicy(Qt.NoFocus)

        self.connect(self.buttonBox.button(QDialogButtonBox.Ok),
                    SIGNAL('clicked()'), self.delete)
        self.connect(self.buttonBox.button(QDialogButtonBox.Cancel),
                    SIGNAL('clicked()'), self.reject)
        self.connect(self, SIGNAL('rejected()'), self.reject)

    def delete(self):
        session.delete(self.health_center)
        session.commit()
        self.success = True
        self.accept()
        return

class RatingCriteriaDialog(QDialog, Ui_RatingCriteriaDialog):
    def __init__(self, rating_criteria=None, parent=None):
        super(RatingCriteriaDialog, self).__init__(parent)
        self.success = False
        self.rating_criteria = rating_criteria
        self.setupUi(self)

        if rating_criteria is not None:
            date = self.rating_criteria.valid_from
            self.nameLineEdit.setText(QString(self.rating_criteria.name))
            self.minValueLineEdit.setText(QString(self.rating_criteria.min_value))
            self.maxValueLineEdit.setText(QString(self.rating_criteria.max_value))
            self.descriptionTextEdit.setText(
                    QString(self.rating_criteria.description))
            self.dateEdit.setDate(QDate(date.year, date.month, date.day))
        else:
            date = datetime.date.today()
            self.dateEdit.setDate(QDate(date.year, date.month, date.day))

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

        if self.rating_criteria is not None:
            session.query(RatingCriteria).filter(
                    RatingCriteria.id == self.rating_criteria.id).update(
                            values=dict(
                                name=self.name, min_value=self.min_value,
                                max_value=self.max_value,
                                description=self.description,
                                valid_from = self.valid_from
                                ))
        else:
            rc = RatingCriteria(self.name, self.min_value, self.max_value,
                    self.valid_from, self.description)
            session.add(rc)

        session.commit()
        self.success = True
        self.accept()

    def isValid(self):

        self.name = unicode(self.nameLineEdit.text())
        if self.name == '':
            QMessageBox.warning(self, 'Error in form', 'Name can\'t be empty.')
            self.nameLineEdit.setFocus()
            return False

        self.min_value = unicode(self.minValueLineEdit.text())
        try:
            float(self.min_value)
        except:
            QMessageBox.warning(self, 'Error in form',
                    'Minimum Value should be numeric.')
            self.minValueLineEdit.setFocus()
            return False

        self.max_value = unicode(self.maxValueLineEdit.text())
        try:
            float(self.max_value)
        except:
            QMessgaeBox.warning(self, 'Error in form',
                    'Maximum Value should be numeric.')
            self.maxValueLineEdit.setFocus()
            return False

        self.description = unicode(self.descriptionTextEdit.toPlainText())

        self.valid_from = self.dateEdit.date().toPyDate()

        return True

class DeleteRatingCriteriaDialog(QDialog, Ui_DeleteConfirmationDialog):
    def __init__(self, rating_criteria=None, parent=None):
        super(DeleteRatingCriteriaDialog, self).__init__(parent)

        self.success = False
        self.rating_criteria = rating_criteria
        self.setupUi(self)

        self.label.setText(QString('Are sure you to delete Rating Criteria '
            '- "%s"' % self.rating_criteria.name))
        self.buttonBox.button(QDialogButtonBox.Cancel).setFocus()

        if not MAC:
            self.buttonBox.setFocusPolicy(Qt.NoFocus)

        self.connect(self.buttonBox.button(QDialogButtonBox.Ok),
                    SIGNAL('clicked()'), self.delete)
        self.connect(self.buttonBox.button(QDialogButtonBox.Cancel),
                    SIGNAL('clicked()'), self.reject)
        self.connect(self, SIGNAL('rejected()'), self.reject)

    def delete(self):
        session.delete(self.rating_criteria)
        session.commit()
        self.success = True
        self.accept()
        return

