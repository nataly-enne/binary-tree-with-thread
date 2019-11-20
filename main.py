from threading import Thread
from time import sleep, time
from node import  No, inserir, busca


ARQUIVO = 'texto_menor.txt'


def inserir_dados(root, arquivo):
    start_tempo = time()

    with open(arquivo) as a:
        linha = a.readline() # lê linha 
        while linha:
            palavra = linha.strip()
            inserir(root, No(palavra)) # insere cada palavra em cada linha lida na árvore.
            # sleep(0.1)
            linha = a.readline()

    fim_tempo = time()
    print(f"--- {(fim_tempo - start_tempo)} segundos decorridos ---")


def main(root): 
    # thread que resulta na paralelização da inserção de dados na árvore.
    thread = Thread(target=inserir_dados, args=(root, ARQUIVO))
    thread.start()


def menu(root):
    while True:
        try:
            value = str(input(">"))
            if not busca(root, value) is None:
                print("Valor encontrado.")
            else:
                print("Valor não econtrado!")
        except KeyboardInterrupt:
            break

# chamando as funçoes e iniciando
if __name__ == '__main__':
    root = No('__init__')
    main(root)
    print("Digite uma palavra:")
    menu(root)
