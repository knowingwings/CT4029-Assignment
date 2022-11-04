from atexit import register
import tkinter as tk
from tkinter import BOTTOM, CENTER, FLAT, SOLID, TOP, UNDERLINE, StringVar, ttk, messagebox
import re
import sqlite3
from tkinter.font import ITALIC
from turtle import color

class window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("High Street Market Brand Application")
        self.attributes('-fullscreen',True)

        # creating a frame and assigning it to container
        container = tk.Frame(self, height=1080, width=1920)
        # specifying the region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #dictionary of frames
        self.frames = {}
        # add the components to the dictionary.
        for F in (LoginPage, RegisterPage, Dashboard_Admin, Dashboard_Staff, Dashboard_Customer, OffersPage):
            frame = F(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(LoginPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()


class LoginPage(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        titleLabel = ttk.Label(
            self,
            text="Login",
            font=("Arial Bold",50))
        titleLabel.place(x=1380, y=50)

        userLabel = ttk.Label(
            self,
            text="Email:",
            font=("Arial", 25)
        )
        userLabel.place(x=1300, y=200)

        usernameInput = ttk.Entry(
            self,
            textvariable=StringVar,
            font=("Arial", 25)
        )
        usernameInput.place(x=1300,y=250)


        passwordLabel = ttk.Label(
            self,
            text="Password:",
            font=("Arial", 25)
        )
        passwordLabel.place(x=1300, y=300)

        passwordInput = ttk.Entry(
            self,
            textvariable=StringVar,
            font=("Arial", 25),
            show="•"
        )
        passwordInput.place(x=1300,y=350)

        mIMG = tk.PhotoImage(file='./assets/branding/loginImage.png')
        mainImg = ttk.Label(
            self,
            image=mIMG)
        mainImg.image = mIMG # Prevents python clean-up destroying image
        mainImg.pack(side="left")


        # switch_window_button in order to call the show_frame() method as a lambda function
        loginButton = tk.Button(
            self,
            text="Login",
            command=lambda: login(controller, usernameInput.get(), passwordInput.get()),
            font=("Arial", 25),
            border=False,
            bg="light gray",
            relief=FLAT           
        )
        loginButton.place(x=1420, y=400)

        registerButton = tk.Button(
            self,
            text="Create new Account",
            command=lambda: controller.show_frame(RegisterPage),
            font=("Arial", 8, UNDERLINE),
            fg="blue",
            border=False,
            relief=FLAT           
        )
        registerButton.place(x=1420, y=475)

        def login(controller, username, password):
            if(username=="" or password == ""):
                tk.messagebox.showwarning(title="Invalid Email or Password", message="Please input an Email or Password")
            elif(validEmail(username)!=True):
                tk.messagebox.showwarning(title="Invalid Email", message="Please input a valid email address")
            elif(findUser(username)==False):
                tk.messagebox.showwarning(title="User not Found", message="User not Found Please Create an account")
            else:
                ident = temp(username)
                role = userRole(ident)
                if(role=="Admin"):
                    controller.show_frame(Dashboard_Admin)
                elif(role=="Customer"):
                    controller.show_frame(Dashboard_Customer)
                else:
                    controller.show_frame(Dashboard_Staff)  
                
class RegisterPage(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        titleLabel = ttk.Label(
            self,
            text="Register",
            font=("Arial Bold",50))
        titleLabel.place(x=1380, y=50)

        userLabel = ttk.Label(
            self,
            text="Email:",
            font=("Arial", 25)
        )
        userLabel.place(x=1300, y=200)

        usernameInput = ttk.Entry(
            self,
            textvariable=StringVar,
            font=("Arial", 25)
        )
        usernameInput.place(x=1300,y=250)


        passwordLabel = ttk.Label(
            self,
            text="Password:",
            font=("Arial", 25)
        )
        passwordLabel.place(x=1300, y=300)

        passwordInput = ttk.Entry(
            self,
            textvariable=StringVar,
            font=("Arial", 25),
            show="•"
        )
        passwordInput.place(x=1300,y=350)

        mIMG = tk.PhotoImage(file='./assets/branding/registerImage.png')
        mainImg = ttk.Label(
            self,
            image=mIMG)
        mainImg.image = mIMG # Prevents TK clean-up destroying image
        mainImg.pack(side="left")


        # switch_window_button in order to call the show_frame() method as a lambda function
        registerButton = tk.Button(
            self,
            text="Register",
            command=lambda: register(self, controller, usernameInput.get(), passwordInput.get()),
            font=("Arial", 25),
            border=False,
            bg="light gray",
            relief=FLAT           
        )
        registerButton.place(x=1420, y=400)

        loginButton = tk.Button(
            self,
            text="Already have an Account?",
            command=lambda: controller.show_frame(LoginPage),
            font=("Arial", 8, UNDERLINE),
            fg="blue",
            border=False,
            relief=FLAT           
        )
        loginButton.place(x=1420, y=475)

        def register(self, controller, username, password):
            if(username=="" or password == ""):
                tk.messagebox.showwarning(title="Invalid Email or Password", message="Please input an Email or Password")
            elif(validEmail(username)!=True):
                tk.messagebox.showwarning(title="Invalid Email", message="Please input a valid email address")
            elif(findUser(username)==True):
                tk.messagebox.showwarning(title="User already exists", message="User already exists")
            else:
                ident = temp(username)
                role = userRole(ident)
                if(role=="Admin"):
                    controller.show_frame(Dashboard_Admin)
                elif(role=="Customer"):
                    controller.show_frame(Dashboard_Customer)
                else:
                    controller.show_frame(Dashboard_Staff)       

class Dashboard_Admin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ADMIN PAGE")
        label.pack(padx=10, pady=10)

        offerIcon = tk.PhotoImage(file='./assets/icons/price-tag180x180.png')
        offersButton = tk.Button(
            self,
            image=offerIcon,
            text="Offers",
            font=("Arial", 12),
            height=220,
            width=220,
            compound= TOP,
            bg="light gray",
            command=lambda: controller.show_frame(OffersPage),
        )
        offersButton.image=offerIcon # Prevents TK clean-up destroying image
        offersButton.place(x=960, y=540)

        staffIcon = tk.PhotoImage(file='./assets/icons/id-card180x180.png')
        staffButton = tk.Button(
            self,
            image=staffIcon,
            text="Staff",
            font=("Arial", 12),
            height=220,
            width=220,
            compound= TOP,
            bg="light gray",
            command=lambda: controller.show_frame(OffersPage),
        )
        staffButton.image=staffIcon # Prevents TK clean-up destroying image
        staffButton.place(x=1210, y=540)

        itemIcon = tk.PhotoImage(file='./assets/icons/search180x180.png')
        itemButton = tk.Button(
            self,
            image=itemIcon,
            text="Items",
            font=("Arial", 12),
            height=220,
            width=220,
            compound= TOP,
            bg="light gray",
            command=lambda: controller.show_frame(OffersPage),
        )
        itemButton.image=itemIcon # Prevents TK clean-up destroying image
        itemButton.place(x=460, y=540)

        dataIcon = tk.PhotoImage(file='./assets/icons/monitor180x180.png')
        dataButton = tk.Button(
            self,
            image=dataIcon,
            text="Staff",
            font=("Arial", 12),
            height=220,
            width=220,
            compound= TOP,
            bg="light gray",
            command=lambda: controller.show_frame(OffersPage),
        )
        dataButton.image=dataIcon # Prevents TK clean-up destroying image
        dataButton.place(x=710, y=540)

class Dashboard_Staff(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="STAFF PAGE")
        label.pack(padx=10, pady=10)

        switch_window_button = tk.Button(
            self,
            text="Go to the Completion Screen",
            command=lambda: controller.show_frame(LoginPage),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)

class Dashboard_Customer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Customer Page")
        label.pack(padx=10, pady=10)

        switch_window_button = tk.Button(
            self,
            text="Go to the Completion Screen",
            command=lambda: controller.show_frame(LoginPage),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)

class OffersPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Offers Page")
        label.pack(padx=10, pady=10)

        switch_window_button = tk.Button(
            self,
            text="Go to the Completion Screen",
            command=lambda: controller.show_frame(LoginPage),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)


# Searches the db for an email address returns id
def findUser(email):
    pass

# Takes the id and input for user and checks if the password matches input
def passwordMatch(id,password):
    pass

def temp(username):
    if(username=="steve@email.com"):
        return 0
    elif(username=="clara@email.com"):
        return 1
    else:
        return 3
# Returns users Roles e.g. Admin, Customer, Staff
def userRole(id):
    match id:
        case 0:
            return "Admin"
        case 1:
            return "Staff"
        case _:
            return "Customer"

def validEmail(email):
  return bool(re.search(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?", email))

if __name__ == "__main__":
    testObj = window()
    testObj.mainloop()