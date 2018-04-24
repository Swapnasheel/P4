import json
import argparse
#from mininet.util import irange

topo = {}
switches = {}
hosts = []
links = []

def get_args():
    parser = argparse.ArgumentParser(description="Parser for the linear code.")
    parser.add_argument('--switches', '-s', help="Number of switches in the topology", required=True, type=int)

    return parser.parse_args()

def addLinear(n):
    lastSwitch = None
    for h in range(1, n+1):
        switch = addSwitch(h)
        host = addHost(h)
        addLinks(switch, host)

        if lastSwitch:
            addLinks(switch, lastSwitch)
        lastSwitch = switch


def addSwitch(s):
    global topo, switches

    cli_input = {}
    temp = "s{}-commands.txt".format(s)
    cli_input['cli_input'] = temp
    switches['s{}'.format(s)] = cli_input
    topo['switches'] = switches
    return "s{}".format(s)


def addHost(h):
    global topo, hosts

    hosts.append("h{}".format(h))
    topo["hosts"] = hosts

    return "h{}".format(h)


def addLinks(s, h):
    global links, topo
    temp = [s, h]
    links.append(temp)
    topo['links'] = links
    
    return


def dumpJSON():
    global topo

    with open('topology.json', 'w') as outfile:
        json.dump(topo, outfile, indent=4)

    print "Done creating JSON file!"
    return


if __name__ == "__main__":
    args = get_args()
    addLinear(args.switches)
    dumpJSON()




