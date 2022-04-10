import sys
import uuid
from PyQt5 import QtWidgets, QtGui, QtCore
from datetime import datetime
from ..view.PatientForm import Ui_Form
from .. import database


class ControllerPatientForm(Ui_Form, QtWidgets.QWidget):
    procDone = QtCore.pyqtSignal(bool)

    def __init__(self):
        super(ControllerPatientForm, self).__init__()
        self.setupUi(self)
        self.init_field()
        
        self.createButton.clicked.connect(self.create_button)
        self.cancelButton.clicked.connect(self.cancel_button)
        self.PatientNam.textChanged.connect(self.changeNameEdit)
        self.PatientSex.textChanged.connect(self.changeSexEdit)
        self.PatientBir.userDateChanged.connect(self.changeBirEdit)

    def retranslateUi(self, Form):
        res = super(ControllerPatientForm, self).retranslateUi(Form)
        Form.setWindowTitle("Create Patient")
        return res

    def init_field(self):
        self.name = ""
        self.sex = ""
        self.birth = int(datetime(year=2000, month=1, day=1).timestamp())
        
    def changeNameEdit(self, value):
        self.name = value

    def changeSexEdit(self, value):
        self.sex = value

    def changeBirEdit(self, value):
        if value.isValid():
            self.birth = int(datetime(
                year=value.year(), month=value.month(), day=value.month()).timestamp())

    @QtCore.pyqtSlot()
    def create_button(self):
        database.activeDatabase.create("DICOMPatients", {"PatientID": uuid.uuid4().hex,
                                                         "PatientNam": self.name,
                                                         "PatientNam": self.name,
                                                         "PatientBir": self.birth,
                                                         "PatientSex": self.sex})
        self.procDone.emit(True)

    def cancel_button(self):
        self.close()