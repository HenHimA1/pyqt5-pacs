import uuid
from .. import database


class Study:
    def __init__(self):
        self.init_field()

    def init_field(self):
        self.StudyInsta = ""
        self.StudyDate = ""
        self.StudyTime = ""
        self.StudyDescr = ""
        self.AccessionN = ""
        self.ReferPhysi = ""
        self.StudyModal = ""
        self.PatientID = ""

    def create(self):
        database.activeDatabase.create("DICOMStudies", {"StudyInsta": uuid.uuid4().hex,
                                                        "StudyDate": self.StudyDate,
                                                        "StudyTime": self.StudyTime,
                                                        "StudyDescr": self.StudyDescr,
                                                        "AccessionN": self.AccessionN,
                                                        "ReferPhysi": self.ReferPhysi,
                                                        "StudyModal": self.StudyModal,
                                                        "PatientID": self.PatientID})

    def read(self):
        records = database.activeDatabase.read("DICOMStudies")
        items = []
        for record in records:
            item = {}
            for key, value in record.items():
                if key in self.__dict__:
                    item[key] = value or ""
            items.append(item)
        return items
