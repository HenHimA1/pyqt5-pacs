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
        records = database.activeDatabase.read("DICOMPatients")
        items = []
        for record in records:
            item = {}
            for key, value in record.items():
                if key in self.__dict__:
                    item[key] = value or ""
            items.append(item)
        return items

    def browse(self, id):
        record = database.activeDatabase.browse(
            "DICOMPatients", "PatientID", id)
        if record:
            for key, value in record[0].items():
                if key in self.__dict__:
                    setattr(self, key, value or "")
        return record

    def delete(self, id):
        record = database.activeDatabase.delete(
            "DICOMPatients", "PatientID", id)
        if record:
            self.init_field()
        return record

    def update(self):
        record = database.activeDatabase.update("DICOMPatients", "PatientID", self.PatientID, {"PatientNam": self.PatientNam,
                                                                                               "PatientBir": self.PatientBir,
                                                                                               "PatientSex": self.PatientSex})
        # if record:
        #     self.init_field()
        return record
