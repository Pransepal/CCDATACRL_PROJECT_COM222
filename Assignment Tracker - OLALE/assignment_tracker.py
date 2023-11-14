import bisect
from queue import Queue, PriorityQueue
import tkinter
from tkinter import END, Label, ttk, PhotoImage
from tkinter import messagebox
from tkinter.font import BOLD
from PIL import ImageTk, Image
import tkinter.simpledialog
from subprocess import call

class AssignmentTracker:
    def __init__(self, assignment_window):
        self.assignment_window = assignment_window
        #Assignment Window
        assignment_window.title("Assignmemt Tracker")
        
        assignment_window.geometry("500x600")
        
        assignment_window.state('zoomed')

        self.be_text = "Be Productive. Be Efficient. Be Organized"
        self.count = 0
        self.text = ''


    
        self.subjects = {}  

        #LABELS
        welcome_label = tkinter.Label(assignment_window, text= "Welcome, Assignment Tracker", fg='#4E70D9', bg='#E9BDCB', font=('Arial 14 bold'))
        welcome_label.place(x=20, y=20)

        track_label = tkinter.Label(assignment_window, text= "Track your upcoming activities", fg='#D48ACF', bg='#C2E3E7', font=('Arial', 8))
        track_label.place(x=20, y=50)

        take_note_label = tkinter.Label(assignment_window, text= "Take note:", fg='#D48ACF', bg='#C2E3E7', font=('Arial', 11))
        take_note_label.place(x=20, y=100)

        be_label = tkinter.Label(assignment_window, text=self.be_text, fg='#D48ACF', bg='#C2E3E7', font=('Arial 14 bold'))
        be_label.place(x=1000, y=20)
        self.be_label = be_label

        tracker_label = tkinter.Label(assignment_window, text= "Tracker", fg='#4E70D9', bg='#E9BDCB', font=('Arial', 11))
        tracker_label.place(x=900, y=100)

        subject_label = tkinter.Label(assignment_window, text= "Subjects", fg='#D48ACF', bg='#C2E3E7', font=('Arial', 14))
        subject_label.place(x=970, y=130)

        activity_label = tkinter.Label(assignment_window, text= "Activities", fg='#D48ACF', bg='#C2E3E7', font=('Arial', 14))
        activity_label.place(x=1300, y=130)

        activities_name_label = tkinter.Label(assignment_window, text= "Name:", fg='grey', bg='#C2E3E7', font=('Arial', 8))
        activities_name_label.place(x=1150, y=165)

        status_label = tkinter.Label(assignment_window, text= "Status:", fg='grey', bg='#C2E3E7', font=('Arial', 8))
        status_label.place(x=1150, y=190)

        due_label = tkinter.Label(assignment_window, text= "Due (YYYY-MM-DD)", fg='grey', bg='#C2E3E7', font=('Arial', 8))
        due_label.place(x=1335, y=190)

        prioritize_label = tkinter.Label(assignment_window, text= "Prioritize:", fg='#FFFCA6', bg='#B19BD9', font=('Arial 14 bold'))
        prioritize_label.place(x=650, y=100)


        #Getting Notes
        self.note_text = tkinter.Text(self.assignment_window, width=50, height=5)
        self.note_text.place(x=20, y=130)
        self.note_text.configure(bg='#FFFCA6')

        self.note_listbox = tkinter.Listbox(self.assignment_window, width=67, height=30, selectmode=tkinter.SINGLE,)
        self.note_listbox.place(x=20, y=260)
        self.note_listbox.configure(bg='#FFFCA6')

        #Buttons
        self.get_note_button = tkinter.Button(self.assignment_window, text="Get Note", command=self.update_note_listbox, bg="#B19BD9", fg="white")
        self.get_note_button.place(x=20, y=220)

        self.clear_note_button = tkinter.Button(self.assignment_window, text="Clear", command=self.clear_notes, bg="#B19BD9", fg="white")
        self.clear_note_button.place(x=90, y=220)

        self.delete_note_button = tkinter.Button(self.assignment_window, text="Delete Note", command=self.delete_notes, bg="#B19BD9", fg="white")
        self.delete_note_button.place(x=20, y=750)

        #Adding subject
        self.add_subject_entry = tkinter.Entry(self.assignment_window, width=30 )
        self.add_subject_entry.place(x=920, y=180)
        self.add_subject_entry.configure(bg='#FFFCA6')

        self.add_subject_button = tkinter.Button(self.assignment_window, text="Add Subject", command=self.add_subject, bg="#B19BD9", fg="white")
        self.add_subject_button.place(x=970, y=210)

        self.subject_listbox = tkinter.Listbox(self.assignment_window, width=30, height=30, selectmode=tkinter.SINGLE)
        self.subject_listbox.place(x=920, y=250)
        self.subject_listbox.configure(bg='#FFFCA6')

            #Adding assignment
        self.add_assignment_entry = tkinter.Entry(self.assignment_window, width=30 )
        self.add_assignment_entry.place(x=1190, y=165)
        self.add_assignment_entry.configure(bg='#FFFCA6')

        self.add_assignment_button = tkinter.Button(self.assignment_window, text="Add Activities", command=self.add_assignment, bg="#B19BD9", fg="white")
        self.add_assignment_button.place(x=1300, y=215)

        self.assignment_listbox = tkinter.Listbox(self.assignment_window, width=60, height=30, selectmode=tkinter.SINGLE)
        self.assignment_listbox.place(x=1150, y=250)
        self.assignment_listbox.configure(bg='#FFFCA6')

        self.assignment_status_entry = ttk.Combobox(self.assignment_window, values=["Upcoming", "Late", "Finished"])
        self.assignment_status_entry.place(x=1190, y=190)

        self.assignment_due_entry = tkinter.Entry(self.assignment_window, width=12 )
        self.assignment_due_entry.place(x=1445, y=190)
        self.assignment_due_entry.configure(bg='#FFFCA6')

        #Deleting
        self.delete_subject_button = tkinter.Button(self.assignment_window, text="Delete sub", command=self.delete_subject, bg="#B19BD9", fg="white")
        self.delete_subject_button.place(x=910, y=750)

        self.delete_assignment_button = tkinter.Button(self.assignment_window, text="Delete assignment", command=self.delete_assignment, bg="#B19BD9", fg="white")
        self.delete_assignment_button.place(x=1150, y=750)

        self.modify_assignment_button = tkinter.Button(self.assignment_window, text="Modify assignment", command=self.modify_assignment, bg="#B19BD9", fg="white")
        self.modify_assignment_button.place(x=1350, y=750)

        #Prioritizing, sana ol prioritize :(
        self.prioritize_listbox = tkinter.Listbox(self.assignment_window, width=40, height=5, selectmode=tkinter.SINGLE)
        self.prioritize_listbox.place(x=580, y=130)
        self.prioritize_listbox.configure(bg='#FFFCA6')
        
        self.prioritize_assignment_button = tkinter.Button(self.assignment_window, text="Prioritize", command=self.prioritize_assignment, bg="#B19BD9", fg="white")
        self.prioritize_assignment_button.place(x=1280, y=750)

        self.delete_prioritize_button = tkinter.Button(self.assignment_window, text="Finished", command=self.delete_prioritize, bg="#B19BD9", fg="white")
        self.delete_prioritize_button.place(x=580, y=220)

        self.search_subject_button = tkinter.Button(self.assignment_window, text="Search", command=self.search_subject, bg="#B19BD9", fg="white")
        self.search_subject_button.place(x=980, y=750)

        self.search_subject_entry = tkinter.Entry(self.assignment_window, width=10)
        self.search_subject_entry.place(x=1030, y=755)
        self.search_subject_entry.configure(bg='#FFFCA6')

        self.logout = tkinter.Button(self.assignment_window, text="Sign out", command=self.logout_user, bg="#B19BD9", fg="white")
        self.logout.place(x=1470, y=750)

        

        # Bind event to update assignment listbox when a subject is selected
        self.subject_listbox.bind('<<ListboxSelect>>', self.update_assignment_listbox)

        # Variable to store the currently selected subject
        self.selected_subject = tkinter.StringVar()

        self.assignment_queue = Queue()

        self.assignment_priority_queue = PriorityQueue()

        self.queue_assignments = Queue()
        self.subject_assignments = {}

        self.slider()

    #Moving text
    def slider(self):
        if self.count >= len(self.be_text):
            self.count = -1
            self.text = ''
            self.be_label.config(text=self.text)
        else:
            self.text = self.text + self.be_text[self.count]
            self.be_label.config(text=self.text)
        self.count += 1

        self.be_label.after(100, self.slider)


    #Getting notes input
    def update_note_listbox(self):
        new_note = self.note_text.get("1.0", "end-1c")
        self.note_listbox.insert(tkinter.END, new_note)
        self.note_text.delete("1.0", tkinter.END)
            
    #Deleting notes input
    def clear_notes(self):
        self.note_text.delete(1.0, END)


    #Deleting Notes
    def delete_notes(self):
        self.note_listbox.delete(tkinter.ANCHOR)

    def add_subject(self):
        new_subject = self.add_subject_entry.get()
        if new_subject:
            # Add the new subject to the sorted list in the listbox
            index = bisect.bisect_left(self.subject_listbox.get(0, tkinter.END), new_subject)
            self.subject_listbox.insert(index, new_subject)

            # Update the subjects dictionary
            self.subjects[new_subject] = []

            # Clear the entry field
            self.add_subject_entry.delete(0, tkinter.END)
            
    def search_subject(self):
        subject_search = self.search_subject_entry.get().strip()

        # Binary search the subject list
        index = bisect.bisect_left(self.subject_listbox.get(0, tkinter.END), subject_search)

        if index != len(self.subject_listbox.get(0, tkinter.END)):
            subject_found = self.subject_listbox.get(index)

            if subject_found.startswith(subject_search):
                self.subject_listbox.selection_clear(0, tkinter.END)
                self.subject_listbox.selection_set(index)
                self.subject_listbox.see(index)
                messagebox.showinfo("Subject Found", f"The subject '{subject_search}' is found in the list.")
            else:
                messagebox.showinfo("No Subject Found", f"No subject matching '{subject_search}' found.")
        else:
            messagebox.showinfo("No Subject Found", f"No subject matching '{subject_search}' found.")
        
    #Method for adding subject
    def update_subject_listbox(self):
        self.subject_listbox.insert(tkinter.END, self.new_subject)
        self.add_subject_entry.delete("0", tkinter.END)

    def add_assignment(self):
        subject1 = self.selected_subject.get()
        ass_status = self.assignment_status_entry.get()
        ass_due = self.assignment_due_entry.get()
        new_assignment = self.add_assignment_entry.get()

        if subject1 and new_assignment and ass_status and ass_due:
            subject = {
                "Ass name": new_assignment,
                "Status": ass_status,
                "Due Date": ass_due
            }

            # Check if the assignment belongs to the selected subject
            if subject1 == self.selected_subject.get():
                # Add the assignment to the subject's list
                self.subjects[subject1].append(subject)
            else:
                # Add the assignment to the queue
                self.assignment_queue.put(subject)
                self.queue_assignments.append(subject)

            # Update the assignment listbox
            self.update_assignment_listbox()

            # Clear the entry fields
            self.add_assignment_entry.delete(0, tkinter.END)
            self.assignment_status_entry.set('')
            self.assignment_due_entry.delete(0, tkinter.END)

    #Deleting Subject
    def delete_subject(self):
        self.subject_listbox.delete(tkinter.ANCHOR)

    def delete_assignment(self):
        selected_index = self.assignment_listbox.curselection()
        if selected_index:
            selected_assignment = self.assignment_listbox.get(selected_index)
            selected_subject = self.selected_subject.get()

            # Find and remove the assignment from the subject's list
            if selected_subject in self.subjects:
                for assignment in self.subjects[selected_subject][:]:
                    assignment_str = f"{assignment['Ass name']} (Due: {assignment['Due Date']}, Status: {assignment['Status']})"
                    if assignment_str == selected_assignment:
                        self.subjects[selected_subject].remove(assignment)

            # Find and remove the assignment from the queue_assignments
            queue_size = self.queue_assignments.qsize()
            for _ in range(queue_size):
                assignment = self.queue_assignments.get()
                assignment_str = f"{assignment['Ass name']} (Due: {assignment['Due Date']}, Status: {assignment['Status']})"
                if assignment_str == selected_assignment:
                    # Skip adding the selected assignment back to the queue
                    continue
                self.queue_assignments.put(assignment)

            # Update the assignment listbox immediately
            self.update_assignment_listbox()


    def delete_prioritize(self):
        self.prioritize_listbox.delete(tkinter.ANCHOR)

    def modify_assignment(self):
        selected_index = self.assignment_listbox.curselection()
        if selected_index:
            selected_assignment = self.assignment_listbox.get(selected_index)
            selected_subject = self.selected_subject.get()

            # Find and remove the assignment from the subject's list
            if selected_subject in self.subjects:
                for assignment in self.subjects[selected_subject][:]:
                    assignment_str = f"{assignment['Ass name']} (Due: {assignment['Due Date']}, Status: {assignment['Status']})"
                    if assignment_str == selected_assignment:
                        # Show a new window to get modified details
                        modified_assignment = self.show_modify_window(assignment)
                        if modified_assignment is not None:
                            # Update the assignment details only if modified_assignment is not None
                            assignment.update(modified_assignment)

            # Find and remove the assignment from the queue_assignments
            while not self.queue_assignments.empty():
                assignment = self.queue_assignments.get()
                assignment_str = f"{assignment['Ass name']} (Due: {assignment['Due Date']}, Status: {assignment['Status']}"
                if assignment_str == selected_assignment:
                    # Show a new window to get modified details
                    modified_assignment = self.show_modify_window(assignment)
                    if modified_assignment is not None:
                        # Update the assignment details only if modified_assignment is not None
                        assignment.update(modified_assignment)
                else:
                    self.queue_assignments.put(assignment)


            # Update the assignment listbox immediately
            self.update_assignment_listbox()


    def show_modify_window(self, assignment):
        modify_window = tkinter.Toplevel(self.assignment_window)
        modify_window.title("Modify Assignment")
        modify_window.configure(bg='#C2E3E7')

        name_label = tkinter.Label(modify_window, text="Assignment Name:", fg='#D48ACF', bg='#C2E3E7')
        name_label.grid(row=0, column=0)
        name_entry = tkinter.Entry(modify_window)
        name_entry.insert(tkinter.END, assignment['Ass name'])
        name_entry.grid(row=0, column=1)

        status_label = tkinter.Label(modify_window, text="Status:", fg='#D48ACF', bg='#C2E3E7')
        status_label.grid(row=1, column=0)
        status_combobox = ttk.Combobox(modify_window, values=["Upcoming", "Late", "Finished"])
        status_combobox.set(assignment['Status'])
        status_combobox.grid(row=1, column=1)

        due_label = tkinter.Label(modify_window, text="Due Date (YYYY-MM-DD):",fg='#D48ACF', bg='#C2E3E7')
        due_label.grid(row=2, column=0)
        due_entry = tkinter.Entry(modify_window)
        due_entry.insert(tkinter.END, assignment['Due Date'])
        due_entry.grid(row=2, column=1)

        apply_button = tkinter.Button(modify_window, text="Apply", bg="#B19BD9", fg="white", command=lambda: self.apply_changes(assignment, name_entry.get(), status_combobox.get(), due_entry.get(), modify_window))
        apply_button.grid(row=3, columnspan=2)

    def apply_changes(self, assignment, new_name, new_status, new_due, modify_window):
        # Validate inputs
        if not new_name or not new_status or not new_due:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Update assignment details
        assignment.update({
            'Ass name': new_name,
            'Status': new_status,
            'Due Date': new_due
        })

        # Close the modification window
        modify_window.destroy()

        # Update the assignment listbox immediately
        self.update_assignment_listbox()

    def update_assignment_listbox(self, event=None):
        selected_index = self.subject_listbox.curselection()
        if selected_index:
            subject1 = self.subject_listbox.get(selected_index)
            self.selected_subject.set(subject1)
            assignments = self.subjects.get(subject1, [])

            # Clear the assignment listbox
            self.assignment_listbox.delete(0, tkinter.END)

            # Display assignments from the queue
            # Display assignments from the queue
            while not self.queue_assignments.empty():
                assignment = self.queue_assignments.get()
                self.display_colored_assignment(assignment)
                # Put the assignment back to the queue_assignments
                self.queue_assignments.put(assignment)


            # Display assignments from the subject's list
            for assignment in assignments:
                self.display_colored_assignment(assignment)

    def display_colored_assignment(self, assignment):
        status = assignment['Status']
        color = 'black'  # Default color

        if status == "Finished":
            color = 'green'
        elif status == "Late":
            color = 'red'
        elif status == "Upcoming":
            color = 'blue'

        self.assignment_listbox.insert(
            tkinter.END,
            f"{assignment['Ass name']} (Due: {assignment['Due Date']}, Status: {assignment['Status']})"
        )
        self.assignment_listbox.itemconfig(tkinter.END, {'fg': color})

    def prioritize_assignment(self):
        selected_index = self.assignment_listbox.curselection()
        if selected_index:
            # Get the selected assignment
            selected_assignment = self.assignment_listbox.get(selected_index)

            # Assign priorities and add to the priority queue
            priority = self.assignment_listbox.get(0, tkinter.END).index(selected_assignment)
            self.assignment_priority_queue.put((priority, selected_assignment))

            # Refresh the prioritize listbox
            self.refresh_prioritize_listbox()

    def refresh_prioritize_listbox(self):
        # Clear the prioritize listbox
        self.prioritize_listbox.delete(0, tkinter.END)

        # Sort the items based on their priorities
        sorted_assignments = sorted(self.assignment_priority_queue.queue, key=lambda x: x[0])

        # Add sorted assignments to the prioritize listbox
        for priority, assignment in sorted_assignments:
            self.prioritize_listbox.insert(tkinter.END, f"{assignment} (Olale: {priority})")

    def logout_user(self):
        response = messagebox.askyesno("Sign out", "Sure ka bang aalis ka na?")
        if response:
            self.assignment_window.destroy()
            self.open_py_file1()
        else:
            messagebox.showwarning(title='Warning Message', message='Balak mo pa akong iwan!')
    
    def open_py_file1(self):
        call(["python", "comp.py"])
            

if __name__ == "__main__":
    assignment_window = tkinter.Tk()
    app = AssignmentTracker(assignment_window)
    #Background image
    background_image = PhotoImage(file="gui_images/todolist.png")
    background_label = Label(assignment_window, image=background_image)
    background_label.place(x=0)

    background_label.lower()

    #Picture naming anim, sana ma motivate kayo
    olale_image_path = "gui_images/Olale_Group_6 (1).png"
    olale_image = Image.open(olale_image_path)
    olale_image = olale_image.resize((400, 500), Image.LANCZOS)

    olale_image_tk = ImageTk.PhotoImage(olale_image)
    olale_image_label = tkinter.Label(assignment_window, image=olale_image_tk)
    olale_image_label.place(x=500, y=250)

    assignment_window.mainloop()
    
