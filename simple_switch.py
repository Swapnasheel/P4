import json
import argparse

topo = {}
links = []
hosts = []
switches = {}


def get_args():
    parser = argparse.ArgumentParser(description="Arguments for the simple switch.")
    parser.add_argument("--hosts", '-n', help="Number of hosts", required=True, type=int)

    return parser.parse_args()


def simpleSwitch(n):

    switch = addSwitch(s=1)
    for i in range(1,n+1):
        host = addHost(i)
        addLink(switch, host)

    return 


def addSwitch(s):
    global topo, switches

    cli_input = {}
    cli_input["cli_input"] = 's{}-commands.txt'.format(s)
    switches['s{}'.format(s)] = cli_input
    topo['switches'] = switches

    return 's{}'.format(s)

def addHost(h):
    global topo, hosts

    hosts.append('h{}'.format(h))
    topo['hosts'] = hosts
    return 'h{}'.format(h)


def addLink(s, h):
    global links, topo

    temp = [s, h]
    links.append(temp)
    topo['links'] = links

    return

def dumpJSON():
    global topo

    with open('topology.json', 'w') as outfile:
        json.dump(topo, outfile, indent=4)

    print "Done creating JSON file"
    return

if __name__ == '__main__':
    args = get_args()
    simpleSwitch(args.hosts)
    dumpJSON()


        
