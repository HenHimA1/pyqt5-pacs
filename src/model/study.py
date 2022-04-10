import uuid
from .. import database


class Study:
    StudyInsta = ""
    StudyDate = ""
    StudyTime = ""
    StudyDescr = ""
    AccessionN = ""
    ReferPhysi = ""
    StudyModal = ""
    PatientID = ""

    def create(self):
        database.activeDatabase.create("DICOMStudies", {"StudyInsta": uuid.uuid4().hex,
                                                        "StudyDate": self.StudyDate,
                                                        "StudyTime": self.StudyTime,
                                                        "StudyDescr": self.StudyDescr,
                                                        "AccessionN": self.AccessionN,
                                                        "ReferPhysi": self.ReferPhysi,
                                                        "StudyModal": self.StudyModal,
                                                        "PatientID": self.PatientID})
