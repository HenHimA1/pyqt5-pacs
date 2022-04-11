from PyQt5 import QtWidgets, QtGui, QtCore
from ...view.PatientForm import Ui_Form
from ...model import Patient 


class ControllerUpdatePatientForm(Ui_Form, QtWidgets.QWidget):
    procDone = QtCore.pyqtSignal(bool)

    def __init__(self):
        super(ControllerUpdatePatientForm, self).__init__()
        self.setupUi(self)
        self.patientModel = Patient()
        self.init_field()
        
        self.createButton.setText("Save")

        self.createButton.clicked.connect(self.update_button)
        self.cancelButton.clicked.connect(self.cancel_button)
        
        self.PatientNam.textChanged.connect(self.changeNameEdit)
        self.PatientSex.textChanged.connect(self.changeSexEdit)
        self.PatientBir.userDateChanged.connect(self.changeBirEdit)

    def retranslateUi(self, Form):
        res = super(ControllerUpdatePatientForm, self).retranslateUi(Form)
        Form.setWindowTitle("Update Patient")
        return res

    def show(self):
        self.init_field()
        return super(ControllerUpdatePatientForm, self).show()

    def init_field(self):
        self.PatientNam.setText(self.patientModel.PatientNam)
        self.PatientSex.setText(self.patientModel.PatientSex)
        self.PatientBir.setDate(QtCore.QDate.fromString(self.patientModel.PatientBir))

    def changeNameEdit(self, value):
        self.patientModel.PatientNam = value

    def changeSexEdit(self, value):
        self.patientModel.PatientSex = value

    def changeBirEdit(self, value):
        self.patientModel.PatientBir = value.toString()

    @QtCore.pyqtSlot()
    def update_button(self):
        self.patientModel.update()
        self.procDone.emit(True)
        self.close()

    def cancel_button(self):
        self.close()