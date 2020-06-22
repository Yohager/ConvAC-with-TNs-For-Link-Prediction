'''
embedding for six dataset
'''
import numpy as np
from node2vec import Node2Vec
import networkx as nx
from matplotlib import pyplot as plt

def read_dataset(file_path):
    data = []
    with open(file_path,"r") as file:
        for line in file.readlines():
            line = line.strip('\n')
            data.append(list(map(eval,line.split())))
    return np.array(data)


def construct_networkx_data(data,type):
    Graph = nx.Graph()
    if type == "unweighted":
        Graph.add_edges_from(data)
    elif type == "weighted":
        Graph.add_weighted_edges_from(data)
    #nx.draw(Graph,with_labels=True)
    #plt.show()
    return Graph

def node2vec_function(graph,graph_name):
    node2vec = Node2Vec(graph,dimensions=32,walk_length=30,num_walks=200,workers=4)
    model = node2vec.fit(window=10,min_count=1,batch_words=4)
    model.wv.save_word2vec_format(graph_name)
    model.save(graph_name+'_embedding')
    graph_nodes = np.array(graph.node)
    embedding_vectors = []
    for i in graph_nodes:
        embedding_vectors.append(model[str(i)])
    np.savetxt(graph_name+'_embedding_vectors.txt',embedding_vectors)
    np.savetxt(graph_name+'_nodes.txt',list(map(int,graph_nodes)))
    return embedding_vectors,model


if __name__ == "__main__":
    file_path = "../dataset/Power.txt"
    temp_data = read_dataset(file_path)
    print(temp_data)
    temp_graph = construct_networkx_data(temp_data,"unweighted")
    temp_embedding,temp_model = node2vec_function(temp_graph,"Power")
    #print(temp_embedding)




