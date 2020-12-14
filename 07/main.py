def parse_input(input_file):
    return open(input_file, "r").read().splitlines()


def create_definition_dict(input_lines):
    definitions = {}

    for line in input_lines:
        current_node = ' '.join(line.split()[:2])
        definitions[current_node] = {}

        children = line.split(' contain ')[1]
        for child in children.split(", "):
            if child == "no other bags.":
                continue

            phrase = child.split()
            child_node_name = ' '.join(phrase[1:3])
            child_node_count = phrase[0]
            definitions[current_node][child_node_name] = child_node_count
    return definitions


definitions = create_definition_dict(parse_input("test.txt"))

print(definitions)
# counter = 0


def get_layer_contents(definitions, key_name):
    if len(definitions[key_name].keys()) == 0:
        return []
    else:
        return definitions[key_name].keys()


def get_tree_contents(definitions, root_key):
    max_iter = len(definitions.keys())
    nodes = []
    counter = 0
    key_name = root_key

    while get_layer_contents(definitions, key_name) and counter < max_iter:
        found_nodes = get_layer_contents(definitions, key_name)
        print("Found child nodes", found_nodes)
        nodes += found_nodes
        counter += 1
        for node in found_nodes:
            nodes += get_layer_contents(definitions, node)

    print("FINAL NODES ON TREE:", nodes)
    return


# get_tree_contents(definitions, "light red")


# def solve_part_1(definitions):
#     counter = 0
#     for root in definitions.keys():
#         if "shiny gold" in get_tree_contents(root, definitions):
#             counter+=1
#     return counter
#
#
# print("TEST:", solve_part_1(create_definition_dict(parse_input("test.txt"))))
#
#
# for key_name in definition_dict.keys():
#     print(list(definition_dict[key_name].keys()))
    # elif key is not empty, check child keys (repeat max N times where N is key count to prevent reference loops)
    # elif key is empty - stop




