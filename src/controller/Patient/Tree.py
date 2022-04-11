from PyQt5 import QtWidgets, QtGui, QtCore
from ...view.PatientTree import Ui_Form
from .CreateForm import ControllerCreatePatientForm
from ...model import TableModel
from ...model import Patient


class ControllerPatientTree(Ui_Form, QtWidgets.QWidget):
    def __init__(self):
        super(ControllerPatientTree, self).__init__()
        self.setupUi(self)
        self.patientModel = Patient()
        self.load_patient()
        self.init_patient_tree()

        self.patientForm = ControllerCreatePatientForm()
        self.updatePatientForm = ControllerCreatePatientForm()
        
        self.createPatientButton.clicked.connect(self.create_patient_button)
        self.patientForm.procDone.connect(self.update_patient_tree)
        
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
        self.patientForm.show()
        
    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            if event.button() == QtCore.Qt.LeftButton:
                index = self.patientTree.indexAt(event.pos())
                self.patientModel.browse(self.list_patient[index.row()])
                # if index.data():
                #     self.clipboardLabel.setText(index.data())
        return super(ControllerPatientTree, self).eventFilter(source, event)
