import os
import json
import node
import networkx as nx


def initLog(verbose: bool = False):
    print('start retrieving your log')

    #starting sbot server
    '''
    cmd = 'sbot start'
    os.popen(cmd)
    '''


    cmd = 'sbot whoami'
    stream = os.popen(cmd)
    print('executing command:', cmd)
    output = stream.read()
    id = json.loads(output)
    print('extracted ID:', id['id'])

    cmd = 'sbot createUserStream --id ' + id['id']
    if (verbose):
        print('executing command:', cmd)
        stream = os.popen(cmd)
        output = stream.read()
        print(output)
    os.popen(cmd + ' > log.json')
    print('executed command:', cmd)
    print('log saved as log.json')


if __name__ == '__main__':

    initLog(verbose=False)

    '''
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
    '''
