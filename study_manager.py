from tkinter import *
from tkinter import ttk, font
from tkmacosx import Button
from datetime import datetime
import customtkinter as ctk
from tkcalendar import Calendar

class StudyManagerApp():
    def __init__(self):
        self.events=[]
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
    
    def event_to_db(self):
        today = datetime.today()
        
        earliest_events = sorted(self.events, key=lambda event: datetime.strptime(event.due_date, "%m/%d/%y"))
        
        for event in earliest_events:
            type = f"{event.type}"
            subject = f"{event.subject}"
            due_date = f"{event.due_date}"
            
            event_date = datetime.strptime(event.due_date, "%m/%d/%y")
            days_remain = (event_date-today).days

            if days_remain <= 3:
                alert_colour = "#AD4849"
            elif days_remain >= 4 and days_remain <=7:
                alert_colour = "#CFB353"
            else:
                alert_colour = "#5DAC70"
            
            task_info = Frame(self.db_task_frame, bg= alert_colour)
            task_info.pack(anchor="w", fill="x")
            type_label = Label(self.db_task_frame,
                                       text=type,
                                       font=("Helvetica", 12, "bold"),
                                       bg=alert_colour
                                       )
            type_label.pack(anchor="nw")
            
            subject_label = Label(task_info,
                                    text=subject,
                                    font=("Helvetica", 18),
                                    bg=alert_colour)
            subject_label.pack(anchor="w", pady=5, padx=10)
            
            due_str = event_date.strftime("%B %d, %Y")
            due_label = Label(task_info,
                              text=f"{due_str} -- {days_remain} day(s) away!",
                              font= ("Helvetica", 14),
                              bg= alert_colour)
            due_label.pack(anchor="w", padx=10)

class DisplayAddTask():
    def __init__(self, partner):
        self.firstclick=True
        background = "#F8F5F2"
        med_font = font.Font(family="Helvetica", size=16)
        small_font = font.Font(family="Helvetica", size=14)
        
        self.add_task_gui = Toplevel()
        self.add_task_gui.geometry("700x500")
        self.add_task_gui.configure(bg=background)
        
        partner.add_task_button.configure(state=DISABLED)
        self.add_task_gui.protocol("WM_DELETE_WINDOW",
                               lambda: self.close_task(partner))
        
        title_label = Label(self.add_task_gui,
                            text="Add Task",
                            font=font.Font(family="Helvetica", size=18, weight="bold"),
                            bg=background)
        title_label.pack(pady=20)

        self.main_frame = Frame(self.add_task_gui, bg=background)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.left_side_frame = Frame(self.main_frame, bg=background)
        self.left_side_frame.pack(side="left", fill="both", expand=True, padx=20)

        self.task_type_label = Label(self.left_side_frame, 
                                     text="Choose type of task:",
                                     bg=background,
                                     font=med_font)
        self.task_type_label.pack(anchor="w", pady=10)

        self.rad_var = StringVar()
        for choice in ["Exam", "Assignment", "Study Session"]:
            self.rad_option = Radiobutton(self.left_side_frame, text=choice, variable=self.rad_var, value=choice,
                        font=small_font, bg=background, anchor="w")
            self.rad_option.pack(anchor="w")
            
        self.subject_lb = Label(self.left_side_frame,
                                text="Subject",
                                bg=background,
                                font=med_font)
        self.subject_lb.pack(anchor="w", pady=10)
        
        self.subject_entry = Entry(self.left_side_frame,
                                   font=small_font,
                                   width=25)
        self.subject_entry.pack(anchor="w", pady=5)
    
        self.description_lb = Label(self.left_side_frame,
                                 text="Description",
                                 bg=background,
                                 font=med_font)
        self.description_lb.pack(anchor="w", pady=10)
        
        self.description_entry = Text(self.left_side_frame, 
                                       font=small_font,
                                       bg="#FFFFFF",
                                       width=25,
                                       height=5)
        self.description_entry.pack(anchor="w", pady=5)
        self.description_entry.insert("1.0", "Optional")
        self.description_entry.bind('<FocusIn>', lambda event : self.on_entry_click(event))


        self.right_side_frame = Frame(self.main_frame, bg=background)
        self.right_side_frame.pack(side="right", fill="both", expand=True, padx=20)

        self.due_date_lb = Label(self.right_side_frame,
                                 text="Set Due Date",
                                 bg=background,
                                 font=med_font)
        self.due_date_lb.pack(pady=10)
        
        self.calendar = Calendar(self.right_side_frame, selectmode="day", font=med_font)
        self.calendar.pack(pady=10)

        submit_button = ctk.CTkButton(self.add_task_gui, 
                               text="Add Task",
                               corner_radius=10,
                               command=lambda: self.add_task(partner),
                               font=ctk.CTkFont(family="Helvetica", size=16),
                               fg_color="#5DAC70",
                               width=140,
                               height=70)
        submit_button.pack(pady=20)
        
    def add_task(self, partner):
        task_type = self.rad_var.get()
        subject = self.subject_entry.get()
        description = self.description_entry.get("1.0", "end")
        due_date = self.calendar.get_date()
        
        new_event = Event(subject=subject, event_type=task_type, description=description, due_date=due_date)
        partner.events.append(new_event)

        print(f"Task: {new_event.subject}, ({new_event.type}), Due: {new_event.due_date}, Description: {new_event.description}")
        partner.event_to_db()
        self.close_task(partner)
    
    def on_entry_click(self, event):    
        if self.firstclick:
            self.firstclick = False
            self.description_entry.delete("1.0", "end") 

    def close_task(self, partner):
        """
        Closes Add Task GUI and enables the button
        """
        
        partner.add_task_button.configure(state=NORMAL)
        self.add_task_gui.destroy()
        
    

class Event():
    def __init__(self, subject, event_type, description, due_date):
        self.subject = subject
        self.type = event_type
        self.description = description
        self.due_date = due_date

if __name__ == "__main__":
    root = Tk()
    root.title("Study Manager")
    StudyManagerApp()
    root.mainloop()
