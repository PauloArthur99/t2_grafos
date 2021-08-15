import math

class Grafo:
	def __init__(self, file_name):
		self.inf = math.inf #infinito
		self.file_name = file_name
		self.labels = []
		self.pesos    = {}
		self.num_vertices = None
		self.num_arestas =  None
		self.read_data()

	def qtdVertices(self):
		return self.num_vertices

	def qtdArestas(self):
		return self.num_arestas

	def grau(self, v):
		grau = 0
		for aresta in self.pesos.keys():
			if v == aresta[0]:
				grau += 1
		return grau

	def rotulo(self, v):
		return self.labels[v - 1]

	def vizinhos(self, v):
		vizinhos = []
		for aresta in self.pesos.keys():
			if v == aresta[0]:
				vizinhos.append(aresta[1])
		return vizinhos

	def haAresta(self, u, v):
		for aresta in self.pesos.keys():
			if (u, v) == aresta:
				return True
		return False

	def peso(self, u, v):
		try:
			peso = self.pesos[(u, v)]
		except KeyError:
			peso = float("inf")  
		return peso

	def read_data(self):
		with open(self.file_name) as f:
			conteudo_grafo = f.readlines()
		
		primeira_linha = conteudo_grafo[0].split()
		self.num_vertices = int(primeira_linha[1])
		
		for i in range(self.num_vertices):
			linha = conteudo_grafo[i + 1].split()
			self.labels.append(linha[1])

		arc_or_edge = conteudo_grafo[i + 2]
		i += 3
		if arc_or_edge == "*arcs\n":
			for j in range(i, len(conteudo_grafo)):
				linha = conteudo_grafo[j].split()
				arco = (int(linha[0]), int(linha[1]))
				self.pesos[arco] = float(linha[2])

		if arc_or_edge == "*edges\n":
			for j in range(i, len(conteudo_grafo)):
				linha = conteudo_grafo[j].split()
				arco = (int(linha[0]), int(linha[1]))
				self.pesos[arco] = float(linha[2])
			'''
			for j in range(i, len(conteudo_grafo)):
				linha = conteudo_grafo[j].split()
				arco1 = (int(linha[0]), int(linha[1]))
				arco2 = (int(linha[1]), int(linha[0]))
				self.pesos[arco1] = float(linha[2])
				self.pesos[arco2] = float(linha[2])
			'''

		self.num_arestas = len(self.pesos.keys())

	def transpor(self):
		b = {}
		for key, value in self.pesos.items():
			b[(key[1],key[0])]=value
		self.pesos = b

grafo1 = Grafo("teste.txt")