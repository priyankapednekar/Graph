class Node():
    ''' node has value and the list of edges it connects to'''
    def __init__(self,src):
        self.src = src
        self.dest = {}


class GF():
    """docstring for ."""

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

    def print_graph(self):
        print("\nNodes in graph:")
        nodes=[]
        for i in self.graph.keys():
            nodes.append(i)
        print(nodes)

        print("\nedges in graph:")
        for j in self.graph.values():
            for m,n in j.dest.items():
                print("src= {} dest= {} weight={}".format(j.src,m,n))
        print("\n")

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

    gf1.print_graph()

if __name__ == '__main__':
    main()
