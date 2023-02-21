import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

import string

def introduction():
    # create introduction window
    intro = tk.Tk()
    intro.geometry("500x250")
    intro.resizable(False, False)
    intro.title('Introduction')

    # create frame
    frame = ttk.Frame(intro)
    frame.pack(padx=10, pady=10, fill='x', expand=True)
    

    
    # text using for label
    line1 = "                             Password checker version 1.0"
    line2 = "\nYour password must meet these requirements:"
    line3 = "\n     Must have more than 8 characters but not more than 20 characters!"
    line4 = "\n     Contain at least 1 upper case character!"
    line5 = "\n     Contain at least 1 lower case character!"
    line6 = "\n     Contain at least 1 special character!"
    line7 = "\n     Contain at least 1 digit!"
    line8 = "\n     Special feature: Your password must not exist in the common dictionary!"
    input_text = line2 + line3 + line4 + line5 + line6 + line7
    
    # create the intro label
    top_label = ttk.Label(intro, text=line1.upper(), background="red", font="Arial")
    top_label.pack(fill='x', expand=True)
    
    intro_label = ttk.Label(intro, text=input_text)
    intro_label.pack(fill='x', expand=True)

    bottom_label = ttk.Label(intro, text=line8.upper(), background="red")
    bottom_label.pack(fill='x', expand=True)
    # jump from intro to main
    def jump():
        intro.destroy()
            
    # create a button
    button = ttk.Button(intro, text="Start the program!", command=jump)
    button.pack(fill='x', expand=True, pady=10)
    
    intro.mainloop()
    
introduction()