import uuid
from .. import database


class Patient:
    def __init__(self):
        self.init_field()

    def __del__(self):
        self.init_field()

    def init_field(self):
        self.PatientID = ""
        self.PatientNam = ""
        self.PatientBir = ""
        self.PatientSex = ""

    def create(self):
        database.activeDatabase.create("DICOMPatients", {"PatientID": uuid.uuid4().hex,
                                                         "PatientNam": self.PatientNam,
                                                         "PatientBir": self.PatientBir,
                                                         "PatientSex": self.PatientSex})

    def read(self):
        return database.activeDatabase.read("DICOMPatients")

    def browse(self, id):
        record = database.activeDatabase.browse(
            "DICOMPatients", "PatientID", id)
        if record:
            for key, value in record[0].items():
                if key in self.__dict__:
                    setattr(self, key, value or "")
        return record

    def delete(self, id):
        record = database.activeDatabase.delete("DICOMPatients", "PatientID", id)
        if record:
            self.init_field()
        return record