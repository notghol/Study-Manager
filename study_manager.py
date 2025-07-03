from tkinter import *
from tkinter import ttk, font, messagebox, filedialog
from tkmacosx import Button
from datetime import datetime
import customtkinter as ctk
from tkcalendar import Calendar

class StudyManagerApp():
    def create_db_gui(self):
        root.geometry("850x600")
        root.configure(bg="#F8F5F2")
        self.focus_tab = True
        
        red_alert = "#AD4849"
        yellow_alert = "#CFB353"
        
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(0, weight=1)
        
    
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
                                borderless=1,
                                command=lambda: self.save_data())  
    
        self.save_button.grid(row=0, column=0, sticky="nw")

        self.load_button = Button(self.button_frame,
                                text="Load",
                                bg="#F5F5F5",
                                width=70,
                                height=30,
                                borderless=1,
                                command=lambda: self.load_data())
        self.load_button.grid(row=0, column=1, sticky="nw")
        
        self.all_tasks_button = Button(self.button_frame,
                                       text="All Tasks",
                                       bg="#F5F5F5",
                                       width=120,
                                       height=30,
                                       borderless=1,
                                       command= lambda: self.view_all_tasks())
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
        self.db_task_frame.grid_propagate(False)
        Label(self.db_task_frame, text="No upcoming events.", bg=red_alert).grid(pady=10, padx=10)

        self.db2_task_frame = ctk.CTkFrame(self.db_holder,
                                           corner_radius=20,
                                           fg_color=yellow_alert,
                                           width=350,
                                           height=130,
                                           border_color="black",
                                           border_width=1)
        self.db2_task_frame.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.db2_task_frame.grid_propagate(False)
        Label(self.db2_task_frame, text="No upcoming events.", bg=yellow_alert).grid(pady=10, padx=10)
        
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

        self.calendar = Calendar(self.db_calendar_frame, selectmode="day", font=large_font)
        self.calendar.grid(row=0, column=0)

        self.found_event_button = ctk.CTkButton(self.db_calendar_frame,
                                        text="Select a date and click me",
                                        width=190,
                                        height=60,
                                        fg_color="#FFFFFF",
                                        text_color="#000000",
                                        border_color= "#000000",
                                        border_width=1,
                                        corner_radius=10,
                                        command=lambda:self.cal_show_task())
        self.found_event_button.grid(row=1, column=0, pady=50, sticky="s")
    
    def __init__(self):
        self.app_frame = Frame(bg="#F8F5F2")
        self.app_frame.grid(sticky=NSEW)
        self.app_frame.grid_columnconfigure(0, weight=1)
        self.app_frame.grid_columnconfigure(1, weight=1)
        self.app_frame.grid_rowconfigure(2, weight=0)
        self.app_frame.grid_rowconfigure(3, weight=0)
        self.events=[]
        self.create_db_gui()
        
    def to_add_task(self):
        DisplayAddTask(self)
    
    def event_to_db(self):
        if self.events:
            for frame in [self.db_task_frame, self.db2_task_frame]:
                for widget in frame.winfo_children():
                    widget.destroy()

        today = datetime.today()
        
        earliest_events = sorted(self.events, key=lambda event: datetime.strptime(event.due_date, "%m/%d/%y"))
        count = 0
        for event in earliest_events[:2]:
            count +=1
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
            
            if count == 1:
                frame = self.db_task_frame
            else:
                frame = self.db2_task_frame
                
            frame.configure(fg_color=alert_colour)
            frame.pack_propagate(False)
            
            type_label = Label(frame,
                               text=type,
                               font=("Helvetica", 12, "bold"),
                               bg=alert_colour)
            type_label.pack(anchor="w", pady=4, padx=10)
            
            subject_label = Label(frame,
                                    text=subject,
                                    font=("Helvetica", 18),
                                    bg=alert_colour)
            subject_label.pack(anchor="w", pady=5, padx=10)
            
            due_str = event_date.strftime("%d/%m/%Y")
            due_label = Label(frame,
                              text=f"{due_str} -- {days_remain} day(s) away!",
                              font= ("Helvetica", 14),
                              bg= alert_colour)
            due_label.pack(anchor="w", padx=10)

    def cal_show_task(self):
        date = self.calendar.get_date()
        found_event = []
        for event in self.events:
            if date == event.due_date:
                found_event.append(event)
                break
        try:
            event = found_event[0]
            event_str = f"{event.type} for {event.subject} on {event.due_date}"
            self.found_event_button.configure(text=event_str)
        except IndexError:
            self.found_event_button.configure(text="No event found on that day.")
                
    def save_data(self):
        with open('study_manager.txt', 'w') as text_file:
            for event in self.events:
                format_description = event.description.replace('\n', '\\n')
                
                text_file.write(f"{event.subject}|{event.type}|{format_description}|{event.due_date}\n")
        messagebox.showinfo("Saved!", "File saved successfully!")
        
    def load_data(self):
        filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        self.events=[]
        with open(filepath, "r") as file:
            for line in file:
                line=line.strip()
                parts = line.split("|")
                
                subject, event_type, description, due_date = parts
                description = description.replace("\\n", "\n")
                
                self.events.append(Event(subject=subject, event_type=event_type, description=description, due_date=due_date))
        if self.focus_tab == True:
            self.event_to_db()
        else:
            self.view_all_tasks()

    def view_all_tasks(self):
        for widget in self.app_frame.winfo_children():
            widget.destroy()
        root.geometry("950x600")
        self.focus_tab = False
        background = "#F8F5F2"
        
        
        self.button_frame = Frame(self.app_frame, bg=background)
        self.button_frame.pack(fill="x")
        
        self.save_button = Button(self.button_frame,
                                text="Save",
                                bg="#F5F5F5",
                                width=70,
                                height=30,  
                                borderless=1,
                                command=lambda: self.save_data())  
    
        self.save_button.pack(side="left")

        self.load_button = Button(self.button_frame,
                                text="Load",
                                bg="#F5F5F5",
                                width=70,
                                height=30,
                                borderless=1,
                                command= lambda: self.load_data())
        self.load_button.pack(side="left")
        
        self.db_button = Button(self.button_frame,
                                       text="Dashboard",
                                       bg="#F5F5F5",
                                       width=120,
                                       height=30,
                                       borderless=1,
                                       command= lambda: self.to_db())
        self.db_button.pack(padx=20, side="left")
        
        self.add_task_button = ctk.CTkButton(self.button_frame,
                                        text="+ Add Task",
                                        corner_radius=10,
                                        fg_color="#5DAC70",
                                        height=50,
                                        width=90, 
                                        command=lambda: self.to_add_task())
        self.add_task_button.pack(side="right", padx=10, pady=15)
        self.add_task_button.configure(state=NORMAL)
        
        self.left_frame = Frame(self.app_frame, bg=background)
        self.left_frame.pack(side="left", fill="both", expand=True, padx=1, pady=20)
        self.left_frame.pack_propagate(False)
        
        self.mid_frame = Frame(self.app_frame, bg=background)
        self.mid_frame.pack(side="left", fill="both", expand=True, padx=1, pady=20)
        self.mid_frame.pack_propagate(False)
        
        self.right_frame = Frame(self.app_frame, bg=background)
        self.right_frame.pack(side="left", fill="both", expand=True, padx=1, pady=20)
        self.right_frame.pack_propagate(False)
        
        label_font = font.Font(family="Helvetica", size=16, weight="bold")
        
        Label(self.left_frame, text="Imminent", font=label_font, bg=background).pack()
        Label(self.mid_frame, text="Close", font=label_font, bg=background).pack()
        Label(self.right_frame, text="Far", font=label_font, bg=background).pack()
        
        today = datetime.today()
        earliest_events = sorted(self.events, key=lambda event: datetime.strptime(event.due_date, "%m/%d/%y"))
        for event in earliest_events:
            type = f"{event.type}"
            subject = f"{event.subject}"
            
            event_date = datetime.strptime(event.due_date, "%m/%d/%y")
            days_remain = (event_date-today).days
            
            if days_remain <= 3:
                alert_colour = "#AD4849"
                date_frame = self.left_frame
                
            elif days_remain >= 4 and days_remain <=7:
                alert_colour = "#CFB353"
                date_frame = self.mid_frame
            else:
                alert_colour = "#5DAC70"
                date_frame = self.right_frame
                
            event_frame = ctk.CTkFrame(date_frame,
                                       corner_radius=20,
                                       border_color="black",
                                       border_width=1,
                                       width=300,
                                       height=110,
                                       fg_color=alert_colour)
            event_frame.pack(pady=10)
            event_frame.pack_propagate(False)

            top_row = Frame(event_frame, bg=alert_colour)
            top_row.pack(fill="x", pady=5, padx=10)

            self.expand_btn = Button(top_row,
                                     text="↵",
                                     height=20,
                                     width=20,
                                     bg=alert_colour,
                                     borderless=1)
            self.expand_btn.pack(side="right")

            type_label = Label(top_row,
                               text=type,
                               font=("Helvetica", 12, "bold"),
                               bg=alert_colour)
            type_label.pack(anchor="w")

            
            subject_label = Label(event_frame,
                                  text=subject,
                                  font=("Helvetica", 18),
                                  bg=alert_colour)
            subject_label.pack(anchor="w", pady=5, padx=10)
            
            due_str = event_date.strftime("%d/%m/%Y")
            due_label = Label(event_frame,
                              text=f"{due_str} -- {days_remain} day(s) away!",
                              font= ("Helvetica", 14),
                              bg= alert_colour)
            due_label.pack(anchor="w", padx=10)
                  
    def to_db(self):
        for widget in self.app_frame.winfo_children():
            widget.destroy()
        self.create_db_gui()
        self.event_to_db()
    
        
class DisplayAddTask():
    def __init__(self, partner):
        self.firstclick=True
        background = "#F8F5F2"
        med_font = font.Font(family="Helvetica", size=16)
        small_font = font.Font(family="Helvetica", size=14)
        
        self.add_task_gui = Toplevel()
        self.add_task_gui.geometry("700x550")
        self.add_task_gui.configure(bg=background)
        
        partner.add_task_button.configure(state=DISABLED)
        self.add_task_gui.protocol("WM_DELETE_WINDOW",
                               lambda: self.close_add_task(partner))
        
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
        for choice in ["Exam", "Assignment", "Homework", "Study Session"]:
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
        if partner.focus_tab == True:
            partner.event_to_db()
        else:
            partner.view_all_tasks()
        self.close_add_task(partner)
    
    def on_entry_click(self, event):    
        if self.firstclick:
            self.firstclick = False
            self.description_entry.delete("1.0", "end") 

    def close_add_task(self, partner):
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
