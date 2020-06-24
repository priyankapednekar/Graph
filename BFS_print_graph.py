class Node():
    ''' node has value and the list of edges it connects to'''
    def __init__(self,src):
        self.src = src
        self.dest = {}
        self.visit=False


class GF():
    """docstring for ."""

    '''key- node data and value is Node'''
    def __init__(self):
        self.graph={}

    def insert_node(self,data):
        temp=Node(data)
        self.graph[data]=temp

    ''' destination and weight for given node'''
    def insert_edge(self,u,v,w):
        if self.graph.get(u,None):
            self.graph[u].dest[v]=w
        else:
            print("Node doesnt exist!!")




    def bfs_print(self,data):
        visit=[self.graph[data].src]

        while visit:
            var=visit.pop(0)
            self.graph[var].visit=True
            print(var, end = " " )
            for j in self.graph[var].dest.keys():
                if self.graph[j].visit==False:
                    if j not in visit:
                            visit.append(j)


def main():
    gf1=GF()
    gf1.insert_node(5)
    gf1.insert_node(6)
    gf1.insert_node(7)
    gf1.insert_node(9)

    gf1.insert_edge(5,6,1)
    gf1.insert_edge(5,7,2)
    gf1.insert_edge(6,7,2)
    gf1.insert_edge(7,9,1)
    gf1.insert_edge(9,5,2)

    gf1.bfs_print(5)

if __name__ == '__main__':
    main()
