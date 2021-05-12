import random

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
    if (PosZero[0] + 1) == PosPesquisa[0] or PosZero[0] == PosPesquisa[0] or (PosZero[0] - 1) == PosPesquisa[0]:
        if PosZero[1] == PosPesquisa[1]:
            Matriz[PosZero[0]][PosZero[1]] = Pesquisa
            Matriz[PosPesquisa[0]][PosPesquisa[1]] = 0

    if (PosZero[1] + 1) == PosPesquisa[1] or PosZero[1] == PosPesquisa[1] or (PosZero[1] - 1) == PosPesquisa[1]:
        if PosZero[0] == PosPesquisa[0]:
            Matriz[PosZero[0]][PosZero[1]] = Pesquisa
            Matriz[PosPesquisa[0]][PosPesquisa[1]] = 0


def main():
    tamanho = int(input("Digite a dimeção de uma matriz quadrada: "))
    Matriz=CriaMatriz(tamanho)
    MatrizPronta=MatrizFinal(tamanho)

    while True:

        for i in Matriz:
            for j in i:
                if j < 10:
                    print(f'0{j} ',end='')
                else:
                    print(f'{j} ',end='')
            print('')

        if Matriz == MatrizPronta:
            print("Parabéns! Você Ganhou!")
            break

        pesquisa = int(input("Digite o numero que vai trocar com o 0: "))
        PosPesquisa = PosNumero(pesquisa, Matriz)
        PosZero = PosNumero(0, Matriz)
        Movimento(pesquisa, PosPesquisa, PosZero, Matriz)
        print("\n" * 130)

main()