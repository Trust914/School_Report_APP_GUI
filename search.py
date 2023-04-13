from tkinter import *
import tkinter.messagebox

FILTER_LIST = ["Choose filter", "Full Performance", "Subject Performance", "Grades", "Statuses", ]
SUBJECTS_AVG = ["Chem AVG", "Bio AVG", "Phy AVG", "Math AVG", ]


class Search:

    def __init__(self, parent):
        self.lab = []
        self.status_label = None
        self.status_entry = None
        self.full_label = None
        self.search_label = []
        self.full_performance_widget = []
        self.each_status_widget = []
        self.statuses_widget = []
        self.grade_widgets = []
        self.subjectPerformance_widgets = []
        self.grade_label = None
        self.grade_entry = None
        self.score_label = None
        self.real_info = None
        self.check_button = None
        self.subject_entry = None
        self.subject_label = None
        self.data = None
        self.controller = parent
        self.name_list = self.controller.controller.names
        self.id_list = self.controller.controller.id
        self.score_label = None
        self.func = None
        self.full_label = None
        self.current_filter = ""
        self.current_student_info = None
        self.entry = None
        self.spinbox = None
        self.num_of_times_in_statuses_filter = 0

    def create_search_entry(self):
        self.search_label = Label(text="Search")
        self.search_label.grid(column=0, row=2)
        self.entry = Entry(width=30)
        self.entry.insert(END, string="Type a student name or ID")
        self.entry.grid(column=1, row=2)

    def create_filter_spinbox(self):
        label = Label(text="Filter search")
        label.grid(column=0, row=0)
        self.spinbox = Spinbox(values=FILTER_LIST, width=30, command=self.spinbox_used, )
        self.spinbox.grid(column=1, row=0)

    def spinbox_used(self, ):
        """This function is executed when the user selects a menu from the menu list"""
        self.current_filter = str(self.spinbox.get())
        if self.current_filter == "Full Performance":
            self.clear_widgets(self.lab)
            self.create_search_entry()
            self.full_label = Label(text='')
            self.full_label.grid(column=1, row=3)
            self.check_button = Button(text="Search", command=self.extract_full_performance)
            self.check_button.grid(row=2, column=4)
            self.full_performance_widget = [self.search_label, self.entry, self.full_label, self.check_button]
        else:
            self.clear_widgets(self.full_performance_widget)
        if self.current_filter == "Subject Performance":
            self.clear_widgets(self.lab)
            self.create_search_entry()
            self.subject_label = Label(text="Subject")
            self.subject_label.grid(row=2, column=2)
            self.subject_entry = Entry()
            self.subject_entry.insert(END, "Enter a subject")
            self.subject_entry.grid(row=2, column=3)
            self.check_button = Button(text="Search", command=self.extract_subject_performance)
            self.check_button.grid(row=2, column=4)
            self.score_label = Label(text="Score will appear here", font=self.controller.controller.Header_font)
            self.score_label.grid(column=1, row=3)
            self.subjectPerformance_widgets = [self.subject_label, self.subject_entry, self.check_button,
                                               self.score_label, self.entry, self.search_label]
        else:
            self.clear_widgets(self.subjectPerformance_widgets)
        if self.current_filter == "Grades":
            self.clear_widgets(self.lab)
            self.grade_label = Label(text="Grade")
            self.grade_label.grid(column=0, row=1)
            self.grade_entry = Entry()
            self.grade_entry.insert(END, "Enter a grade")
            self.grade_entry.grid(column=1, row=1)
            self.check_button = Button(text="Search", command=self.extract_students_by_grades)
            self.check_button.grid(row=2, column=4)
            self.grade_widgets = [self.grade_label, self.grade_entry, self.check_button]
        else:
            self.clear_widgets(self.grade_widgets)
        if self.current_filter == "Statuses":
            self.clear_widgets(self.lab)
            self.num_of_times_in_statuses_filter += 1
            if self.num_of_times_in_statuses_filter == 1:
                self.status_label = Label(text="Status")
                self.status_label.grid(column=0, row=1)
                self.status_entry = Entry()
                self.status_entry.insert(END, "Enter a status")
                self.status_entry.grid(column=1, row=1)
                self.check_button = Button(text="Search", command=self.extract_students_by_statuses)
                self.check_button.grid(row=2, column=4)
                self.statuses_widget = [self.status_label, self.status_entry, self.check_button]
        else:
            self.num_of_times_in_statuses_filter = 0
            self.clear_widgets(self.statuses_widget)
        if self.current_filter == "Choose filter":
            self.clear_widgets(self.lab)
            self.clear_widgets(self.full_performance_widget)
            self.clear_widgets(self.subjectPerformance_widgets)
            self.clear_widgets(self.grade_widgets)
            self.clear_widgets(self.statuses_widget)

    def get_student_info(self):
        """Get the student info as entered by the user"""
        self.current_student_info = str(self.entry.get())
        if self.current_student_info in self.id_list:
            return self.current_student_info
        else:
            if self.current_student_info == "" or self.current_student_info == "Type a student name or ID":
                return False
            else:
                return self.current_student_info.title()

    def get_real_student_info(self):
        self.data = self.controller.controller.create_final_data()
        student_info = self.get_student_info()
        if student_info is False or self.data is None:
            return student_info
        if self.data is not None:
            if student_info in self.id_list:
                return student_info
            else:
                name_list = self.name_list
                for index in range(len(name_list)):
                    name_list[index].replace(" ", "")
                    if student_info[:4] in name_list[index]:
                        student_info = self.name_list[index]
                        break
                return student_info

    def extract_full_performance(self, ):
        ind = None
        new_student_info = self.get_real_student_info()
        x = 0
        try:
            if new_student_info in self.id_list:
                ind = self.data.index[self.data["ID"] == new_student_info].item()
            elif new_student_info in self.name_list:
                ind = self.data.index[self.data["Student Name"] == new_student_info].item()
        except ValueError:
            x += 1
            self.full_label.config(text="")
            self.show_message()
        if ind is not None:
            student_performance = self.data.loc[ind].to_string()
            self.full_label.config(text=student_performance)
        elif ind is None and x < 1:
            self.full_label.config(text="")
            self.show_message()

    def extract_subject_performance(self):
        # subj = ""
        real_subj = None
        data = None
        new_student = self.get_real_student_info()
        if self.current_filter == "Subject Performance":
            subj = str(self.subject_entry.get()).title()
            li = SUBJECTS_AVG
            for i in range(len(li)):
                li[i].replace(" ", "")
                if self.subject_entry.get() and subj[:3] in li[i]:
                    real_subj = SUBJECTS_AVG[i]
                    break
            if real_subj in SUBJECTS_AVG:
                if new_student in self.name_list:
                    data = self.data[self.data["Student Name"] == new_student][real_subj].item()
                    self.score_label.config(text=f"{real_subj}: {data}", )
                elif new_student in self.id_list:
                    data = self.data[self.data["ID"] == new_student][real_subj].item()
                    self.score_label.config(text=f"{real_subj}: {data}", )
            elif real_subj not in SUBJECTS_AVG or data is None:
                self.score_label.config(text="")
                self.show_message()

    def extract_students(self, by_val):
        list_of_students = []
        show = False
        self.data = self.controller.controller.create_final_data()
        if self.data is not None:
            if len(by_val) > 1 and by_val in ["Pass", "Retake", "Fail"]:
                list_of_students = self.data[self.data["Status"] == by_val]["Student Name"].to_list()
            elif len(by_val) == 1 and by_val in ["A", "B", "C", "D", "E", "F"]:
                list_of_students = self.data[self.data["Grade"] == by_val]["Student Name"].to_list()
                # print(list_of_students)
            else:
                self.show_message()
                show = True
            for index in range(len(list_of_students)):
                label = Label(text=list_of_students[index], font=self.controller.controller.Header_font)
                label.grid(row=index + 2, column=1)
                self.lab.append(label)
        if self.data is None or list_of_students == [] and not show:
            self.show_message()

    def extract_students_by_grades(self):
        self.clear_widgets(self.lab)
        self.extract_students(by_val=str(self.grade_entry.get()).upper())

    def extract_students_by_statuses(self):
        self.clear_widgets(self.lab)
        self.extract_students(by_val=str(self.status_entry.get()).title())

    @staticmethod
    def clear_widgets(widget_list):
        for vals in widget_list:
            if vals is not None:
                vals.destroy()

    @staticmethod
    def show_message():
        tkinter.messagebox.showwarning(title="No Data", message="Invalid entry or no data for this selection")
