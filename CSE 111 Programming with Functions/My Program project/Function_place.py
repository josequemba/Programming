import tkinter
import tkinter as tk 
from tkinter import *


def total_in_list (items_cost):
    
    total = sum(items_cost)

    return total

def box_entry_clear (button, item_ent, cost_ent):

    button.focus ()
    
    item_ent.delete (0, END)
    cost_ent.delete (0, END)
    
    item_ent.focus ()

def break_even_point (fixed_cost, price, variable_cost):

    bep = fixed_cost / (price - variable_cost)

    return bep
    