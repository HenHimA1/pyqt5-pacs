import uuid
from .. import database


class Patient:
    PatientID = ""
    PatientNam = ""
    PatientBir = ""
    PatientSex = ""

    def create(self):
        database.activeDatabase.create("DICOMPatients", {"PatientID": uuid.uuid4().hex,
                                                         "PatientNam": self.PatientNam,
                                                         "PatientBir": self.PatientBir,
                                                         "PatientSex": self.PatientSex})
