from collections import OrderedDict

def load_csv(filename):
    """Load and parse the given csv file of nodes
    :param filename: The name of the file to load
    :returns: OrderedDict of nodes, keyed by post_id, in descending order
    """
    file = open(filename)
    nodes = OrderedDict()
    lines = file.read().splitlines()
    parsed_lines = []

    for line in lines:
        post_id, repost_id, followers = line.split(",")
        node = (int(post_id), int(repost_id), int(followers))
        parsed_lines.append(node)

    parsed_lines.sort(key=lambda line:line[0], reverse=True) # Could be replaced by reversed() on OrderedDict in py3.5 for less hassle
    for line in parsed_lines:
        node = {
            "post_id": line[0],
            "repost_id": line[1],
            "followers": line[2]
        }
        nodes[line[0]] = node

    return nodes

def is_root(node):
    """ Return true if the node is a root node """
    return node["repost_id"] == -1

def get_parent(node, nodes):
    """ Returns the parent of this node. """
    return nodes[node["repost_id"]]

def get_follower_totals(nodes):
    """ Returns dict of root_post_ids to follower counts """
    totals = {}
    for post_id, node in nodes.items():
        if is_root(node):
            totals[node["post_id"]] = node["followers"]
        else:
            parent = get_parent(node, nodes)
            parent["followers"] += node["followers"]
    return totals

if __name__ == '__main__':
    nodes = load_csv("network.csv")
    #nodes = load_csv("big_network.csv")    
    follower_totals = get_follower_totals(nodes)
    for root_post_id, total in follower_totals.items():
        print("{0}: {1}".format(root_post_id, total))
