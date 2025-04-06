from graph_class import graph

this_is_a_graph = graph()

this_is_a_graph.add_node_to_dic(1, [2,3,5])
this_is_a_graph.add_node_to_dic(2, [])
this_is_a_graph.add_node_to_dic(3, [2, 1])


print(this_is_a_graph.nodes)

this_is_a_graph.clear_nodes_without_neighbours()

print(this_is_a_graph.nodes)

print(this_is_a_graph.check_if_there_are_any_edges())

this_is_a_graph.remove_node(1)
print(this_is_a_graph.nodes)

print(this_is_a_graph.check_if_there_are_any_edges())



