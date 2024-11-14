import tkinter as tk
from tkinter import ttk

def enkripsi(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isupper():
            cipher_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            cipher_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            cipher_text += char
    return cipher_text

def dekripsi(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        if char.isupper():
            plain_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            plain_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            plain_text += char
    return plain_text

def process_text():
    try:
        shift = int(shift_value.get())
        text = input_text.get("1.0", "end-1c")
        if mode.get() == "encrypt":
            result = enkripsi(text, shift)
        else:
            result = dekripsi(text, shift)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)
    except ValueError:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Please enter a valid shift value.")

# GUI setup
root = tk.Tk()
root.title("Cipher Encryption Machine")
root.geometry("500x400")
root.config(bg="#e6dccf")  # Background color

# Styling
title_font = ("Courier New", 20, "bold")  # Aesthetic font for title
label_font = ("Courier New", 12, "bold")  # Aesthetic font for labels
button_font = ("Courier New", 12, "bold")  # Aesthetic font for buttons

# Shift Value Frame
shift_frame = tk.Frame(root, bg="#e6dccf")
shift_frame.pack(pady=10)
tk.Label(shift_frame, text="Set Shift Value:", font=label_font, bg="#e6dccf", fg="#34495e").grid(row=0, column=0, padx=10, pady=5)
shift_value = tk.Entry(shift_frame, width=5, font=label_font, bg="#ffffff", fg="#34495e", relief="solid")
shift_value.grid(row=0, column=1, padx=5, pady=5)

# Input Text Frame
input_frame = tk.Frame(root, bg="#e6dccf")
input_frame.pack(pady=10)
tk.Label(input_frame, text="Input Text to Encrypt/Decrypt:", font=label_font, bg="#e6dccf", fg="#34495e").grid(row=0, column=0, padx=10, pady=5)
input_text = tk.Text(input_frame, height=5, width=40, font=("Courier New", 10), bg="#ffffff", fg="#34495e", relief="solid")
input_text.grid(row=1, column=0, padx=10, pady=5)

# Mode selection
mode_frame = tk.Frame(root, bg="#e6dccf")
mode_frame.pack(pady=10)
mode = tk.StringVar(value="encrypt")
ttk.Style().configure("TRadiobutton", background="#e6dccf", foreground="#34495e", font=label_font)
ttk.Radiobutton(mode_frame, text="Encrypt", variable=mode, value="encrypt", style="TRadiobutton").grid(row=0, column=0, padx=20)
ttk.Radiobutton(mode_frame, text="Decrypt", variable=mode, value="decrypt", style="TRadiobutton").grid(row=0, column=1, padx=20)

# Process Button
process_button = tk.Button(root, text="Process Text", command=process_text, font=button_font, bg="#c3b091", fg="#ffffff", activebackground="#a89075", activeforeground="#ffffff", relief="raised")
process_button.pack(pady=10)

# Output Text Frame
output_frame = tk.Frame(root, bg="#e6dccf")
output_frame.pack(pady=10)
tk.Label(output_frame, text="Output:", font=label_font, bg="#e6dccf", fg="#34495e").grid(row=0, column=0, padx=10, pady=5)
output_text = tk.Text(output_frame, height=5, width=40, font=("Courier New", 10), bg="#ffffff", fg="#34495e", relief="solid")
output_text.grid(row=1, column=0, padx=10, pady=5)

root.mainloop()
