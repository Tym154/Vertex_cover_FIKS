class graph:
    nodes = {}

    # Adding a node to the nodes dictionary
    def add_node_to_dir(self, node_index, neighbour_nodes = []):
        if node_index in neighbour_nodes:
            raise Exception("Node cannot have itself as a neighbour")  
        
        if node_index not in self.nodes:
            self.nodes.update({node_index : neighbour_nodes})
        elif node_index in self.nodes and len(neighbour_nodes) == 1:
            self.nodes[node_index].append(neighbour_nodes)
        else:
            for i in neighbour_nodes:
                if i not in self.nodes[node_index]:
                    self.nodes[node_index].append(i)

    # Removing a node from a graph
    def remove_node(self, node_index):
        del self.nodes[node_index]

        for i in self.nodes:
            if node_index in self.nodes[i]:
                self.nodes[i].remove(node_index)
        
    # Deleting all nodes that have no neighbours
    def clear_nodes_without_neighbours(self):
        nodes_to_delete = []
        for i in self.nodes:
            if not len(self.nodes[i]): # If the nodes neighbour list is empty, delete that node
                nodes_to_delete.append(i)

        for j in nodes_to_delete:
            del self.nodes[j]

    # Removing all nodes that have no neighbours
    def clear_nodes_without_neighbours(self):
        nodes_to_delete = []
        for i in self.nodes:
            if not len(self.nodes[i]): # If the nodes neighbour list is empty, delete that node
                nodes_to_delete.append(i)

        for j in nodes_to_delete:
            self.remove_node(j)

    # Returs False if there are any edges. 
    def check_if_there_are_any_edges(self):
        for i in self.nodes:
            if len(self.nodes[i]):
                return False
            
        return True
    