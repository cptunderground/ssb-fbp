import argparse
import os
import json
import node
import networkx as nx


def initLog(verbose: bool = False):
    print('start retrieving your log')

    # starting sbot server
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

    def str2bool(v):
        if isinstance(v, bool):
            return v
        if v.lower() in ('yes', 'true', 't', 'y', '1'):
            return True
        elif v.lower() in ('no', 'false', 'f', 'n', '0'):
            return False
        else:
            raise argparse.ArgumentTypeError('Boolean value expected.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process command line arguments for the ssb-fbp')
    parser.add_argument('-v', dest='verbose', nargs='?', const=True, default=False,
                        help='Display all actions of the ssb-fbp')
    parser.add_argument('--verbose', dest='verbose', nargs='?', const=True, default=False,
                        help='Display all actions of the ssb-fbp')
    args = parser.parse_args()

    initLog(verbose=args.verbose)

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
