import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Message", "Hello, World!")

# Membuat jendela utama
root = tk.Tk()
root.title("Contoh GUI")

# Membuat tombol dan menambahkannya ke jendela
btn = tk.Button(root, text="Click Me!", command=show_message)
btn.pack(pady=20)

# Menjalankan aplikasi
root.mainloop()
