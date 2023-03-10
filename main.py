import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

from source import pwchecker
from source import intro

def program():
    
    """create the program window with its functions
    # window - create display window
    # password - the string using to store our input password
    # screen - frame of window
    # password_label - display text above input box
    # password_entry - display the typed input
    # check_button - button to execute commands
    """

    window = tk.Tk()
    window.geometry("300x150")
    window.resizable(False, False)
    window.title('Input password')

    
    password = tk.StringVar()


    def check_clicked():
        """ assign the in put pw to the pwchecker.py and run the pwchecker.py """
        
        pwchecker.pw = password.get()
        
        
        pwchecker.start()



    
    screen = ttk.Frame(window)
    screen.pack(padx=10, pady=10, fill='x', expand=True)


    
    password_label = ttk.Label(screen, text="Password:")
    password_label.pack(fill='x', expand=True)

    
    password_entry = ttk.Entry(screen, textvariable=password, show="*")
    password_entry.pack(fill='x', expand=True)

    
    check_button = ttk.Button(screen, text="Check", command=check_clicked)
    check_button.pack(fill='x', expand=True, pady=10)

    
    def reveal():
        """ Reveal the input password """
        
        msg = f'Entered password: {password.get()}'
        showinfo(
            title='Information',
            message=msg
        )
        
    
    reveal_button = ttk.Button(screen, text="Reveal Password", command=reveal)
    reveal_button.pack(fill='x', expand=True, pady=10)

    window.mainloop()


if __name__=="__main__":
    """ Run the program if it is executed """
    program()