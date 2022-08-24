from Graph_ADT import Graph


g = Graph(4)
g.display_adjMat()

#to create an undirected link we use insert edge

g.insert_edge(0,1)
g.insert_edge(1,0)
g.insert_edge(1,2)
g.insert_edge(2,1)
g.insert_edge(0,2)
g.insert_edge(2,0)
g.insert_edge(2,3)
g.insert_edge(3,2)


#to view the link

print('**********************')

g.display_adjMat()
print('edges : ', g.edge_count())

print('**********************')
g.edges()