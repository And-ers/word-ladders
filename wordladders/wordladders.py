import networkx as nx
import matplotlib.pyplot as plt
import enchant
import twl
import itertools
import os.path

def countSameLetters(word1, word2):
    count = 0
    for i in range(min(len(word1),len(word2))):
        if word1[i] == word2[i]:
            count += 1
    return count

def generateWordGraph(dic, letters):
    path_string = './word-graphs/' + dic + "_" + str(letters) + "_word_graph.gexf"
    if os.path.isfile(path_string):
        return nx.read_gexf(path_string)
    else:
        if dic == 'twl':
            all_words = [''.join(word) for word in itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=letters) if twl.check(''.join(word))]
        else:
            d = enchant.Dict(dic)
            all_words = [''.join(word) for word in itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=letters) if d.check(''.join(word))]
        G = nx.Graph()
        G.add_nodes_from(all_words)
        for node1 in G:
            for node2 in G:
                if countSameLetters(node1, node2) == letters - 1:
                    G.add_edge(node1, node2)
        nx.write_gexf(G, path_string)
        return G

word_graph = generateWordGraph('twl', 4)

print(nx.number_connected_components(word_graph))
nx.draw_networkx(word_graph, pos = nx.kamada_kawai_layout(word_graph), with_labels = True, node_size = 5, font_size = 3, width = 0.5)
plt.show()
