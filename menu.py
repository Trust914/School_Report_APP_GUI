import tkinter as tk

from search import Search

"""This class handles each menu in the menu list"""


class MenuBar(tk.Menu):
    def __init__(self, parent):
        self.controller = parent  # the  parent is the main class which is in the student_record module
        self.search_menu = Search(self)
        tk.Menu.__init__(self, parent, tearoff=False)
        self.menus = tk.Menu(self, tearoff=0)
        self.menus.add_command(label="Calculate Records", command=self.calculate_records_menu)
        self.menus.add_command(label="Perform search", command=lambda: self.perform_search_menu())
        self.menus.add_separator()
        self.menus.add_command(label="Exit", command=lambda: self.quit_button())
        self.index_of_active_menu = ''
        self.add_cascade(label="Menu", menu=self.menus)
        parent.config(menu=self)
        self.track = 0

    def calculate_records_menu(self):
        """This function is executed each time the user selects the Calculate records menu"""
        if self.index_of_active_menu == "" or self.index_of_active_menu == "Perform search":
            # the user has selected the Calculate records menu
            if self.controller.count > 0:
                if self.controller.count == self.controller.number and self.controller.count != 2:
                    self.controller.count += 1
                    self.controller.cur = self.controller.names[self.controller.count - 1]
                    self.controller.cur_id = self.controller.id[self.controller.count - 1]
            self.index_of_active_menu = "Calculate Records"
            self.controller.clear_window()
            self.controller.int()
            self.controller.app_labels()
            self.controller.create_save_button()
            self.controller.create_subject_labels()
            self.controller.create_score_labels()
            if not self.controller.end:
                self.controller.next_button()
                self.controller.calculate_button(self.calculate_button_function)
                self.controller.create_save_button()

    def calculate_button_function(self):
        x = self.controller.entries_not_empty()
        if x == 16:
            self.controller.create_each_student_data()
            self.controller.update_avr_label()

    def perform_search_menu(self):
        """This function is executed each time the user selects the Perform search menu"""
        if self.index_of_active_menu == "" or "Calculate Records":
            # the user has selected the perform search menu
            self.index_of_active_menu = "Perform search"
            self.controller.clear_window()
            self.search_menu.create_filter_spinbox()

    def quit_button(self):
        """THis function is executed when the user selects Exit"""
        self.controller.destroy()
