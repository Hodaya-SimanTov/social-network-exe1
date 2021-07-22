import snap
import sparse
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

#first try networkx     נסיון ראשון לפי 
# my_graph = nx.Graph()
# my_graph = nx.read_gml('celegansneural.gml')

# print(nx.info(my_graph))

# max_grade = max(my_graph.degree, key=lambda x: x[1])[1]
# Adam = [node[0] for node in my_graph.degree if node[1] == max_grade]  #Node with thw largest degree
# print(Adam)

# G = my_graph.neighbors(Adam)
# G = nx.path_graph(4)  # or DiGraph, MultiGraph, MultiDiGraph, etc
# G[0]

# G = nx.path_graph(4)  # or DiGraph, MultiGraph, MultiDiGraph, etc
# [n for n in my_graph.neighbors(Adam)]


# my_graph = nx.Graph()
# gml_graph = nx.read_gml("./celegansneural.gml")
# nx.draw(gml_graph, with_labels=True, font_weight='bold')


#second try snap   נסיון שני לפי
# G1 = snap.LoadEdgeList(snap.TUNGraph, "facebook_combined.txt", 0, 1)   #Load the facebook combined graph using snap.py

# Adam = G1.GetMxDegNId()                                                #Adam is the largest degree node
# print("I am the node with the largest degree: ", Adam)

# Gneighbors = snap.TUNGraph.New()                                       #Build Adam`s neighbors graph.     

# edgeAmount = 0                                                         #Count the amount of edges in the neighbors graph
# NodeNum, NodeVec = G1.GetNodesAtHop(Adam, 1, False)                    #All the nodes that are in one hop from Adam   
# for item in NodeVec:
#     Gneighbors.AddNode(item)                                           #Add node to neighbors graph
#     Gneighbors.AddEdge(Adam,item)                                      #Add edge to neighbors graph
#     edgeAmount += 1

# print("Amount of nodes in adam's neighbors graph:  " , NodeNum)
# print("Amount of edges in adam's neighbors graph:  " , edgeAmount)


#third try from csv and panda networkx  נסיון שלישי לפי
df = pd.read_csv("musae_ENGB_edges.csv") #load data from csv file
# df = pd.read_csv("Test.csv")
snaG = nx.from_pandas_edgelist(df, source="from", target="to")                                              #graph information
max_grade = max(snaG.degree, key=lambda x: x[1])[1]
Adam = [node[0] for node in snaG.degree if node[1] == max_grade]    #Node with the largest degree
Adam = Adam[0]
print("I am the node with the largest degree: ",Adam)


neighbors = list(snaG.neighbors(Adam)) #List of Adam's neighbors
neighbors.append(Adam)
#Create undirected graph for neighbors
nG = snaG.subgraph(neighbors) 
nx.draw_random(nG,node_color = "pink", with_labels = True)
print("The Adam's neighbors graph  is beloe")
plt.show()                                 #Add the edges between to Adam's neighbors
# plt.savefig("AdamNeighborsGraph.png")


print(nx.info(nG))                                                #All the information of Adam's neighbor graph
print( 'Number Connected Components: {0}'.format(nx.number_connected_components(nG)))
connectedomCponentssortedList=sorted(nx.connected_components(nG), key = len, reverse=True)
print('Size of Largest connected component: {0}'.format(len(connectedomCponentssortedList[0])))

def plot_degree_dist(G):
    # clearing the current plot
    plt.clf()
    degrees = [G.degree(n) for n in G.nodes()]
    plt.hist(degrees)
    print("The degree distribution of Adam's neighbors graph  is beloe")
    plt.show()

plot_degree_dist(nG)

print("The amount of triangles that includes Adam : {0}".format((nx.triangles(nG,(Adam,)))[Adam]))

completeGraph=nx.complete_graph(len(nG.nodes), create_using=None)
print("The  maximum number of triangles a network of Adam's network size is : {0}".format((nx.triangles(completeGraph,(1,)))[1]))

neighbors.remove(Adam)
neighborsG = nG.subgraph(neighbors) 
max_grade = max(neighborsG.degree, key=lambda x: x[1])[1]
BestfriendAdam = [node[0] for node in neighborsG.degree if node[1] == max_grade]    #Node with the largest degree
BestfriendAdam = BestfriendAdam.pop(0)
print("The best friend  of Adam is {0}".format(BestfriendAdam))

bfG=nx.Graph()
bfG.add_node(Adam)
for i in neighbors:
    if(neighborsG.has_edge(i,BestfriendAdam)):
        bfG.add_node(i)
        bfG.add_edge(i,BestfriendAdam)
        bfG.add_edge(i,Adam)
plt.clf()
bfG.add_edge(Adam,BestfriendAdam)


nx.draw_random(bfG,node_size =1200,node_color = "pink", with_labels = True)
plt.show()


print( 'Number Connected Components of subgroup of freing in Adam: {0}'.format(nx.number_connected_components(neighborsG)))
plt.clf()
nx.draw_random(neighborsG,node_size =1200,node_color = "pink", with_labels = True)
plt.show()


















