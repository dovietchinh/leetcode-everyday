from typing import List
from itertools import permutations
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def countDiff(word1,word2):
            count = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    count += 1
            return count
        if not endWord in wordList:
            return []
        ## make a graph 
        edges = []
        if not beginWord in wordList:
            wordList.insert(0,beginWord)
        graph = {}
        for i in range(len(wordList)):
            graph[wordList[i]] = []
        for i in range(len(wordList)-1):
            # graph[wordList[i]] = []
            for j in range(1,len(wordList)):
                if countDiff(wordList[i],wordList[j]) == 1:
                    graph[wordList[i]] = graph.get(wordList[i],[]) + [wordList[j]]
                    graph[wordList[j]] = graph.get(wordList[j],[]) + [wordList[i]]
                    # graph[i] = graph.get(i,[]) + [j]
                    # graph[j] = graph.get(j,[]) + [i]
        print(graph)

        res = []
        def dijkstra_algorithms(graph,start):
            table = {i: {
                'distance': float('inf'),
                'previous': None,
            } for i in graph}
            queue = [start]
            table[start] = {
                'distance': 0,
                'previous': [],
            }
            visited = set()
            while queue:
                node = queue.pop(0)
                # print('node: ',node)
                if node in visited:
                    continue
                visited.add(node)
                for neighbor in graph[node]:
                    if table[neighbor]['distance'] is None:
                        table[neighbor]['distance'] = table[node]['distance'] + 1
                        table[neighbor]['previous'] = [node]
                    elif table[neighbor]['distance'] < table[node]['distance'] + 1:
                        continue 
                    elif table[neighbor]['distance'] > table[node]['distance'] + 1:
                        table[neighbor]['distance'] = table[node]['distance'] + 1
                        table[neighbor]['previous'] = [node]
                    elif table[neighbor]['distance'] == table[node]['distance'] + 1:
                        if node not in table[neighbor]['previous']:
                            table[neighbor]['previous'].append(node)
                    else:
                        continue 
                    queue.append(neighbor)
            return table 
        table = dijkstra_algorithms(graph,beginWord)
        # print(table)
        res = []
        def get_sortest_path_from_table(table,point,tail=[]):
            nonlocal res 
            distance = table[point]['distance']
            previous = table[point]['previous']
            if distance == float('inf'):
                return
            if distance == 0:
                res.append(tail[::-1])
                return    
            if distance != 0:
                # print('table: ',table)
                # print('point: ',point)
                # print('table[point]: ',table[point])
                distance = table[point]['distance']
                previous = table[point]['previous']
                for pre in previous:
                    get_sortest_path_from_table(table,pre,[*tail,pre])
                # point = table[point]['previous']
            # res.append([wordList[i] for i in tail[::-1]])

        # print(table)
        get_sortest_path_from_table(table,endWord,[endWord])
        # print(res)
        return res


        
def visualize(graph, label=False):
    import matplotlib.pyplot as plt
    import networkx as nx
    G = nx.DiGraph()
    # Add edges to the graph
    for node, edges in graph.items():
        for neighbor in edges:
            G.add_edge(node, neighbor, weight=1)

    # Define positions of nodes
    pos = nx.spring_layout(G)
    # Draw the graph
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=16, font_weight='bold', arrows=True)

    # Draw edge labels
    if label:
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=12)
    plt.show()
        

if __name__ == '__main__':
    beginWord = "hot"
    endWord = "dog"
    wordList = ["hot","dog"] 
    r = Solution().findLadders(beginWord,endWord,wordList)
    # visualize(r)
    # for i in r:
    print(r)

