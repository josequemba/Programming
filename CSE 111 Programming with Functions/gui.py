#Heart rate
#Author: josé Quemba
print ()

from tkinter import *
import tkinter as tk
from number_entry import IntEntry
import math


def main ():

    mother_window = tk.Tk ()

    Cal_window = Frame (mother_window)
    Cal_window.master.title ("Area of a circle calculator")
    Cal_window.pack (padx=50, pady=50, fill=tk.BOTH, expand=1)

    features_f(Cal_window)

    mother_window.mainloop ()

def features_f(cal_window):

    # frm: a frame (window) widget
    # lbl: a label widget that displays text for the user to see
    # ent: an entry widget where a user will type text or numbers
    # btn: a button widget that the user will click

    lbl_text1 = Label(cal_window, text="Enter the circle radius:")

    user_entry = IntEntry(cal_window, width=4, lower_bound=0, upper_bound=90)

    lbl_text2 = Label(cal_window, text="cm")

    lbl_text3 = Label(cal_window, text="The area for the circle is:")

    lbl_result = Label(cal_window, width=3)
    
    lbl_text4 = Label(cal_window, text="cm^2")

    btn_calc = Button(cal_window, text="Calculate")
    
    #layouts
    lbl_text1.grid(  row=0, column=0, columnspan=3, padx=3, pady=3)
    user_entry.grid( row=1, column=0, columnspan=2, padx=3, pady=3)
    lbl_text2.grid(  row=1, column=1, padx=3, pady=3)
    lbl_text3.grid(  row=2, column=0, columnspan=3, padx=3, pady=3)
    lbl_result.grid( row=3, column=0, columnspan=1, padx=3, pady=3)
    lbl_text4.grid(  row=3, column=1, padx=3, pady=3)
    btn_calc.grid(   row=4, column=1, columnspan=3, padx=3, pady=3)

    def calculate ():
        try:
            radius = user_entry.get()

            area = math.pi * (radius**2)

            btn_calc.focus ()
            lbl_result.config (text=f"{area:.2f}")

        except ValueError:
            lbl_result.config (text="")

    btn_calc.config(command=calculate)

    user_entry.focus ()

if __name__ == "__main__":
    main ()