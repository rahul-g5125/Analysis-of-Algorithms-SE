import sys
from prettytable import PrettyTable

class Graph:
	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	def printMST(self, parent):
		table = PrettyTable(["Edge", "Weight"])
		for i in range(1, self.V):
			table.add_row([str(parent[i]) + " - " + str(i), self.graph[i][parent[i]]])
		print(table)


	def minKey(self, key, mstSet):

		min = sys.maxsize

		for v in range(self.V):
			if key[v] < min and mstSet[v] == False:
				min = key[v]
				min_index = v

		return min_index


	def primMST(self):

		key = [sys.maxsize] * self.V
		parent = [None] * self.V
		# Make key 0 so that this vertex is picked as first vertex
		key[0] = 0
		mstSet = [False] * self.V

		parent[0] = -1 # First node is always the root

		for cout in range(self.V):

			# Pick the minimum distance vertex from
			u = self.minKey(key, mstSet)

			# Put the minimum distance vertex in
			# the shortest path tree
			mstSet[u] = True


			for v in range(self.V):

				if 0 < self.graph[u][v] < key[v] and mstSet[v] == False:
					key[v] = self.graph[u][v]
					parent[v] = u

		self.printMST(parent)

if __name__ == '__main__':
	g = Graph(9)
	g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
			   [4, 0, 8, 0, 0, 0, 0, 11, 0],
			   [0, 8, 0, 7, 0, 4, 0, 0, 2],
			   [0, 0, 7, 0, 9, 14, 0, 0, 0],
			   [0, 0, 0, 9, 0, 10, 0, 0, 0],
			   [0, 0, 4, 14, 10, 0, 2, 0, 0],
			   [0, 0, 0, 0, 0, 2, 0, 1, 6],
			   [8, 11, 0, 0, 0, 0, 1, 0, 7],
			   [0, 0, 2, 0, 0, 0, 6, 7, 0]
			   ]

	g.primMST()


