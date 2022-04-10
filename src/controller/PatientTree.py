from PyQt5 import QtWidgets, QtGui, QtCore
from ..view.PatientTree import Ui_Form
from .PatientForm import ControllerPatientForm
from ..model import TableModel
from .. import database


class ControllerPatientTree(Ui_Form, QtWidgets.QWidget):
    def __init__(self):
        super(ControllerPatientTree, self).__init__()
        self.setupUi(self)
        self.load_patient()
        self.init_patient_tree()

        self.patientForm = ControllerPatientForm()

        self.createPatientButton.clicked.connect(self.create_patient_button)
        self.patientForm.procDone.connect(self.update_patient_tree)

    def retranslateUi(self, Form):
        res = super(ControllerPatientTree, self).retranslateUi(Form)
        Form.setWindowTitle("Patient")
        return res

    def load_patient(self):
        self.patients = database.activeDatabase.read("DICOMPatients")

    def init_patient_tree(self):
        self.patientTree.setModel(TableModel(self.patients))

    def update_patient_tree(self):
        self.load_patient()
        self.init_patient_tree()

    def create_patient_button(self):
        self.patientForm.show()
