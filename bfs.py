class Node:
    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False


def breath_first_search(startnode):
    queue = [startnode]

    while queue:
        actual_node = queue.pop(0)
        actual_node.visited = True
        print(actual_node.name)

        for n in actual_node.adjacency_list:
            if not n.visited:
                queue.append(n)

if __name__ == '__main__':
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)
    node4.adjacency_list.append(node5)

    breath_first_search(node1)