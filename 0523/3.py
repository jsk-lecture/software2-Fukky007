graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F','G'],
    'D' : ['H','I'],
    'E' : ['J','K'],
    'F' : ['L','M'],
    'G' : ['N','O'],
    'H' : [], 'I' : [], 'J' : [], 'K' : [], 'L' : [], 'M' : [], 'N' : [], 'O' : []
}

def deep_limited_search(graph, start, goal, limit, depth=0):
    cutoff = False
    print("traverse:{}, level:{}".format(start, depth))
    depth += 1
    if start == goal:
        print("found target {}".format(start))
        return start
    if depth > limit:
        return 'cutoff'
    for n in reversed(graph[start]):
        ret = deep_limited_search(graph, n, goal, limit, depth)
        if ret == 'cutoff':
            cutoff = True
        elif ret != None:
            return ret
    if cutoff:
        return 'cutoff'
    return None

def iterative_deepening_search(graph, start, goal):
    limit = 1
    ret = 'cutoff'
    while(ret == 'cutoff'):
        print("\nsearch in limit={}".format(limit))
        ret = deep_limited_search(graph, start, goal, limit)
        limit += 1
    if ret == None:
        print("{} is NOT in this graph.".format(start))
