from fileinput import close
from PyQt5 import QtWidgets, QtGui, QtCore
from ..view.PopupConfirm import Ui_Dialog


class ControllerPopupConfirm(Ui_Dialog, QtWidgets.QDialog):
    def __init__(self, titleLabel, messageLabel):
        super(ControllerPopupConfirm, self).__init__()
        self.titleLabel = titleLabel
        self.setupUi(self)
        self.labelPopup.setText(messageLabel)

        self.cancelButton.clicked.connect(self.cancel_button)
        self.confirmButton.clicked.connect(self.confirm_button)

    def retranslateUi(self, Form):
        res = super(ControllerPopupConfirm, self).retranslateUi(Form)
        Form.setWindowTitle(self.titleLabel)
        return res

    def cancel_button(self):
        self.close()

    def confirm_button(self):
        QtWidgets.QDialog.accept(self)
        self.close()