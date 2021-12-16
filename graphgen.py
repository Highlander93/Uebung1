import random
from datetime import datetime

import graphviz

graph = graphviz.Graph('G', filename='./graphen/Graph_Aus_graphgen.dot', strict=True)
n = 14
m = 20

print(datetime.now())
print('Getting random graph for ' + str(n) + ' nodes')
graph.attr('node', shape='ellipse')
for i in range(1, n+1):
    graph.node(str(i), str(i))

number_of_edges = 0
random_edge = random.randrange(1, n)
while number_of_edges < m:
    for i in range(1, n+1):
        while random_edge == i:
            random_edge = random.randrange(1, n)
        while random_edge == 1:
            random_edge = random.randrange(1, n)
        graph.edge(str(i), str(random_edge))
        number_of_edges += 1

graph.view()
