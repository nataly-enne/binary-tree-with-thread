import random
rand = random.random

class No:
     
     def __init__(self, key, dir, esq):
          self.item = key
          self.dir = dir
          self.esq = esq

class Tree:

     def __init__(self):
          self.root = No(None,None,None)
          self.root = None

     def inserir(self, v):
          novo = No(v,None,None) # cria um novo Nó
          if self.root == None:
               self.root = novo
          else: # se nao for a raiz
               atual = self.root
               while True:
                    anterior = atual
                    if v <= atual.item: # ir para esquerda
                         atual = atual.esq
                         if atual == None:
                                anterior.esq = novo
                                return
                    # fim da condição ir a esquerda
                    else: # ir para direita
                         atual = atual.dir
                         if atual == None:
                                 anterior.dir = novo
                                 return
                    # fim da condição ir a direita

     def buscar(self, chave):
         if self.root == None:
              return None # se arvore vazia
         atual = self.root # começa a procurar desde raiz
         while atual.item != chave: # enquanto nao encontrou
               if chave < atual.item:
                    atual = atual.esq # caminha para esquerda
               else:
                    atual = atual.dir # caminha para direita
               if atual == None:
                    return None # encontrou uma folha -> sai
         return atual  # terminou o laço while e chegou aqui é pq encontrou item    

  
     def inOrder(self, atual):
         if atual != None:
              self.inOrder(atual.esq)
              print(atual.item,end=" ")
              self.inOrder(atual.dir)
  
     def preOrder(self, atual):
         if atual != None:
              print(atual.item,end=" ")
              self.preOrder(atual.esq)
              self.preOrder(atual.dir)
       
     def posOrder(self, atual):
         if atual != None:
              self.posOrder(atual.esq)
              self.posOrder(atual.dir)
              print(atual.item,end=" ")

  
     def altura(self, atual):
          if atual == None or atual.esq == None and atual.dir == None:
               return 0
          else:
             if self.altura(atual.esq) > self.altura(atual.dir):
                return  1 + self.altura(atual.esq) 
             else:
                return  1 + self.altura(atual.dir) 
  
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
             return  1 + self.contarNos(atual.esq) + self.contarNos(atual.dir)

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


arv = Tree()

opcao = 0
while opcao != 3:
     word = gerapalavra()
     arv.inserir(word)
     print(word)
     print("***********************************")
     print("Entre com a opcao:")
     print(" --- 1: Continuar a gerar")
     print(" --- 2: Pesquisar")
     print(" --- 3: Sair do programa")
     print("***********************************")
     opcao = int(input("-> "))
     if opcao == 1:
          continue
     elif opcao == 2:
          x = str(input(" Informe o valor -> "))
          if arv.buscar(x) != None:
               print(" Valor Encontrado")
          else:
               print(" Valor nao encontrado!")	 
     elif opcao == 3:
          break
