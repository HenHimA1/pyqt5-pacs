from PyQt5 import QtWidgets, QtGui, QtCore
from datetime import datetime
from ...view.StudyForm import Ui_Form
from ...model import Study, Patient

currentTime = datetime.now()


class ControllerStudyForm(Ui_Form, QtWidgets.QWidget):
    procDone = QtCore.pyqtSignal(bool)

    def __init__(self):
        super(ControllerStudyForm, self).__init__()
        self.setupUi(self)
        self.studyModel = Study()
        self.load_patient()
        self.init_field()

        self.PatientID.currentIndexChanged.connect((self.changePatientEdit))
        self.StudyDate.dateChanged.connect(self.changeDateEdit)
        self.studyTime.timeChanged.connect(self.changeTimeEdit)
        self.StudyModal.textChanged.connect(self.changeModalEdit)
        self.StudyDescr.textChanged.connect(self.changeDescriptionEdit)
        self.AccessionN.textChanged.connect(self.changeAccessionEdit)
        self.ReferPhysi.textChanged.connect(self.changeReferPhysiEdit)

        self.createButton.clicked.connect(self.create_button)
        self.cancelButton.clicked.connect(self.cancel_button)

    def retranslateUi(self, Form):
        res = super(ControllerStudyForm, self).retranslateUi(Form)
        Form.setWindowTitle("Create Study")
        return res

    def changeReferPhysiEdit(self, value):
        self.studyModel.ReferPhysi = value

    def changeAccessionEdit(self, value):
        self.studyModel.AccessionN = value

    def changeDescriptionEdit(self, value):
        self.studyModel.StudyDescr = value 

    def changeModalEdit(self, value):
        self.studyModel.StudyModal = value

    def changeDateEdit(self, value):
        self.studyModel.StudyDate = value.toString()

    def changeTimeEdit(self, value):
        self.studyModel.StudyTime = value.toString()

    def changePatientEdit(self, value):
        self.studyModel.PatientID = self.list_patient[value]

    def init_field(self):
        self.StudyDate.setDate(QtCore.QDate().currentDate())
        self.studyTime.setTime(QtCore.QTime().currentTime())
        self.PatientID.addItems([patient['PatientNam']
                                for patient in self.patients])

        self.studyModel.PatientID = self.list_patient[self.PatientID.currentIndex(
        )]
        self.studyModel.StudyTime = self.studyTime.time().toString()
        self.studyModel.StudyDate = self.StudyDate.date().toString()

    def load_patient(self):
        self.patients = Patient().read()
        self.list_patient = [patient["PatientID"] for patient in self.patients]

    @QtCore.pyqtSlot()
    def create_button(self):
        self.studyModel.create()
        self.procDone.emit(True)

    def cancel_button(self):
        self.close()
