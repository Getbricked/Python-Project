# create the program window with its functions


import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

from source import pwchecker
from source import intro

# function that create the window
def program():
    
    window = tk.Tk()
    window.geometry("300x150")
    window.resizable(False, False)
    window.title('Input password')

    # store the input password
    password = tk.StringVar()


    def check_clicked():
        #assign the "pw" value from "pwchecker.py" file = input password
        pwchecker.pw = password.get()
        
        #start the commands from "pwchecker.py"
        pwchecker.start()



    # create screen frame
    screen = ttk.Frame(window)
    screen.pack(padx=10, pady=10, fill='x', expand=True)


    # create the password label
    password_label = ttk.Label(screen, text="Password:")
    password_label.pack(fill='x', expand=True)

    # show the input password but as *
    password_entry = ttk.Entry(screen, textvariable=password, show="*")
    password_entry.pack(fill='x', expand=True)

    # create check button and its commands
    check_button = ttk.Button(screen, text="Check", command=check_clicked)
    check_button.pack(fill='x', expand=True, pady=10)

    def reveal():
        # Show entered password with a dialog
        msg = f'Entered password: {password.get()}'
        showinfo(
            title='Information',
            message=msg
        )
        
    # create reveal password button
    reveal_button = ttk.Button(screen, text="Reveal Password", command=reveal)
    reveal_button.pack(fill='x', expand=True, pady=10)

    window.mainloop()

# run the program    
if __name__=="__main__":
    program()