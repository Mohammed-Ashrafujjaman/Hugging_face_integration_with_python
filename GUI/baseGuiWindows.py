'''
Group Name: Sydney Group 17
Group Members: 4
Mohammed Ashrafujjaman Hera - 391197
Pujan Dey  - 395076
Shaown Imtiaz - 396121
Al-Amin Dhaly - 395230
'''

import tkinter as tk

# This a base class for tkinter GUI
# will inherite this file into gui.py pyhton file
# This is done this way to show inheritance 
class BaseWindow:
    """ This class is for initializing the tkinter window and define window size"""
    def __init__(self):
        # encapsulated attribute
        self._root = tk.Tk()      
        # Giving title to out GUI windows    
        self._root.title("HIT137 GeekBytes AI SYDN-17")
        # Initial window size
        self._root.geometry("820x620")

    def root(self):
        # Encapsulation with private variable
        return self._root

    def run(self):
        self._root.mainloop()