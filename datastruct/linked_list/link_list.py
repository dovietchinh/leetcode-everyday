import matplotlib.pyplot as plt
import networkx as nx
class Node: 
    def __init__(self,value):
        self.value = value 
        self.next = None 
        
class LinkedList:
    def __init__(self,data=[]):
        self.head = None
        if len(data) != 0:
            for v in data:
                node = Node(v)
                if self.head is None:
                    self.head = node 
                    ptr = node
                else:
                    ptr.next = node
                    ptr = node
            
                
    
    def append(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:    
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = node 
    
    def visualize(self):
        G = nx.DiGraph()
        # Add edges to the graph
        # for node, edges in graph.items():
        #     for neighbor, weight in edges.items():
        #         G.add_edge(node, neighbor, weight=weight)
        ptr = self.head 
        if ptr.next is None:
            G.add_node(ptr.value)
        while ptr.next is not None:
            G.add_edge(ptr.value, ptr.next.value, weight=1)
            ptr = ptr.next
        # Define positions of nodes
        pos = nx.spring_layout(G)

        # Draw the graph
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=16, font_weight='bold', arrows=True)

        # Draw edge labels
        # edge_labels = nx.get_edge_attributes(G, 'weight')
        # nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=12)

        # Show the plot
        plt.title("Graph Visualization with Dijkstra's Algorithm")
        plt.axis('off')
        plt.show()

    def remove_last_node(self): 
        if self.head is None:
            return 
        elif self.head.next is None :
            self.head = None 
            return 
        ptr = self.head 
        while ptr.next.next is not None:
            ptr = ptr.next 
        ptr.next = None 

    def traverse(self):
        ptr = self.head 
        while ptr is not None:
            print(ptr.value)
            ptr = ptr.next

    def delete_node_by_index(self,index):
        if index == 0:
            if self.head is not None:
                self.head = self.head.next
            else:
                print("Out of bounds")
                return 
        ptr = self.head 
        for _ in range(index-1):
            if ptr.next is None:
                print("Out of bounds")
                return 
            ptr = ptr.next
        ptr.next = ptr.next.next 

    def delete_node_by_value(self,value):
        ptr = self.head 
        while ptr.next is not None:
            if ptr.next.value == value:
                ptr.next = ptr.next.next 
                break
            ptr = ptr.next 


    def size(self):
        index = 0 
        ptr = self.head 
        while ptr is not None:
            ptr = ptr.next 
            index += 1
        return index 

    def insert(self,index,value):
        node = Node(value)
        if index == 0:
            if self.head is not None:
                node.next = self.head 
                self.head = node 
            else:
                self.head = node
            return 
        ptr = self.head 
        for _ in range(index-1):
            if ptr.next is None:
                print("insert Out of bounds")
                return 
            ptr = ptr.next
        node.next = ptr.next
        ptr.next = node
        

if __name__ == '__main__':
    l = LinkedList([0])
    # l.append(0)
    # l.append(1)
    # l.append(2)
    # l.append(3)
    # l.append(4)
    # l.append(5)
    # l.append(6)
    # l.append(7)
    # l.append(8)
    # l.insert(8,99)
    # l.remove_last_node()
    # l.delete_node_by_index(2)
    # l.delete_node_by_value(4)
    l.traverse()
    print("l.size: ",l.size())
    # l.delete_node_by_index(0)
    l.visualize()