import tkinter as tk
from openpyxl import Workbook, load_workbook
from tkinter import messagebox
import matplotlib.pyplot as plt

import pyrebase

config = {
  "apiKey": "AIzaSyAgo4wouZJWiMBMzCSotXybN0zKP7eZE0o",
  "authDomain": "dbpy-c45e3.firebaseapp.com",
  "databaseURL": "https://dbpy-c45e3-default-rtdb.firebaseio.com",
  "projectId": "dbpy-c45e3",
  "storageBucket": "dbpy-c45e3.appspot.com",
  "messagingSenderId": "1018244276755",
  "appId": "1:1018244276755:web:f5356387bf63317994d5e6"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def add_client():
    nome = entry_nome.get()
    data_nascimento = entry_data_nascimento.get()
    cpf = entry_cpf.get()
    origem = entry_origem.get()
    score = entry_score.get()
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    
    data = {
        'Nome':nome,
        'Data de Nascimento': data_nascimento,
        'CPF': cpf,
        'Origem': origem,
        'Score': score,
        'Usuario': usuario,
        'Senha': senha
    }
    
    db.child('clientes').push(data)
    
    entry_nome.delete(0, tk.END)
    entry_data_nascimento.delete(0, tk.END)
    entry_cpf.delete(0, tk.END)
    entry_origem.delete(0, tk.END)
    entry_score.delete(0, tk.END)
    entry_usuario.delete(0, tk.END)
    entry_senha.delete(0, tk.END)
    
    messagebox.showinfo("Resultado", "Cadastrado com sucesso!")
    
    
def validate_login():
   username = entry_usuario.get()   
   password = entry_senha.get() 
   
   db = firebase.database()
   
   users = db.child('clientes').get().val()
   
        
    
window = tk.Tk()
window['bg'] = 'gray'
window.title("Cadastro de Clientes")

label_name = tk.Label(window, text="Entre com o seu nome completo!")
label_name.pack()

entry_nome = tk.Entry(window, text="")
entry_nome.pack()

label_cpf = tk.Label(window, text="Entre com o seu cpf!")
label_cpf.pack()

entry_cpf = tk.Entry(window, text="")
entry_cpf.pack()

label_data_nascimento = tk.Label(window, text="Entre com a sua data de nascimento!")
label_data_nascimento.pack()

entry_data_nascimento = tk.Entry(window, text="")
entry_data_nascimento.pack()

label_origem = tk.Label(window, text="Chegaste a está aplicação através do site ou loja?")
label_origem.pack()

entry_origem = tk.Entry(window, text="")
entry_origem.pack()

label_score = tk.Label(window, text="Entre com o seu score!")
label_score.pack()

entry_score = tk.Entry(window, text="")
entry_score.pack()

label_usuario = tk.Label(window, text="Usuário")
label_usuario.pack()

entry_usuario = tk.Entry(window, text="")
entry_usuario.pack()

label_senha = tk.Label(window, text="Senha")
label_senha.pack()

entry_senha = tk.Entry(window, text="")
entry_senha.pack()

button_adicionar = tk.Button(window, text="Adicionar", command=add_client)
button_adicionar.pack()

window.mainloop()