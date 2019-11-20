from threading import Thread

class No:
    def __init__(self, key):
        self.direita = None
        self.esquerda = None
        self.item = key


def inserir(root, no):
    if root is None:
        root = no # cria um novo Nó
    else:
        if root.item < no.item:
            if root.esquerda is None:
                root.esquerda = no
            # se nao for a raiz
            else:
                # insere com a thread na esquerda
                thread_esquerda = Thread(target=inserir, args=(root.esquerda, no))
                thread_esquerda.start()
        else: # condicao ir para a direita (caso n tenha nenhum no ele cria)
            if root.direita is None:
                root.direita = no
            else:
                # insere com a thread na direita
                thread_direita = Thread(target=inserir, args=(root.direita, no))
                thread_direita.start()


def busca(root, key):
    if root is None or root.item == key:
        return root # se arvore for vazia

    if root.item < key:
        return busca(root.esquerda, key)  # anda para esquerda

    return busca(root.direita, key) # anda para direita
