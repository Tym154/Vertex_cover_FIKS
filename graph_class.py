class graph:
    nodes = {}

    # Function to add a node to the nodes dictionary
    def add_node_to_dic(self, node_index, neighbour_nodes = []):
        if node_index not in neighbour_nodes:
            self.nodes.update({node_index : neighbour_nodes})
        else:
            raise Exception("Node cannot have itself as a neighbour")
    
