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
df = pd.read_csv("musae_ENGB_edges.csv")                            #load data from csv file
#df.head()
snaG = nx.from_pandas_edgelist(df, source="from", target="to")
#print(nx.info(snaG))                                               #graph information

max_grade = max(snaG.degree, key=lambda x: x[1])[1]
Adam = [node[0] for node in snaG.degree if node[1] == max_grade]    #Node with the largest degree
Adam = Adam[0]
print("I am the node with the largest degree: ",Adam)


nG = nx.Graph()                                                   #Create undirected graph for neighbors
neighbors = list(snaG.neighbors(Adam))                            #List of Adam's neighbors

for item in neighbors:
    nG.add_node(item)                                             #Add node to neighbors graph
    nG.add_edge(Adam,item)                                        #Add edge to neighbors graph
nG = snaG.subgraph(neighbors)  
pos = nx.spring_layout(nG)

nx.draw(nG, pos, node_color = "lavender", 
        node_size = 500, with_labels = True)  
print("The Adam's neighbors graph  is beloe")
plt.show()                                 #Add the edges between to Adam's neighbors
# plt.savefig("AdamNeighborsGraph.png")

# nx.draw_shell(nG,node_size = 500, with_labels = True)
# plt.savefig("filename6.png")

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

plot_degree_dist(nx.gnp_random_graph(100, 0.5, directed=True))

ego_g = nx.ego_graph(nG, Adam)
# d = dict(ego_g.degree)
# nx.draw(ego_g, node_color='lightblue', 
#         with_labels=True, 
#         nodelist=d, 
#         node_size=[d[k]*300 for k in d])









