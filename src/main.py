import node
import networkx as nx

if __name__ == '__main__':
    basel = node.ISP('basel', 3)
    jb = node.butt('jb', 5)
    basel.print()
    jb.print()

    jb.connect(basel)

    basel.print()
    jb.print()

    g = nx.Graph()
    g.add_edge(jb, basel)
    print(g)
