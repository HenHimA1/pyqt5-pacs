# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\src\view\StudyForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(376, 449)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelPatientID = QtWidgets.QLabel(Form)
        self.labelPatientID.setObjectName("labelPatientID")
        self.horizontalLayout_2.addWidget(self.labelPatientID)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.PatientID = QtWidgets.QComboBox(Form)
        self.PatientID.setObjectName("PatientID")
        self.verticalLayout_2.addWidget(self.PatientID)
        self.verticalLayout_11.addLayout(self.verticalLayout_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelStudyDate = QtWidgets.QLabel(Form)
        self.labelStudyDate.setObjectName("labelStudyDate")
        self.horizontalLayout_5.addWidget(self.labelStudyDate)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.StudyDate = QtWidgets.QDateEdit(Form)
        self.StudyDate.setObjectName("StudyDate")
        self.verticalLayout_5.addWidget(self.StudyDate)
        self.verticalLayout_11.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.labelStudyTime = QtWidgets.QLabel(Form)
        self.labelStudyTime.setObjectName("labelStudyTime")
        self.horizontalLayout_6.addWidget(self.labelStudyTime)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.studyTime = QtWidgets.QTimeEdit(Form)
        self.studyTime.setObjectName("studyTime")
        self.verticalLayout_6.addWidget(self.studyTime)
        self.verticalLayout_11.addLayout(self.verticalLayout_6)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.labelStudyDescr = QtWidgets.QLabel(Form)
        self.labelStudyDescr.setObjectName("labelStudyDescr")
        self.horizontalLayout_9.addWidget(self.labelStudyDescr)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        self.StudyDescr = QtWidgets.QLineEdit(Form)
        self.StudyDescr.setObjectName("StudyDescr")
        self.verticalLayout_9.addWidget(self.StudyDescr)
        self.verticalLayout_11.addLayout(self.verticalLayout_9)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.labelAccessionN = QtWidgets.QLabel(Form)
        self.labelAccessionN.setObjectName("labelAccessionN")
        self.horizontalLayout_11.addWidget(self.labelAccessionN)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)
        self.verticalLayout_12.addLayout(self.horizontalLayout_11)
        self.AccessionN = QtWidgets.QLineEdit(Form)
        self.AccessionN.setObjectName("AccessionN")
        self.verticalLayout_12.addWidget(self.AccessionN)
        self.verticalLayout_11.addLayout(self.verticalLayout_12)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.labelReferPhysi = QtWidgets.QLabel(Form)
        self.labelReferPhysi.setObjectName("labelReferPhysi")
        self.horizontalLayout_10.addWidget(self.labelReferPhysi)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.verticalLayout_10.addLayout(self.horizontalLayout_10)
        self.ReferPhysi = QtWidgets.QLineEdit(Form)
        self.ReferPhysi.setObjectName("ReferPhysi")
        self.verticalLayout_10.addWidget(self.ReferPhysi)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.labelStudyModal = QtWidgets.QLabel(Form)
        self.labelStudyModal.setObjectName("labelStudyModal")
        self.horizontalLayout_12.addWidget(self.labelStudyModal)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem6)
        self.verticalLayout_13.addLayout(self.horizontalLayout_12)
        self.StudyModal = QtWidgets.QLineEdit(Form)
        self.StudyModal.setObjectName("StudyModal")
        self.verticalLayout_13.addWidget(self.StudyModal)
        self.verticalLayout_11.addLayout(self.verticalLayout_13)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 6, -1, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.createButton = QtWidgets.QPushButton(Form)
        self.createButton.setObjectName("createButton")
        self.horizontalLayout.addWidget(self.createButton)
        self.cancelButton = QtWidgets.QPushButton(Form)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_11.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_11, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelPatientID.setText(_translate("Form", "Patient"))
        self.labelStudyDate.setText(_translate("Form", "Date"))
        self.labelStudyTime.setText(_translate("Form", "Time"))
        self.labelStudyDescr.setText(_translate("Form", "Description"))
        self.labelAccessionN.setText(_translate("Form", "Acc. Number"))
        self.labelReferPhysi.setText(_translate("Form", "Phy. Ref"))
        self.labelStudyModal.setText(_translate("Form", "Modality"))
        self.createButton.setText(_translate("Form", "Create"))
        self.cancelButton.setText(_translate("Form", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
