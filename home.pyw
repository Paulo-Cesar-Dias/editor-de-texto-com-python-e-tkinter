
from tkinter import *
from tkinter import filedialog
janela=Tk()
#cores
preto="black"
branco="white"
roxo="purple"
cinza="grey"

#configurações da janela
janela.geometry("300x300")
janela["bg"]=preto

#funções
def editar():
    janela.destroy()
    import editar

def savando():
    janela.destroy()
    import criar

#objetos da janela
label_1=Label(janela,text="Olá, seja bem-vindo\nEscolha oque deseja fazer hoje!",bg=preto,fg=branco,font="25")
botaoeditar=Button(janela,fg=branco,bg=preto,text="Editar",font="Arial 25",command=editar)
botaocriar=Button(janela,bg=preto,fg=branco,text="Criar",font="Arial 28",command=savando)

#localização dos objetos
label_1.pack()
botaoeditar.pack()
botaocriar.pack()

janela.mainloop()