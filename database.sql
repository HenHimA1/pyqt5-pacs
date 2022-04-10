BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "DICOMPatients" (
	"PatientID"	varchar(64) NOT NULL,
	"PatientNam"	varchar(64),
	"PatientBir"	char(8),
	"PatientSex"	varchar(16),
	"AccessTime"	int,
	"qTimeStamp"	int,
	"qFlags"	int,
	"qSpare"	varchar(64),
	PRIMARY KEY("PatientID")
);
CREATE TABLE IF NOT EXISTS "DICOMStudies" (
	"StudyInsta"	varchar(64) NOT NULL,
	"StudyDate"	char(8),
	"StudyTime"	varchar(16),
	"StudyID"	varchar(16),
	"StudyDescr"	varchar(64),
	"AccessionN"	varchar(16),
	"ReferPhysi"	varchar(64),
	"PatientsAg"	varchar(16),
	"PatientsWe"	varchar(16),
	"StudyModal"	varchar(64),
	"PatientNam"	varchar(64),
	"PatientBir"	char(8),
	"PatientSex"	varchar(16),
	"PatientID"	varchar(64),
	"AccessTime"	int,
	"qTimeStamp"	int,
	"qFlags"	int,
	"qSpare"	varchar(64),
	PRIMARY KEY("StudyInsta")
);
CREATE TABLE IF NOT EXISTS "DICOMSeries" (
	"SeriesInst"	varchar(64) NOT NULL,
	"SeriesNumb"	varchar(12),
	"SeriesDate"	char(8),
	"SeriesTime"	varchar(16),
	"SeriesDesc"	varchar(64),
	"Modality"	varchar(16),
	"PatientPos"	varchar(16),
	"ContrastBo"	varchar(64),
	"Manufactur"	varchar(64),
	"ModelName"	varchar(64),
	"BodyPartEx"	varchar(64),
	"ProtocolNa"	varchar(64),
	"StationNam"	varchar(16),
	"Institutio"	varchar(64),
	"FrameOfRef"	varchar(64),
	"SeriesPat"	varchar(64),
	"StudyInsta"	varchar(64),
	"AccessTime"	int,
	"qTimeStamp"	int,
	"qFlags"	int,
	"qSpare"	varchar(64),
	PRIMARY KEY("SeriesInst")
);
CREATE TABLE IF NOT EXISTS "DICOMImages" (
	"SOPInstanc"	varchar(64) NOT NULL,
	"SOPClassUI"	varchar(64),
	"ImageNumbe"	varchar(12),
	"ImageDate"	char(8),
	"ImageTime"	varchar(16),
	"EchoNumber"	varchar(64),
	"NumberOfFr"	varchar(12),
	"AcqDate"	char(8),
	"AcqTime"	varchar(16),
	"ReceivingC"	varchar(16),
	"AcqNumber"	varchar(12),
	"SliceLocat"	varchar(16),
	"SamplesPer"	varchar(5),
	"PhotoMetri"	varchar(16),
	"QRows"	varchar(5),
	"QColumns"	varchar(5),
	"BitsStored"	varchar(5),
	"ImageType"	varchar(128),
	"ImageID"	varchar(16),
	"ImagePat"	varchar(64),
	"SeriesInst"	varchar(64),
	"AccessTime"	int,
	"qTimeStamp"	int,
	"qFlags"	int,
	"qSpare"	varchar(64),
	"ObjectFile"	varchar(255),
	"DeviceName"	varchar(32),
	PRIMARY KEY("SOPInstanc")
);
CREATE TABLE IF NOT EXISTS "UIDMODS" (
	"MODTime"	int,
	"OldUID"	varchar(64),
	"MODType"	varchar(32),
	"NewUID"	varchar(64),
	"Stage"	varchar(32),
	"Annotation"	varchar(64)
);
CREATE TABLE IF NOT EXISTS "DICOMWorkList" (
	"AccessionN"	varchar(16),
	"PatientID"	varchar(64),
	"PatientNam"	varchar(64),
	"PatientBir"	char(8),
	"PatientSex"	varchar(16),
	"MedicalAle"	varchar(64),
	"ContrastAl"	varchar(64),
	"StudyInsta"	varchar(64),
	"ReqPhysici"	varchar(64),
	"ReqProcDes"	varchar(64),
	"Modality"	varchar(16),
	"ReqContras"	varchar(64),
	"ScheduledA"	varchar(16),
	"StartDate"	char(8),
	"StartTime"	varchar(16),
	"PerfPhysic"	varchar(64),
	"SchedPSDes"	varchar(64),
	"SchedPSID"	varchar(16),
	"SchedStati"	varchar(16),
	"SchedPSLoc"	varchar(16),
	"PreMedicat"	varchar(64),
	"SchedPSCom"	varchar(64),
	"ReqProcID"	varchar(16),
	"ReqProcPri"	varchar(16),
	"AccessTime"	int,
	"qTimeStamp"	int,
	"qFlags"	int,
	"qSpare"	varchar(64)
);
CREATE INDEX IF NOT EXISTS "study_lnk" ON "DICOMStudies" (
	"PatientID"
);
CREATE INDEX IF NOT EXISTS "idx_patientid" ON "DICOMStudies" (
	"PatientSex"
);
CREATE INDEX IF NOT EXISTS "idx_patientid_studyinsta" ON "DICOMStudies" (
	"PatientSex",
	"PatientID"
);
CREATE INDEX IF NOT EXISTS "series_lnk" ON "DICOMSeries" (
	"StudyInsta"
);
CREATE INDEX IF NOT EXISTS "series_pat" ON "DICOMSeries" (
	"SeriesPat"
);
CREATE INDEX IF NOT EXISTS "idx_studyinsta_seriesinst" ON "DICOMStudies" (
	"PatientID",
	"StudyInsta"
);
CREATE INDEX IF NOT EXISTS "images_lnk" ON "DICOMImages" (
	"SeriesInst"
);
CREATE INDEX IF NOT EXISTS "images_pat" ON "DICOMImages" (
	"ImagePat"
);
CREATE INDEX IF NOT EXISTS "mods_old" ON "UIDMODS" (
	"OldUID"
);
CREATE INDEX IF NOT EXISTS "mods_stage" ON "UIDMODS" (
	"Stage"
);
CREATE INDEX IF NOT EXISTS "mods_joint" ON "UIDMODS" (
	"OldUID",
	"Stage"
);
CREATE INDEX IF NOT EXISTS "mods_back" ON "UIDMODS" (
	"NewUID",
	"Stage"
);
COMMIT;
