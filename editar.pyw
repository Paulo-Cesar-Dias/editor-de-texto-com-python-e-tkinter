from os import read
from tkinter import *
from tkinter import filedialog
janela=Tk()
#cores
preto="black"
branco="white"
roxo="purple"
cinza="grey"

#configurações da janela
janela.geometry("500x500")
janela["bg"]=preto

arquivo = str(filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all filles","*.*"))))#buscando o arquivo
print(arquivo)
x=open(arquivo,"r")#abindo ele de acordo com a localização
z=x.read()#lendo
frame=Frame(janela)

descendo=Scrollbar(frame)
texto=Text(frame,bg=preto,fg=branco,insertbackground=branco,yscrollcommand = descendo.set)
descendo.pack(side = RIGHT, fill = Y)  
texto.insert(0.0,z)#inserindo o arquivo no whidth testo
texto.focus_force()
descendo.config(command=texto.yview)
#funções-----------
def save():
    salvando=open(arquivo,"w")
    salvando.write(texto.get(1.0,END))
    print("Alterações salvas")
bt_save=Button(janela,text="Salvar alterações",bg=preto,fg=branco,command=save)
bt_save.pack()
frame.pack()
texto.pack()

janela.mainloop()