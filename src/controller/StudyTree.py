from PyQt5 import QtWidgets, QtGui, QtCore
from ..view.StudyTree import Ui_Form
from .StudyForm import ControllerStudyForm
from ..model import TableModel
from .. import database


class ControllerStudyTree(Ui_Form, QtWidgets.QWidget):
    def __init__(self):
        super(ControllerStudyTree, self).__init__()
        self.setupUi(self)
        self.load_study()
        self.init_study_tree()

        self.studyForm = ControllerStudyForm()

        self.createStudyButton.clicked.connect(self.create_study_button)
        self.studyForm.procDone.connect(self.update_study_tree)
        
    def retranslateUi(self, Form):
        res = super(ControllerStudyTree, self).retranslateUi(Form)
        Form.setWindowTitle("Study")
        return res

    def create_study_button(self):
        self.studyForm.show()

    def load_study(self):
        self.studies = database.activeDatabase.read("DICOMStudies")

    def init_study_tree(self):
        self.studyTree.setModel(TableModel(self.studies))

    def update_study_tree(self):
        self.load_study()
        self.init_study_tree()