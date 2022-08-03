from datetime import date
from Teacher import teacher
from Student import student
from Course import course   
from Report import report
from Test import test
import pyodbc

class pySQL:
    def __init__(self):
        self.cnxn = pyodbc.connect('*YOUR CONNECTION*')
        self.cursor = self.cnxn.cursor()
        pass

    def Connection(self):
        self.cursor.close()
        self.cnxn = pyodbc.connect('*YOUR CONNECTION*')
        self.cursor = self.cnxn.cursor()

    def Disconnection(self):
        self.cursor.close() #DISCONNECTION
        
    def StudentLogIn(self, user, pwd):
        self.cursor.execute("{CALL PQ_LOG_IN_STUDENT(?,?)} ", user, pwd)
        rset = self.cursor.fetchone()
        self.Connection()
        if rset == None:
            print('No such user and pass\n')
            return None
        else:
            newStd = student()
            newStd.SID = int(rset[0])
            newStd.User = rset[1]
            newStd.Pass = rset[2]
            newStd.FName = rset[3]
            newStd.LName = rset[4]
            newStd.DOB = rset[5]
            newStd.Addr1 = rset[6]
            newStd.Addr2 = rset[7]
            newStd.City = rset[8]
            newStd.State = rset[9]
            newStd.Zip = rset[10]
            newStd.Email = rset[11]
            newStd.PhoneNo = rset[12]
            newStd.GPA = rset[13]
            newStd.Fixed = rset[14]

            return newStd #LOGINSTUDENT
        
    def ModifyStudent(self, modStd):
        args = (modStd.SID, modStd.User, modStd.Pass, modStd.FName, modStd.LName, modStd.DOB, modStd.Addr1, modStd.Addr2, modStd.City, modStd.State, modStd.Zip, modStd.Email, modStd.PhoneNo)
        self.cursor.execute("{CALL PQ_UPDATE_STUDENT(?,?,?,?,?,?,?,?,?,?,?,?,?)}", args)
        self.cnxn.commit()
        self.Connection()

    def ModifyTeacher(self, modTch):
        args = (modTch.TID, modTch.User, modTch.Pass, modTch.FName, modTch.LName, modTch.Email, modTch.Dptmpt, modTch.College, modTch.Subj, modTch.PhoneNo, modTch.Website)
        self.cursor.execute("{CALL PQ_UPDATE_STUDENT(?,?,?,?,?,?,?,?,?,?,?)}", args)
        self.cnxn.commit()
        self.Connection()

    def DeleteStudent(self, SID):
        self.cursor.execute("DELETE FROM STUDENTS WHERE SID = " + SID)
        self.cnxn.commit()
        self.Connection()

    def DeleteTeacher(self, TID):
        self.cursor.execute("DELETE FROM TEACHERS WHERE TID = " + TID)
        self.cnxn.commit()
        self.Connection()

    def AppendNewStudentInfo(self, newStd) -> student:
        self.cursor.execute("{CALL PQ_NEW_SID}")
        rset = self.cursor.fetchone()
        newStd.SID = rset[0]

        args = (newStd.SID, newStd.User, newStd.Pass, newStd.FName, newStd.LName, newStd.DOB, newStd.Addr1, newStd.Addr2, newStd.City, newStd.State, newStd.Zip, newStd.Email, newStd.PhoneNo)
        self.cursor.execute("{CALL PQ_INSERT_STUDENT(?,?,?,?,?,?,?,?,?,?,?,?,?)}", args)
        self.cnxn.commit()

        return newStd #APPENDNEWSTUDENT

    def ViewStudentList(self):
        self.cursor.execute("SELECT * FROM STUDENTS")
        rows = self.cursor.fetchall()
        
        print('SID'.ljust(4, ' ') + 'User'.ljust(10, ' ') + 'Pass'.ljust(10, ' ') + 'Name'.ljust(18, ' ') + 'DOB'.ljust(13, ' ') + 'Addr 1'.ljust(15, ' ') + 'Addr 2'.ljust(10, ' ') + 'City '.ljust(10, ' ') + 'St ' + 'Zip   ' + 'Email'.ljust(30, ' ') + 'Phone'.ljust(13, ' ') + 'GPA'.ljust(5, ' ') + 'Fixed')
        print('---'.ljust(4, ' ') + '----'.ljust(10, ' ') + '----'.ljust(10, ' ') + '----'.ljust(18, ' ') + '---'.ljust(13, ' ') + '------'.ljust(15, ' ') + '------'.ljust(10, ' ') + '---- '.ljust(10, ' ') + '-- ' + '----- ' + '-----'.ljust(30, ' ') + '-----'.ljust(13, ' ') + '---'.ljust(5, ' ') + '-----')
        for row in rows:
            print(str(row[0]).ljust(4, ' ')\
                + row[1].ljust(10, ' ')\
                + row[2].ljust(10, ' ')\
                + (row[3] + ' ' + row[4]).ljust(18, ' ')\
                + row[5].ljust(13, ' ')\
                + row[6].ljust(15, ' ')\
                + row[7].ljust(10, ' ')\
                + row[8].ljust(10, ' ')\
                + row[9].ljust(3, ' ')\
                + row[10] + ' '\
                + row[11].ljust(30, ' ')\
                + row[12].ljust(13, ' ')\
                + str(row[13]).ljust(5, ' ')\
                + str(row[14]))
        print() #VIEWSTUDENTLIST
    
    def JoinCourse(self, CID, SID, time):
        args = (CID, SID, time, "F1", date.today().strftime("%Y"))
        self.cursor.execute("{CALL PQ_JOIN_COURSE(?,?,?,?,?)}", args)
        self.cnxn.commit()
        self.Connection() #JOINCOURSE

    def SelectCoursesSID(self, SID):
        self.cursor.execute("{CALL PQ_SELECT_COURSES_BY_SID(?)}", SID) 
        courses = self.cursor.fetchall()
        self.Connection()

        return courses
    
    def LeaveCourse(self, CID, SID):
        self.cursor.execute("{CALL PQ_LEAVE_COURSE(?, ?)}", CID, SID)
        self.cnxn.commit()
        self.Connection() 

    def GetCategories(self):
        self.cursor.execute("{CALL PQ_GET_CATEGORIES}") 
        categories = self.cursor.fetchall()
        self.Connection()
        
        return categories

    def GetCourses(self, category, sid):
        print((category, sid))
        self.cursor.execute("{CALL PQ_GET_COURSES_IN_CAT(?, ?)}", (category, sid))
        courses = self.cursor.fetchall()
        self.Connection()
        
        return courses
    
    def ViewCoursesStudent(self, SID):
        self.cursor.execute("{CALL PQ_SELECT_COURSES_BY_SID(?)}", SID) 
        courses = self.cursor.fetchall()
        
        i = 1
        for c in courses:
            print('Course ' + str(i) + ': ' + c[1])
            i += 1
        print() #VIEWCOURSES

    def GetStudentCourses(self, SID):
        self.cursor.execute("{CALL PQ_SELECT_COURSES_BY_SID(?)}", SID) 
        courses = self.cursor.fetchall()
        self.Connection()

        return courses

    def GetStudentReports(self, CID, SID):
        self.cursor.execute("{CALL PQ_FIND_REPORT_IN_CID_WITH_SID(?,?)}", (CID, SID)) 
        reportList = self.cursor.fetchall()
        self.Connection()

        return reportList

    def GetStudentReport(self, ReportID, SID):
        self.cursor.execute("{CALL PQ_FIND_REPORT_WITH_SID(?,?)}", (SID, ReportID)) 
        report = self.cursor.fetchall()[0]
        self.Connection()

        return report
                        
    def DoReport(self, ReportId, SID, answer):
        args = (ReportId, SID, answer)
        self.cursor.execute("{CALL PQ_UPDATE_REPORT_ANSWERS(?,?,?)}", args) 
        self.cnxn.commit()
        self.Connection()

    def GetStudentTests(self, CID, SID):
        self.cursor.execute("{CALL PQ_FIND_TEST_IN_CID_WITH_SID(?,?)}", (CID, SID)) 
        testList = self.cursor.fetchall()
        self.Connection()

        return testList

    def GetStudentTest(self, TestID, SID):
        self.cursor.execute("{CALL PQ_FIND_TEST_WITH_SID(?,?)}", (SID, TestID)) 
        test = self.cursor.fetchall()[0]
        self.Connection()

        return test
                        
    def DoTest(self, TestId, SID, answer):
        self.cursor.execute("{CALL PQ_UPDATE_TEST_ANSWERS(?,?,?)}", (TestId, SID, answer)) 
        self.cnxn.commit()
        self.Connection()
    
    def ViewGrades(self, SID):
        self.cursor.execute("{CALL PQ_GET_GRADES(?)}", (SID)) 
        grades = self.cursor.fetchall()
        
        return grades
    
        
        
    def TeacherLogIn(self, user, pwd):
        self.cursor.execute("{CALL PQ_LOG_IN_TEACHER(?,?)}", (user, pwd))
        rset = self.cursor.fetchone()
        self.Connection()
        if rset == None:
            print('No such user and pass\n')
            return None
        else:
            newTch = teacher()
            newTch.TID = rset[0]
            newTch.User = rset[1]
            newTch.Pass = rset[2]
            newTch.FName = rset[3]
            newTch.LName = rset[4]
            newTch.Email = rset[5]
            newTch.Dptmt = rset[6]
            newTch.College = rset[7]
            newTch.Subj = rset[8]
            newTch.PhoneNo = rset[9]
            newTch.Website = rset[10]

            return newTch #LOGINTEACHER

    def AppendNewTeacherInfo(self, newTch):
        self.cursor.execute("{CALL PQ_NEW_TID}")
        rset = self.cursor.fetchone()
        newTch.TID = rset[0]
        
        args = (newTch.TID, newTch.User, newTch.Pass, newTch.FName, newTch.LName, newTch.Email, newTch.Dptmt, newTch.College, newTch.Subj, newTch.PhoneNo, newTch.Website)
        self.cursor.execute("{CALL PQ_INSERT_TEACHER(?,?,?,?,?,?,?,?,?,?,?)}", args)
        self.cnxn.commit()
        self.Connection()

        return newTch #APPENDNEWTEACHER

    def ViewTeacherList(self):
        self.cursor.execute("SELECT * FROM TEACHERS")
        rows = self.cursor.fetchall()
        
        print('SID'.ljust(4, ' ') + 'User'.ljust(10, ' ') + 'Pass'.ljust(10, ' ') + 'Name'.ljust(18, ' ') + 'DOB'.ljust(13, ' ') + 'Addr 1'.ljust(15, ' ') + 'Addr 2'.ljust(10, ' ') + 'City '.ljust(10, ' ') + 'St ' + 'Zip   ' + 'Email'.ljust(30, ' ') + 'Phone'.ljust(13, ' ') + 'GPA'.ljust(5, ' ') + 'Fixed')
        print('---'.ljust(4, ' ') + '----'.ljust(10, ' ') + '----'.ljust(10, ' ') + '----'.ljust(18, ' ') + '---'.ljust(13, ' ') + '------'.ljust(15, ' ') + '------'.ljust(10, ' ') + '---- '.ljust(10, ' ') + '-- ' + '----- ' + '-----'.ljust(30, ' ') + '-----'.ljust(13, ' ') + '---'.ljust(5, ' ') + '-----')
        for row in rows:
            print(str(row[0]).ljust(4, ' ')
                + row[1].ljust(10, ' ')\
                + row[2].ljust(10, ' ')\
                + (row[3] + ' ' + row[4]).ljust(18, ' ')\
                + row[5].ljust(30, ' ')\
                + row[6].ljust(15, ' ')\
                + row[7].ljust(10, ' ')\
                + row[8].ljust(30, ' ')\
                + row[9].ljust(13, ' ')\
                + row[10])
        print() #VIEWTEACHERLIST

    def GetCollegeName(self, CollegeID):
        self.cursor.execute("{CALL PQ_GET_COLLEGENAME_WITH_ID(?)}", CollegeID) 
        name = self.cursor.fetchone()
        self.Connection()
        
        return name

    def GetColleges(self):
        self.cursor.execute("SELECT * FROM COLLEGES") 
        departments = self.cursor.fetchall()
        self.Connection()
        
        return departments

    def AppendCourse(self, TID, newCourse):

        self.cursor.execute("{CALL PQ_NEW_CID}")
        rset = self.cursor.fetchone()
        newCourse.CID = rset[0]
        self.Connection()
        
        args = (newCourse.CID, newCourse.CollegeId, newCourse.ClassName, newCourse.Textbook, newCourse.MaxSize, newCourse.RoomNo, newCourse.Category, newCourse.Time)
        
        self.cursor.execute("{CALL PQ_MAKE_COURSE(?,?,?,?,?,?,?,?)}", args)
        self.cnxn.commit()
        self.Connection()
        self.cursor.execute("{CALL PQ_JOIN_LECTURE(?,?)}", (newCourse.CID, TID))
        self.cnxn.commit() 
        self.Connection() #APPENDCOURSE

    def DeleteCourse(self, CID):
        self.cursor.execute("{CALL PQ_DELETE_COURSES_BY_CID(?)}", CID)
        self.cnxn.commit()
        self.Connection() #DELETECOURSE

    def ViewCoursesTeacher(self, TID):
        self.cursor.execute("{CALL PQ_SELECT_COURSES_BY_TID(?)}", TID)
        courses = self.cursor.fetchall()
        self.Connection()
        return courses #VIEWCOURSES

    def GetSidListInCID(self, CID):
        self.cursor.execute("{CALL PQ_SID_LIST_IN_CID(?)}", CID)
        SIDlist = self.cursor.fetchall()
        self.Connection()

        return SIDlist

    def MakeReport(self, SIDlist, newReport):   
        for SID in SIDlist:
            newReport.SID = SID[0]
            args = (newReport.SID, newReport.TID, newReport.CID, newReport.Title, newReport.Task, newReport.DueDate, newReport.Year)
            print(args)
            self.cursor.execute("{CALL PQ_MAKE_REPORT(?,?,?,?,?,?,?)}", args)
            self.cnxn.commit()
            self.Connection() #MAKEREPORT

    def MakeTest(self, SIDlist, newTest):
        for SID in SIDlist:
            newTest.SID = SID[0]
            args = (newTest.SID, newTest.TID, newTest.CID, newTest.Subj, newTest.Task, newTest.TakeDate, newTest.Year)
            self.cursor.execute("{CALL PQ_MAKE_TEST(?,?,?,?,?,?,?)}", args)
            self.cnxn.commit()
            self.Connection()#MAKETEST


    def ReportList(self, CID):
        self.cursor.execute("{CALL PQ_REPORT_LIST_WITH_CID(?)}", CID)
        reports = self.cursor.fetchall()
        self.Connection()

        return reports

    def TeacherReport(self, ReportTitle):
        self.cursor.execute("{CALL PQ_FIND_REPORTS_WITH_TITLE(?)}", ReportTitle)
        report = self.cursor.fetchall()
        self.Connection()

        return report
        

    def JudgeReport(self, RID, SID, CID, sgrade, prvgrade):
        grade = float(sgrade)

        self.cursor.execute("{CALL PQ_JUDGE_REPORT(?,?)}", (RID, grade))
        self.cnxn.commit()
        self.Connection()
        self.cursor.execute("{CALL PQ_UPDATE_STUDENT_GRADE(?,?,?,?)}", (SID, CID, grade, prvgrade))
        self.cnxn.commit()
        self.Connection()


    def TestList(self, CID):
        self.cursor.execute("{CALL PQ_TEST_LIST_WITH_CID(?)}", CID)
        tests = self.cursor.fetchall()
        self.Connection()

        return tests

    def TeacherTest(self, TestTitle):
        self.cursor.execute("{CALL PQ_FIND_TEST_WITH_TITLE(?)}", TestTitle)
        test = self.cursor.fetchall()
        self.Connection()

        return test
        

    def JudgeTest(self, TTID, SID, CID, sgrade, prvgrade):
        grade = float(sgrade)
        self.cursor.execute("{CALL PQ_JUDGE_TEST(?,?)}", (TTID, grade))
        self.cnxn.commit()
        self.Connection()
        self.cursor.execute("{CALL PQ_UPDATE_STUDENT_GRADE(?,?,?,?)}", (SID, CID, grade, prvgrade))
        self.cnxn.commit()
        self.Connection() #JUDGETEST
