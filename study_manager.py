from tkinter import *
from tkinter import ttk, font
from tkmacosx import Button
from datetime import datetime
import customtkinter as ctk
from tkcalendar import Calendar

class StudyManagerApp():
    def __init__(self):
        
        root.geometry("850x600")
        root.configure(bg="#F8F5F2")
        
        red_alert = "#AD4849"
        yellow_alert = "#CFB353"
        
        
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(0, weight=1)
        
        self.app_frame = Frame(bg="#F8F5F2")
        self.app_frame.grid(sticky=NSEW)
        self.app_frame.grid_columnconfigure(0, weight=1)
        self.app_frame.grid_columnconfigure(1, weight=1)
        self.app_frame.grid_rowconfigure(2, weight=0)
        self.app_frame.grid_rowconfigure(3, weight=0)



    
        self.button_frame = Frame(self.app_frame,
                                  bg="#F8F5F2")
        self.button_frame.grid(row=0, column=0, columnspan=2, sticky="ew")
        self.button_frame.grid_columnconfigure(0, weight=0)
        self.button_frame.grid_columnconfigure(1, weight=0)
        self.button_frame.grid_columnconfigure(2, weight=0)
        self.button_frame.grid_columnconfigure(3, weight=1)  


        
        self.save_button = Button(self.button_frame,
                                text="Save",
                                bg="#F5F5F5",
                                width=70,
                                height=30,  
                                borderless=1)  
    
        self.save_button.grid(row=0, column=0, sticky="nw")

        self.load_button = Button(self.button_frame,
                                text="Load",
                                bg="#F5F5F5",
                                width=70,
                                height=30,
                                borderless=1)
        self.load_button.grid(row=0, column=1, sticky="nw")
        
        self.all_tasks_button = Button(self.button_frame,
                                       text="All Tasks",
                                       bg="#F5F5F5",
                                       width=120,
                                       height=30,
                                       borderless=1)
        self.all_tasks_button.grid(row=0, column=2, padx=20, sticky="nw")
        
        self.db_label = Label(self.app_frame, 
                              text="Dashboard",
                              font=("Helvetica", "20"),
                              bg="#F8F5F2")
        self.db_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        
        self.db_holder = Frame(self.app_frame, bg="#F8F5F2")
        self.db_holder.grid(row=2, column=0, sticky="nw")

        self.db_task_frame = ctk.CTkFrame(self.db_holder,
                                          corner_radius=20,
                                          fg_color=red_alert,
                                          width=350,
                                          height=130,
                                          border_color="black",
                                          border_width=1)
        self.db_task_frame.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        self.db2_task_frame = ctk.CTkFrame(self.db_holder,
                                          corner_radius=20,
                                          fg_color=yellow_alert,
                                          width=350,
                                          height=130,
                                          border_color="black",
                                          border_width=1)
        self.db2_task_frame.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        
        self.session_reminder = ctk.CTkFrame(self.db_holder,
                                             corner_radius=20,
                                             fg_color="#D5E8D4",
                                             width=260,
                                             height=60,
                                             border_color="#82B366",
                                             border_width=1)
        self.session_reminder.grid(row=2, column=0,padx=20, pady=30, sticky="s")
        
        self.add_task_button = ctk.CTkButton(self.button_frame,
                                             text="+ Add Task",
                                             corner_radius=10,
                                             fg_color="#5DAC70",
                                             height=50,
                                             width=90, 
                                             command=lambda: self.to_add_task())
        self.add_task_button.grid(row=0, column=3, padx=10, pady=15, sticky="e")
        self.add_task_button.configure(state=NORMAL)
        
        large_font = font.Font(family="Helvetica", size=14)
        
        self.db_calendar_frame = Frame(self.app_frame,
                                    width=320,
                                    bg="#F8F5F2")
        self.db_calendar_frame.grid(row=2, column=1, padx=10, pady=10, sticky="nw")

        self.db_calendar_frame.grid_rowconfigure(0, weight=0)
        self.db_calendar_frame.grid_rowconfigure(1, weight=0)
        self.db_calendar_frame.grid_columnconfigure(0, weight=1)

        cal = Calendar(self.db_calendar_frame, selectmode="day", font=large_font )
        cal.grid(row=0, column=0)

        self.streak_frame = ctk.CTkLabel(self.db_calendar_frame,
                                        text="sdf",
                                        width=190,
                                        height=60,
                                        fg_color="#DF7341",
                                        corner_radius=10)
        self.streak_frame.grid(row=1, column=0, pady=50, sticky="s")
        
    def to_add_task(self):
        DisplayAddTask(self)
        

class DisplayAddTask():
    def __init__(self, partner):
        background = "#F8F5F2"
        
        self.add_task_gui = Toplevel()
        self.add_task_gui.geometry("700x400")
        self.add_task_gui.configure(bg=background)
        partner.add_task_button.configure(state=DISABLED)
        
        self.add_task_gui.protocol("WM_DELETE_WINDOW",
                               lambda: self.close_task(partner))
        
        

        title_label = Label(self.add_task_gui,
                            text="Add Task",
                            font=font.Font(family="Helvetica", size=18, weight="bold"),
                            bg="#F8F5F2")
        title_label.pack(pady=20)

        self.main_frame = Frame(self.add_task_gui,
                           bg="#F8F5F2")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.left_side_frame = Frame(self.main_frame, 
                                bg="#F8F5F2")
        self.left_side_frame.pack(side="left", fill="both", expand=True, padx=20)

        self.task_type_label = Label(self.left_side_frame, 
                                     text="Choose type of task:",
                                     bg="#F8F5F2", font=font.Font(family="Helvetica", size=16))
        self.task_type_label.pack(anchor="w", pady=10)

        for choice in ["Exam", "Assignment", "Study Session"]:
            self.rad_option = Radiobutton(self.left_side_frame, text=choice, variable=StringVar(), value=choice,
                        font=font.Font(family="Helvetica", size=14), bg="#F8F5F2", anchor="w")
            self.rad_option.pack(anchor="w")


    def close_task(self, partner):
        """
        Closes Add Task GUI and enables the button
        """
        
        partner.add_task_button.configure(state=NORMAL)
        self.add_task_gui.destroy()
        
    

class Event():
    def __init__(self, title, event_type, due_date):
        self.title = title
        self.type = event_type
        self.due_date = due_date

if __name__ == "__main__":
    root = Tk()
    root.title("Study Manager")
    StudyManagerApp()
    root.mainloop()
