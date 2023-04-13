from tkinter import filedialog
import tkinter.messagebox
import pandas as pd
from tkinter import *
from statistics import mean
from menu import MenuBar

DATA = pd.read_csv('students_file.csv')
RATIO = pd.read_csv('ratio.csv')
GRADE_COMP = pd.read_csv('grade component.csv')
TOTAL_GPA = 5
COLUMNS_LIST = ["Student Name", "ID", "Chem Quiz", "Bio Quiz", "Phy Quiz", "Math Quiz", "Chem HW", "Bio HW",
                "Phy HW", "Math HW", "Chem Attend", "Bio Attend", "Phy Attend", "Math Attend", "Chem Exam", "Bio Exam",
                "Phy Exam", "Math Exam", "Chem AVG", "Bio AVG", "Phy AVG", "Math AVG", "Avg Score", "GPA", "Grade",
                "Status"]

APP_LABELS = ["Student Name", "ID", "Quiz Score", "Home Work", "Class Attendance", "Exam Score", "Average Score",
              "Average", "GPA", "Grade", "Status"]


class Report(Tk):
    def __init__(self, title):
        super().__init__()
        self.end = False
        self.title(title)
        self.minsize(width=1000, height=600)
        self.num = 0
        self.save_button = None
        self.current_student = None
        self.names = DATA["Student name"].to_list()
        self.id = DATA.ID.to_list()
        self.menu = MenuBar(self)
        self.next_student_button = None
        self.grade = ''
        self.num = 0  # this is used to track if the calculate button has been pressed
        self.avr_l = []  # contains the labels of the average scores of each subject for each student
        self.final_avr = 0  # the values of the final average score of all subjects for each student
        self.stats = []  # list to store the statuses of all students such as grade,gpa,status
        self.ratio = RATIO.Ratio.to_list()  # ratios for the calculation of the scores for each subject
        self.grade_components = GRADE_COMP.Total.to_list()
        self.final_data = []  # list containing the final data for all students such as each student's name, id,
        # scores,etc.
        self.entry = []
        self.avr = []  # contains the values of the average scores of each subject for each student
        self.Header_font = ('Arial', 15,)
        self.pad = 10
        self.subjects = ["Chem", "Bio", "Phy", "Math"]
        self.scores = []
        self.students_data = self.get_students_data()
        self.count = 0  # used to track when the next button is pressed
        self.cur, self.cur_id = '', ''
        self.dataframe = None
        self.first_init()

    def create_save_button(self):
        self.save_button = Button(text='Save file')

    def first_init(self):
        welcome = Label(text="WELCOME TO THE STUDENTS'\nRECORD CALCULATION APP.\nCHOOSE A MENU TO BEGIN",
                        font=self.Header_font)
        welcome.place(x=300, y=150)

    def int(self):
        self.avr_l = []
        self.current_student = Label()
        if self.count > 0:
            self.current_student.config(text=f"{self.names[self.count - 1]}")
        else:
            self.current_student.config(text="Press the 'next' button below to proceed")
        self.current_student.grid(column=0, row=2, )

    @staticmethod
    def get_students_data():
        student_data = {row['Student name']: row.ID for (index, row) in DATA.iterrows()}
        return student_data

    def app_labels(self):
        """Create the app labels,that is the columns in the app such as student name, id,etc."""
        for i in range(len(APP_LABELS)):
            if i in range(2):
                app_labels = Label(text=f"{APP_LABELS[i]}", font=self.Header_font, padx=self.pad)
                app_labels.grid(column=i, row=0)
            elif i in range(2, 7):
                app_labels = Label(text=f"{APP_LABELS[i]}", font=self.Header_font, padx=self.pad)
                app_labels.grid(column=i * 2, row=0, columnspan=2)
            else:
                app_labels = Label(text=f"{APP_LABELS[i]}:", font=self.Header_font, )
                app_labels.grid(column=7, row=i - 2, )

    @staticmethod
    def subject_labels_template(col, the_list):
        """Create the label for a subject"""
        for index in range(len(the_list)):
            new_label = Label(text=f"{the_list[index]}", )
            new_label.grid(column=col, row=index + 1)

    @staticmethod
    def entries(col, row):
        """Create the entry for a subject"""
        new_entry = Entry(width=3)
        new_entry.grid(column=col + 1, row=row + 1)
        return new_entry

    def create_subject_labels(self):
        """Create the labels and entries for all subjects"""
        chem_entry = []
        bio_entry = []
        phy_entry = []
        math_entry = []
        for i in range(4, 11, 2):  # the column range is (4,11,2) because some app labels,e.g, quiz score,home
            # work have a column span of 2 meaning that the column is divided into 2
            self.subject_labels_template(i, self.subjects)
            for j in range(len(self.subjects)):
                v = self.entries(i, j)
                if j == 0:
                    chem_entry.append(v)
                elif j == 1:
                    bio_entry.append(v)
                elif j == 2:
                    phy_entry.append(v)
                elif j == 3:
                    math_entry.append(v)
        self.entry = [chem_entry, bio_entry, phy_entry, math_entry]

    def get(self):
        """Get the actual values in each entry"""
        chem_scores = []
        bio_scores = []
        phy_scores = []
        math_scores = []
        for x in range(len(self.entry)):
            for y in self.entry[x]:
                v = y.get()
                if not v == '':
                    v = float(v)
                    if x == 0:
                        chem_scores.append(v)
                    elif x == 1:
                        bio_scores.append(v)
                    elif x == 2:
                        phy_scores.append(v)
                    elif x == 3:
                        math_scores.append(v)
        scores = [chem_scores, bio_scores, phy_scores, math_scores]
        return scores

    def next_button(self):
        self.next_student_button = Button(text="Next", command=self.execute_next)
        self.next_student_button.grid(column=0, row=9, pady=20)

    @staticmethod
    def calculate_button(func):
        calculate = Button(text="Calculate", command=func)
        calculate.grid(column=12, row=9, pady=20)

    def student_label(self):
        """Show the current student and their ID in the app"""
        self.cur = self.names[self.count]
        self.cur_id = self.id[self.count]
        # print(self.cur)
        self.current_student.config(text=self.cur)
        current_id = Label(text=self.cur_id)
        current_id.grid(column=1, row=2)

    def increment_count(self):
        """Increment the count value when the user presses the next button"""
        self.count += 1
        if self.count == len(self.students_data):
            self.count = 0

    def execute_next(self):
        """Functions to execute when the next button is pressed"""
        # print(self.count)
        # print(self.num)
        # self.next_student_button.config(text="Next student")
        if self.count == self.num:
            self.student_label()
            self.increment_count()
            self.clear_entries()

    def clear_entries(self):
        for ls in self.entry:
            for entry in ls:
                entry.delete(0, 'end')
        for labels in self.avr_l:
            labels.config(text="")

    def create_each_student_data(self):
        self.stats = []
        self.avr = []
        score_vas = []
        each_data = {}
        score = self.get()
        status = ""
        for ls in score:
            sums = 0
            if not ls == []:
                for j in range(len(ls)):
                    # average score for each subject under a section is: the score divided by the total obtainable
                    # score in the section times the ratio(t0 100)
                    avr = (ls[j] / self.grade_components[j]) * self.ratio[j]
                    sums += avr  # total average for a subject under a section,e.g., for chemistry under quiz score
                self.avr.append(round(sums, 2))
        # print(self.avr)
        if not self.avr == []:
            self.final_avr = round(mean(self.avr), 2)  # final average of all scores
            avr_f = round(self.final_avr)
            gpa = round((self.final_avr / 100 * TOTAL_GPA), 1)

            if avr_f in range(90, 101):
                self.grade = "A"
            elif avr_f in range(75, 90):
                self.grade = "B"
            elif avr_f in range(65, 75):
                self.grade = "C"
            elif avr_f in range(55, 65):
                self.grade = "D"
            elif avr_f in range(50, 55):
                self.grade = "E"
                status = "Retake"
            elif avr_f in range(50):
                self.grade = "F"
                status = "Fail"
            if self.grade in ["A", "B", "C", "D"]:
                status = "Pass"
            self.stats.append(self.final_avr)
            self.stats.append(gpa)
            self.stats.append(self.grade)
            self.stats.append(status)

            for i in range(len(score)):
                for j in range(len(score)):
                    score_vas.append(score[j][i])
            # creating the dictionary to store the data for each student such as their name, id,scores,gpa,etc.
            for x in range(len(COLUMNS_LIST)):
                if x == 0:
                    each_data[COLUMNS_LIST[x]] = self.cur
                elif x == 1:
                    each_data[COLUMNS_LIST[x]] = self.cur_id
                if x in range(2, 18):
                    each_data[COLUMNS_LIST[x]] = score_vas[x - 2]
                elif x in range(18, 22):
                    each_data[COLUMNS_LIST[x]] = self.avr[x - 18]
                elif x in range(22, 26):
                    each_data[COLUMNS_LIST[x]] = self.stats[x - 22]
            # print(self.stats)
            self.final_data.append(each_data)
            # print(self.final_data)

    def create_score_labels(self):
        for i in range(8):
            score_label = Label()
            if i in range(4):
                score_label.grid(column=12, row=i + 1)
            else:
                score_label.grid(column=8, row=i + 1)
                score_label.config(font=self.Header_font)
            self.avr_l.append(score_label)
            # print(self.avr_l)

    def update_avr_label(self):
        """Update the score and gpa and grade and status labels for each student when the calculate button is pressed"""
        for index in range(len(self.avr_l)):
            if index in range(4):
                self.avr_l[index].config(text=f"{self.avr[index]}")
            elif index >= 4:
                self.avr_l[index].config(text=f"{self.stats[index - 4]}")
        self.num += 1
        if self.num == len(self.names):
            # print(self.num)
            self.next_student_button.destroy()
            self.save_button.config(command=self.savefile)
            self.save_button.grid(column=9, row=9)
            self.end = True

    def create_final_data(self):
        """Generate the final data for all students"""
        indexes = list(range(self.num))
        if self.num > 0:
            df = pd.DataFrame(columns=COLUMNS_LIST, index=indexes)
            for i in indexes:
                df.loc[i] = pd.Series(self.final_data[i])
            self.dataframe = df
            # print(df)
            return df

    def savefile(self):
        """Save the data file to a directory specified by the user"""
        data = self.create_final_data()
        files = [("CSV Files", ".csv"), ("Word", ".doc"), ("All Files", "*.*")]
        try:
            with filedialog.asksaveasfile(mode='w', defaultextension='.csv', filetypes=files) as file:
                data.to_csv(file.name, index=False)
                self.show_message()
        except AttributeError:
            pass
        self.save_button.destroy()

    def entries_not_empty(self):
        """Check if all entries are empty: only when all entries are not empty can the app perform necessary
        calculations """
        count = 0
        for lists in self.entry:
            for index_entries in range(len(lists)):
                if lists[index_entries].get():
                    if float(lists[index_entries].get()) <= self.grade_components[index_entries]:
                        count += 1
        if count == len(self.entry) * len(self.entry) and self.cur in self.names and self.count != self.num:
            return count

    @staticmethod
    def show_message():
        tkinter.messagebox.showinfo(title="File Saved", message="Your file has been saved.\nGo to the location to "
                                                                "check.")

    def clear_window(self):
        for widget in self.winfo_children():
            if widget.widgetName == "menu":
                continue
            else:
                widget.destroy()
