from tkinter import *
import tkinter as tk
from tkinter import messagebox
from subprocess import call

# Declare global variables for entry widgets
username = None
emailentry = None
passentry = None
conpass = None
userentry = None
passWentry = None
start_window = None
login_window = None
signup_window = None  # Declare signup_window as a global variable

def login():
    global userentry, passWentry
    entered_username = userentry.get()
    entered_password = passWentry.get()

    with open("users.txt", "r") as file:
        user_data = file.read().split("\n\n")
        for user_info in user_data:
            if not user_info:
                continue
            user_info_lines = user_info.split("\n")
            stored_username = user_info_lines[0].split(":")[1].strip()
            stored_password = user_info_lines[2].split(":")[1].strip()

            if entered_username == stored_username and entered_password == stored_password:
                messagebox.showinfo("Complete", "Log in Success")
                login_window.destroy()
                open_py_file()
                return
    messagebox.showerror("Error", "Password Incorrect")


def create_account():
    global username, emailentry, passentry, conpass
    global start_window, login_window, signup_window

    username_value = username.get()
    email_value = emailentry.get()
    password_value = passentry.get()
    confirm_password_value = conpass.get()

    if password_value == confirm_password_value:
        with open("users.txt", "a") as file:
            file.write(f"Username: {username_value}\nEmail: {email_value}\nPassword: {password_value}\n\n")

        # Clear the entry fields after saving
        username.delete(0, END)
        emailentry.delete(0, END)
        passentry.delete(0, END)
        conpass.delete(0, END)

        messagebox.showinfo("Complete", "Registration Success")
        signup_window.destroy()
        open_login_page
    else:
        messagebox.showerror("Error", "Passwords Do Not Match")


def startPage():
    global start_window, login_window, signup_window
    start_window = Tk()

    strt_img = PhotoImage(file="gui_images/design.png")
    extra = Label(start_window, image=strt_img)
    extra.place(x=0)
    extra.lower()

    screen_width = start_window.winfo_screenwidth()
    screen_height = start_window.winfo_screenheight()

    x = (screen_width - 500) // 2
    y = (screen_height - 600) // 2

    start_window.geometry(f"500x600+{x}+{y}")
    start_window.title("Start")

    label = Label(start_window, text="Assign, Finish, Celebrate.", font=('Times New Roman', 40, 'bold'), bg="#9fb8d2", width=20, height=2, fg="white")
    label.place(x=420, y=70)

    frame_login = Frame(start_window, bg="lightgray")
    frame_login.place(x=(screen_width - 500) // 2, y=(screen_height - 500) // 2 + 120)

    button2 = Button(frame_login, text="Login", font=('Times New Roman', 30), bg="#9fb8d2", width=20, height=2, fg="white",
                    command=open_login_page)
    button2.pack()

    frame_create_account = Frame(start_window, bg="lightgray")
    frame_create_account.place(x=(screen_width - 500) // 2, y=(screen_height - 500) // 2 + 300)

    button3 = Button(frame_create_account, text="Create Account", font=('Times New Roman', 30), bg="#9fb8d2", width=20, height=2,
                    fg="white", command=open_signup_page)
    button3.pack()

    start_window.state('zoomed')
    start_window.mainloop()

def open_signup_page():
    global username, emailentry, passentry, conpass, signup_window
    global start_window, login_window
    start_window.destroy()

    signup_window = Tk()
    Logo = PhotoImage(file="gui_images/nj.png")
    signup_window.iconphoto(True, Logo)
    signup_window.config(background="#9fb8d2")
    
    bgimg = PhotoImage(file="gui_images/design.png")
    extra = Label(signup_window, image=bgimg, )
    extra.place(x=0)

    signup_window.title("Create Account")
    width = signup_window.winfo_screenwidth()
    height = signup_window.winfo_screenheight()

    signup_window.geometry("%dx%d" % (width, height))
    

    label = Label(signup_window, text="BE EFFICIENT", font=('Times New Roman', 40, 'bold'), fg='#284377', bg="#9fb8d2")
    label.pack(padx=50, pady=250)

    lab1 = Label(signup_window, text="Username: ", font=('Times New Roman', 16), fg="white", bg="#9fb8d2")
    lab1.place(x=580, y=355)
    username = Entry(signup_window)
    username.place(x=680, y=355, height=30, width=250)

    lab2 = Label(signup_window, text="Email: ", font=('Times New Roman', 16), fg="white", bg="#9fb8d2")
    lab2.place(x=612, y=390)

    emailentry = Entry(signup_window)
    emailentry.place(x=680, y=390, height=30, width=250)

    lab3 = Label(signup_window, text="Password: ", font=('Times New Roman', 16), fg="white", bg="#9fb8d2")
    lab3.place(x=580, y=425)

    passentry = Entry(signup_window, show=("*", 15))
    passentry.place(x=680, y=425, height=30, width=250)

    lab4 = Label(signup_window, text="Confirm Password: ", font=('Times New Roman', 16), fg="white", bg="#9fb8d2")
    lab4.place(x=505, y=460)

    conpass = Entry(signup_window,show=("*", 15))
    conpass.place(x=680, y=460, width=250, height=30)
    
    finalbutton = Button(signup_window, text="Create Account", font=('Times New Roman', 16), fg="white", bg="#9fb8d2", command=lambda:[create_account(), startPage()])
    finalbutton.place(x=500, y=510, width=200, height=40)

    backbuttonsign = Button(signup_window, text="Back", font=('Times New Roman', 16), fg="white", bg="#9fb8d2", command=logback1)
    backbuttonsign.place(x=800, y=510, width= 200, height= 40)

    # finalbutton2 = Button(signup_window, text="Log in", font=('Times New Roman', 14), command=open_login_page)
    #finalbutton2.place(x=700, y=570, width=200, height=40)

    signup_window.mainloop()

def open_login_page():
    global userentry, passWentry, login_window, start_window, signup_window
    
    start_window.destroy()
    
    login_window = Tk()

    logo = PhotoImage(file="gui_images/nj.png")
    login_window.iconphoto(True, logo)
    login_window.config(background="#9fb8d2")
    
    log_img = PhotoImage(file="gui_images/design.png")
    extra = Label(login_window, image=log_img, )
    extra.place(x=0)
    
    login_window.title("Login")
    width= login_window.winfo_screenwidth() 
    height= login_window.winfo_screenheight()
    
    login_window.geometry("%dx%d" % (width, height))

    label = Label(login_window, text="BE PRODUCTIVE. :)", font=('Times New Roman', 40, 'bold'), fg='#284377', bg= "#9fb8d2", )
    label.place(x= 520, y= 200)
    
    label2 = Label(login_window, text="Username: ", font=('Times New Roman', 16), fg="white", bg="#9fb8d2")
    label2.place(x=580, y= 325)
    
    userentry = Entry(login_window)
    userentry.place(x=690, y=325, height=30, width=250)
    
    label3 = Label(login_window, text="Password: ", font=('Times New Roman', 16), fg="white", bg="#9fb8d2")
    label3.place(x=580, y= 425)
    
    passWentry = Entry(login_window, show=("*", 15))
    passWentry.place(x=690, y=425, height=30, width=250)
    
    logbutton = Button(login_window, text="Login", font=('Times New Roman', 16), fg="white", bg="#9fb8d2", command= login)
    logbutton.place(x=700, y=500, width= 110, height= 30)

    backbutton = Button(login_window, text="Back", font=('Times New Roman', 16), fg="white", bg="#9fb8d2", command=logback)
    backbutton.place(x=830, y=500, width= 110, height= 30)

    login_window.mainloop()

def logback():
    login_window.destroy()
    startPage()

def logback1():
    signup_window.destroy()
    startPage()

def open_py_file():
    call(["python", "assignment_tracker.py"])






startPage()
