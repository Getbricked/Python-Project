


import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

from source import pwchecker
from source import intro

"""create the program window with its functions"""
def program():
    
    window = tk.Tk()
    window.geometry("300x150")
    window.resizable(False, False)
    window.title('Input password')

    
    password = tk.StringVar()


    def check_clicked():
        
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

    """ Reveal the input password """
    def reveal():
        
        msg = f'Entered password: {password.get()}'
        showinfo(
            title='Information',
            message=msg
        )
        
    
    reveal_button = ttk.Button(screen, text="Reveal Password", command=reveal)
    reveal_button.pack(fill='x', expand=True, pady=10)

    window.mainloop()

""" Run the program if it is executed """
if __name__=="__main__":
    program()