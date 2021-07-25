import snap
import sparse
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import collections


df = pd.read_csv("musae_ENGB_edges.csv")                            #load database from csv file
snaG = nx.from_pandas_edgelist(df, source="from", target="to")      #graph information
max_grade = max(snaG.degree, key=lambda x: x[1])[1]
Adam = [node[0] for node in snaG.degree if node[1] == max_grade]    #Node with the largest degree
Adam = Adam[0]
print("I am the node with the largest degree: ",Adam)

neighbors = list(snaG.neighbors(Adam))                              #List of Adam's neighbors
neighbors.append(Adam)                                              #Adding adam to the list

nG = snaG.subgraph(neighbors)                                       #Create undirected graph of Adam's neighbors
nx.draw_random(nG,node_color = "pink", with_labels = True)          #Drawing the neighbors graph
print("The Adam's neighbors graph is shown below: ")
plt.show()                                            


print(nx.info(nG))                                                                             #All the information of Adam's neighbor graph
print( 'The number Connected Components: {0}'.format(nx.number_connected_components(nG)))      #Print the number of connected components in the nieghbors graph
connectedomCponentssortedList=sorted(nx.connected_components(nG), key = len, reverse=True)     #Sorting the connected components according to the size from the bigest to the smallest
print('The size of the Largest connected component is: {0}'.format(len(connectedomCponentssortedList[0])))   #Printing the bigest connected component in the nieghbors graph

def plot_degree_dist(G):                                                            #The functiom gets a graph and displays the degree distribution of the graph
    plt.clf()                                                                       #Clearing the current plot
    degrees = [G.degree(n) for n in G.nodes()]  #A list with all the graph's degrees  
    degreeCount = collections.Counter(degrees)
    deg, cnt = zip(*degreeCount.items())  
    myMax=max(degrees)                                                   
    plt.hist(deg, facecolor='gray', align='mid') 
    plt.title("Degree Histogram") 
    plt.axis([0, 100, 0, 50])
    plt.xticks(np.arange(0,myMax+25,20))   
    plt.xlabel('Degree');  
    plt.ylabel('Fraction of nodes')                                       
    print("The degree distribution of Adam's neighbors graph is shown below: ")
    plt.show()

plot_degree_dist(nG)                                                                #Call the plot_degree_dist function with the neighbors graph (nG)

print("The amount of triangles that includes Adam in the network is: {0}".format((nx.triangles(nG,(Adam,)))[Adam]))         #Printing the amount of triangles that includes Adam in the network

completeGraph=nx.complete_graph(len(nG.nodes), create_using=None)                   #Building a conplete graph in the size of Adam's graph
print("The maximum number of triangles a network of Adam's network size can have is : {0}".format((nx.triangles(completeGraph,(1,)))[1]))      #Printing the maximum number of triangles a network of Adam's network size can have
 #Finding Adam's best friend
neighbors.remove(Adam)                                                             
neighborsG = nG.subgraph(neighbors) 
max_grade = max(neighborsG.degree, key=lambda x: x[1])[1]                           #Find the node with the largest degree except for Adam
BestfriendAdam = [node[0] for node in neighborsG.degree if node[1] == max_grade]    #Adam's bff - because usually with the best friend we have the most common circles because if he is the best friend then he knows the family and the other friends and so on.
BestfriendAdam = BestfriendAdam.pop(0)                                              #So the node with the largest degree in the neighbors graph is the one that has the most common circles with Adam.
print("The best friend of Adam is: {0}".format(BestfriendAdam))

bfG=nx.Graph()                                                                      #Showing Adam's best friend in a graph that contain Adam and his bff and all the common friends.
bfG.add_node(Adam)                                                                  #Building the best friend graph
for i in neighbors:
    if(neighborsG.has_edge(i,BestfriendAdam)):
        bfG.add_node(i)
        bfG.add_edge(i,BestfriendAdam)
        bfG.add_edge(i,Adam)
plt.clf()
bfG.add_edge(Adam,BestfriendAdam)


nx.draw_random(bfG,node_size =1200,node_color = "pink", with_labels = True)         #Drawing the best friend graph
plt.show()


print( 'The number of subgroups of Adam`s friends is: {0}'.format(nx.number_connected_components(neighborsG)))        #Dividing Adam's friend to subgroups according to the connected components
plt.clf()
nx.draw_random(neighborsG,node_size =1200,node_color = "pink", with_labels = True)
plt.show()


