# save_data.py
import numpy as np
import tkinter as tk
from tkinter import messagebox
from matplotlib.widgets import Button

def save_creation(T, base_filename="heat_data"):
    np.save(f"{base_filename}.npy", T)
    np.savetxt(f"{base_filename}.csv", T, delimiter=",", fmt="%.2f")

    print(" The painting has been saved! yay ;))")
    print(f"  - {base_filename}.npy")
    print(f"  - {base_filename}.csv")

    try:
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Saved!"," Your masterpiece has been saved! yayy ")
        root.destroy()
    except Exception:
        print("(No GUI popup available)")

def add_buttons(fig, T_ref, pause_flag):
    
    ax_toggle = fig.add_axes([0.81, 0.01, 0.1, 0.05])
    btn_toggle = Button(ax_toggle, 'DURDUR')

    def on_toggle(event):
        pause_flag[0] = not pause_flag[0]
        btn_toggle.label.set_text('Continue' if pause_flag[0] else 'Stop')

    btn_toggle.on_clicked(on_toggle)
