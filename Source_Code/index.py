from mimetypes import init
import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter.tix import Form

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
        for F in (LoginPage, Dashboard, RegisterPage):
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
            text="Username",
            font=("Arial", 25)
        )
        userLabel.place(x=1230, y=200)


        mIMG = tk.PhotoImage(file='./assets/loginPage/loginImage.png')
        mainImg = ttk.Label(
            self,
            image=mIMG)
        mainImg.image = mIMG # Prevents python clean-up destroying image
        mainImg.pack(side="left")


        # switch_window_button in order to call the show_frame() method as a lambda function
        switch_window_button = tk.Button(
            self,
            text="Go to the Side Page",
            command=lambda: login(self, controller),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)

        def login(self, controller):
            print("LOGIN PRESSED")
            controller.show_frame(Dashboard)
            


class Dashboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome to [INSERT HIFHSTREET BRAND HERE]")
        label.pack(padx=10, pady=10)

        switch_window_button = tk.Button(
            self,
            text="Go to the Completion Screen",
            command=lambda: controller.show_frame(LoginPage),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)


class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Completion Screen, we did it!")
        label.pack(padx=10, pady=10)
        switch_window_button = ttk.Button(
            self, text="Return to menu", command=lambda: controller.show_frame(LoginPage)
        )
        switch_window_button.pack(side="bottom", fill=tk.X)



if __name__ == "__main__":
    testObj = window()
    testObj.mainloop()