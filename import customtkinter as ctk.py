import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            if mode == "encrypt":
                result += chr(start + (ord(char) - start + shift) % 26)
            else:
                result += chr(start + (ord(char) - start - shift) % 26)
        else:
            result += char
    return result

def process_text(mode):
    try:
        text = message_entry.get()
        shift = int(shift_entry.get())

        if not text:
            messagebox.showwarning("Warning", "Please enter a message.")
            return

        result = caesar_cipher(text, shift, mode)
        result_box.delete("1.0", "end")
        result_box.insert("end", result)

    except ValueError:
        messagebox.showerror("Error", "Shift value must be a number.")


app = ctk.CTk()
app.title("Caesar Cipher")
app.geometry("520x420")
app.resizable(False, False)


title = ctk.CTkLabel(
    app,
    text="Caesar Cipher Tool",
    font=ctk.CTkFont(size=22, weight="bold")
)
title.pack(pady=20)


frame = ctk.CTkFrame(app, corner_radius=15)
frame.pack(padx=20, pady=10, fill="both", expand=True)


ctk.CTkLabel(frame, text="Message", font=("Arial", 14)).pack(anchor="w", padx=20, pady=(20, 5))
message_entry = ctk.CTkEntry(frame, height=35)
message_entry.pack(fill="x", padx=20)


ctk.CTkLabel(frame, text="Shift Value", font=("Arial", 14)).pack(anchor="w", padx=20, pady=(15, 5))
shift_entry = ctk.CTkEntry(frame, width=100, height=35)
shift_entry.pack(anchor="w", padx=20)


button_frame = ctk.CTkFrame(frame, fg_color="transparent")
button_frame.pack(pady=20)

encrypt_btn = ctk.CTkButton(
    button_frame,
    text="Encrypt",
    width=140,
    command=lambda: process_text("encrypt")
)
encrypt_btn.grid(row=0, column=0, padx=10)

decrypt_btn = ctk.CTkButton(
    button_frame,
    text="Decrypt",
    width=140,
    command=lambda: process_text("decrypt")
)
decrypt_btn.grid(row=0, column=1, padx=10)


ctk.CTkLabel(frame, text="Result", font=("Arial", 14)).pack(anchor="w", padx=20)
result_box = ctk.CTkTextbox(frame, height=80)
result_box.pack(fill="x", padx=20, pady=(5, 20))

app.mainloop()
