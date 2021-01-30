from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    """
    DAG()
    """
    # Constructor
    def __init__(self, vertices: dict = None):
        self.graph = defaultdict(list)
        if vertices is not None:
            self.init_digraph(vertices)
        
    def addEdge(self, fr, to):
        self.graph[fr].append(to)

    def init_digraph(self, digraph: dict):
        for key, values in digraph.items():
            for value in values:
                self.addEdge(key, value)
    
    def topological_sort(self, digraph=None):
        if digraph is not None:
            self.graph = defaultdict(list)
            self.init_digraph(digraph)
        sorted_node = []
        outputs = set(self.graph.keys())
        inputs = set([ i for v in self.graph.values() for i in v])
        input_nodes = outputs - inputs
        

people_relatioship = {
    'Wang': ['Liu', 'Tom'],
    'Tom': ['Zhang', 'Xu'],
    'Xu': ['Zhao', 'Li']
}

graph = Graph(people_relatioship)
print(graph.graph)
ggraph = nx.DiGraph(graph.graph)
glayout = nx.layout.spring_layout(ggraph)
nx.draw(ggraph, glayout, with_labels=True, node_color='red')
plt.show()
graph.topological_sort()