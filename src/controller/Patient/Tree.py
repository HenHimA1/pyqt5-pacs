from PyQt5 import QtWidgets, QtGui, QtCore
from ...component.controller import ControllerPopupConfirm
from ...view.PatientTree import Ui_Form
from .CreateForm import ControllerCreatePatientForm
from .UpdateForm import ControllerUpdatePatientForm
from ...model import TableModel
from ...model import Patient


class ControllerPatientTree(Ui_Form, QtWidgets.QWidget):
    def __init__(self):
        super(ControllerPatientTree, self).__init__()
        self.setupUi(self)
        self.patientModel = Patient()
        self.load_patient()
        self.init_patient_tree()

        self.createPatientForm = ControllerCreatePatientForm()
        self.updatePatientForm = ControllerUpdatePatientForm()
        
        self.deletePatientButton.setDisabled(True)
        self.updatePatientButton.setDisabled(True)

        self.createPatientButton.clicked.connect(self.create_patient_button)
        self.updatePatientButton.clicked.connect(self.update_patient_button)
        self.deletePatientButton.clicked.connect(self.delete_patient_button)
        self.createPatientForm.procDone.connect(self.update_patient_tree)
        self.updatePatientForm.procDone.connect(self.update_patient_tree)
        
        self.patientTree.viewport().installEventFilter(self)

    def retranslateUi(self, Form):
        res = super(ControllerPatientTree, self).retranslateUi(Form)
        Form.setWindowTitle("Patient")
        return res

    def load_patient(self):
        self.patients = self.patientModel.read()
        self.list_patient = [patient["PatientID"] for patient in self.patients]

    def init_patient_tree(self):
        self.patientTree.setModel(TableModel(self.patients))

    def update_patient_tree(self):
        self.load_patient()
        self.init_patient_tree()

    def create_patient_button(self):
        self.createPatientForm.show()

    def update_patient_button(self):
        self.updatePatientForm.patientModel = self.patientModel
        self.updatePatientForm.show()

    def delete_patient_button(self):
        self.deletePopup = ControllerPopupConfirm("Delete Patient", f"Are you sure want to delete {self.patientModel.PatientNam}?")
        self.deletePopup.show()
        if self.deletePopup.exec_() == self.deletePopup.Accepted:
            self.patientModel.delete(self.patientModel.PatientID)
            self.update_patient_tree()
            self.deletePatientButton.setDisabled(True)
            self.updatePatientButton.setDisabled(True)
        
    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            if event.button() == QtCore.Qt.LeftButton:
                index = self.patientTree.indexAt(event.pos())
                self.patientModel.browse(self.list_patient[index.row()])
                self.deletePatientButton.setDisabled(False)
                self.updatePatientButton.setDisabled(False)
        return super(ControllerPatientTree, self).eventFilter(source, event)
