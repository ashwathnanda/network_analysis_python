import networkx as nx
import matplotlib.pyplot as plt
def plot_deg_dist(G):
    all_degrees=nx.degree(G).values()
    unique_degrees=list(set(all_degrees))

    count_of_degrees=[]
    for i in unique_degrees:
        x=all_degrees.count(i)
        count_of_degrees.append(x)
    plt.plot(unique_degrees,count_of_degrees,'yo-')
    plt.xlabel('Degree')
    plt.ylabel('Number of nodes')
    plt.title('Degree distribution of Facebook data')
    plt.show()

def edge_to_remove(G):
    dict1=nx.edge_betweenness_centrality(G)
    list_of_tuples=dict1.items()
    list_of_tuples.sort(key=lambda x:x[1], reverse=True)
    return list_of_tuples[0][0] #(a,b)

def girvan(G):
    c=list(nx.connected_component_subgraphs(G))
    l = len(c)
    print 'The number of connected components are ' , l

    while(l==1):
        G.remove_edge(*edge_to_remove(G))
        c=list(nx.connected_component_subgraphs(G))
        l=len(c)
        print 'the number of connected components are ',l
    return c

G=nx.read_edgelist('A0505.txt')
H=nx.read_edgelist('A0601.txt')

print 'Info of the graph G'
print nx.info(G)
plot_deg_dist(G)
print 'Info of the graph H'
print nx.info(H)
plot_deg_dist(H)

print 'the Density of the network G is ', nx.density(G)
print 'the Density of the netowrk H is ', nx.density(H)

#clustering coefficient
for i in nx.clustering(G).items():
    print i

#average clustering
print 'Average clustering value for G is ' , nx.average_clustering(G)
print 'Average clustering value for H is ' , nx.average_clustering(H)

#diameter of data
print 'Diameter of the dataset G is ' , nx.diameter(G)
print 'Diameter of the dataset H is ' , nx.diameter(H)


#degree centrality
for i in nx.degree_centrality(G).items():
    print i

#Calculates the no of communities
p=girvan(G)

for i in p:
    print i.nodes()
    print'........',i.number_of_nodes()

nx.draw(G)
plt.show()
