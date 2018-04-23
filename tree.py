'''
Script trying to json.dump topology
'''

import json
import argparse

topo = {}
switches = {}
hosts = []
links = []
sNumber = 0
hNumber = 0

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--depth', '-d', help="Depth of the tree topology", required=True, type=int)
    parser.add_argument('--fanout', '-f', help="Fanout for the tree topology", required=True, type=int)

    return parser.parse_args()


def addTree(depth, fanout):
    global sNumber, hNumber

    toAdd = depth > 0

    if toAdd:
        node = addSwitch(sNumber = int(sNumber) + 1)
        sNumber += 1
        for i in range(fanout):
            child = addTree(depth = (depth - 1), fanout = fanout)
            addLink(node, child)
    else:
        node = addHost(hNumber = int(hNumber) + 1)
        hNumber += 1
    return node


def addSwitch(sNumber):
    global topo
    global switches

    cli_input = {}
    temp = "s{}-commands.txt".format(sNumber)
    cli_input["cli_input"] = temp
    switches["s{}".format(sNumber)] = cli_input
    topo["switches"] = switches
    return "s{}".format(sNumber)

def addHost(hNumber):
    global topo
    global hosts

    hosts.append("h{}".format(hNumber))
    topo["hosts"] = hosts
    return "h{}".format(hNumber)

def addLink(node, child):
    global links, topo

    temp = [node, child]
    links.append(temp)

    topo["links"] = links
    return

def dumpJSON():
    global topo
    with open("topology.json", "w") as outfile:
        json.dump(topo, outfile, indent=4)

    print "Done creating JSON file!"


if __name__ == "__main__":
    args = get_args()
    addTree(args.depth, args.fanout)
    dumpJSON()

