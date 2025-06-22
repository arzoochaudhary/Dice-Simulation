# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 11:12:16 2021
@author: Arzoo
Modularized without changing original layout
"""

import random
import os
import tkinter as tk
from PIL import Image, ImageTk

# --- Constants ---
DICE = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png']
SCRIPT_DIR = os.path.dirname(__file__)

# --- Utility Functions ---
def pick_image(biased=False):
    """Return file path for dice image, biased adds extra '6's."""
    choices = DICE + (['6.png'] * 2 if biased else [])
    return os.path.join(SCRIPT_DIR, random.choice(choices))

def prepare_open_path(fp):
    """Normalize Windows backslashes to forward slashes."""
    return fp.replace('\\', '/')

def load_photo(filepath):
    return ImageTk.PhotoImage(Image.open(filepath))

# --- GUI Setup ---
def setup_root():
    root = tk.Tk()
    root.geometry('400x400')
    root.title('Dice Simulation')
    return root

def add_heading(root):
    tk.Label(root, text="").pack()
    heading1 = tk.Label(root, text='Dice Simulator', fg='white', bg='black', font=("", 44))
    heading1.pack()
    tk.Label(root, text="").pack()

def add_dice_and_button(root, side, btn_text, biased=False):
    # Load initial image
    fp = prepare_open_path(pick_image(biased))
    img = load_photo(fp)
    lbl = tk.Label(root, image=img)
    lbl.image = img
    lbl.pack(side=side, expand=True)

    def on_roll():
        fp2 = prepare_open_path(pick_image(biased))
        new_img = load_photo(fp2)
        lbl.configure(image=new_img)
        lbl.image = new_img

    btn = tk.Button(root, text=btn_text, fg='black', bg='white',
                    height=2, width=30, command=on_roll)
    btn.pack(side=side, expand=True)

# --- Main ---
def main():
    root = setup_root()
    add_heading(root)

    add_dice_and_button(root, side=tk.LEFT, btn_text="Roll the normal Dice", biased=False)
    add_dice_and_button(root, side=tk.RIGHT, btn_text="Roll the Dice with high prob of 6", biased=True)

    root.mainloop()

if __name__ == "__main__":
    main()
