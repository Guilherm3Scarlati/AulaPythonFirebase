import tkinter as tk
import subprocess
from PIL import Image, ImageTk
from tkinter import messagebox
import sys

def abrir_cadastro_cliente():
    subprocess.run (["python", "cliente.py"])


def abrir_cadastro_produto():
    subprocess.run(["python", "produto.py"])
    
def abrir_cadastro_vendedor():
    subprocess.run(["python", "vendedor.py"])
    
def verify_logged_user(data_from_previous_screen):
    if data_from_previous_screen == "Cliente":
        btnProduct.pack_forget()
        btnSeller.pack_forget()
    elif data_from_previous_screen == "Vendedor":
        btnClient.pack_forget()
        btnProduct.pack_forget()
    else:
        messagebox.showinfo("DATA", f"{data_from_previous_screen}")
        
        
        
    

data_from_previous_screen = sys.argv[1]

window = tk.Tk()
window['bg'] = 'gray'
window.title("Menu Loja")

image = Image.open("img/anac.jpg")
foto = ImageTk.PhotoImage(image)

txtImg = tk.Label(window, image=foto, width=300, height=300)
txtImg.pack()

btnClient = tk.Button(window, text="Cliente", command=abrir_cadastro_cliente)
btnClient.pack()

btnProduct = tk.Button(window, text="Produto", command=abrir_cadastro_produto)
btnProduct.pack()

btnSeller = tk.Button(window, text="Vendedor", command=abrir_cadastro_vendedor)
btnSeller.pack()

verify_logged_user(data_from_previous_screen)

window.mainloop()