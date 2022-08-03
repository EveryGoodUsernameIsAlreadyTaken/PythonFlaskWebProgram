USE SCHOOLPYDB;

DROP TABLE REPORTS;
DROP TABLE TESTS;
DROP TABLE LECTURES;
DROP TABLE COURSEHIST;
DROP TABLE COURSES;
DROP TABLE COLLEGES;
DROP TABLE TEACHERS;
DROP TABLE STUDENTS;

CREATE TABLE STUDENTS(
	SID			INT PRIMARY KEY NOT NULL,
	USERNAME	VARCHAR(30) NOT NULL,
	PASSWORD	VARCHAR(30) NOT NULL, 
	FIRSTNAME	VARCHAR(30) NOT NULL DEFAULT(''),
	LASTNAME	VARCHAR(30) NOT NULL DEFAULT(''),
	DOB			VARCHAR(10) NOT NULL,
	ADDR1		VARCHAR(30) NOT NULL,
	ADDR2		VARCHAR(30),
	CITY		VARCHAR(30) NOT NULL,
	ST			VARCHAR(2) NOT NULL,
	ZIP			VARCHAR(5) NOT NULL,
	EMAIL		VARCHAR(30) NOT NULL,
	PHONENO		VARCHAR(15)	NOT NULL,
	GPA			DECIMAL(3,2) NOT NULL DEFAULT(0.0),
	FIXED		BIT
);

CREATE TABLE TEACHERS(
	TID			INT PRIMARY KEY NOT NULL,
	USERNAME	VARCHAR(30) NOT NULL,
	PASSWORD	VARCHAR(30) NOT NULL,
	FIRSTNAME	VARCHAR(30) NOT NULL DEFAULT(''),
	LASTNAME	VARCHAR(30) NOT NULL DEFAULT(''),
	EMAIL		VARCHAR(30) NOT NULL,
	DEPARTMENT	VARCHAR(30)	NOT NULL,
	COLLEGE		VARCHAR(30)	NOT NULL,
	SUBJECTS	VARCHAR(30)	NOT NULL,
	PHONENO		VARCHAR(15)	NOT NULL,
	WEBSITE		VARCHAR(30)	NOT NULL
);

CREATE TABLE COLLEGES(
	COLLEGEID	INT NOT NULL,
	NAME		VARCHAR(30)	NOT NULL,
    PRIMARY KEY (COLLEGEID)
);

/*
INSERT INTO COLLEGES VALUES(1, 'HUMANITIES');
INSERT INTO COLLEGES VALUES(2, 'SCIENCES');
INSERT INTO COLLEGES VALUES(3, 'ENGINEERING');
INSERT INTO COLLEGES VALUES(4, 'MEDICAL');
INSERT INTO COLLEGES VALUES(5, 'MATHEMATICS');
INSERT INTO COLLEGES VALUES(6, 'BIOLOGY');
INSERT INTO COLLEGES VALUES(7, 'CHEMISTRY');
INSERT INTO COLLEGES VALUES(8, 'ATHLETICS');
INSERT INTO COLLEGES VALUES(9, 'COMPUTER');
INSERT INTO COLLEGES VALUES(10, 'ECONOMIES');
*/

CREATE TABLE COURSES(
	CID			INT NOT NULL,
	COLLEGEID	INT NOT NULL,
	CLASSNAME	VARCHAR(30) NOT NULL,
	TEXTBOOK	VARCHAR(30),
	MAXSIZE		INT NOT NULL,
	CURSIZE		INT NOT NULL,
	ROOMNO		INT NOT NULL,
	CATEGORY	VARCHAR(20) NOT NULL,
	TIME		VARCHAR(20) NOT NULL,
    PRIMARY KEY(CID),
    FOREIGN KEY (COLLEGEID) REFERENCES COLLEGES(COLLEGEID)
);

CREATE TABLE COURSEHIST(
	CID			INT NOT NULL,
	SID			INT NOT NULL,
	POINTS		DECIMAL(8,2) NOT NULL DEFAULT(0.0),
	TIME		VARCHAR(20) NOT NULL,
	WGRADE		VARCHAR(2) NOT NULL,
	YEAR		INT NOT NULL,
	WORKDONE	INT NOT NULL,
    FOREIGN KEY (CID) REFERENCES COURSES (CID) ON DELETE CASCADE,
	FOREIGN KEY (SID) REFERENCES STUDENTS (SID) ON DELETE CASCADE
);

CREATE TABLE LECTURES(
	CID			INT NOT NULL,
	TID			INT NOT NULL,
	PRIMARY KEY (CID,  TID),
    FOREIGN KEY (CID) REFERENCES COURSES (CID) ON DELETE CASCADE,
    FOREIGN KEY (TID) REFERENCES TEACHERS (TID) ON DELETE CASCADE
);

CREATE TABLE REPORTS(
	REPORTID	INT	NOT NULL,
	SID			INT NOT NULL,
	TID			INT NOT NULL,
	CID			INT NOT NULL,
	TITLE		VARCHAR(30) NOT NULL,
	TASK		VARCHAR(200) NOT NULL,
	ANSWERS		VARCHAR(1000) NOT NULL,
	DUEDATE		VARCHAR(10) NOT NULL,
	GRADE		DECIMAL NOT NULL DEFAULT(0.0),
	YEAR		INT  NOT NULL,
	FINISHED	BIT NOT NULL,
	GRADED		BIT NOT NULL,
    PRIMARY KEY (REPORTID),
	FOREIGN KEY (SID) REFERENCES STUDENTS (SID) ON DELETE CASCADE,
	FOREIGN KEY (TID) REFERENCES TEACHERS (TID) ON DELETE CASCADE,
	FOREIGN KEY (CID) REFERENCES COURSES (CID)
);

CREATE TABLE TESTS(
	TESTID		INT	NOT NULL,
	SID			INT NOT NULL,
	TID			INT NOT NULL,
	CID			INT NOT NULL,
	SUBJECT		VARCHAR(30) NOT NULL,
	TASK		VARCHAR(200) NOT NULL,
	ANSWERS		VARCHAR(1000) NOT NULL,
	TAKEDATE	VARCHAR(10) NOT NULL,
	GRADE		DECIMAL NOT NULL DEFAULT(0.0),
	YEAR		INT  NOT NULL,
	FINISHED	BIT NOT NULL,
	GRADED		BIT NOT NULL,
    PRIMARY KEY (TESTID),
	FOREIGN KEY (SID) REFERENCES STUDENTS (SID) ON DELETE CASCADE,
	FOREIGN KEY (TID) REFERENCES TEACHERS (TID) ON DELETE CASCADE,
	FOREIGN KEY (CID) REFERENCES COURSES (CID)
);