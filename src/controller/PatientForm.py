from PyQt5 import QtWidgets, QtGui, QtCore
from ..view.PatientForm import Ui_Form
from ..model import Patient 


class ControllerPatientForm(Ui_Form, QtWidgets.QWidget):
    procDone = QtCore.pyqtSignal(bool)

    def __init__(self):
        super(ControllerPatientForm, self).__init__()
        self.setupUi(self)
        self.patientModel = Patient()
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
        self.patientModel.PatientBir = self.PatientBir.date().toString()

    def changeNameEdit(self, value):
        self.patientModel.PatientNam = value

    def changeSexEdit(self, value):
        self.patientModel.PatientSex = value

    def changeBirEdit(self, value):
        self.patientModel.PatientBir = value.toString()

    @QtCore.pyqtSlot()
    def create_button(self):
        self.patientModel.create()
        self.procDone.emit(True)

    def cancel_button(self):
        self.close()