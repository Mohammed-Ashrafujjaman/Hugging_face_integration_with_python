'''
Group Name: Sydney Group 17
Group Members: 4
Mohammed Ashrafujjaman Hera - 391197
Pujan Dey  - 395076
Shaown Imtiaz - 396121
Al-Amin Dhaly - 395230
'''
from tkinter import messagebox
from GUI.gui import guiApp
from utils.all_information import information

# Our program starts from This main file
# guiApp() class is in GUI/gui.py file
# GUI/gui.py file contains all the logical code and implementation 
if __name__ == "__main__":
    messagebox.showinfo("Required packages", information.show_required_packages())
    app = guiApp()
    app.build_gui()
    app.run()
    
"""
References:
https://www.pythontutorial.net/tkinter/

This website has all the information and examples for every elements of TKinter.
"""