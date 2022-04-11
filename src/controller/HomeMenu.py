from PyQt5 import QtWidgets, QtGui, QtCore
from .Patient import ControllerPatientTree
from .Study import ControllerStudyTree
from ..view.HomeMenu import Ui_Form
from ..model import Patient 


class ControllerHomeMenu(Ui_Form, QtWidgets.QWidget):
    procDone = QtCore.pyqtSignal(bool)

    def __init__(self):
        super(ControllerHomeMenu, self).__init__()
        self.setupUi(self)
        self.tabWidget.removeTab(self.tabWidget.indexOf(self.PatientView))
        self.tabWidget.removeTab(self.tabWidget.indexOf(self.StudyView))
        self.PatientView = ControllerPatientTree()
        self.StudyView = ControllerStudyTree()
        self.tabWidget.addTab(self.PatientView, "Patient")
        self.tabWidget.addTab(self.StudyView, "Study")
        
    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        res = super(ControllerHomeMenu, self).retranslateUi(Form)
        Form.setWindowTitle(_translate("Database", "Database"))
        return res
