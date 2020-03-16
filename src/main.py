import argparse
import os
import json
import time

import ndjson
import node
import networkx as nx

global peers
peers = []


def initLog(verbose: bool = False, id: str = None):
    if id == None:
        print('no id to initialise feed')
        print('start retrieving your log')

        id = whoami()
    else:
        print('start retrieving ' + id + ' log')
    cmd = 'sbot createUserStream --id ' + id
    if (verbose):
        print('executing command:', cmd)
        stream = os.popen(cmd)
        output = stream.read()
        print(output)

    escapedID = escapeID(id)
    os.popen(cmd + ' > logs/' + escapedID + '.json')
    print('executed command:', cmd)
    print('log saved as ' + escapedID + '.json')


def escapeID(id):
    return id.replace('/', '_')


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def initPeers(verbose: bool = False):
    id = whoami()
    cmd = 'sbot friends.hops ' + id + ' | grep 1,'
    stream = os.popen(cmd)
    output = stream.read()
    cmd = cmd + ' > peers.json'
    os.popen(cmd)
    time.sleep(1)

    data = json.loads('{' + output + '"end":2}')

    global peers
    for peer in data:
        if data[peer] == 0 or data[peer] == 1:
            peers.append(peer)


def whoami():
    cmd = 'sbot whoami'
    stream = os.popen(cmd)
    print('executing command:', cmd)
    output = stream.read()
    id = json.loads(output)
    print('extracted ID:', id['id'])
    return id['id']


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process command line arguments for the ssb-fbp')
    parser.add_argument('-v', dest='verbose', nargs='?', const=True, default=False,
                        help='Display all actions of the ssb-fbp')
    parser.add_argument('--verbose', dest='verbose', nargs='?', const=True, default=False,
                        help='Display all actions of the ssb-fbp')
    args = parser.parse_args()

    initLog(verbose=args.verbose, id=None)
    initPeers(verbose=args.verbose)

    peers

    for peer in peers:
        initLog(verbose=args.verbose, id=peer)

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
