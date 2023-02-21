import string
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

pw = "test"
def start():
    # check type of characters
    upper_case = any([1 if c in string.ascii_uppercase else 0 for c in pw])
    lower_case = any([1 if c in string.ascii_lowercase else 0 for c in pw])
    specials = any([1 if c in string.punctuation else 0 for c in pw])
    digits = any([1 if c in string.digits else 0 for c in pw])

    # total check
    pwcheck = [upper_case, lower_case, specials, digits]

    # count length of password
    pwlen = len(pw)

    # open dictionary
    with open('source/password.txt', 'r') as f:
        common = f.read().splitlines()

    # try to find the input password in dictionary
    if pw in common: 
        msg = "This password was found in common dictionary!"
        
        showinfo(
            title='Password Checker',
            message=msg
        )
        return

    # check if password is from 8 to 20 characters
    if pwlen > 20 or pwlen < 8:
        msg ="Password should have 8 - 20 characters!"
        
        showinfo(
            title='Password Checker',
            message=msg
        )
        return
    # check sum condition
    if sum(pwcheck) < 4:
        msg1 = "Password must contain: "
        msg2 = "\nAt least 1 upper case character."
        msg3 = "\nAt least 1 lower case character."
        msg4 ="\nAt least 1 special character."
        msg5 ="\nAt least 1 digit character."
        msg = msg1 + msg2 + msg3 + msg4 + msg5
        
        showinfo(
            title='Password Checker',
            message=msg
        )
        return
    
    # if the password is good this dialog will appear!
    showinfo(
            title='Information',
            message="That's a good password!"
        )
