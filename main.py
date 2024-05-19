import tkinter as tk


def encrypt_cesar(message, key):
    encrypted_text = ""
    for char in message:
        if char.isalpha():
            shift = (ord(char) + key - ord('A')) % 26 + \
                ord('A') if char.isupper() else (
                    ord(char) + key - ord('a')) % 26 + ord('a')
            encrypted_text += chr(shift)
        else:
            encrypted_text += char
    return encrypted_text


def decrypt_cesar(encrypted_message, key):
    return encrypt_cesar(encrypted_message, -key)


def on_encrypt_button_click():
    message = entry_message.get()
    key = int(entry_key.get())

    encrypted_text = encrypt_cesar(message, key)

    text_encrypted.delete(1.0, tk.END)
    text_encrypted.insert(tk.END, encrypted_text)

    text_binary.delete(1.0, tk.END)
    text_binary.insert(tk.END, ' '.join(format(ord(char), '08b')
                       for char in encrypted_text))

    text_hex.delete(1.0, tk.END)
    text_hex.insert(tk.END, ' '.join(format(ord(char), '02X')
                    for char in encrypted_text))

    text_ascii.delete(1.0, tk.END)
    text_ascii.insert(tk.END, ' '.join(str(ord(char))
                      for char in encrypted_text))


def on_decrypt_button_click():
    encrypted_message = entry_message.get()
    key = int(entry_key.get())

    decrypted_text = decrypt_cesar(encrypted_message, key)

    text_decrypted.delete(1.0, tk.END)
    text_decrypted.insert(tk.END, decrypted_text)


def on_clear_button_click():
    entry_message.delete(0, tk.END)
    entry_key.delete(0, tk.END)

    text_encrypted.delete(1.0, tk.END)
    text_binary.delete(1.0, tk.END)
    text_hex.delete(1.0, tk.END)
    text_ascii.delete(1.0, tk.END)
    text_decrypted.delete(1.0, tk.END)


def select_exercise(exercise_num):
    if exercise_num == 1:
        label_message.config(text="Mensaje:")
        btn_encrypt.config(text="Encriptar", command=on_encrypt_button_click)
        btn_decrypt.config(text="Limpiar", command=on_clear_button_click)
    elif exercise_num == 2:
        label_message.config(text="Mensaje Encriptado:")
        btn_encrypt.config(text="Desencriptar",
                           command=on_decrypt_button_click)
        btn_decrypt.config(text="Limpiar", command=on_clear_button_click)


# Crear la ventana principal
window = tk.Tk()
window.title("ACO | Encriptador Cesar")

# Crear menu
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

exercise_menu = tk.Menu(menu_bar, tearoff=0)
exercise_menu.add_command(
    label="Ejercicio 1", command=lambda: select_exercise(1))
exercise_menu.add_command(
    label="Ejercicio 2", command=lambda: select_exercise(2))

menu_bar.add_cascade(label="Ejercicios", menu=exercise_menu)

# Crear widgets
label_message = tk.Label(window, text="Mensaje:")
entry_message = tk.Entry(window, width=30)

label_key = tk.Label(window, text="Llave:")
entry_key = tk.Entry(window, width=5)

btn_encrypt = tk.Button(window, text="Encriptar",
                        command=on_encrypt_button_click)
btn_decrypt = tk.Button(window, text="Desencriptar",
                        command=on_decrypt_button_click)

text_encrypted = tk.Text(window, height=5, width=40)
text_binary = tk.Text(window, height=5, width=40)
text_hex = tk.Text(window, height=5, width=40)
text_ascii = tk.Text(window, height=5, width=40)

text_decrypted = tk.Text(window, height=5, width=40)

# Posicionar widgets en la ventana
label_message.grid(row=0, column=0, sticky=tk.E)
entry_message.grid(row=0, column=1, columnspan=2)

label_key.grid(row=1, column=0, sticky=tk.E)
entry_key.grid(row=1, column=1, sticky=tk.W)

btn_encrypt.grid(row=2, column=0, pady=5)
btn_decrypt.grid(row=2, column=1, pady=5)

text_encrypted.grid(row=3, column=0, columnspan=3)
text_binary.grid(row=4, column=0, columnspan=3)
text_hex.grid(row=5, column=0, columnspan=3)
text_ascii.grid(row=6, column=0, columnspan=3)

text_decrypted.grid(row=7, column=0, columnspan=3)

# Iniciar el bucle principal de la ventana
window.mainloop()