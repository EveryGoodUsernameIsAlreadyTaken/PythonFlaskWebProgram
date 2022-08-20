from math import comb, fabs
from msilib.schema import ComboBox, ListBox
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from turtle import st
from pysql import pySQL
from Student import student
from Teacher import teacher
from Course import course   
from Report import report
from Test import test
from datetime import date
import time

sql = pySQL()
curStudent = student()
curTeacher = teacher()
root = Tk()

root.title("Joe Gui")
root.geometry("800x600+300+50")
root.resizable(False, False)

topLabel = Label(root, text = "Login", font = ("Times New Roman", 20, "bold"))
topLabel.pack(side="top")

def loginpage():      
    topLabel.config(text = "Login")

    frame = Frame(root,relief="solid", bd = 4, width = 600, height = 350)
    frame.pack()                
    frame.pack_propagate(0)
    
    Label(frame, text="\nUsername").pack()
    username_login_entry = Entry(frame, textvariable="username")
    username_login_entry.pack()
    Label(frame, text="\nPassword\n").pack()
    password__login_entry = Entry(frame, textvariable="password", show= '*')
    password__login_entry.pack()

    selected = StringVar()
    r1 = ttk.Radiobutton(frame, text='Student', value='Student', variable=selected)
    r1.pack(padx = 5, pady= 5)
    r2 = ttk.Radiobutton(frame, text='Teacher', value='Teacher', variable=selected) 
    r2.pack(padx = 5, pady= 5)

    def loginbtn():
        username = username_login_entry.get()
        password = password__login_entry.get()         
        if selected.get() == 'Student':
            global curStudent
            result = sql.StudentLogIn(username, password)
            if result == None:
                msgbox.showwarning("Warning", "No such username and password")
            else:                                                
                msgbox.showinfo("Alarm", "Successful sign in")
                curStudent = result
                frame.pack_forget()
                student_home_page()
        elif selected.get() == 'Teacher':
            global curTeacher
            result = sql.TeacherLogIn(username, password)
            if result == None:                               
                msgbox.showwarning("Warning", "No such username and password")
            else:                                                
                msgbox.showinfo("Alarm", "Successful sign in")
                curTeacher = result
                frame.pack_forget()
                teacher_home_page()
            
    def registerbtn():
        frame.pack_forget()
        registerpage()

    Button(frame, text="Login", width=10, height=1, command= loginbtn).pack(pady=5)       
    Button(frame, text="Register", width=10, height=1, command = registerbtn).pack(pady=5)  
                  
def registerpage():       
    topLabel.config(text = "Register")
    tabsystem = ttk.Notebook(root)
                                      
    studenttab = Frame(tabsystem,relief="solid", bd = 4)
    teachertab = Frame(tabsystem,relief="solid", bd = 4)

    tabsystem.add(studenttab, text='Student')
    tabsystem.add(teachertab, text='Teacher')
    tabsystem.pack(fill="both", expand = True)

    def filltab1():
        leftframe = Frame(studenttab)
        leftframe.grid(row = 0, column = 0, sticky=N+S+E+W)
        rightframe = Frame(studenttab)
        rightframe.grid(row = 0, column = 1, sticky=N+S+E+W)
        bottomframe = Frame(studenttab)
        bottomframe.grid(row = 1, columnspan = 2, sticky=E+W)
        
        studenttab.columnconfigure(tuple(range(2)), weight=1)
        studenttab.rowconfigure(tuple(range(2)), weight=1)

        Label(leftframe, text="\nUsername").pack()
        user = Entry(leftframe)
        user.pack(ipadx = 30, ipady = 6)
        Label(rightframe, text="\nPassword").pack()
        pwd = Entry(rightframe, show= '*')
        pwd.pack(ipadx = 30, ipady = 6)
        Label(leftframe, text="\nFirstname").pack()
        fname = Entry(leftframe)
        fname.pack(ipadx = 30, ipady = 6)
        Label(rightframe, text="\nLastname").pack()
        lname = Entry(rightframe)
        lname.pack(ipadx = 30, ipady = 6)
        Label(leftframe, text="\nDate of Birth").pack()
        dob = Entry(leftframe)
        dob.pack(ipadx = 30, ipady = 6)
        Label(rightframe, text="\nAddress 1").pack()
        addr1 = Entry(rightframe)
        addr1.pack(ipadx = 30, ipady = 6)
        Label(leftframe, text="\nAddress 2").pack()
        addr2 = Entry(leftframe)
        addr2.pack(ipadx = 30, ipady = 6)
        Label(rightframe, text="\nCity").pack()
        city = Entry(rightframe)
        city.pack(ipadx = 30, ipady = 6)

        Label(leftframe, text="\nState").pack()
        states = ("AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY")

        combobox = ttk.Combobox(leftframe, values = states, height = 7)
        combobox.set(states[0])
        combobox.pack(ipadx = 30, ipady = 6)

        Label(rightframe, text="\nZip").pack()
        zipNo = Entry(rightframe)
        zipNo.pack(ipadx = 30, ipady = 6)
        Label(leftframe, text="\nEmail").pack()
        email = Entry(leftframe)
        email.pack(ipadx = 30, ipady = 6)
        Label(rightframe, text="\nPhoneNo").pack()
        phoneno = Entry(rightframe)
        phoneno.pack(ipadx = 30, ipady = 6)
        
        def registerbtn():
            global curStudent
            curStudent.User = user.get()
            if len(curStudent.User) == 0:
                msgbox.showwarning("Warning", "Username cannot be empty")
                return

            curStudent.Pass = pwd.get()
            if len(curStudent.Pass) == 0:
                msgbox.showwarning("Warning", "Password cannot be empty")
                return

            curStudent.FName = fname.get()
            if len(curStudent.FName) == 0:
                msgbox.showwarning("Warning", "Firstname cannot be empty")
                return

            curStudent.LName = lname.get()
            if len(curStudent.LName) == 0:
                msgbox.showwarning("Warning", "Lastname cannot be empty")
                return

            curStudent.DOB = dob.get()
            if len(curStudent.DOB) == 0:
                msgbox.showwarning("Warning", "Please write your date of birth")
                return

            curStudent.Addr1 = addr1.get()
            if len(curStudent.Addr1) == 0:
                msgbox.showwarning("Warning", "Address1 cannot be empty")
                return

            curStudent.Addr2 = addr2.get()

            curStudent.City = city.get()
            if len(curStudent.City) == 0:
                msgbox.showwarning("Warning", "City cannot be empty")
                return

            curStudent.State = combobox.get()
            if len(curStudent.State) == 0:
                msgbox.showwarning("Warning", "State cannot be empty")
                return

            curStudent.Zip = zipNo.get()
            if len(curStudent.Zip) == 0:
                msgbox.showwarning("Warning", "Zip cannot be empty")
                return

            curStudent.Email = email.get()
            if len(curStudent.Email) == 0:
                msgbox.showwarning("Warning", "Email cannot be empty")
                return

            curStudent.PhoneNo = phoneno.get()
            if len(curStudent.PhoneNo) == 0:
                msgbox.showwarning("Warning", "Phone number cannot be empty")
                return

            curStudent = sql.RegisterStudent(curStudent)             
            msgbox.showinfo("Alarm", "Successful sign up!")
            frame.pack_forget()
            student_home_page()
            
        def loginbtn():
            tabsystem.pack_forget()
            loginpage()

        Button(bottomframe, text="Register", width=10, height=1, command = registerbtn).pack(pady=5)  
        Button(bottomframe, text="Login", width=10, height=1, command= loginbtn).pack(pady=5)       

    def filltab2():
        leftframe = Frame(teachertab)
        leftframe.grid(row = 0, column = 0, sticky=N+S+E+W)
        rightframe = Frame(teachertab)
        rightframe.grid(row = 0, column = 1, sticky=N+S+E+W)
        bottomframe = Frame(teachertab)
        bottomframe.grid(row = 1, columnspan = 2, sticky=E+W)
        
        teachertab.columnconfigure(tuple(range(2)), weight=1)
        teachertab.rowconfigure(tuple(range(2)), weight=1)

        Label(leftframe, text="\nUsername").pack()
        user = Entry(leftframe)
        user.pack(ipadx = 30, ipady = 6)
        Label(rightframe, text="\nPassword").pack()
        pwd = Entry(rightframe, show= '*')
        pwd.pack(ipadx = 30, ipady = 6)
        Label(leftframe, text="\nFirstname").pack()
        fname = Entry(leftframe)
        fname.pack(ipadx = 30, ipady = 6)
        Label(rightframe, text="\nLastname").pack()
        lname = Entry(rightframe)
        lname.pack(ipadx = 30, ipady = 6)
        Label(leftframe, text="\nEmail").pack()
        email = Entry(leftframe)
        email.pack(ipadx = 30, ipady = 6)

        Label(rightframe, text="\nDepartment").pack()
        departments = sql.GetColleges()
        values = list(i[1] for i in departments)
        combobox = ttk.Combobox(rightframe, values = values, height = 5)
        combobox.pack(ipadx = 30, ipady = 6)

        Label(leftframe, text="\nCollege").pack()
        college = Entry(leftframe)
        college.pack(ipadx = 30, ipady = 6)

        Label(rightframe, text="\nSubjects").pack()
        subj = Entry(rightframe)
        subj.pack(ipadx = 30, ipady = 6)

        Label(leftframe, text="\nPhoneNo").pack()
        phoneno = Entry(leftframe)
        phoneno.pack(ipadx = 30, ipady = 6)

        Label(rightframe, text="\nWebsite").pack()
        website = Entry(rightframe)
        website.pack(ipadx = 30, ipady = 6)
        
        def registerbtn():
            global curTeacher
            curTeacher.User = user.get()
            if len(curStudent.User) == 0:
                msgbox.showwarning("Warning", "Username cannot be empty")
                return

            curTeacher.Pass = pwd.get()
            if len(curStudent.Pass) == 0:
                msgbox.showwarning("Warning", "Password cannot be empty")
                return

            curTeacher.FName = fname.get()
            if len(curStudent.FName) == 0:
                msgbox.showwarning("Warning", "Firstname cannot be empty")
                return

            curTeacher.LName = lname.get()
            if len(curStudent.LName) == 0:
                msgbox.showwarning("Warning", "Lastname cannot be empty")
                return

            curTeacher.Email = email.get()
            if len(curTeacher.Email) == 0:
                msgbox.showwarning("Warning", "Email cannot be empty")
                return

            curTeacher.Dptmt = combobox.get()
            if len(curTeacher.Dptmt) == 0:
                msgbox.showwarning("Warning", "Please choose your department")
                return

            curTeacher.College = college.get()
            if len(curTeacher.College) == 0:
                msgbox.showwarning("Warning", "College cannot be empty")
                return

            curTeacher.Subj = subj.get()
            if len(curTeacher.Subj) == 0:
                msgbox.showwarning("Warning", "Subjects cannot be empty")
                return
            
            curTeacher.PhoneNo = phoneno.get()
            if len(curTeacher.PhoneNo) == 0:
                msgbox.showwarning("Warning", "Phone number cannot be empty")
                return

            curTeacher.Website = website.get()
            if len(curTeacher.Website) == 0:
                msgbox.showwarning("Warning", "Website cannot be empty")
                return

            curTeacher = sql.RegisterTeacher(curTeacher)             
            msgbox.showinfo("Alarm", "Successful sign up!")
            frame.pack_forget()
            teacher_home_page()
            
        def loginbtn():
            frame.pack_forget()
            loginpage()

        Button(bottomframe, text="Register", width=10, height=1, command = registerbtn).pack(pady=5)  
        Button(bottomframe, text="Login", width=10, height=1, command= loginbtn).pack(pady=5)    

    filltab1()
    filltab2()

    # Students
def student_menu(a):
    topbar = Frame(root, relief="solid", bd = 1)
    topbar.pack(side = "top", fill="x")
    
    
    Button(topbar, text="Home", width=14, height=1, command = lambda : (topbar.pack_forget(), a.pack_forget(), student_home_page())).pack(side="left", pady=5) 
    Button(topbar, text="Explore Courses", width=14, height=1, command = lambda : (topbar.pack_forget(), a.pack_forget(), student_explore_courses())).pack(side="left", pady=5) 
    Button(topbar, text="Your Courses", width=14, height=1, command = lambda : (topbar.pack_forget(), a.pack_forget(), student_courses())).pack(side="left", pady=5) 
    Button(topbar, text="Reports", width=14, height=1, command = lambda : (topbar.pack_forget(), a.pack_forget(), student_reports())).pack(side="left", pady=5) 
    Button(topbar, text="Tests", width=14, height=1, command = lambda : (topbar.pack_forget(), a.pack_forget(), student_tests())).pack(side="left", pady=5) 
    Button(topbar, text="View Grades", width=14, height=1, command = lambda : (topbar.pack_forget(), a.pack_forget(), student_grades())).pack(side="left", pady=5) 


    options = ["View Info", "Modify", "Delete", "Log Out"]

    def select_options():
        if var.get() == options[0]:
            topbar.pack_forget()
            a.pack_forget()
            student_view()
        elif var.get() == options[1]:
            topbar.pack_forget()
            a.pack_forget()
            student_modify()
        elif var.get() == options[2]:
            topbar.pack_forget()
            if msgbox.askyesno("Delete", "Are you sure you want to delete?"):
                student_delete()
        elif var.get() == options[3]:
            topbar.pack_forget()
            a.pack_forget()
            logout()
            
    var = StringVar()
    menubutton = Menubutton(topbar, text="Profile", borderwidth=1, relief="raised", width=14, height=1)
    menu = Menu(menubutton, tearoff=False)
    menubutton.configure(menu=menu)
    for option in options:
        menu.add_radiobutton(label=option, variable=var, value=option, command = select_options)
    menubutton.pack(side="right")

def student_home_page():
    topLabel.config(text = "Home")

    global curStudent
    frame = Frame(root, relief="solid", bd = 1)
    student_menu(frame)
    frame.pack(fill = BOTH, expand = True)

def student_explore_courses():
    topLabel.config(text = "Explore Courses")

    global curStudent
    frame = Frame(root, relief="solid", bd = 1)
    student_menu(frame)
    frame.pack(fill = BOTH, expand = True)

    left_frame = Frame(frame, relief="solid", bd = 3)
    left_frame.grid(rowspan=2, column = 0, sticky = N+S+W+E)
    tr_frame = Frame(frame, relief="solid", bd = 3)
    tr_frame.grid(row=0, column = 1, sticky = N+S+W+E)
    br_frame = Frame(frame, relief="solid", bd = 3)
    br_frame.grid(row=1, column = 1, sticky = N+S+W+E)

    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=5)
    frame.rowconfigure(tuple(range(2)), weight=1)

    Label(left_frame, text="Categories").pack()

    info = sql.GetCategories()
    categories = list(i[0] for i in info)
    variable = StringVar()
    variable.set(categories[0])

    listbox = Listbox(tr_frame, bd = 3)
    scrollbar = Scrollbar(tr_frame, command = listbox.yview)
    listbox.pack(side = LEFT, fill = BOTH, expand = True, padx = 20, pady = 10)
    scrollbar.pack(side = RIGHT, fill = BOTH)

    def choose_cat_btn(selection):
        info = sql.GetCourses(selection, curStudent.SID)
        dt = dict()

        for i in info:
            listbox.insert(END, "Course ID: " + "{:5d}".format(i[0]) + " |       " + i[2])
            dt[i[0]] = i
            
        listbox.config(yscrollcommand = scrollbar.set)
        
        def callback(event):
            sel = event.widget.curselection()
            if sel:
                index = sel[0]
                data = str(event.widget.get(index))
                CID = int(data[11:16])
                Label(br_frame, text = data[25:]).grid(row = 0, column = 0, sticky = W+E)

                Label(br_frame, text = "Textbook").grid(row = 1, column = 0, sticky = W+E)
                Label(br_frame, text = "Size").grid(row = 1, column = 1, sticky = W+E)
                Label(br_frame, text = "Room Number").grid(row = 1, column = 2, sticky = W+E)
                Label(br_frame, text = "Time").grid(row = 1, column = 3, sticky = W+E)

                Label(br_frame, text = str(dt[CID][3])).grid(row = 2, column = 0, sticky = W+E)
                Label(br_frame, text = str(dt[CID][5])+"/"+str(dt[CID][4])).grid(row = 2, column = 1, sticky = W+E)
                Label(br_frame, text = str(dt[CID][6])).grid(row = 2, column = 2, sticky = W+E)
                Label(br_frame, text = dt[CID][8]).grid(row = 2, column = 3, sticky = W+E)

                button_frame = Frame(br_frame)
                button_frame.grid(row = 3, columnspan = 4)

                def clear_br():
                    for widget in br_frame.winfo_children():
                        widget.destroy()

                Button(button_frame, text = "JOIN", relief = "raised", bg = "blue", 
                       command = lambda : (
                            sql.JoinCourse(CID,curStudent.SID, dt[CID][8], date.today().year),
                            msgbox.showinfo("Join Course", "Succesfully Joined Course!"),
                            listbox.delete(0, END),
                            clear_br(),
                            choose_cat_btn(selection))
                       ).grid(row =3, columnspan = 4, sticky = N+S+W+E)
                br_frame.columnconfigure(tuple(range(4)), weight=1)
                br_frame.rowconfigure(tuple(range(3)), weight=1)
                br_frame.rowconfigure(3, weight=5)

        listbox.bind("<<ListboxSelect>>", callback)

    OptionMenu(left_frame, variable, *categories, command=choose_cat_btn).pack(side = TOP, pady = 20)
        
def student_courses():
    topLabel.config(text = "Your Courses")

    global curStudent
    frame = Frame(root, relief="solid", bd = 1)
    student_menu(frame)
    frame.pack(fill = BOTH, expand = True)
    
    def inCourse():
        Label(frame, relief = "solid", bd = 1).grid(row = 0, column = 0, sticky = S+W+E)
        Label(frame, text = "Classname", relief = "solid", bd = 1).grid(row = 0, column = 1, sticky = S+W+E)
        Label(frame, text = "Textbook", relief = "solid", bd = 1).grid(row = 0, column = 2, sticky = S+W+E)
        Label(frame, text = "Size", relief = "solid", bd = 1).grid(row = 0, column = 3, sticky = S+W+E)
        Label(frame, text = "Room Number", relief = "solid", bd = 1).grid(row = 0, column = 4, sticky = S+W+E)
        Label(frame, text = "Time", relief = "solid", bd = 1).grid(row = 0, column = 5, sticky = S+W+E)

        courses = sql.StudentCourses(curStudent.SID)

        def drop_course(CID):
            if msgbox.askyesno("Drop", "Are you sure you want to drop?"):
                sql.LeaveCourse(curStudent.SID, CID)
                for widget in frame.winfo_children():
                    widget.destroy()
                inCourse()

        for i, course in enumerate(courses):
            Button(frame, text = "Drop Course", command = lambda : drop_course(course[0])).grid(row = i+1, column = 0, pady = 1)
            Label(frame, text = course[2]).grid(row = i+1, column = 1, sticky = W+E, pady = 1)
            Label(frame, text = course[3]).grid(row = i+1, column = 2, sticky = W+E, pady = 1)
            Label(frame, text = str(course[5])+"/"+str(course[4])).grid(row = i+1, column = 3, sticky = W+E, pady = 1)
            Label(frame, text = str(course[6])).grid(row = i+1, column = 4, sticky = W+E, pady = 1)
            Label(frame, text = course[8]).grid(row = i+1, column = 5, sticky = W+E, pady = 1)

        frame.columnconfigure(0, weight=2)
        frame.columnconfigure(1, weight=6)
        frame.columnconfigure(2, weight=4)
        frame.columnconfigure(3, weight=1)
        frame.columnconfigure(4, weight=2)
        frame.columnconfigure(5, weight=1)

    inCourse()

def student_reports():
    topLabel.config(text = "Reports")

    global curStudent
    frame = Frame(root, relief="solid", bd = 1)
    student_menu(frame)
    frame.pack(fill = BOTH, expand = True)
    
    def inCourse():
        Label(frame, relief = "solid", bd = 1).grid(row = 0, column = 0, sticky = S+W+E)
        Label(frame, text = "Classname", relief = "solid", bd = 1).grid(row = 0, column = 1, sticky = S+W+E)
        Label(frame, text = "Textbook", relief = "solid", bd = 1).grid(row = 0, column = 2, sticky = S+W+E)
        Label(frame, text = "Size", relief = "solid", bd = 1).grid(row = 0, column = 3, sticky = S+W+E)
        Label(frame, text = "Room Number", relief = "solid", bd = 1).grid(row = 0, column = 4, sticky = S+W+E)
        Label(frame, text = "Time", relief = "solid", bd = 1).grid(row = 0, column = 5, sticky = S+W+E)

        courses = sql.StudentCourses(curStudent.SID)
        
        def report_list(CID):
            for widget in frame.winfo_children():
                widget.destroy()
            
            f = Frame(frame, padx=50)
            f.pack(fill=BOTH, expand = True)
            reports = sql.GetStudentReports(CID, curStudent.SID)

            def do_report(report):
                reportframe = Frame(frame)
                reportframe.pack(side = TOP, fill=BOTH, expand = True)

                Label(reportframe, text="\n"+"Report Title\n"+ report[4]).pack()
                Label(reportframe, text="\n"+"Report Task\n"+ report[5]).pack()

                Label(reportframe, text="\n"+"Answer").pack()
                reportanswer = Text(reportframe, height = 10, width = 40)
                reportanswer.pack(expand = True)

                def report_submit():
                    sql.DoReport(report[0], curStudent.SID, reportanswer.get("1.0",'end-1c'))
                    report_list(CID)

                Button(reportframe, text = "Submit", command = lambda : (reportframe.pack_forget(), report_submit())).pack(pady = 1)

            Label(f, text = "Report").grid(row = 0, column = 0, sticky = W+E, pady = 1)
            Label(f, text = "Task").grid(row = 0, column = 1, sticky = W+E, pady = 1)
            for i, report in enumerate(reports):
                Button(f, text = "Do Report", command = lambda : (f.pack_forget(), do_report(report))).grid(row = i+1, column = 0, pady = 1)
                Label(f, text = report[5]).grid(row = i+1, column = 1, sticky = W+E, pady = 1)
            f.columnconfigure(0, weight=1)
            f.columnconfigure(1, weight=3)
            
        for i, course in enumerate(courses):
            def rptlist(cid = course[0]):
                report_list(cid)
            Button(frame, text = "Do Reports", command = rptlist).grid(row = i+1, column = 0, pady = 1)
            Label(frame, text = course[2]).grid(row = i+1, column = 1, sticky = W+E, pady = 1)
            Label(frame, text = course[3]).grid(row = i+1, column = 2, sticky = W+E, pady = 1)
            Label(frame, text = str(course[5]) + "/" + str(course[4])).grid(row = i+1, column = 3, sticky = W+E, pady = 1)
            Label(frame, text = str(course[6])).grid(row = i+1, column = 4, sticky = W+E, pady = 1)
            Label(frame, text = course[8]).grid(row = i+1, column = 5, sticky = W+E, pady = 1)

        frame.columnconfigure(0, weight=2)
        frame.columnconfigure(1, weight=6)
        frame.columnconfigure(2, weight=4)
        frame.columnconfigure(3, weight=1)
        frame.columnconfigure(4, weight=2)
        frame.columnconfigure(5, weight=1)

    inCourse()

def student_tests():
    topLabel.config(text = "Tests")

    global curStudent
    frame = Frame(root, relief="solid", bd = 1)
    student_menu(frame)
    frame.pack(fill = BOTH, expand = True) 
    
    def inCourse():
        Label(frame, relief = "solid", bd = 1).grid(row = 0, column = 0, sticky = S+W+E)
        Label(frame, text = "Classname", relief = "solid", bd = 1).grid(row = 0, column = 1, sticky = S+W+E)
        Label(frame, text = "Textbook", relief = "solid", bd = 1).grid(row = 0, column = 2, sticky = S+W+E)
        Label(frame, text = "Size", relief = "solid", bd = 1).grid(row = 0, column = 3, sticky = S+W+E)
        Label(frame, text = "Room Number", relief = "solid", bd = 1).grid(row = 0, column = 4, sticky = S+W+E)
        Label(frame, text = "Time", relief = "solid", bd = 1).grid(row = 0, column = 5, sticky = S+W+E)

        courses = sql.StudentCourses(curStudent.SID)
        
        def test_list(CID):
            for widget in frame.winfo_children():
                widget.destroy()
            
            f = Frame(frame, padx=50)
            f.pack(fill=BOTH, expand = True)
            tests = sql.GetStudentTests(CID, curStudent.SID)

            def do_test(test):
                testframe = Frame(frame)
                testframe.pack(side = TOP, fill=BOTH, expand = True)

                Label(testframe, text="\n"+"Report Title\n"+ test[4]).pack()
                Label(testframe, text="\n"+"Report Task\n"+ test[5]).pack()

                Label(testframe, text="\n"+"Answer").pack()
                testanswer = Text(testframe, height = 10, width = 40)
                testanswer.pack(expand = True)

                def test_submit():
                    sql.DoTest(test[0], curStudent.SID, testanswer.get("1.0",'end-1c'))
                    report_list(CID)

                Button(testframe, text = "Submit", command = lambda : (testframe.pack_forget(), test_submit())).pack(pady = 1)

            Label(f, text = "Test").grid(row = 0, column = 0, sticky = W+E, pady = 1)
            Label(f, text = "Task").grid(row = 0, column = 1, sticky = W+E, pady = 1)
            for i, test in enumerate(tests):
                Button(f, text = "Do Test", command = lambda : (f.pack_forget(), do_test(test))).grid(row = i+1, column = 0, pady = 1)
                Label(f, text = test[5]).grid(row = i+1, column = 1, sticky = W+E, pady = 1)
            f.columnconfigure(0, weight=1)
            f.columnconfigure(1, weight=3)
            
        for i, course in enumerate(courses):
            def tstlist(cid = course[0]):
                test_list(cid)
            Button(frame, text = "Do Tests", command = tstlist).grid(row = i+1, column = 0, pady = 1)
            Label(frame, text = course[2]).grid(row = i+1, column = 1, sticky = W+E, pady = 1)
            Label(frame, text = course[3]).grid(row = i+1, column = 2, sticky = W+E, pady = 1)
            Label(frame, text = str(course[5]) + "/" + str(course[4])).grid(row = i+1, column = 3, sticky = W+E, pady = 1)
            Label(frame, text = str(course[6])).grid(row = i+1, column = 4, sticky = W+E, pady = 1)
            Label(frame, text = course[8]).grid(row = i+1, column = 5, sticky = W+E, pady = 1)

        frame.columnconfigure(0, weight=2)
        frame.columnconfigure(1, weight=6)
        frame.columnconfigure(2, weight=4)
        frame.columnconfigure(3, weight=1)
        frame.columnconfigure(4, weight=2)
        frame.columnconfigure(5, weight=1)

    inCourse()

def student_grades():
    topLabel.config(text = "Grades")

    global curStudent
    frame = Frame(root, relief="solid", bd = 1)
    student_menu(frame)
    frame.pack(fill = BOTH, expand = True)
    
    GPA = 0.0
    i = 1
    grades = sql.GetGrades(curStudent.SID)
    for grade in grades:
        GPA += float(grade[1])
        i+=1
    GPA = (GPA/(i-1))/25

    fr = Frame(frame)
    fr.grid(row = 0, column = 0, padx = 250, sticky = N+S+W+E)
    
    Label(fr, text = "GPA: " + str(GPA), font = ("Times New Roman", 18)).grid(row = 0, columnspan = 2)
    Label(fr, text = "Class").grid(row = 1, column = 0)
    Label(fr, text = "Grade").grid(row = 1, column = 1)
    
    for i, grade in enumerate(grades):
        Label(fr, text = grade[0]).grid(row = i+2, column = 0)
        Label(fr, text = str(grade[1])).grid(row = i+2, column = 1)
        

def student_view():
    topLabel.config(text = "View")

    global curStudent
    frame = Frame(root, relief="solid", bd = 1, bg ="#29bdc1")
    student_menu(frame)
    
    def fill_frame():
        frame.pack(fill = BOTH, expand = True)
    
        topframe = Frame(frame, relief="solid", bd = 1, bg = "White")
        topframe.grid(row = 1, column = 0, sticky=N+E+W)
    
        Label(frame, text = "    " + curStudent.FName + " " + curStudent.LName).grid(row = 0, column = 0, sticky="W")
        Label(frame, text = "Student ID = " + str(curStudent.SID) + "    ").grid(row = 0, column = 1, sticky="E")
    
        leftframe = Frame(frame)
        leftframe.grid(row = 1, column = 0, sticky=N+S+E+W)
        rightframe = Frame(frame)
        rightframe.grid(row = 1, column = 1, sticky=N+S+E+W)
        bottomframe = Frame(frame)
        bottomframe.grid(row = 2, columnspan = 2, sticky=E+W)
        frame.columnconfigure(tuple(range(2)), weight=1)
        frame.rowconfigure(tuple(range(3)), weight=1)

        Label(leftframe, text="Username\n"+curStudent.User).pack()

        Label(rightframe, text="Password\n"+curStudent.Pass).pack()

        Label(leftframe, text="\nFirstname\n"+curStudent.FName).pack()

        Label(rightframe, text="\nLastname\n"+curStudent.LName).pack()

        Label(leftframe, text="\nDate of Birth\n"+curStudent.DOB).pack()

        Label(rightframe, text="\nAddress 1\n"+curStudent.Addr1).pack()

        Label(leftframe, text="\nAddress 2\n"+curStudent.Addr2).pack()

        Label(rightframe, text="\nCity\n"+curStudent.City).pack()

        Label(leftframe, text="\nState\n"+curStudent.State).pack()

        Label(rightframe, text="\nZip\n"+curStudent.Zip).pack()

        Label(leftframe, text="\nEmail\n"+curStudent.Email).pack()

        Label(rightframe, text="\nPhoneNo\n"+curStudent.PhoneNo).pack()

        Button(bottomframe, text="Modify", width=10, height=1, command = lambda :(frame.pack_forget(), student_modify())).pack(pady=5)  
    
    fill_frame()

def student_modify():
    topLabel.config(text = "Modify")
    
    global curStudent
    frame = Frame(root, relief="solid", bd = 1)
    student_menu(frame)
    frame.pack(fill = BOTH, expand = True)

    topframe = Frame(frame)
    topframe.grid(row = 1, column = 0, sticky=N+E+W)
    
    Label(frame, text = "    " + curStudent.FName + " " + curStudent.LName).grid(row = 0, column = 0, sticky="W")
    Label(frame, text = "Student ID = " + str(curStudent.SID) + "    ").grid(row = 0, column = 1, sticky="E")
    
    leftframe = Frame(frame)
    leftframe.grid(row = 1, column = 0, sticky=N+S+E+W)
    rightframe = Frame(frame)
    rightframe.grid(row = 1, column = 1, sticky=N+S+E+W)
    bottomframe = Frame(frame)
    bottomframe.grid(row = 2, column = 1, sticky=E+W)
    frame.columnconfigure(tuple(range(2)), weight=1)
    frame.rowconfigure(tuple(range(3)), weight=1)

    Label(leftframe, text="Username").pack()
    user = Entry(leftframe)
    user.insert(0, curStudent.User)
    user.pack(ipadx = 30, ipady = 6)

    Label(rightframe, text="Password").pack()
    pwd = Entry(rightframe, show= '*')
    pwd.insert(0, curStudent.Pass)
    pwd.pack(ipadx = 30, ipady = 6)

    Label(leftframe, text="\nFirstname").pack()
    fname = Entry(leftframe)
    fname.insert(0, curStudent.FName)
    fname.pack(ipadx = 30, ipady = 6)

    Label(rightframe, text="\nLastname").pack()
    lname = Entry(rightframe)
    lname.insert(0, curStudent.LName)
    lname.pack(ipadx = 30, ipady = 6)

    Label(leftframe, text="\nDate of Birth").pack()
    dob = Entry(leftframe)
    dob.insert(0, curStudent.DOB)
    dob.pack(ipadx = 30, ipady = 6)

    Label(rightframe, text="\nAddress 1").pack()
    addr1 = Entry(rightframe)
    addr1.insert(0, curStudent.Addr1)
    addr1.pack(ipadx = 30, ipady = 6)

    Label(leftframe, text="\nAddress 2").pack()
    addr2 = Entry(leftframe)
    addr2.insert(0, curStudent.Addr2)
    addr2.pack(ipadx = 30, ipady = 6)

    Label(rightframe, text="\nCity").pack()
    city = Entry(rightframe)
    city.insert(0, curStudent.City)
    city.pack(ipadx = 30, ipady = 6)

    Label(leftframe, text="\nState").pack()
    states = ("AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY")
    combobox = ttk.Combobox(leftframe, values = states, height = 7)
    combobox.set(curStudent.State)
    combobox.pack(ipadx = 30, ipady = 6)

    Label(rightframe, text="\nZip").pack()
    zipNo = Entry(rightframe)
    zipNo.insert(0, curStudent.Zip)
    zipNo.pack(ipadx = 30, ipady = 6)

    Label(leftframe, text="\nEmail").pack()
    email = Entry(leftframe)
    email.insert(0, curStudent.Email)
    email.pack(ipadx = 30, ipady = 6)

    Label(rightframe, text="\nPhoneNo").pack()
    phoneno = Entry(rightframe)
    phoneno.insert(0, curStudent.PhoneNo)
    phoneno.pack(ipadx = 30, ipady = 6)

    def modifybtn():
        username = user.get()
        if len(username) != 0:
            curStudent.User = username

        password = pwd.get()
        if len(pwd) != 0:
            curStudent.Pass = password

        firstname = fname.get()
        if len(firstname) != 0:
            curStudent.FName = firstname

        lastname = lname.get()
        if len(lastname) != 0:
            curStudent.LName = lastname

        dateofbirth = dob.get()
        if len(dateofbirth) != 0:
            curStudent.DOB = dateofbirth

        address1 = addr1.get()
        if len(address1) != 0:
            curStudent.Addr1 = address1

        curStudent.Addr2 = addr2.get()

        modcity = city.get()
        if len(modcity) != 0:
            curStudent.City = modcity 

        st = combobox.get()
        if len(st) != 0:
            curStudent.State = st

        zp = zipNo.get()
        if len(zp) != 0:
            curStudent.Zip = zp
                
        eml = email.get()
        if len(eml) != 0:
            curStudent.Email = eml
                
        phn = phoneno.get()
        if len(phn) != 0:
            curStudent.PhoneNo = phn

        sql.ModifyStudent(curStudent)             
        msgbox.showinfo("Alarm", "Successfully modified!")
        frame.pack_forget()
        student_view()

    Button(bottomframe, text="Modify", width=10, height=1, command = modifybtn).pack(pady=5)  
    
def student_delete():
    global curStudent
    sql.DeleteStudent(curStudent.SID)
    logout()
   
    # teachers
def teacher_menu(a):
    topbar = Frame(root, relief="solid", bd = 1)
    topbar.pack(side = "top", fill="x")
    
    
    Button(topbar, text="Home", width=14, height=1, command = lambda : (topbar.pack_forget(), a.pack_forget(), teacher_home_page())).pack(side="left", pady=5) 
    Button(topbar, text="Make Course", width=14, height=1, command = lambda : (topbar.pack_forget(), a.pack_forget(), teacher_make_course())).pack(side="left", pady=5) 
    Button(topbar, text="Your Courses", width=14, height=1, command = lambda : (topbar.pack_forget(), a.pack_forget(), teacher_courses())).pack(side="left", pady=5) 
    Button(topbar, text="Judge", width=14, height=1, command = lambda : (topbar.pack_forget(), a.pack_forget(), teacher_judge())).pack(side="left", pady=5) 


    options = ["View Info", "Modify", "Delete", "Log Out"]

    def select_options():
        if var.get() == options[0]:
            topbar.pack_forget()
            a.pack_forget()
            teacher_view()
        elif var.get() == options[1]:
            topbar.pack_forget()
            a.pack_forget()
            teacher_modify()
        elif var.get() == options[2]:
            topbar.pack_forget()
            if msgbox.askyesno("Delete", "Are you sure you want to delete?"):
                teacher_delete()
        elif var.get() == options[3]:
            topbar.pack_forget()
            a.pack_forget()
            logout()
            
    var = StringVar()
    menubutton = Menubutton(topbar, text="Profile", borderwidth=1, relief="raised", width=14, height=1)
    menu = Menu(menubutton, tearoff=False)
    menubutton.configure(menu=menu)
    for option in options:
        menu.add_radiobutton(label=option, variable=var, value=option, command = select_options)
    menubutton.pack(side="right")

def teacher_home_page():
    topLabel.config(text = "Home")

    global curTeacher
    frame = Frame(root, relief="solid", bd = 1)
    teacher_menu(frame)

    frame.pack(fill = BOTH, expand = True)

def teacher_make_course():
    topLabel.config(text = "Your Courses")

    global curTeacher
    frame = Frame(root, relief="solid", bd = 1)
    teacher_menu(frame)

    def fill_frame():
        frame.pack(fill = BOTH, expand = True)
    
        Label(frame, text="\nClassname").grid(row = 0, column = 0)
        classname = Entry(frame, relief="solid", width = 35)
        classname.grid(row = 1, column = 0)

        Label(frame, text="\nTextbook").grid(row = 0, column = 1)
        textbook = Entry(frame, relief="solid", width = 35)
        textbook.grid(row = 1, column = 1)
    
        Label(frame, text="\nMaxSize").grid(row = 2, column = 0)
        maxsize = Entry(frame, relief="solid", width = 35)
        maxsize.grid(row = 3, column = 0)

        Label(frame, text="\nRoomNo").grid(row = 2, column = 1)
        roomno = Entry(frame, relief="solid", width = 35)
        roomno.grid(row = 3, column = 1)

        Label(frame, text="\nDepartment").grid(row = 4, column = 0)
        departments = sql.GetColleges()
        dt = dict()
        for i in departments:
            dt[i[1]] = i[0]
        values = list(i[1] for i in departments)
        combobox = ttk.Combobox(frame, values = values, height = 7, width = 35)
        combobox.grid(row = 5, column = 0)

        Label(frame, text="\nCategory").grid(row = 4, column = 1)
        category = Entry(frame, relief="solid", width = 35)
        category.grid(row = 5, column = 1)

        Label(frame, text="\nClass time").grid(row = 6, column = 0)
        classtime = Entry(frame, relief="solid", width = 35)
        classtime.grid(row = 7, column = 0)

        def make_course():
            newCourse = course()
            newCourse.ClassName = classname.get()
            newCourse.CollegeId = str(dt[combobox.get()])
            newCourse.Textbook = textbook.get()
            newCourse.MaxSize = int(maxsize.get())
            newCourse.RoomNo = roomno.get()
            newCourse.Category = category.get()
            newCourse.Department = combobox.get()
            newCourse.Time = classtime.get()

            sql.AppendCourse(curTeacher.TID, newCourse)
            msgbox.showinfo("Make Course", "Successfully made course!")
            for widget in frame.winfo_children():
                widget.destroy()
            fill_frame()

        bottom_frame = Frame(frame)
        bottom_frame.grid(row = 8, columnspan = 2, sticky = N+S+W+E)
        Button(bottom_frame, text="Make Course", width=10, height=1, command = make_course).pack(pady = 15)

        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
    
    fill_frame()
    
def teacher_courses():
    topLabel.config(text = "Your Course")

    global curTeacher
    frame = Frame(root, relief="solid", bd = 1)
    teacher_menu(frame)

    def fill_frame():
        frame.pack(fill = BOTH, expand = True)

        Label(frame, relief = "solid", bd = 1).grid(row = 0, columnspan = 3, sticky = S+W+E)
        Label(frame, text = "Classname", relief = "solid", bd = 1).grid(row = 0, column = 3, sticky = S+W+E)
        Label(frame, text = "Textbook", relief = "solid", bd = 1).grid(row = 0, column = 4, sticky = S+W+E)
        Label(frame, text = "Size", relief = "solid", bd = 1).grid(row = 0, column = 5, sticky = S+W+E)
        Label(frame, text = "Room Number", relief = "solid", bd = 1).grid(row = 0, column = 6, sticky = S+W+E)
        Label(frame, text = "Time", relief = "solid", bd = 1).grid(row = 0, column = 7, sticky = S+W+E)

        courses = sql.TeacherCourses(curTeacher.TID)
        
        def drop_course(CID):
            if msgbox.askyesno("Delete", "Are you sure you want to delete course?"):
                sql.DropCourse(CID)
                for widget in frame.winfo_children():
                    widget.destroy()
                fill_frame()

        def expand_course(CID, classname):
            for widget in frame.winfo_children():
                widget.destroy()

            f = Frame(frame, padx = 50)
            f.pack(fill=BOTH, expand = True)

            Label(f, text = classname, font = ("Arial", 15, "bold")).grid(row = 0, columnspan = 3, sticky= W+E)

            info = sql.ExpandCourse(CID)
            Label(f, text = "Student ID", relief = "solid", bd = 1).grid(row = 1, column = 0, sticky = N+W+E, padx = 1)
            Label(f, text = "Student", relief = "solid", bd = 1).grid(row = 1, column = 1, sticky = N+W+E, padx = 1)
            Label(f, text = "Grade", relief = "solid", bd = 1).grid(row = 1, column = 2, sticky = N+W+E, padx = 1)

            for r, i in enumerate(info):
                Label(f, text = str(i[3])).grid(row = r+2, column = 0, sticky = N)
                Label(f, text = str(i[0]) + " " + str(i[1])).grid(row = r+2, column = 1, sticky = N)
                Label(f, text = str(i[2])).grid(row = r+2, column = 2, sticky = N)
            f.columnconfigure(0, weight = 1)
            f.columnconfigure(1, weight = 10)
            f.columnconfigure(2, weight = 1)

        def assign_course(CID):
            for widget in frame.winfo_children():
                widget.destroy()

            fr = Frame(frame)
            fr.pack()
            Button(fr, text = "REPORT", relief="raised", padx = 15, pady = 15, command = lambda : (
                testframe.pack_forget(),
                reportframe.pack(side = TOP, fill=BOTH, expand = True)
                )).pack(side=LEFT, padx = 5)
            Button(fr, text = "TEST", relief="raised", padx = 15, pady = 15, command = lambda : (
                reportframe.pack_forget(),
                testframe.pack(side = TOP, fill=BOTH, expand = True)
                )).pack(side=RIGHT, padx = 5)

            reportframe = Frame(frame)
            reportframe.pack(side = TOP, fill=BOTH, expand = True)

            Label(reportframe, text="\n"+"Report Title").pack()
            reporttitle = Entry(reportframe)
            reporttitle.pack(ipadx = 30, ipady = 6)

            Label(reportframe, text="\n"+"Report task").pack()
            reporttask = Entry(reportframe)
            reporttask.pack(ipadx = 30, ipady = 6)

            Label(reportframe, text="\n"+"Due Date").pack()
            reportdate = Entry(reportframe)
            reportdate.pack(ipadx = 30, ipady = 6)

            def make_report():
                newReport = report()
                newReport.TID = curTeacher.TID
                newReport.CID = CID
                newReport.Title = reporttitle.get()
                newReport.Task = reporttask.get()
                newReport.DueDate = reportdate.get()
                newReport.Year = int(date.today().year)
                
                sidlist = sql.GetSidListInCID(CID)
                sql.MakeReport(sidlist, newReport)
                msgbox.showinfo("Report", "Successfully made new report!")
                assign_course(CID)

            Button(reportframe, text = "Assign", relief="raised", command = make_report).pack()

            testframe = Frame(frame)

            Label(testframe, text="\n"+"Test Name").pack()
            testname = Entry(testframe)
            testname.pack(ipadx = 30, ipady = 6)

            Label(testframe, text="\n"+"Test task").pack()
            testtask = Entry(testframe)
            testtask.pack(ipadx = 30, ipady = 6)

            Label(testframe, text="\n"+"Due Date").pack()
            testdate = Entry(testframe)
            testdate.pack(ipadx = 30, ipady = 6)

            def make_test():
                newTest = test()
                newTest.TID = curTeacher.TID
                newTest.CID = CID
                newTest.Title = testtitle.get()
                newTest.Task = testtask.get()
                newTest.DueDate = testdate.get()
                newTest.Year = int(date.today().year)
                
                sidlist = sql.GetSidListInCID(CID)
                sql.MakeTest(sidlist, newTest)
                msgbox.showinfo("Test", "Successfully made new test!")
                assign_course()

            Button(testframe, text = "Assign", relief="raised", command=make_test).pack()

        for i, course in enumerate(courses):
            def drp_course(a = course[0]):
                drop_course(a)
            def exp_course(a = course[0], b = course[2]):
                expand_course(a, b)
            def asn_course(a = course[0]):
                assign_course(a)
            Button(frame, text = "Drop", command =  drp_course).grid(row = i+1, column = 0, pady = 1, padx = 3)
            Button(frame, text = "Expand", command =  exp_course).grid(row = i+1, column = 1, pady = 1, padx = 3)
            Button(frame, text = "Assign", command = asn_course).grid(row = i+1, column = 2, pady = 1, padx = 3)
            Label(frame, text = course[2]).grid(row = i+1, column = 3, sticky = W+E, pady = 1)
            Label(frame, text = course[3]).grid(row = i+1, column = 4, sticky = W+E, pady = 1)
            Label(frame, text = str(course[5])+"/"+str(course[4])).grid(row = i+1, column = 5, sticky = W+E, pady = 1)
            Label(frame, text = str(course[6])).grid(row = i+1, column = 6, sticky = W+E, pady = 1)
            Label(frame, text = course[8]).grid(row = i+1, column = 7, sticky = W+E, pady = 1)
            
        frame.columnconfigure(3, weight=6)
        frame.columnconfigure(4, weight=4)
        frame.columnconfigure(5, weight=1)
        frame.columnconfigure(6, weight=2)
        frame.columnconfigure(7, weight=1)
    
    fill_frame()

def teacher_judge():
    topLabel.config(text = "Your Course")

    global curTeacher
    frame = Frame(root, relief="solid", bd = 1)
    teacher_menu(frame)

    def t_reports_judge(reporttitle, CID):
        for widget in frame.winfo_children():
            widget.destroy()
            
        f = Frame(frame, padx=50)
        f.pack(fill=BOTH, expand = True)

        studentreports = sql.TeacherReport(reporttitle)

        def give_grade(reportID, SID, pgrade, newgrade):
            if len(newgrade) > 0:
                RID = int(reportID)
                SID = int(SID)
                grade = int(newgrade)
                prvgrade = int(pgrade)

                sql.JudgeReport(RID, SID, CID, grade, prvgrade)
                msgbox.showinfo("Grade", "Successfully updated grade!")
            
        Label(f, text = reporttitle, font = ("Arial", 15)).grid(row = 0, columnspan = 4)

        Label(f, text = "Name", relief = "solid", bd = 1).grid(row = 1, column = 0, sticky = W+E)
        Label(f, text = "Answer", relief = "solid", bd = 1).grid(row = 1, column = 1, sticky = W+E)
        Label(f, text = "Grade", relief = "solid", bd = 1).grid(row = 1, column = 2,columnspan = 2, sticky = W+E)
 
        listgrade = []
        for i, rep in enumerate(studentreports):
            Label(f, text = rep[4] + " " + rep[5]).grid(row = i+2, column = 0, sticky = W+E)
            Label(f, text = rep[2]).grid(row = i+2, column = 1, sticky = W+E)
            grade = Entry(f)
            grade.insert(0, rep[3])
            grade.grid(row = i+2, column= 2, ipadx = 30, ipady =6, sticky = W+E)
            listgrade.append(grade)

            def g_grade(a = rep[0], b = rep[6], c = rep[3], d = i):
                give_grade(a, b, c, listgrade[d].get())

            Button(f, text = "Grade", command = g_grade).grid(row = i+2, column= 3)
                
        f.columnconfigure(0, weight = 1)
        f.columnconfigure(1, weight = 5)
        f.columnconfigure(2, weight = 1)
        f.columnconfigure(3, weight = 1)

    def t_tests_judge(testtitle, CID):
        for widget in frame.winfo_children():
            widget.destroy()
            
        f = Frame(frame, padx=50)
        f.pack(fill=BOTH, expand = True)

        studenttests = sql.TeacherTest(testtitle)

        def give_grade(testID, SID, pgrade, newgrade):
            if len(newgrade) > 0:
                RID = int(testID)
                SID = int(SID)
                grade = int(newgrade)
                prvgrade = int(pgrade)

                sql.JudgeTest(RID, SID, CID, grade, prvgrade)
                msgbox.showinfo("Grade", "Successfully updated grade!")
            
        Label(f, text = testtitle, font = ("Arial", 15)).grid(row = 0, columnspan = 4)

        Label(f, text = "Name", relief = "solid", bd = 1).grid(row = 1, column = 0, sticky = W+E)
        Label(f, text = "Answer", relief = "solid", bd = 1).grid(row = 1, column = 1, sticky = W+E)
        Label(f, text = "Grade", relief = "solid", bd = 1).grid(row = 1, column = 2,columnspan = 2, sticky = W+E)
        
        listgrade = []
        for i, tst in enumerate(studenttests):
            Label(f, text = tst[4] + " " + tst[5]).grid(row = i+2, column = 0, sticky = W+E)
            Label(f, text = tst[2]).grid(row = i+2, column = 1, sticky = W+E)
            grade = Entry(f)
            grade.insert(0, tst[3])
            grade.grid(row = i+2, column= 2, ipadx = 30, ipady =6, sticky = W+E)
            listgrade.append(grade)

            def g_grade(a = tst[0], b = tst[6], c = tst[3], d = i):
                give_grade(a, b, c, listgrade[d].get())

            Button(f, text = "Grade", command = g_grade).grid(row = i+2, column= 3)
                
        f.columnconfigure(0, weight = 1)
        f.columnconfigure(1, weight = 5)
        f.columnconfigure(2, weight = 1)
        f.columnconfigure(3, weight = 1)

    def fill_frame():
        frame.pack(fill = BOTH, expand = True)

        Label(frame, relief = "solid", bd = 1).grid(row = 0, columnspan = 2, sticky = S+W+E)
        Label(frame, text = "Classname", relief = "solid", bd = 1).grid(row = 0, column = 2, sticky = S+W+E)
        Label(frame, text = "Textbook", relief = "solid", bd = 1).grid(row = 0, column = 3, sticky = S+W+E)
        Label(frame, text = "Size", relief = "solid", bd = 1).grid(row = 0, column = 4, sticky = S+W+E)
        Label(frame, text = "Room Number", relief = "solid", bd = 1).grid(row = 0, column = 5, sticky = S+W+E)
        Label(frame, text = "Time", relief = "solid", bd = 1).grid(row = 0, column = 6, sticky = S+W+E)

        courses = sql.TeacherCourses(curTeacher.TID)

        def reports_list(CID):
            for widget in frame.winfo_children():
                widget.destroy()
            
            a_frame = Frame(frame, padx=50)
            a_frame.pack(fill=BOTH, expand = True)
            reports = sql.ReportList(CID)

            Label(a_frame, relief = "solid", bd = 1).grid(row = 0, column = 0, sticky = S+W+E)
            Label(a_frame, text = "Report Task", relief = "solid", bd = 1).grid(row = 0, column  = 1, sticky = S+W+E)

            for i, rpt in enumerate(reports):
                def rpts_judge(a = rpt[0], b = CID):
                    t_reports_judge(rpt[0], CID)
                Button(a_frame, text = "Judge", command = rpts_judge).grid(row = i+1, column = 0, sticky = W+E, pady = 1)
                Label(a_frame, text = rpt[0]).grid(row = i+1, column = 1, sticky = W+E, pady = 1)

        def tests_list(CID):
            for widget in frame.winfo_children():
                widget.destroy()
            
            a_frame = Frame(frame, padx=50)
            a_frame.pack(fill=BOTH, expand = True)
            tests = sql.TestList(CID)

            Label(a_frame, relief = "solid", bd = 1).grid(row = 0, column = 0, sticky = S+W+E)
            Label(a_frame, text = "Test Task", relief = "solid", bd = 1).grid(row = 0, column  = 1, sticky = S+W+E)

            for i, tst in enumerate(tests):
                def tsts_judge(a = tst[0], b = CID):
                    t_tests_judge(tst[0], CID)
                Button(a_frame, text = "Judge", command = tsts_judge).grid(row = i+1, column = 0, sticky = W+E, pady = 1)
                Label(a_frame, text = tst[0]).grid(row = i+1, column = 1, sticky = W+E, pady = 1)

        for i, course in enumerate(courses):
            def call_reports(a = course[0]):
                reports_list(a)
            def call_tests(a = course[0]):
                tests_list(a)
            Button(frame, text = "Reports", command = call_reports).grid(row = i+1, column = 0, pady = 1, padx = 3)
            Button(frame, text = "Tests", command = call_tests).grid(row = i+1, column = 1, pady = 1, padx = 3)
            Label(frame, text = course[2]).grid(row = i+1, column = 2, sticky = W+E, pady = 1)
            Label(frame, text = course[3]).grid(row = i+1, column = 3, sticky = W+E, pady = 1)
            Label(frame, text = str(course[5])+"/"+str(course[4])).grid(row = i+1, column = 4, sticky = W+E, pady = 1)
            Label(frame, text = str(course[6])).grid(row = i+1, column = 5, sticky = W+E, pady = 1)
            Label(frame, text = course[8]).grid(row = i+1, column = 6, sticky = W+E, pady = 1)
            
        frame.columnconfigure(2, weight=6)
        frame.columnconfigure(3, weight=4)
        frame.columnconfigure(4, weight=1)
        frame.columnconfigure(5, weight=2)
        frame.columnconfigure(6, weight=1)
    
    fill_frame()

def teacher_view(): 
    topLabel.config(text = "View")

    global curTeacher
    frame = Frame(root, relief="solid", bd = 1, bg ="#29bdc1")
    teacher_menu(frame)
    frame.pack(fill = BOTH, expand = True)

    frame.pack(fill = BOTH, expand = True)
    topframe = Frame(frame, relief="solid", bd = 1, bg = "White")
    topframe.grid(row = 1, column = 0, sticky=N+E+W)
    
    Label(frame, text = "    " + curTeacher.FName + " " + curTeacher.LName).grid(row = 0, column = 0, sticky="W")
    Label(frame, text = "Teacher ID = " + str(curTeacher.TID) + "    ").grid(row = 0, column = 1, sticky="E")
    
    leftframe = Frame(frame)
    leftframe.grid(row = 1, column = 0, sticky=N+S+E+W)
    rightframe = Frame(frame)
    rightframe.grid(row = 1, column = 1, sticky=N+S+E+W)
    bottomframe = Frame(frame)
    bottomframe.grid(row = 2, columnspan = 2, sticky=E+W)
    frame.columnconfigure(tuple(range(2)), weight=1)
    frame.rowconfigure(tuple(range(3)), weight=1)

    Label(leftframe, text="Username\n"+curTeacher.User).pack()

    Label(rightframe, text="Password\n"+curTeacher.Pass).pack()

    Label(leftframe, text="\nFirstname\n"+curTeacher.FName).pack()

    Label(rightframe, text="\nLastname\n"+curTeacher.LName).pack()

    Label(leftframe, text="\nEmail\n"+curTeacher.Email).pack()

    Label(rightframe, text="\nDepartment\n"+curTeacher.Dptmt).pack()

    Label(leftframe, text="\nCollege\n"+curTeacher.College).pack()

    Label(rightframe, text="\nSubjects\n"+curTeacher.Subj).pack()
    
    Label(leftframe, text="\nPhoneNo\n"+curTeacher.PhoneNo).pack()

    Label(rightframe, text="\nWebsite\n"+curTeacher.Website).pack()
    
    Button(bottomframe, text="Modify", width=10, height=1, command = lambda :(frame.pack_forget(), teacher_modify())).pack(pady=5)  

def teacher_modify():
    topLabel.config(text = "Modify")
    
    global curTeacher
    frame = Frame(root, relief="solid", bd = 1)
    teacher_menu(frame)
    frame.pack(fill = BOTH, expand = True)

    topframe = Frame(frame)
    topframe.grid(row = 1, column = 0, sticky=N+E+W)
    
    Label(frame, text = "    " + curTeacher.FName + " " + curTeacher.LName).grid(row = 0, column = 0, sticky="W")
    Label(frame, text = "Teacher ID = " + str(curTeacher.TID) + "    ").grid(row = 0, column = 1, sticky="E")
    
    leftframe = Frame(frame)
    leftframe.grid(row = 1, column = 0, sticky=N+S+E+W)
    rightframe = Frame(frame)
    rightframe.grid(row = 1, column = 1, sticky=N+S+E+W)
    bottomframe = Frame(frame)
    bottomframe.grid(row = 2, column = 1, sticky=E+W)
    frame.columnconfigure(tuple(range(2)), weight=1)
    frame.rowconfigure(tuple(range(3)), weight=1)

    Label(leftframe, text="Username").pack()
    user = Entry(leftframe)
    user.insert(0, curTeacher.User)
    user.pack(ipadx = 30, ipady = 6)

    Label(rightframe, text="Password").pack()
    pwd = Entry(rightframe, show= '*')
    pwd.insert(0, curTeacher.Pass)
    pwd.pack(ipadx = 30, ipady = 6)

    Label(leftframe, text="\nFirstname").pack()
    fname = Entry(leftframe)
    fname.insert(0, curTeacher.FName)
    fname.pack(ipadx = 30, ipady = 6)

    Label(rightframe, text="\nLastname").pack()
    lname = Entry(rightframe)
    lname.insert(0, curTeacher.LName)
    lname.pack(ipadx = 30, ipady = 6)

    Label(leftframe, text="\nEmail").pack()
    email = Entry(leftframe)
    email.insert(0, curTeacher.Email)
    email.pack(ipadx = 30, ipady = 6)

    Label(rightframe, text="\nDepartment").pack()
    dptmt = Entry(rightframe)
    dptmt.insert(0, curTeacher.Dptmt)
    dptmt.pack(ipadx = 30, ipady = 6)

    Label(leftframe, text="\nCollege").pack()
    college = Entry(leftframe)
    college.insert(0, curTeacher.College)
    college.pack(ipadx = 30, ipady = 6)

    Label(rightframe, text="\nSubjects").pack()
    subj = Entry(rightframe)
    subj.insert(0, curTeacher.Subj)
    subj.pack(ipadx = 30, ipady = 6)

    Label(leftframe, text="\nPhoneNo").pack()
    phoneno = Entry(leftframe)
    phoneno.insert(0, curTeacher.PhoneNo)
    phoneno.pack(ipadx = 30, ipady = 6)

    Label(rightframe, text="\nWebsite").pack()
    website = Entry(rightframe)
    website.insert(0, curTeacher.Website)
    website.pack(ipadx = 30, ipady = 6)

    def modifybtn():
        username = user.get()
        if len(username) != 0:
            curTeacher.User = username

        password = pwd.get()
        if len(pwd) != 0:
            curTeacher.Pass = password

        firstname = fname.get()
        if len(firstname) != 0:
            curTeacher.FName = firstname

        lastname = lname.get()
        if len(lastname) != 0:
            curTeacher.LName = lastname

        eml = email.get()
        if len(eml) != 0:
            curTeacher.Email = eml

        dpt = dptmt.get()
        if len(dpt) != 0:
            curTeacher.Dptmt = dpt

        clg = college.get()
        if len(clg) != 0:
            curTeacher.College = clg

        sbj = subj.get()
        if len(sbj) != 0:
            curTeacher.Subj = sbj
                
        phn = phoneno.get()
        if len(phn) != 0:
            curTeacher.PhoneNo = phn
                
        wbst = website.get()
        if len(wbst) != 0:
            curTeacher.Website = wbst

        sql.ModifyTeacher(curTeacher)             
        msgbox.showinfo("Alarm", "Successfully modified!")
        frame.pack_forget()
        student_view()

    Button(bottomframe, text="Modify", width=10, height=1, command = modifybtn).pack(pady=5) 

def teacher_delete():
    global curTeacher
    sql.DeleteTeacher(curTeacher.TID)
    logout()

def logout():
    global curStudent
    global curTeacher
    curStudent = student()
    curTeacher = teacher()

    loginpage()

loginpage()
root.mainloop()
