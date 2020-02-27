import node
import networkx as nx

if __name__ == '__main__':
    basel = node.ISP('basel', 3)
    zurich = node.ISP('zürich', 7)
    jb = node.butt('jb', 5)
    basel.print()
    zurich.print()
    jb.print()

    jb.connect(basel)

    basel.print()
    zurich.print()
    jb.print()

    jb.connect(zurich)

    basel.print()
    zurich.print()
    jb.print()

    g = nx.Graph()
    g.add_edge(jb, basel)
    print(g)
