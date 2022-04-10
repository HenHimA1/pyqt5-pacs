from PyQt5 import QtWidgets
from .controller.PatientTree import ControllerPatientTree
# from .controller.StudyTree import ControllerStudyTree
from . import database
import sys

database.activeDatabase = database.Database("database.db3", open("database.sql"))
app = QtWidgets.QApplication(sys.argv)
ui = ControllerPatientTree()
# ui = ControllerStudyTree()
ui.show()
sys.exit(app.exec_())