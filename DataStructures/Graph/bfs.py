from DataStructures.Queue import queue as cola
from DataStructures.Graph import adj_list_graph as graph
from DataStructures.Stack import stack as satck
from DataStructures.List import array_list as lt
from DataStructures.Map import map_linear_probing as mp

def breath_first_search(my_graph, source):
    search = {"source": source, "visited": None}
    search['visited'] =mp.new_map(num_elements=graph.num_vertices(my_graph),load_factor=0.5)
    mp.put(search['visited'], source, {'marked': True,'edge_to': None,'dist_to': 0})
    bfs_vertex(search, my_graph, source)
    
def bfs_vertex(search, my_graph, source):
    adjsqueue= cola.newQueue()
    cola.enqueue(adjsqueue, source)
    while not(cola.isEmpty(adjsqueue)):
        vertex=cola.dequeue(adjsqueue)
        visited_v=mp.get(search['visited'], vertex)['value']
        adjslst=graph.adjacents(my_graph, vertex)
        for w in lt.iterator(adjslst):
            visited_w=mp.get(search['visited'], w)
            if visited_w is None:
                dist_to_w=visited_v['distTo'] +1
                visited_w={'marked': True,'edgeTo': vertex,"distTo": dist_to_w}
                mp.put(search['visited'], w, visited_w)
                cola.enqueue(adjsqueue, w)
                
    return search

def has_path_to(search, vertex): 
    return search['marked'].get(vertex, False)

def path_to(search, vertex): 
    if not has_path_to(search, vertex): 
        return None
    path = [] 
    while vertex is not None:
        path.append(vertex) 
        vertex = search['edge_to'].get(vertex) 
    path.reverse() 
    return path

def init_search(my_graph, source): 
    search = { 'marked': {v: False for v in mp.key_set(my_graph['vertices'])['elements']}, 'edge_to': {} } 
    search['marked'][source] = True 
    return