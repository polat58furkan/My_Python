# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 14:31:08 2024

@author: user
"""

import threading
import webbrowser
from pynput.mouse import Button, Controller, Listener
import time
import tkinter as tk
from tkinter import ttk

# Fare denetleyicisi oluşturma
mouse = Controller()

# Global flag'ler ve fare tıklama düğmeleri listeleri
button_pressed = False
button_pressed_x2 = False
button_pressed_middle = False
click_buttons = [Button.left]
click_right = [Button.right]
selected_button = None
listener = None

def on_click(x, y, button, pressed):
    global button_pressed, button_pressed_x2, button_pressed_middle, listener, root
    if button == Button.x1:
        button_pressed = pressed
        print(f"Mouse button {button} {'pressed' if pressed else 'released'} at ({x}, {y})")
    elif button == Button.x2:
        button_pressed_x2 = pressed
        print(f"Mouse button {button} {'pressed' if pressed else 'released'} at ({x}, {y})")
    elif button == Button.middle:
        button_pressed_middle = pressed
        print(f"Mouse button {button} {'pressed' if pressed else 'released'} at ({x}, {y})")
        if pressed:
            print("Exiting...")
            listener.stop()
            root.deiconify()
            return False

# Belirli işlemi sürekli gerçekleştirme fonksiyonu
def perform_task():
    global root
    while not button_pressed_middle:
        if button_pressed:
            print("Performing left click task...")
            for btn in click_buttons:
                mouse.click(btn)
        if button_pressed_x2:
            print("Performing right click task...")
            for btn in click_right:
                mouse.click(btn)
        time.sleep(0.1)

    print("Middle button clicked. Exiting task loop.")
    root.deiconify()

# Dinleyiciyi başlatma
def start_listener():
    global listener
    listener = Listener(on_click=on_click)
    listener.start()
    listener.join()

# URL açma fonksiyonu
def open_link(event):
    webbrowser.open_new("https://www.youtube.com/@ILegendI")

# Tkinter arayüzü başlatma
def start_gui():
    global root
    def on_start():
        root.withdraw()  # Tkinter penceresini gizle
        listener_thread = threading.Thread(target=start_listener)
        listener_thread.start()

        task_thread = threading.Thread(target=perform_task)
        task_thread.start()

    root = tk.Tk()
    root.title("Macro Of LéGéND")
    root.config(bg="black")
    
    # Pencere boyutunu ve konumunu belirleme
    window_width = 400
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_x = (screen_width // 2) - (window_width // 2)
    position_y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TFrame', background='black')
    style.configure('TLabel', background='black', foreground='cyan')
    style.configure('TButton', background='black', foreground='cyan')

    frame = ttk.Frame(root, padding="5")
    frame.pack(expand=True, fill='both')
    
    # "Welcome, My Friend" etiketi ekleme
    label = ttk.Label(frame, text="Welcome, My Friend", style='TLabel')
    label.pack(pady=10)

    # Tıklanabilir link etiketi ekleme
    link = ttk.Label(frame, text="Click here to visit Youtube", style='TLabel', foreground="blue", cursor="hand2")
    link.pack(pady=50)
    link.bind("<Button-1>", open_link)
    
    start_button = ttk.Button(frame, text="Start", command=on_start)
    start_button.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    start_gui()
