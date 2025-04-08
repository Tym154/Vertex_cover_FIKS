class graph:
    vertices = {}
    current_vertice_num = 0
    current_edges_num = 0

    starting_vertice_num = 0
    starting_edges_num = 0

    # graph constructor
    def __init__(self, in_edges_num, in_vertices_num, edges):
        self.starting_vertice_num = in_vertices_num
        self.starting_edges_num = in_edges_num

        for i in edges:
            self.add_edge(i)
                
    # Add vertice based on the edge
    def add_edge(self, edge = []):
        if len(edge) != 2:
            raise Exception("Path E needs to have precisely 2 elements")
        
        if edge[0] not in self.vertices:
            self.vertices[edge[0]] = []
            self.current_vertice_num += 1
        if edge[1] not in self.vertices:
            self.vertices[edge[1]] = []
            self.current_vertice_num += 1

        here = 0
        if edge[0] not in self.vertices[edge[1]]:
            self.vertices[edge[1]].append(edge[0])
            here = 1
        if edge[1] not in self.vertices[edge[0]]:
            self.vertices[edge[0]].append(edge[1])
            here = 1
        
        if here:
            self.current_edges_num += 1

    # Add vertice based on its neighbours
    def add_vertice(self, vertice_index, neighbours):
        if vertice_index in neighbours:
            raise Exception("Node cannot have itself as a neighbour")  
        
        if vertice_index not in self.vertices:
            self.vertices.update({vertice_index : neighbours})
            self.current_vertice_num += 1
            self.current_edges_num += len(neighbours)
            for i in neighbours:
                self.vertices[i].append(vertice_index)
        else:
            for i in neighbours:
                if i not in self.vertices[vertice_index]:
                    self.vertices[vertice_index].append(i)
                    self.current_edges_num += 1
                    
                    self.vertices[i].append(vertice_index)

    # Removing a vertice from a graph
    def remove_vertice(self, vertice_index):
        for i in self.vertices[vertice_index]:
            self.vertices[i].remove(vertice_index)

        self.current_edges_num -= len(self.vertices[vertice_index])
        del self.vertices[vertice_index]
        self.current_vertice_num -= 1
        
    # Deleting all vertices that have no neighbours
    def clear_vertices_without_neighbours(self):
        vertices_to_delete = []
        for i in self.vertices:
            if not len(self.vertices[i]): # If the vertices neighbour list is empty, delete that vertice
                vertices_to_delete.append(i)

        for j in vertices_to_delete:
            del self.vertices[j]
            self.current_vertice_num -= 1
    