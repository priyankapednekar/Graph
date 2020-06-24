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

    def dfs_print_rec(self,data):
        print(self.graph[data].src, end = " ")
        self.graph[data].visit=True

        for i in self.graph[data].dest.keys():
            if not self.graph[i].visit:
                    self.dfs_print_rec(i)



def main():
        gf1=GF()

        gf1.insert_node(0)
        gf1.insert_node(1)
        gf1.insert_node(2)
        gf1.insert_node(3)

        gf1.insert_edge(0,1,1)
        gf1.insert_edge(0,2,1)
        gf1.insert_edge(1,2,1)
        gf1.insert_edge(2,0,1)
        gf1.insert_edge(2,3,1)
        gf1.insert_edge(3,3,1)

        gf1.dfs_print_rec(2)

if __name__ == '__main__':
    main()
