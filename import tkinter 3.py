import tkinter as tk
import random

# Create window
root = tk.Tk()
root.title("Valentine 💖")
root.geometry("420x520")
root.configure(bg="#f2c1ff")
root.resizable(False, False)

# Title
title1 = tk.Label(
    root,
    text="Dear Hala,",
    font=("Arial", 16),
    bg="#f2c1ff"
)
title1.pack(pady=(40, 5))

title2 = tk.Label(
    root,
    text="Will you be my Valentine?",
    font=("Arial", 20, "bold"),
    fg="#ff3f8e",
    bg="#f2c1ff"
)
title2.pack(pady=10)

# Message
message = tk.Label(
    root,
    text="I promise I would never leave you,\n"
         "you’re the perfect girl in my eyes 💋",
    font=("Arial", 12),
    bg="#f2c1ff"
)
message.pack(pady=20)

signature = tk.Label(
    root,
    text="- Yousef",
    font=("Arial", 12, "italic"),
    bg="#f2c1ff"
)
signature.pack(pady=10)

# Button frame
btn_frame = tk.Frame(root, bg="#f2c1ff", width=400, height=200)
btn_frame.pack(pady=30)
btn_frame.pack_propagate(False)

# Yes button action
def yes_clicked():
    for widget in root.winfo_children():
        widget.destroy()

    success = tk.Label(
        root,
        text="YAAAY 💖💖💖\nBest Valentine Ever 🥰",
        font=("Arial", 22, "bold"),
        fg="#ff3f8e",
        bg="#f2c1ff"
    )
    success.pack(expand=True)

# No button movement
def move_no(event=None):
    x = random.randint(20, 300)
    y = random.randint(20, 150)
    no_btn.place(x=x, y=y)

# Yes Button
yes_btn = tk.Button(
    btn_frame,
    text="Yes ❤️",
    font=("Arial", 14, "bold"),
    bg="#ff5fa2",
    fg="white",
    relief="flat",
    padx=20,
    pady=10,
    command=yes_clicked
)
yes_btn.place(x=150, y=40)

# No Button
no_btn = tk.Button(
    btn_frame,
    text="No",
    font=("Arial", 14),
    bg="white",
    fg="#555",
    relief="solid",
    padx=20,
    pady=10
)
no_btn.place(x=170, y=100)

# Make No button escape
no_btn.bind("<Enter>", move_no)
no_btn.bind("<Button-1>", move_no)

# Run app
root.mainloop()