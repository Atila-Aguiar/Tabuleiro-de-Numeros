import random
from tkinter import *

def CriaMatriz(tamanho):
    Matriz = []
    numeros = []

    for i in range(tamanho*tamanho):
        numeros.append(i)

    for i in range(tamanho):
        linha = []

        for j in range(tamanho):
            aleatorio = random.choice(numeros)
            linha.append(aleatorio)
            numeros.remove(aleatorio)

        Matriz.append(linha)

    return Matriz

def MatrizFinal(tamanho):
    Matriz = []
    numeros = []

    for i in range(tamanho * tamanho):
        numeros.append(i)
    numeros.pop(0)
    numeros.append(0)

    contador = 0
    for i in range(tamanho):
        linha = []

        for j in range(tamanho):
            linha.append(numeros[contador])
            contador+=1

        Matriz.append(linha)

    return Matriz

def PosNumero(numero, Matriz):
        linha = 0

        for i in Matriz:
            if numero in i:
                coluna = (i.index(numero))
                break
            linha += 1

        return (linha,coluna)

def Movimento(Pesquisa, PosPesquisa, PosZero, Matriz):
    try:
        for i in Frame3.winfo_children():
            i.destroy()
    except NameError:
        print(NameError)

    if (PosZero[0] + 1) == PosPesquisa[0] or PosZero[0] == PosPesquisa[0] or (PosZero[0] - 1) == PosPesquisa[0]:
        if PosZero[1] == PosPesquisa[1]:
            Matriz[PosZero[0]][PosZero[1]] = Pesquisa
            Matriz[PosPesquisa[0]][PosPesquisa[1]] = 0

    if (PosZero[1] + 1) == PosPesquisa[1] or PosZero[1] == PosPesquisa[1] or (PosZero[1] - 1) == PosPesquisa[1]:
        if PosZero[0] == PosPesquisa[0]:
            Matriz[PosZero[0]][PosZero[1]] = Pesquisa
            Matriz[PosPesquisa[0]][PosPesquisa[1]] = 0


    for i in Matriz:
        subframe = Frame(Frame3)
        subframe.pack ()
        for j in i:
            if j == 0:
                espaçamento = Label (subframe, padx=38, pady=25)
                espaçamento.pack (side="left")
            elif j < 10:
                botão = Button (subframe, text=f"0{j}", bg="yellow", padx=25, pady=25, font=40)
                botão['command'] = lambda bot=j, posnumero=PosNumero (j, Matriz), poszero=PosNumero (0, Matriz), matriz=Matriz: Movimento(bot, posnumero, poszero, matriz)
                botão.pack (side="left")
            else:
                botão = Button (subframe, text=f"{j}", bg="yellow", padx=25, pady=25, font=40)
                botão['command'] = lambda bot=j, posnumero=PosNumero(j, Matriz), poszero=PosNumero(0, Matriz), matriz=Matriz: Movimento(bot, posnumero, poszero, matriz)
                botão.pack (side="left")

        if Matriz == MatrizPronta:
            telinha = Tk()
            Texto = Label(telinha, text="Você Venceu! Parabéns!")
            Texto.pack()
            telinha.mainloop()
        else:
            Frame3.pack()


def main():
    instancia = Tk()
    tamanho = 3 #int(input("Digite a dimeção da matriz: "))
    Matriz=CriaMatriz(tamanho)
    global MatrizPronta
    MatrizPronta=MatrizFinal(tamanho)

    global Frame3
    Frame3 = Frame(instancia)
    Frame3.pack()
    for i in Matriz:
        subframe = Frame (Frame3)
        subframe.pack ()
        for j in i:
            if j == 0:
                espaçamento = Label (subframe, padx=38, pady=25)
                espaçamento.pack (side="left")
            elif j < 10:
                botão = Button(subframe, text=f"0{j}", bg="yellow", padx=25, pady=25, font=40)
                botão['command'] = lambda bot=j, posnumero=PosNumero(j,Matriz), poszero=PosNumero(0,Matriz), matriz=Matriz: Movimento(bot, posnumero, poszero, matriz)
                botão.pack(side="left")
            else:
                botão = Button(subframe, text=f"{j}", bg="yellow", padx=25, pady=25, font=40)
                botão['command'] = lambda bot=j, posnumero=PosNumero(j,Matriz), poszero=PosNumero(0,Matriz), matriz=Matriz: Movimento(bot, posnumero, poszero, matriz)
                botão.pack(side="left")

        if Matriz == MatrizPronta:
            print("Parabéns! Você Ganhou!")
            instancia.destroy()

    instancia.mainloop()


main()