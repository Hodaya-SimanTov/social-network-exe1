import snap
import networkx as nx

my_graph = nx.Graph()
my_graph = nx.read_gml('celegansneural.gml')

print(nx.info(my_graph))

max_grade = max(my_graph.degree, key=lambda x: x[1])[1]
Adam = [node[0] for node in my_graph.degree if node[1] == max_grade]  #Node with thw largest degree
print(Adam)


#G = nx.path_graph(4)  # or DiGraph, MultiGraph, MultiDiGraph, etc
[n for n in my_graph.neighbors(Adam)]


# my_graph = nx.Graph()
# gml_graph = nx.read_gml("./celegansneural.gml")
# nx.draw(gml_graph, with_labels=True, font_weight='bold')

# G1 = snap.LoadEdgeList(snap.TUNGraph, "facebook_combined.txt", 0, 1)

# Adam = G1.GetMxDegNId()    #Adam is the largest degree node
# print(Adam)

# neighbor_graph = G1.neighbors(Adam)    # Adam`s neighbors graph

# NodeNum, NodeVec = G1.GetNodesAtHop(Adam, 1, False)    #All the nodes that are in 0ne hop from Adam - neighberhood graph   
# for item in NodeVec:
#     print(item)
#     print("num: " , NodeNum)

