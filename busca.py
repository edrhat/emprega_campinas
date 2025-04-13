import os
import tkinter as tk
from tkinter import ttk

#chave = input("Palavra chave: ")

#b = ("start chrome https://www.google.com/search?q=site%3Aempregacampinas.com.br+%22{}%22+inurl:2022".format(chave))
#os.system(b)

class Tela:

    def __init__(self, master):

        #Imagem EMPREGA CAMPINAS
        cab = tk.PhotoImage(file="cab.png")
        img = tk.Label(janela, image=cab)
        img.cab = cab
        img.place(x=145, y=2)

        #Imagem de RODAPE
        rodape = tk.PhotoImage(file="rodape.png")
        img2 = tk.Label(janela, image=rodape)
        img2.rodape = rodape
        img2.place(x=0, y=370)

        borracha = tk.PhotoImage(file="borracha.png")
        self.img3 = tk.Label(janela, image=borracha)
        self.img3.borracha = borracha
        self.img3.place(x=540, y=125)
        self.img3.bind("<Button-1>", self.bor1)
        

        borracha2 = tk.PhotoImage(file="borracha2.png")
        self.img4 = tk.Label(janela, image=borracha2)
        self.img4.borracha2 = borracha2
        self.img4.place(x=480, y=248)
        self.img4.bind("<Button-1>", self.bor2)
        
###########################################################################
        self.chave = tk.Label(janela, text="Pesquisar vagas para:")
        self.chave["font"] = ("Helvetica", "17")
        self.chave.config(bg="white", foreground="darkblue")
        self.chave.place(x=30, y=130)

        self.chaveE = tk.Entry(janela)
        self.chaveE["font"] = ("Helvetica", "17")
        self.chaveE.config(bg="#C0C0C0", foreground="red")
        self.chaveE.place(x=270, y=130)

        self.cidade = tk.Label(janela, text="Cidade:")
        self.cidade["font"] = ("Helvetica", "17")
        self.cidade.config(bg="white", foreground="darkblue")
        self.cidade.place(x=150, y=180)

        self.cidadeE = tk.Entry(janela)
        self.cidadeE["font"] = ("Helvetica", "17")
        self.cidadeE.config(bg="#C0C0C0", foreground="red")
        self.cidadeE.place(x=270, y=180)



        self.mess = tk.Label(janela, text="Mês da vaga:")
        self.mess["font"] = ("Helvetica", "17")
        self.mess.config(bg="white", foreground="darkblue")
        self.mess.place(x=80, y=250)

        meses = ["JANEIRO", "FEVEREIRO", "MARÇO", "ABRIL", "MAIO", "JUNHO", "JULHO", "AGOSTO", "SETEMBRO", "OUTUBRO", "NOVEMBRO", "DEZEMBRO"]
        self.mesE = ttk.Combobox(janela, values=meses)
        self.mesE["font"] = ("Helvetica", "17")
        self.mesE.place(x=270, y=250, width=200)
        
        

        self.buscar = tk.Button(janela, text="Buscar")
        self.buscar["font"] = ("Helvetica", "17")
        self.buscar.config(bg="#FFD700", foreground="black")
        self.buscar.place(x=320, y=300)
        self.buscar.bind("<Button-1>", self.buscarr)

        self.limpar = tk.Button(janela, text="Limpar")
        self.limpar["font"] = ("Helvetica", "17")
        self.limpar.config(bg="red", foreground="white")
        self.limpar.place(x=200, y=300)
        self.limpar.bind("<Button-1>", self.limparr)

    def buscarr(self, event):

        chave = self.chaveE.get()
        mes = self.mesE.get()
        cidade = self.cidadeE.get()

        if mes == "JANEIRO":
            mes = "01/2025"
        
        if mes == "FEVEREIRO":
            mes = "02/2025"

        if mes == "MARÇO":
            mes = "03/2025"

        if mes == "ABRIL":
            mes = "04/2025"

        if mes == "MAIO":
            mes = "05/2025"

        if mes == "JUNHO":
            mes = "06/2025"

        if mes == "JULHO":
            mes = "07/2025"

        if mes == "AGOSTO":
            mes = "08/2025"

        if mes == "SETEMBRO":
            mes = "09/2025"

        if mes == "OUTUBRO":
            mes = "10/2025"

        if mes == "NOVEMBRO":
            mes = "11/2025"

        if mes == "DEZEMBRO":
            mes = "12/2025"

            
        b = ("start chrome https://www.google.com/search?q=site%3Aempregacampinas.com.br+%22{}%22+intext:{}+intext:{}".format(chave,cidade,mes))
        os.system(b)

    def limparr(self, event):

        self.chaveE.delete(0, "end")
        self.mesE.delete(0, "end")

    def bor1(self, event):

        self.chaveE.delete(0, "end")

    def bor2(self, event):

        self.mesE.delete(0, "end")
        

            

            


janela = tk.Tk()
Tela(janela)

janela.geometry("600x420+200+100")
janela.title("Busca vagas")
janela.config(bg="white")

janela.resizable(width=False, height=False)
janela.mainloop()

