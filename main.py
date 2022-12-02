from array_queue import ArrayQueue

class treeNode(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.height = 1

class AVLTree(object):
  # Adicionando elemento na Árvore AVL
	def insert(self, root, key):
		if not root:
			return treeNode(key)
		elif key < root.value:
			root.left = self.insert(root.left, key)
		else:
			root.right = self.insert(root.right, key)

		root.height = 1 + max(self.getHeight(root.left),
						self.getHeight(root.right))

		b = self.getBal(root)

		if b > 1 and key < root.left.value:
			return self.rRotate(root)

		if b < -1 and key > root.right.value:
			return self.lRotate(root)

		if b > 1 and key > root.left.value:
			root.left = self.lRotate(root.left)
			return self.rRotate(root)

		if b < -1 and key < root.right.value:
			root.right = self.rRotate(root.right)
			return self.lRotate(root)

		return root

  # Fazendo a rotação para esquerda
	def lRotate(self, z):
		y = z.right
		T2 = y.left

		y.left = z
		z.right = T2

		z.height = 1 + max(self.getHeight(z.left),
						self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left),
						self.getHeight(y.right))

		return y

  # Fazendo a rotação para direita
	def rRotate(self, z):
		y = z.left
		T3 = y.right

		y.right = z
		z.left = T3

		z.height = 1 + max(self.getHeight(z.left),
						self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left),
						self.getHeight(y.right))

		return y

  # Medindo a altura da Árvore AVL
	def getHeight(self, root):
		if not root:
			return 0

		return root.height

  # Checando se a Árvore está balanceada
	def getBal(self, root):
		if not root:
			return 0

		return self.getHeight(root.left) - self.getHeight(root.right)

if __name__ == "__main__":
  # Caminhamento por nível
  def nivelArbin(arbin):
    queue = ArrayQueue()
    queue.enqueue(arbin)
    while not queue.is_empty():
      node = queue.dequeue()
      print("{0} ".format(node.value), end="")
      if node.left:
        queue.enqueue(node.left)
      if node.right:
        queue.enqueue(node.right)

  # Menu
  def menu_principal():
    print('\n----------MENU PRINCIPAL------------\n')
    print('(1) Adicionar elemento na Árvore AVL')
    print('(2) Exibir a Árvore por nível')      
    print('(3) Sair\n')
    
  def menu_secundario():
    print('\n----------MENU SECUNDÁRIO-----------\n')
    print('(1) Exibir a Árvore por nível')      
    print('(2) Sair\n')

  def menu_final():
    print('\n-------------MENU FINAL-------------\n')   
    print('(1) Sair\n')
    
  menu_principal()

  opcoes = int(input('Escolha a função desejada: '))
  while opcoes < 1 or opcoes > 3:
    print('\n------------------------------------\n')
    print('Opção inválida. Por favor, selecione uma das opções do menu.\n')
    opcoes = int(input('Escolha a função desejada: '))
  else:
    if opcoes == 1:
      posicoes = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto', 'Sexto']

      print('\n------------------------------------\n')
      
      # Adicionando elemento na Árvore AVL
      for posicao in posicoes:
        with open('entrada.txt', 'a') as f1:
          f1.write(input(posicao + ' elemento: ') + "\r\n")
          
      menu_secundario()
      
      opcoes = int(input('Escolha a função desejada: ')) + 1      
      while opcoes < 2 or opcoes > 3:
        print('\n------------------------------------\n')
        print('Opção inválida. Por favor, selecione uma das opções do menu.\n')
        opcoes = int(input('Escolha a função desejada: ')) + 1

    if opcoes == 2:
      # Criação da Árvore AVL
      Tree = AVLTree()
      root = None
    
      # Lendo arquivo de texto
      file1 = open('entrada.txt', 'r')
      Lines = file1.readlines()
    
      # For loop adicionando as palavras do txt na Árvore
      count = 0
      for line in Lines:
        count += 1
        root = Tree.insert(root, line.strip())
        
      print('\n------------------------------------\n')

      # Verificando se a Árvore está vázia
      if (root == None):
        print('A Árvore está vázia.')
      else:
        # Exibindo a árvore por nivel
        nivelArbin(root)
        print()

        menu_final()

        opcoes = int(input('Escolha a função desejada: ')) + 2
        while opcoes != 3:
          print('\n------------------------------------\n')
          print('Opção inválida. Por favor, selecione uma das opções do menu.\n')
          opcoes = int(input('Escolha a função desejada: ')) + 2

    # Saindo do menu
    if opcoes == 3:
      clearfile = open("entrada.txt",'w')
      clearfile.close()

      print('\n------------------------------------\n')
      print('Encerrando aplicação...')
