from PyQt5 import QtWidgets
from .controller import ControllerHomeMenu
from . import database
import sys

database.activeDatabase = database.Database("database.db3", open("database.sql"))
app = QtWidgets.QApplication(sys.argv)
ui = ControllerHomeMenu()
ui.show()
sys.exit(app.exec_())