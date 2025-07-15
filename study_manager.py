"""This file let's users adds events to manage study an time."""
from tkinter import *
from tkinter import font, messagebox, filedialog
from tkmacosx import Button
from datetime import datetime
import customtkinter as ctk
from tkcalendar import Calendar


class StudyManagerApp():
    """Main application class for study manager."""

    def create_db_gui(self):
        """Create the UI of the dashboard."""
        # Configures the window
        root.geometry("850x600")
        root.configure(bg="#313131")
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(0, weight=1)

        self.focus_tab = True

        red_alert = "#AD4849"
        yellow_alert = "#CFB353"

        large_font = font.Font(family="Helvetica", size=14)

        # Changes the grid on the button frame to adjust button spacing
        self.button_frame = Frame(self.app_frame,
                                  bg=self.background)
        self.button_frame.grid(row=0, column=0, columnspan=2, sticky="ew")
        self.button_frame.grid_columnconfigure(0, weight=0)
        self.button_frame.grid_columnconfigure(1, weight=0)
        self.button_frame.grid_columnconfigure(2, weight=0)
        self.button_frame.grid_columnconfigure(3, weight=1)

        # Creates basic UI layout
        self.save_button = Button(self.button_frame,
                                  text="Save",
                                  bg=self.btn_background,
                                  fg=self.text_colour,
                                  width=70,
                                  height=30,
                                  borderless=1,
                                  command=lambda: self.save_data())
        self.save_button.grid(row=0, column=0, sticky="nw")

        self.load_button = Button(self.button_frame,
                                  text="Load",
                                  bg=self.btn_background,
                                  fg=self.text_colour,
                                  width=70,
                                  height=30,
                                  borderless=1,
                                  command=lambda: self.load_data())
        self.load_button.grid(row=0, column=1, sticky="nw")

        self.all_tasks_button = Button(self.button_frame,
                                       text="All Tasks",
                                       bg=self.btn_background,
                                       fg=self.text_colour,
                                       width=120,
                                       height=30,
                                       borderless=1,
                                       command=lambda: self.view_all_tasks())
        self.all_tasks_button.grid(row=0, column=2, padx=20, sticky="nw")

        self.db_label = Label(self.app_frame,
                              text="Dashboard",
                              font=("Helvetica", "20"),
                              bg=self.background,
                              fg=self.text_colour)
        self.db_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        self.db_holder = Frame(self.app_frame, bg=self.background)
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
        Label(self.db_task_frame,
              text="No upcoming events.",
              bg=red_alert,
              fg=self.text_colour).grid(pady=10, padx=10)

        self.db2_task_frame = ctk.CTkFrame(self.db_holder,
                                           corner_radius=20,
                                           fg_color=yellow_alert,
                                           width=350,
                                           height=130,
                                           border_color="black",
                                           border_width=1)
        self.db2_task_frame.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.db2_task_frame.grid_propagate(False)
        Label(self.db2_task_frame,
              text="No upcoming events.",
              bg=yellow_alert,
              fg=self.text_colour).grid(pady=10, padx=10)

        self.color_switch_btn = ctk.CTkButton(self.db_holder,
                                              text=self.change_colour_txt,
                                              corner_radius=20,
                                              fg_color="#4C9C89",
                                              text_color=self.text_colour,
                                              width=260,
                                              height=60,
                                              border_color="#000000",
                                              border_width=1,
                                              command=lambda: self.switch_colour())
        self.color_switch_btn.grid(row=2, column=0, padx=20, pady=30, sticky="s")

        self.add_task_button = ctk.CTkButton(self.button_frame,
                                             text="+ Add Task",
                                             corner_radius=10,
                                             fg_color="#5DAC70",
                                             text_color=self.text_colour,
                                             height=50,
                                             width=90,
                                             command=lambda: self.to_add_task())
        self.add_task_button.grid(row=0, column=3, padx=10, pady=15, sticky="e")
        self.add_task_button.configure(state=NORMAL)

        self.db_cal_frame = Frame(self.app_frame,
                                       width=320,
                                       bg=self.background)
        self.db_cal_frame.grid(row=2, column=1, padx=10, pady=10, sticky="nw")

        self.db_cal_frame.grid_rowconfigure(0, weight=0)
        self.db_cal_frame.grid_rowconfigure(1, weight=0)
        self.db_cal_frame.grid_columnconfigure(0, weight=1)

        self.cal = Calendar(self.db_cal_frame, selectmode="day", font=large_font)
        self.change_cal_colour(self.cal)  # Chooses dark or light colour for calendar
        self.cal.grid(row=0, column=0)

        self.found_event_btn = ctk.CTkButton(self.db_cal_frame,
                                                text="Select a date and click me",
                                                width=190,
                                                height=60,
                                                fg_color="#456D98",
                                                text_color=self.text_colour,
                                                border_color="#000000",
                                                border_width=1,
                                                corner_radius=10,
                                                command=lambda: self.cal_show_task())
        self.found_event_btn.grid(row=1, column=0, pady=50, sticky="s")

    def __init__(self):
        """Initialize main frame and colour theme."""
        # Sets colour theme for different mode
        self.light_mode = ["#F8F5F2", "#F5F5F5", "#000000", "Dark Mode"]
        self.dark_mode = ["#313131", "#494444", "#FFFFFF",  "Light Mode"]
        self.colours = self.light_mode
        self.background = self.colours[0]
        self.btn_background = self.colours[1]
        self.text_colour = self.colours[2]
        self.change_colour_txt = self.colours[3]

        # Creates and configures main frame
        self.app_frame = Frame(bg=self.background)
        self.app_frame.grid(sticky=NSEW)
        self.app_frame.grid_columnconfigure(0, weight=1)
        self.app_frame.grid_columnconfigure(1, weight=1)
        self.app_frame.grid_rowconfigure(2, weight=0)
        self.app_frame.grid_rowconfigure(3, weight=0)
        self.events = []
        self.create_db_gui()  # Calls to create the dashboard GUI

    def to_add_task(self):
        """Open Add Task window for creating a new task."""
        DisplayAddTask(self, None)
    
    def event_to_db(self):
        """Refresh the dashboard page showing new events."""
        # Clears all the content in the DB frames
        if self.events:
            for frame in [self.db_task_frame, self.db2_task_frame]:
                for widget in frame.winfo_children():
                    widget.destroy()

        today = datetime.today().date()
        # Sorts events from earliest to latest in a list
        earliest_events = sorted(self.events, key=lambda event: datetime.strptime(event.due_date, "%m/%d/%y"))

        # Add the first 2 earliest events to dashboard
        count = 0
        for event in earliest_events[:2]:
            count += 1
            type = f"{event.type}"
            subject = f"{event.subject}"

            event_date = datetime.strptime(event.due_date, "%m/%d/%y").date()
            days_remain = (event_date-today).days

            # Change colour based on importancy
            if days_remain <= 3:
                alert_colour = "#AD4849"
            elif days_remain >= 4 and days_remain <= 7:
                alert_colour = "#CFB353"
            else:
                alert_colour = "#5DAC70"

            if count == 1:
                frame = self.db_task_frame
            else:
                frame = self.db2_task_frame

            frame.configure(fg_color=alert_colour)
            frame.pack_propagate(False)  # Keeps the frame size constant

            # Adds event information to UI
            type_label = Label(frame,
                               text=type,
                               font=("Helvetica", 12, "bold"),
                               bg=alert_colour,
                               fg=self.text_colour)
            type_label.pack(anchor="w", pady=4, padx=10)

            subject_label = Label(frame,
                                  text=subject,
                                  font=("Helvetica", 18),
                                  bg=alert_colour,
                                  fg=self.text_colour)
            subject_label.pack(anchor="w", pady=5, padx=10)

            due_str = event_date.strftime("%d/%m/%Y")
            due_label = Label(frame,
                              text=f"{due_str} -- {days_remain} day(s) away!",
                              font= ("Helvetica", 14),
                              bg= alert_colour,
                              fg=self.text_colour)
            due_label.pack(anchor="w", padx=10)
            # fix text errors
            if days_remain == 0:
                due_label.configure(text=f"{due_str} -- Due TODAY!")
            elif days_remain < 0:
                overdue_days = (today-event_date).days
                due_label.configure(text=f"{due_str} -- OVERDUE by {overdue_days} day(s)!")

    def cal_show_task(self):
        """Display event info for selected calendar date."""
        date = self.cal.get_date()
        found_event = []

        # Finds event with same date as calendar choice
        for event in self.events:
            if date == event.due_date:
                found_event.append(event)

        # If event is found, show it on UI
        try:
            event = found_event[0]
            event_date = datetime.strptime(event.due_date, "%m/%d/%y").date()
            due_str = event_date.strftime("%d/%m/%Y")
            # if multiple events are on the same day
            if len(found_event) > 1:
                event_str = f"Multiple events on this day. Here is one:\n{event.type} for {event.subject} on {due_str}."
            else:
                event_str = f"{event.type} for {event.subject} on {due_str}."
            self.found_event_btn.configure(text=event_str)
        # If not event is found
        except IndexError:
            self.found_event_btn.configure(text="No event found on that day.")

    def save_data(self):
        """Save all events as a .txt file."""
        # saves file as shown .txt
        with open('study_manager.txt', 'w') as text_file:
            for event in self.events:
                # Replaces the new lines in description with a placemarker
                format_description = event.description.replace('\n', '\\n')
                text_file.write(f"{event.subject}|{event.type}|{format_description}|{event.due_date}\n")
        messagebox.showinfo("Saved!", "File saved successfully!")
        
    def load_data(self):
        """Load the saved .txt file"""
        filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        self.events=[]

        # Processes saved data and adds it to event list
        with open(filepath, "r") as file:
            for line in file:
                line=line.strip()
                parts = line.split("|")

                subject, event_type, description, due_date = parts
                description = description.replace("\\n", "\n")

                self.events.append(Event(subject=subject, event_type=event_type, description=description, due_date=due_date))

        # Add events to the tab based on what user is on
        if self.focus_tab == True:
            self.event_to_db()
        else:
            self.view_all_tasks()

    def view_all_tasks(self):
        """Show all the events added in the manager."""
        # Wipe everything in the app frame
        for widget in self.app_frame.winfo_children():
            widget.destroy()

        root.geometry("950x600")

        self.focus_tab = False

        scroll_label_font = ("Helvetica", 16, "bold")

        # Sets up button frame and creates buttons
        self.button_frame = Frame(self.app_frame, bg=self.background)
        self.button_frame.pack(fill="x")

        self.save_button = Button(self.button_frame,
                                  text="Save",
                                  bg=self.background,
                                  fg=self.text_colour,
                                  width=70,
                                  height=30,
                                  borderless=1,
                                  command=lambda: self.save_data())
        self.save_button.pack(side="left")

        self.load_button = Button(self.button_frame,
                                  text="Load",
                                  bg=self.background,
                                  fg=self.text_colour,
                                  width=70,
                                  height=30,
                                  borderless=1,
                                  command=lambda: self.load_data())
        self.load_button.pack(side="left")

        self.db_button = Button(self.button_frame,
                                text="Dashboard",
                                bg=self.background,
                                fg=self.text_colour,
                                width=120,
                                height=30,
                                borderless=1,
                                command=lambda: self.to_db())
        self.db_button.pack(padx=20, side="left")

        self.add_task_button = ctk.CTkButton(self.button_frame,
                                             text="+ Add Task",
                                             corner_radius=10,
                                             fg_color="#5DAC70",
                                             text_color=self.text_colour,
                                             height=50,
                                             width=90, 
                                             command=lambda: self.to_add_task())
        self.add_task_button.pack(side="right", padx=10, pady=15)
        self.add_task_button.configure(state=NORMAL)

        # Sets up the 3 main scrollable frames
        self.left_frame = ctk.CTkScrollableFrame(self.app_frame,
                                                 orientation="vertical",
                                                 fg_color=self.background,
                                                 label_text="Imminent",
                                                 label_text_color=self.text_colour,
                                                 label_fg_color=self.background,
                                                 label_font=scroll_label_font,)
        self.left_frame.pack(side="left", fill="both", expand=True, padx=1, pady=20)

        self.mid_frame = ctk.CTkScrollableFrame(self.app_frame,
                                                orientation="vertical",
                                                fg_color=self.background,
                                                label_text="Close",
                                                label_text_color=self.text_colour,
                                                label_fg_color=self.background,
                                                label_font=scroll_label_font)
        self.mid_frame.pack(side="left", fill="both", expand=True, padx=1, pady=20)

        self.right_frame = ctk.CTkScrollableFrame(self.app_frame,
                                                  orientation="vertical",
                                                  fg_color=self.background,
                                                  label_text="Far",
                                                  label_text_color=self.text_colour,
                                                  label_fg_color=self.background,
                                                  label_font=scroll_label_font)
        self.right_frame.pack(side="left", fill="both", expand=True, padx=1, pady=20)

        today = datetime.today().date()
        # Sorts events based on earliest date in a list
        earliest_events = sorted(self.events, key=lambda event: datetime.strptime(event.due_date, "%m/%d/%y"))

        # Adds every event to UI
        for event in earliest_events:
            type = f"{event.type}"
            subject = f"{event.subject}"

            event_date = datetime.strptime(event.due_date, "%m/%d/%y").date()
            days_remain = (event_date-today).days
            
            # Chooses what frame to put event in
            if days_remain <= 3:
                alert_colour = "#AD4849"
                date_frame = self.left_frame

            elif days_remain >= 4 and days_remain <= 7:
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

            # Frame for delete and expand/edit button
            top_row = Frame(event_frame, bg=alert_colour)
            top_row.pack(fill="x", pady=5, padx=10)

            delete_btn = Button(top_row,
                                text="x",
                                height=20,
                                width=20,
                                bg=alert_colour,
                                fg=self.text_colour,
                                borderless=1,
                                command=lambda e=event: self.delete_task(e))
            delete_btn.pack(side="right")

            expand_btn = Button(top_row,
                                text="↵",
                                height=20,
                                width=20,
                                bg=alert_colour,
                                fg=self.text_colour,
                                borderless=1,
                                command= lambda e=event: self.to_edit_task(e))
            expand_btn.pack(side="right")

            type_label = Label(top_row,
                               text=type,
                               font=("Helvetica", 12, "bold"),
                               bg=alert_colour,
                               fg=self.text_colour)
            type_label.pack(anchor="w")

            subject_label = Label(event_frame,
                                  text=subject,
                                  font=("Helvetica", 18),
                                  bg=alert_colour,
                                  fg=self.text_colour)
            subject_label.pack(anchor="w", pady=5, padx=10)

            due_str = event_date.strftime("%d/%m/%Y")
            due_label = Label(event_frame,
                              text=f"{due_str} -- {days_remain} day(s) away!",
                              font=("Helvetica", 14),
                              bg=alert_colour,
                              fg=self.text_colour)
            due_label.pack(anchor="w", padx=10)
            # Fixing text errors 
            if days_remain == 0:
                due_label.configure(text=f"{due_str} -- Due TODAY!")
            elif days_remain < 0:
                overdue_days = (today-event_date).days
                due_label.configure(text=f"{due_str} -- OVERDUE by {overdue_days} day(s)!")

    def to_db(self):
        """Wipe tab and create dashboard."""
        for widget in self.app_frame.winfo_children():
            widget.destroy()

        self.create_db_gui()
        self.event_to_db()

    def to_edit_task(self, event):
        """Call class with event."""
        DisplayAddTask(self, event)
       
    def delete_task(self, event):
        """Delete user chosen event."""
        # Remove event if in list
        if event in self.events:
            self.events.remove(event)

        # Refreshes the correct tab
        if self.focus_tab:
            self.event_to_db()
        else:
            self.view_all_tasks()

    def switch_colour(self):
        """Switch colour theme of application."""
        # Switches to opposite colour theme
        if self.colours == self.light_mode:
            self.colours = self.dark_mode
        else:
            self.colours = self.light_mode

        self.background = self.colours[0]
        self.btn_background = self.colours[1]
        self.text_colour = self.colours[2]
        self.change_colour_txt = self.colours[3]

        # Resets app frame with new colour
        self.app_frame.destroy()
        self.app_frame = Frame(root, bg=self.background)
        self.app_frame.grid(sticky=NSEW)
        self.app_frame.grid_columnconfigure(0, weight=1)
        self.app_frame.grid_columnconfigure(1, weight=1)
        self.app_frame.grid_rowconfigure(2, weight=0)
        self.app_frame.grid_rowconfigure(3, weight=0)

        # Refresh the correct tab
        if self.focus_tab:
            self.create_db_gui()
            self.event_to_db()
        else:
            self.view_all_tasks()

    def change_cal_colour(self, cal):
        """Change colour of calendar based on dark or light mode"""
        if self.colours == self.dark_mode:
            cal.configure(background='#2e2e2e',
                               foreground='white',
                               headersbackground='#1c1c1c',
                               headersforeground='white',
                               selectbackground='#4a90e2',
                               selectforeground='white',
                               normalbackground='#2e2e2e',
                               normalforeground='white',
                               weekendbackground='#3e3e3e',
                               weekendforeground='white',
                               othermonthbackground='#1c1c1c',
                               othermonthforeground='gray',
                               bordercolor='black',
                               disableddaybackground="#1c1c1c",
                               disableddayforeground="#gray",
                               tooltipbackground="black",
                               tooltipforeground="white")
        else:
            cal.configure(background='white',
                               foreground='black',
                               headersbackground='lightgray',
                               headersforeground='black',
                               selectbackground='#4a90e2',
                               selectforeground='white',
                               normalbackground='white',
                               normalforeground='black',
                               weekendbackground='white',
                               weekendforeground='black',
                               othermonthbackground='lightgray',
                               othermonthforeground='gray',
                               bordercolor='black',
                               disableddaybackground='lightgray',
                               disableddayforeground='gray',
                               tooltipbackground='white',
                               tooltipforeground='black')

class DisplayAddTask():
    """Window that lets user add and edit tasks."""
    
    def __init__(self, partner, event):
        """Initialize the add/edit task window."""
        self.firstclick = True  # user hasn't clicked yet
        self.event = event
        today = datetime.today()

        self.colours = partner.colours
        background = self.colours[0]
        text_colour = self.colours[2]

        med_font = font.Font(family="Helvetica", size=16)
        small_font = font.Font(family="Helvetica", size=14)

        # Chooses text based on action
        if event:
            action_text = "Edit Task"
        else:
            action_text = "Add Task"

        # Creates new window
        self.add_task_gui = Toplevel()
        self.add_task_gui.geometry("700x550")
        self.add_task_gui.configure(bg=background)

        partner.add_task_button.configure(state=DISABLED)  # Disables add task button
        # if user presses 'x', delete window
        self.add_task_gui.protocol("WM_DELETE_WINDOW",
                               lambda: self.close_add_task(partner))

        # Creates UI
        title_label = Label(self.add_task_gui,
                            text=action_text,
                            font=font.Font(family="Helvetica", size=18, weight="bold"),
                            bg=background,
                            fg=text_colour)
        title_label.pack(pady=20)

        self.main_frame = Frame(self.add_task_gui, bg=background)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.left_side_frame = Frame(self.main_frame, bg=background)
        self.left_side_frame.pack(side="left", fill="both", expand=True, padx=20)

        self.task_type_label = Label(self.left_side_frame,
                                     text="Choose type of task:",
                                     bg=background,
                                     font=med_font,
                                     fg=text_colour)
        self.task_type_label.pack(anchor="w", pady=10)

        self.rad_var = StringVar()
        for choice in ["Exam", "Assignment", "Homework", "Study Session"]:
            self.rad_option = Radiobutton(self.left_side_frame, text=choice, variable=self.rad_var, value=choice,
                        font=small_font, bg=background, anchor="w", fg=text_colour)
            self.rad_option.pack(anchor="w")
        if event:
            self.rad_var.set(event.type)

        self.subject_lb = Label(self.left_side_frame,
                                text="Subject",
                                bg=background,
                                font=med_font,
                                fg=text_colour)
        self.subject_lb.pack(anchor="w", pady=10)

        self.subject_entry = Entry(self.left_side_frame,
                                   font=small_font,
                                   width=25)
        self.subject_entry.pack(anchor="w", pady=5)
        if event:
            self.subject_entry.insert(0, event.subject)

        self.description_lb = Label(self.left_side_frame,
                                    text="Description",
                                    bg=background,
                                    font=med_font,
                                    fg=text_colour)
        self.description_lb.pack(anchor="w", pady=10)

        self.description_entry = Text(self.left_side_frame,
                                      font=small_font,
                                      bg="#FFFFFF",
                                      width=25,
                                      height=5)
        self.description_entry.pack(anchor="w", pady=5)
        # if editing event insert it's description.
        if event:
            self.description_entry.insert("1.0", event.description)
        # if not, optional
        else:
            self.description_entry.insert("1.0", "Optional")
            self.description_entry.bind('<FocusIn>', lambda event: self.on_entry_click(event))

        self.right_side_frame = Frame(self.main_frame, bg=background)
        self.right_side_frame.pack(side="right", fill="both", expand=True, padx=20)

        self.due_date_lb = Label(self.right_side_frame,
                                 text="Set Due Date",
                                 bg=background,
                                 fg=text_colour,
                                 font=med_font,)
        self.due_date_lb.pack(pady=10)

        self.cal = Calendar(self.right_side_frame,
                            selectmode="day",
                            font=med_font,
                            mindate=today)
        partner.change_cal_colour(self.cal)  # Choose dark of light colours
        self.cal.pack(pady=10)
        if event:
            self.cal.selection_set(datetime.strptime(event.due_date, "%m/%d/%y"))

        submit_button = ctk.CTkButton(self.add_task_gui, 
                                      text=action_text,
                                      corner_radius=10,
                                      command=lambda: self.add_task(partner),
                                      font=ctk.CTkFont(family="Helvetica", size=16),
                                      fg_color="#5DAC70",
                                      text_color=text_colour,
                                      width=140,
                                      height=70)
        submit_button.pack(pady=20)

    def add_task(self, partner):
        """Adds event to class."""
        # Get user input values
        task_type = self.rad_var.get()
        subject = self.subject_entry.get()
        description = self.description_entry.get("1.0", "end")
        due_date = self.cal.get_date()

        # If nothing has been entered
        if task_type == "":
            messagebox.showerror("Missing Info", "Please select a task type.")
            return
        if subject == "":
            messagebox.showerror("Missing Info", "Please enter a subject.")
            return
        # If the user does not click description box at all
        if description.strip() == "Optional":
            description = ""

        # Editing task
        if self.event:
            self.event.type = task_type
            self.event.subject = subject
            self.event.description = description
            self.event.due_date = due_date
        # Adding new task
        else:
            new_event = Event(subject=subject, event_type=task_type, description=description, due_date=due_date)
            partner.events.append(new_event)
            print(f"Task: {new_event.subject}, ({new_event.type}), Due: {new_event.due_date}, Description: {new_event.description}")

        # Refresh correct tab
        if partner.focus_tab == True:
            partner.event_to_db()
        else:
            partner.view_all_tasks()
        self.close_add_task(partner)
    
    def on_entry_click(self, event):
        """Remove optional text when user clicks description"""
        if self.firstclick:
            self.firstclick = False
            self.description_entry.delete("1.0", "end") 

    def close_add_task(self, partner):
        """Close Add Task GUI and enable the button"""
        partner.add_task_button.configure(state=NORMAL)  # Enables add task button
        self.add_task_gui.destroy()  # Destroys window

class Event():
    """Represents a single event"""

    def __init__(self, subject, event_type, description, due_date):
        """Initialize event arguments."""
        self.subject = subject
        self.type = event_type
        self.description = description
        self.due_date = due_date

# Runs application
if __name__ == "__main__":
    root = Tk()
    root.title("Study Manager")
    StudyManagerApp()
    root.mainloop()
