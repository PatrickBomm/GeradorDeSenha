from cgitb import text
from random import *
from tkinter import *
import pyperclip

import string



def generate_password(n):
    password = ""

    for i in range(n):
        password += choice(string.ascii_letters + string.digits + string.punctuation)
        
    mensagem = Label(janela, text="Your password is: ")
    mensagem.grid(row=4, column=0)
    
    labelInsertNumber.delete(0, END)
    passwordshow["text"] = password
    pyperclip.copy(password)
    labelCopy = Label(janela, text="Copied to clipboard!")
    labelCopy.grid(row=10, column=0)
    

janela = Tk()
janela.title = "Gerador de Senha"
janela.grid = ("500x500")

text_orientation = Label(janela, text="How many characters do you want in your password? ")
text_orientation.grid(row=0, column=0)

passwordshow = Label(janela, text="")
passwordshow.grid(row=5, column=0)

labelInsertNumber = Entry(janela)
labelInsertNumber.grid(row=2, column=0)

gerar = Button(janela, text="Gerar", command=lambda: generate_password(int(labelInsertNumber.get())))
gerar.grid(row=3, column=0)

if labelInsertNumber.get() == "" or len(labelInsertNumber.get()) == 0:
    mensagem = Label(janela, text="Type a number!")
    mensagem.grid(row=4, column=0)
    


janela.mainloop()