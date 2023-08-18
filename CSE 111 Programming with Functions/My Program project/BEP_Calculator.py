#Heart rate
#Author: josé Quemba

import tkinter
import tkinter as tk 
from tkinter import *
from number_entry import IntEntry
from Function_place import total_in_list, box_entry_clear, break_even_point
import textwrap
 
#lists
fixed_item = ['']
fixed_cost = [0]
variable_item = ['']
variable_cost = [0]
price_container = []
quantity_container = []

def main ():

    root = tkinter.Tk ()
    root.geometry ("600x500")
    root.title ("Even Point Calculator - BEP")
    
    displays (root)

    root.mainloop ()

def displays (root):

    about_m = Frame (root)
    about_m.pack ()
    about_m.config (width=600, height=500)

    l1 = Label (about_m, text = "Welcome to break Even Point Calculater BEP", font=("Helvetica", "20"))
    l1.place (bordermode=OUTSIDE, x=24, y=50)

    l2 = Label (about_m, text = "Knowing your break-even point is essential to running a business.\
 Where \nyou can check to see if you'll have enough demand to cover\
 your \ncosts and hopefully make a profit. The program will allow\
 the \nuser to enter their business data and have the program do every\
 calculation \nfor the user to have a persize information about the\
 break even \npoint to help him better make some decisions.", font=("Arial", "12"))
    l2.place (bordermode=OUTSIDE, x=44, y=100)

    l3 = Label (about_m, text = "Click on Start to Start calculating your monthly buisness break even point", font=("Arial", "12"))
    l3.place (bordermode=OUTSIDE, x=50, y=280)

    #(family="Helvetica",size=36,weight="bold",slant, underline, overstrike
    b1 = Button (about_m, text = "START", bg = "light blue", bd = 3, font=("Helvetica", "32"))
    b1.place (bordermode=OUTSIDE, x=208, y=312)

    def buttom_start ():

        #make the welcome window desappear
        about_m.pack_forget ()

        menu_v_bar = Frame (root, bg="#A6E6E5")
        menu_v_bar.config (width=200, height=500)
        menu_v_bar.place (bordermode=OUTSIDE, x=0, y=0)

        b_1 = Button (menu_v_bar, text= "Fixed Costs & \nVariable Costs", bg= "light blue", font=("arial", "12"), relief=FLAT)
        b_1.config (width=20, height=2)
        b_1.place (bordermode=OUTSIDE, x=8, y=16)
                    #Green highlight
        highlight_1 = Frame (menu_v_bar, bg= "#33D61A")
        highlight_1.config (width=7, height=50)
        highlight_1.place (bordermode=OUTSIDE, x=0, y=16)

        b_2 = Button (menu_v_bar, text= "View List", bg= "light blue", font=("arial", "12"), relief=FLAT)
        b_2.config (width=20, height=2)
        b_2.place (bordermode=OUTSIDE, x=8, y=70)
                    #Green highlight
        highlight_2 = Frame (menu_v_bar, bg= "#33D61A")
        highlight_2.config (width=7, height=50)
        highlight_2.place (bordermode=OUTSIDE, x=0, y=70)

        b_3 = Button (menu_v_bar, text= "Remove Item", bg= "light blue", font=("arial", "12"), relief=FLAT)
        b_3.config (width=20, height=2)
        b_3.place (bordermode=OUTSIDE, x=8, y=124)
                    #Green highlight
        highlight_3 = Frame (menu_v_bar, bg= "#33D61A")
        highlight_3.config (width=7, height=50)
        highlight_3.place (bordermode=OUTSIDE, x=0, y=124)

        b_4 = Button (menu_v_bar, text= "Enter the price \nof your product", bg= "light blue", font=("arial", "12"), relief=FLAT)
        b_4.config (width=20, height=2)
        b_4.place (bordermode=OUTSIDE, x=8, y=178)
                    #Green highlight
        highlight_4 = Frame (menu_v_bar, bg= "#33D61A")
        highlight_4.config (width=7, height=50)
        highlight_4.place (bordermode=OUTSIDE, x=0, y=178)

        b_5 = Button (menu_v_bar, text= "Bep", bg= "light blue", font=("arial", "12"), relief=FLAT)
        b_5.config (width=20, height=2)
        b_5.place (bordermode=OUTSIDE, x=8, y=232)
                    #Green highlight
        highlight_5 = Frame (menu_v_bar, bg= "#33D61A")
        highlight_5.config (width=7, height=50)
        highlight_5.place (bordermode=OUTSIDE, x=0, y=232)

        copyright = Label (menu_v_bar, text= "© 2023 - Jose Quemba", font=("arial", "10"), relief=FLAT)
        copyright.place (bordermode=OUTSIDE, x=26, y=450)

        def buttom_1 ():

            b_1.config (bg="#D9F4DA")
            b_2.config (bg="light blue")
            b_3.config (bg="light blue")
            b_4.config (bg="light blue")
            b_5.config (bg="light blue")

            highlight_1.config (bg="#33D61A")
            highlight_2.config (bg="light blue")
            highlight_3.config (bg="light blue")
            highlight_4.config (bg="light blue")
            highlight_5.config (bg="light blue")

            service_bar_1 = Frame (root, bg="#D9F4DA")
            service_bar_1.config (width=400, height=500)
            service_bar_1.place (bordermode=OUTSIDE, x=200, y=0)

            #fixed and variable costs desgnations
            l_c_fixed = Label (service_bar_1, text="Fixed Costs:", font=("arial", "13", "bold"), bg="#D9F4DA")
            l_c_fixed.place (bordermode=OUTSIDE, x=20, y=40)
            
            #items and costs entry
            item_entry = Label (service_bar_1, text = "Item:", font=("arial", "12"), bg="#D9F4DA")
            item_entry.place (bordermode=OUTSIDE, x=30, y=90)

            cost_entry = Label (service_bar_1, text = "cost:", font=("arial", "12"), bg="#D9F4DA")
            cost_entry.place (bordermode=OUTSIDE, x=30, y=130)

            #entry boxes
            item_entry_box = Entry (service_bar_1)
            item_entry_box.place (bordermode=OUTSIDE, x=100, y=90)
            
            cost_entry_box = IntEntry (service_bar_1, width=7, lower_bound=0, upper_bound=1000000000000000)
            cost_entry_box.place (bordermode=OUTSIDE, x=100, y=130)

            l_c_fixed = Label (service_bar_1, text="Variable Costs:", font=("arial", "13", "bold"), bg="#D9F4DA")
            l_c_fixed.place (bordermode=OUTSIDE, x=20, y=250)

            #items and costs entry
            item_entry2 = Label (service_bar_1, text = "Item:", font=("arial", "12"), bg="#D9F4DA")
            item_entry2.place (bordermode=OUTSIDE, x=30, y=300)

            cost_entry2 = Label (service_bar_1, text = "cost:", font=("arial", "12"), bg="#D9F4DA")
            cost_entry2.place (bordermode=OUTSIDE, x=30, y=340)

            #entry boxes
            item_entry_box2 = Entry (service_bar_1)
            item_entry_box2.place (bordermode=OUTSIDE, x=100, y=300)
            
            cost_entry_box2 = IntEntry (service_bar_1, width=7, lower_bound=0, upper_bound=1000000000000000)
            cost_entry_box2.place (bordermode=OUTSIDE, x=100, y=340)

            #buttons
            b_a_1 = Button (service_bar_1, text="Add", font=("arial", "12"))
            b_a_1.place (bordermode=OUTSIDE, x=100, y=190)

            b_a_2 = Button (service_bar_1, text="Add", font=("arial", "12"))
            b_a_2.place (bordermode=OUTSIDE, x=100, y=400)

            def add_b1 ():
                
                item = item_entry_box.get ()
                cost = cost_entry_box.get ()

                fixed_item.append (item)
                fixed_cost.append (cost)

                box_entry_clear (b_a_1, item_entry_box, cost_entry_box)

                #if item == str and cost and int or float:
                #    with open ("fixed_item", "wt") as item_f:
                #        print (f'{item}', file= item_f)
                #
                #if item == str and cost == int or float:
                #    with open ("fixed_cost", "wt") as cost_f:
                #        print (f'{cost}', file= cost_f)

            b_a_1.config(command=add_b1)

            def add_b2 ():
                
                item1 = item_entry_box2.get ()
                cost1 = cost_entry_box2.get ()

                variable_item.append (item1) 
                variable_cost.append (cost1)
                
                box_entry_clear (b_a_2, item_entry_box2, cost_entry_box2)

                #if item1 == str and cost1 == int or float:
                #    with open ("variable_item", "wt") as items_c:
                #        print (f'{item1}', file= items_c)

                #if item1 == str and cost1 == int or float:
                #    with open ("variable_cost", "wt") as cost_c:
                #        print (f'{cost1}', file= cost_c)

            b_a_2.config(command=add_b2)

        b_1.config (command=buttom_1)

        def buttom_2 ():

            b_1.config (bg="light blue")
            b_2.config (bg="#D9F4DA")
            b_3.config (bg="light blue")
            b_4.config (bg="light blue")
            b_5.config (bg="light blue")

            highlight_1.config (bg="light blue")
            highlight_2.config (bg="#33D61A")
            highlight_3.config (bg="light blue")
            highlight_4.config (bg="light blue")
            highlight_5.config (bg="light blue")

            service_bar_2 = Frame (root, bg="#D9F4DA")
            service_bar_2.config (width=400, height=500)
            service_bar_2.place (bordermode=OUTSIDE, x=200, y=0)

            #fixed and variable costs list
            fixed = Label (service_bar_2, text="Fixed Costs:", font=("arial", "13", "bold"), bg="#D9F4DA")
            fixed.place (bordermode=OUTSIDE, x=20, y=40)
            
            variable = Label (service_bar_2, text="Variable Costs:", font=("arial", "13", "bold"), bg="#D9F4DA")
            variable.place (bordermode=OUTSIDE, x=220, y=40)
            
            #list containers
            fixed_container_f = Frame (service_bar_2)
            fixed_container_f.config (width=160, height=380) #frame width=160, height=400
            fixed_container_f.place (bordermode=OUTSIDE, x=15, y=70)

            fixed_container = Listbox (fixed_container_f)
            fixed_container.config (width=26, height=23) #frame width=160, height=400
            fixed_container.pack(side=LEFT, fill=BOTH)

            # Create a Scrollbar widget
            scrollbar = Scrollbar(fixed_container_f)
            scrollbar.pack(side=RIGHT, fill=Y)

            # Associate the Scrollbar with the Listbox
            fixed_container.config(yscrollcommand=scrollbar.set)
            scrollbar.config(command=fixed_container.yview)

            for i in range (1, len(fixed_item)):
                ite = fixed_item [i]
                cos = fixed_cost [i]            	
                #fixed_container.yview_scroll ()
                fixed_container.insert(tk.END, f'{i}. {ite} - ${cos}')  

            #Variable
            variable_container_f = Frame (service_bar_2)
            variable_container_f.config (width=160, height=380)
            variable_container_f.place (bordermode=OUTSIDE, x=215, y=70)

            variable_container = Listbox (variable_container_f)
            variable_container.config (width=26, height=23)
            variable_container.pack (side=LEFT, fill=BOTH)

            scrollbar1 = Scrollbar (variable_container_f)
            scrollbar1.pack (side=RIGHT, fill=Y)

            variable_container.config (yscrollcommand=scrollbar1.set)
            scrollbar1.config (command=variable_container.yview)

            for i1 in range (1, len(variable_item)):
                ite1 = variable_item [i1]
                cos1 = variable_cost [i1]            	
                #fixed_container.yview_scroll ()
                variable_container.insert(tk.END, f'{i1}. {ite1} - ${cos1}')  

            fixed_total = Label (service_bar_2, text="Total of \nFixed Costs:", font=("arial", "9"), bg="#D9F4DA")
            fixed_total.place (bordermode=OUTSIDE, x=10, y=450)
            
            variable_total = Label (service_bar_2, text="Total of \nVariable Costs:", font=("arial", "9"), bg="#D9F4DA")
            variable_total.place (bordermode=OUTSIDE, x=210, y=450)

            fixed_total = Label (service_bar_2, text=f"{total_in_list (fixed_cost):.2f}", font=("arial", "8", "bold"), bg="#D9F4DA")
            fixed_total.place (bordermode=OUTSIDE, x=81, y=465)
            fixed_total.config (width=10, height=1)
            
            variable_total = Label (service_bar_2, text=f"{total_in_list (variable_cost):.2f}", font=("arial", "8", "bold"), bg="#D9F4DA")
            variable_total.place (bordermode=OUTSIDE, x=299, y=465)
            variable_total.config (width=10, height=1)

        b_2.config (command=buttom_2)

        def buttom_3 ():

            b_1.config (bg="light blue")
            b_2.config (bg="light blue")
            b_3.config (bg="#D9F4DA")
            b_4.config (bg="light blue")
            b_5.config (bg="light blue")

            highlight_1.config (bg="light blue")
            highlight_2.config (bg="light blue")
            highlight_3.config (bg="#33D61A")
            highlight_4.config (bg="light blue")
            highlight_5.config (bg="light blue")

            service_bar_3 = Frame (root, bg="#D9F4DA")
            service_bar_3.config (width=400, height=500)
            service_bar_3.place (bordermode=OUTSIDE, x=200, y=0)

            info_bar = Label (service_bar_3, text="Please enter the index of the items \nyou want to remove from the list", font=("arial", "13", "bold"), bg="#D9F4DA")
            info_bar.place (bordermode=OUTSIDE, x=64, y=40)
            
            #fixed and variable costs list
            fixed = Label (service_bar_3, text="Fixed Costs:", font=("arial", "13"), bg="#D9F4DA")
            fixed.place (bordermode=OUTSIDE, x=60, y=150)
            
            variable = Label (service_bar_3, text="Variable Costs:", font=("arial", "13"), bg="#D9F4DA")
            variable.place (bordermode=OUTSIDE, x=60, y=300)

            #entry bars for index
            entry_fixed_remove = IntEntry (service_bar_3, width=7, lower_bound=1, upper_bound=1000000000000000)
            entry_fixed_remove.place (bordermode=OUTSIDE, x=70, y=190)

            entry_variable_remove = IntEntry (service_bar_3, width=7, lower_bound=1, upper_bound=1000000000000000)
            entry_variable_remove.place (bordermode=OUTSIDE, x=70, y=340)

            #buttons to remove
            remove_fixed = Button (service_bar_3, text="Remove", font=("arial", "10"))
            remove_fixed.place (bordermode=OUTSIDE, x=70, y=220)

            remove_variable = Button (service_bar_3, text="Remove", font=("arial", "10"))
            remove_variable.place (bordermode=OUTSIDE, x=70, y=370)

            def action_remove_fixed ():
                
                user_index = entry_fixed_remove.get ()
                fixed_item.pop (user_index)
                fixed_cost.pop (user_index)
                
                #clear after removing
                box_entry_clear (remove_fixed, entry_fixed_remove, entry_fixed_remove)
            
            remove_fixed.config (command=action_remove_fixed)
        
            def action_remove_variable ():
                
                user_index = entry_variable_remove.get ()
                variable_item.pop (user_index)
                variable_cost.pop (user_index)
                
                #clear after removing
                box_entry_clear (remove_variable, entry_variable_remove, entry_variable_remove)
            
            remove_variable.config (command=action_remove_variable)

        b_3.config (command=buttom_3)

        def buttom_4 ():

            b_1.config (bg="light blue")
            b_2.config (bg="light blue")
            b_3.config (bg="light blue")
            b_4.config (bg="#D9F4DA")
            b_5.config (bg="light blue")

            highlight_1.config (bg="light blue")
            highlight_2.config (bg="light blue")
            highlight_3.config (bg="light blue")
            highlight_4.config (bg="#33D61A")
            highlight_5.config (bg="light blue")

            service_bar_4 = Frame (root, bg="#D9F4DA")
            service_bar_4.config (width=400, height=500)
            service_bar_4.place (bordermode=OUTSIDE, x=200, y=0)

            info_bar1 = Label (service_bar_4, text="This is the last step \nPlease enter the seling price of the unit:", font=("arial", "13", "bold"), bg="#D9F4DA")
            info_bar1.place (bordermode=OUTSIDE, x=42, y=40)

            price_product = IntEntry (service_bar_4, width=7, lower_bound=0, upper_bound=1000000000000000)
            price_product.place (bordermode=OUTSIDE, x=174, y=90)

            price_product_add = Button (service_bar_4, text="Add price", font=("arial", "10"))
            price_product_add.place (bordermode=OUTSIDE, x=164, y=124)

            info_bar2 = Label (service_bar_4, font=("arial", "10", "bold"), bg="#D9F4DA")
            info_bar2.place (bordermode=OUTSIDE, x=98, y=155)

            def add_price ():
                #clean the list for a new price
                price_container.clear()

                price = float(price_product.get ())
                price_container.append (price)

                for word in price_container:

                    wrap_text = f"The price of your product is $ {word:.2f}"

                    info_bar2.config (text= textwrap.fill(wrap_text, width=30))

                box_entry_clear (price_product_add , price_product, price_product)

            price_product_add.config (command=add_price)


            info_bar3 = Label (service_bar_4, text="Also enter the quantity of units you produced:", font=("arial", "13", "bold"), bg="#D9F4DA")
            info_bar3.place (bordermode=OUTSIDE, x=15, y=250)
                        
            quantity_product = IntEntry (service_bar_4, width=7, lower_bound=0, upper_bound=1000000000000000)
            quantity_product.place (bordermode=OUTSIDE, x=174, y=300)

            quantity_product_add = Button (service_bar_4, text="Add Quantity", font=("arial", "10"))
            quantity_product_add.place (bordermode=OUTSIDE, x=154, y=334)

            info_bar4 = Label (service_bar_4, font=("arial", "10", "bold"), bg="#D9F4DA")
            info_bar4.place (bordermode=OUTSIDE, x=108, y=365)

            def add_quantity ():
                #clean the list for a new price
                quantity_container.clear()

                quantity = quantity_product.get ()
                quantity_container.append (quantity)

                for number in quantity_container:

                    wrap_text = f"The quantity equivalent to your company's cost is of '{number:.0f} units'"

                    info_bar4.config (text= textwrap.fill(wrap_text, width=30))

                box_entry_clear (quantity_product_add, quantity_product, quantity_product)

            quantity_product_add.config (command=add_quantity)

        b_4.config (command=buttom_4)

        def buttom_5 ():

            b_1.config (bg="light blue")
            b_2.config (bg="light blue")
            b_3.config (bg="light blue")
            b_4.config (bg="light blue")
            b_5.config (bg="#D9F4DA")

            highlight_1.config (bg="light blue")
            highlight_2.config (bg="light blue")
            highlight_3.config (bg="light blue")
            highlight_4.config (bg="light blue")
            highlight_5.config (bg="#33D61A")

            service_bar_5 = Frame (root, bg="#D9F4DA")
            service_bar_5.config (width=400, height=500)
            service_bar_5.place (bordermode=OUTSIDE, x=200, y=0)

            BEP_btm = Button (service_bar_5, text="BEP", font=("arial", "13"))
            BEP_btm.place (bordermode=OUTSIDE, x=164, y=124)
        
            info_bar2 = Label (service_bar_5, font=("arial", "12", "bold"), bg="#D9F4DA")
            info_bar2.place (bordermode=OUTSIDE, x=88, y=200)

            def calcule_BEP ():

                fixed_cost_total = total_in_list (fixed_cost)
                Variable_cost_per_unit = total_in_list (variable_cost) / total_in_list (quantity_container)
                price = total_in_list (price_container)

                BEP = break_even_point(fixed_cost_total, price, Variable_cost_per_unit)

                text_wrap= (f"Your company needs to sell '{BEP:.1f} units' of its product just to cover all the costs and reach the break even point.")

                info_bar2.config (text = textwrap.fill(text_wrap, width=30))
                
            BEP_btm.config (command=calcule_BEP) 

        b_5.config (command=buttom_5)

    b1.config (command=buttom_start)

if __name__== "__main__":
    main ()