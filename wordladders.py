import networkx as nx
import enchant
import itertools

def countSameLetters(word1, word2):
    count = 0
    for i in range(min(len(word1),len(word2))):
        if word1[i] == word2[i]:
            count += 1
    return count

d1 = enchant.Dict("en_US")
d2 = enchant.Dict("en_UK")

four_letter_words = [''.join(word) for word in itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=4) if d1.check(''.join(word)) or d2.check(''.join(word))]

G = nx.Graph()
G.add_nodes_from(four_letter_words)

for node1 in G:
    for node2 in G:
        if countSameLetters(node1, node2) == 3:
            G.add_edge(node1, node2)

print(nx.number_connected_components(G))
nx.draw(G)