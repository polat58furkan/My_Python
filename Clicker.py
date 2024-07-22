# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 17:23:47 2024

@author: user
"""
import time
import keyboard
import mouse

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox



def on_button_help_click():
    message=(" This button is about Timing between two click. \n " 
                        "It must be between 0.01 - 5 \n "
                        "Example: Time is 2 \n " 
                        "First Click is at 00:00:00 \n " 
                        "Second Click is at 00:00:02 \n")
    
    messagebox.showinfo("Info", message)
    
    
    
def on_button_help2_click():
    
    message_2=(" Which buttons will be clicked. \n " )
    
    messagebox.showinfo("Info", message_2)



def on_button_help3_click():
    
    message_3=("How many times it will click . \n"
               "The 0 (zero) is infinite \n "
               "Press 9 to exit from infinite loop \n ")
    
    messagebox.showinfo("Info", message_3)
    
    
def on_button_click():
    
    selected_value_time = scale_time.get()
    selected_value_click_number = scale_number.get()
    selected_value_button=combo.get()
    once=True
    if selected_value_button == "Select Mouse Button" and once:
        messagebox.showinfo("Attention", " Chose mouse button please")
    if selected_value_button != "Select Mouse Button" and once:
        start_job(selected_value_time, selected_value_button, selected_value_click_number)

def start_job(time_sleep,button,number):
    if root.state() == 'withdrawn':
        root.deiconify()
    else:
        root.withdraw()
    boolean= True
    once=True
    print(time_sleep ,"  " , button , "  ", number)
    if number == 0 and once:
        once=False
        while boolean:
            if button == "Right":
                mouse.click('right')
            if button == "Left":
                mouse.click('left')
            if button == "Both":
                mouse.click('left')
                mouse.click('right')
            if keyboard.is_pressed('9'):
                boolean= False
                break
            time.sleep(time_sleep)
    if number != 0 and once: 
        once=False
        
        for i in range(int(number)):
            
            if button == "Right":
                mouse.click('right')
                
            if button == "Left":
                mouse.click('left')
                
            if button == "Both":
                mouse.click('left')
                mouse.click('right')    
                
            time.sleep(time_sleep)
    time.sleep(2)
    if root.state() != 'withdrawn':
        root.withdraw()
    else:
        root.deiconify()
# Create the main window
root = tk.Tk()
root.title("Clicker Of LéGéND")
root.config(bg="black")

# Set the window size
window_width = 400
window_height = 300

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the position to center the window on the screen
position_x = (screen_width // 2) - (window_width // 2)
position_y = (screen_height // 2) - (window_height // 2)

# Set the window size and position
root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

# Create a label
label = tk.Label(root, text="Hello, Welcome My Friend!" )
label.config(bg="red",width=20)
label.place(x=120, y=0)


#------------------------------ First Row --------
# Create a Scale (slider) widget
scale_time = tk.Scale(root, from_=0.01, resolution=0.01, to=5.0, orient='horizontal')
scale_time.place(x=10, y=60)
# Create a button
button_help = tk.Button(root, text="Help", command=on_button_help_click)
button_help.place(x=120, y=70)
button_help.config(bg="cyan")
# Create a label
label_time = tk.Label(root, text="Timing")
label_time.place(x=10, y=35)
label_time.config(bg="green")

#-------------------------------------------------

#------------------------------ Second Row --------
# Create a label
label_times = tk.Label(root, text="Which button")
label_times.place(x=10, y=130)
label_times.config(bg="green")
# Create a Combobox
options = ["Right", "Left", "Both"]
combo = ttk.Combobox(root, values=options, state="readonly")
combo.set("Select Mouse Button")  # Set default text
combo.place(x=10, y=155)
# Create a button
button_help2 = tk.Button(root, text="Help", command=on_button_help2_click)
button_help2.place(x=157.5, y=152.5)
button_help2.config(bg="cyan")

#-------------------------------------------------

#------------------------------ Third Row --------

# Create a button
button_help3 = tk.Button(root, text="Help", command=on_button_help3_click)
button_help3.place(x=120, y=240)
button_help3.config(bg="cyan")
# Create a label
label_times = tk.Label(root, text="How many times")
label_times.place(x=10, y=205)
label_times.config(bg="green")
# # Create an entry widget for user input
# entry = tk.Entry(root, width=20)
# entry.place(x=10, y=155)
# Create a Scale (slider) widget
scale_number = tk.Scale(root, from_=0, resolution=1, to=1000, orient='horizontal')
scale_number.place(x=10, y=230)
#-------------------------------------------------



# Create a button
button = tk.Button(root, text="Start", command=on_button_click)
button.place(x=350, y=255)


# Start the Tkinter event loop
root.mainloop()
