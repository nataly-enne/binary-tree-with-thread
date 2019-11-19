import random
import threading
import time
rand = random.random

global atual


class No:

    def __init__(self, key, dir, esq):
        self.item = key
        self.dir = dir
        self.esq = esq


class Tree:

    def __init__(self):
        self.root = No(None, None, None)
        self.root = None

    def inserir(self, v):
        novo = No(v, None, None)  # cria um novo Nó

        if self.root == None:
            self.root = novo
        else:  # se nao for a raiz
            self.atual = self.root
            while True:
                self.anterior = self.atual
                if v <= self.atual.item:  # ir para esquerda
                    self.esquerda(novo)
                    return
                # fim da condição ir a esquerda
                else:  # ir para direita
                    self.direita(novo)
                    return
                # fim da condição ir a direita

    def esquerda(self, novo):
        self.atual = self.atual.esq
        if self.atual == None:
            self.anterior.esq = novo

    def direita(self, novo):
        self.atual = self.atual.dir
        if self.atual == None:
            self.anterior.dir = novo

    def buscar(self, chave):
        if self.root == None:
            return None  # se arvore for vazia
        atual = self.root  # começa a procurar desde raiz
        while atual.item != chave:  # enquanto nao encontrou
            if chave < atual.item:
                atual = atual.esq  # anda para esquerda
            else:
                atual = atual.dir  # anda para direita
            if atual == None:
                return None  # encontrou uma folha -> sai
        return atual  # terminou o laço while e chegou aqui é pq encontrou item

 # aqueles negocios de in order, pre order e pos order
    def inOrder(self, atual):
        if atual != None:
            self.inOrder(atual.esq)
            print(atual.item, end=" ")
            self.inOrder(atual.dir)

    def preOrder(self, atual):
        if atual != None:
            print(atual.item, end=" ")
            self.preOrder(atual.esq)
            self.preOrder(atual.dir)

    def posOrder(self, atual):
        if atual != None:
            self.posOrder(atual.esq)
            self.posOrder(atual.dir)
            print(atual.item, end=" ")

    def altura(self, atual):
        if atual == None or atual.esq == None and atual.dir == None:
            return 0
        else:
            if self.altura(atual.esq) > self.altura(atual.dir):
                return 1 + self.altura(atual.esq)
            else:
                return 1 + self.altura(atual.dir)

    def folhas(self, atual):
        if atual == None:
            return 0
        if atual.esq == None and atual.dir == None:
            return 1
        return self.folhas(atual.esq) + self.folhas(atual.dir)

    def contarNos(self, atual):
        if atual == None:
            return 0
        else:
            return 1 + self.contarNos(atual.esq) + self.contarNos(atual.dir)

    def minn(self):
        atual = self.root
        anterior = None
        while atual != None:
            anterior = atual
            atual = atual.esq
        return anterior

    def maxx(self):
        atual = self.root
        anterior = None
        while atual != None:
            anterior = atual
            atual = atual.dir
        return anterior

#### fim da classe ####


#### gerador de palavras [random generator] ####
consoantes = 'bcdfghjlmnpqrstvxz'
vogais = 'aeiou'


def pegaletra(tipo):
    if tipo == 0:
        return consoantes[int(rand()*len(consoantes))]
    if tipo == 1:
        return vogais[int(rand()*len(vogais))]


def gerapalavra():
    tamanho = int(rand()*4+3)
    atual = int(rand()*2)
    palavra = ''
    for letr in range(tamanho+1):
        letra = pegaletra(atual)
        if letra == 'q':
            letra = 'qu'
        palavra = palavra + letra
        if atual == 0:
            atual = 1
        else:
            atual = 0
    return palavra

#### fim ####


def inserirValores(arv):
    while True:
        word = gerapalavra()
        arv.inserir(word)
        print('Palavra inserida: ', word)
        time.sleep(4)


arv = Tree()

t = threading.Thread(target=inserirValores, args=(arv,))
t.start()

opcao = 0
while opcao != 2:
    print("***********************************")
    print("Entre com a opcao:")
    print(" --- 1: Pesquisar")
    print(" --- 2: Sair do programa")
    print("***********************************")
    opcao = int(input("-> "))
    if opcao == 1:
        x = str(input(" Informe o valor -> "))
        if arv.buscar(x) != None:
            print(" Valor Encontrado")
        else:
            print("Valor nao encontrado!")
    elif opcao == 2:
        break
