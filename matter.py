import random
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import tree
import time
from tqdm import tqdm
from try_1 import gnp_random_connected_graph

from itertools import combinations, groupby
G = gnp_random_connected_graph(1000, 1, False)

def main():

    def sort_edges_in_graph(graph):
        '''
        Return edges from the less weighted to the most
        '''
        sorted_edges = sorted(graph.edges(data=True), key=lambda x: x[2]["weight"])
        number_of_vers = len(graph.nodes())
        return sorted_edges, number_of_vers


    def create_sets(numb_of_vert):
        '''
        Create sets, which contain vert and put it in list
        '''
        list_of_sets = []
        for set_elem in range(numb_of_vert):
            list_of_sets.append({set_elem})
        return list_of_sets

    def uniting_sets(big_set, ver1, ver2):
        '''
        Unite sets, if they have same elements
        '''
        counter = 0
        bad_sets = []
        right_set = set()
        for this_set in big_set:
            if counter < 2:
                if ver1 in this_set or ver2 in this_set:
                    right_set = right_set | this_set
                    counter +=1
                else:
                    bad_sets.append(this_set)
            else:
                bad_sets.append(this_set)
        list_of_right_set = [right_set]
        final_list_of_sets = bad_sets + list_of_right_set
        return final_list_of_sets

    def if_in_same(list_of_sets, ver1, ver2):
        '''
        Check if vertes in different sets or no
        '''
        for this_set in list_of_sets:
                if ver1 in this_set or ver2 in this_set:
                    if ver1 in this_set and ver2 in this_set:
                        return False
                    return True

    def main_algorythm(edges, number_of_vers):
        '''
        The main algorythm. Return list of edges to create the smallest carcas
        '''
        spanning_tree = nx.Graph()
        count = 0
        graph_edge_list = []
        numb_of_vert = number_of_vers
        list_of_sets = create_sets(numb_of_vert)
        for pair in edges:
            if if_in_same(list_of_sets, pair[0], pair[1]):
                # spanning_tree.add_edge(pair[0], pair[1])
                graph_edge_list.append(pair)
                count += 1
                if count == numb_of_vert - 1:
                    # return spanning_tree
                    return graph_edge_list
                list_of_sets = uniting_sets(list_of_sets, pair[0], pair[1])
                
    edges, numbers_of_vers = sort_edges_in_graph(G)
    edges_list = main_algorythm(edges, numbers_of_vers)

    # f_graph = nx.Graph()

    # f_graph.add_edges_from(edges_list)

    # nx.draw(f_graph, node_color='lightgreen', 
    #             with_labels=True, 
    #             node_size=500)
    # plt.show()

# if __name__ == "__main__":
#     main()

NUM_OF_ITERATIONS = 1
time_taken = 0
for i in tqdm(range(NUM_OF_ITERATIONS)):

    start = time.time()
    main()
    end = time.time()
    
    time_taken += end - start
    
print(time_taken / NUM_OF_ITERATIONS)
