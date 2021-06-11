# vacation planner
# given a collection of vacation start and end date pairs, return a max set of non-overlapping
# vacation periods while prioritizing longer vacations

class Node():
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.length = end - start
        self.children = set()
        self.visited = False

    def relate_previous(self, node):
        if self.start > node.end:
            return
        if self.length > node.length:
            self.children.add(node)
        else:
            node.children.add(self)

def get_vacations(date_ranges):
    # build directed graph
    nodes = set()

    for start, end in date_ranges:
        new_node = Node(start, end)

        for node in nodes:
            new_node.relate_previous(node)

        nodes.add(new_node)

    # sort nodes
    sorted_nodes = []

    def _visit(node):
        if not node.visited:
            node.visited = True

            for child in node.children:
                _visit(child)

            sorted_nodes.append(node)

    for node in nodes:
        _visit(node)

    # remove shorter overlaps
    for node in sorted_nodes[::-1]:
        if node in nodes:
            nodes -= node.children

    return [(node.start, node.end) for node in nodes]

def main():
    test_cases = [
        ([], []),
        ([(0, 10)], [(0,10)]),
        ([(0, 10), (20, 25)], [(0, 10), (20, 25)]),
        ([(0, 10), (8, 12)], [(0, 10)]),
        ([(0, 10), (5, 15)], [(0, 10)]),
        ([(0, 10), (5, 20)], [(5, 20)]),
        ([(0, 10), (10, 20)], [(0, 10)]),
        ([(0, 10), (0, 5)], [(0, 10)]),
        ([(0, 10), (5, 10)], [(0, 10)]),
        ([(0, 10), (0, 10)], [(0, 10)]),
        ([(0, 10), (0, 1), (1, 3), (2, 4)], [(0, 10)]),
        ([(0, 10), (5, 20), (15, 35)], [(0, 10), (15, 35)])
    ]

    for input_date_ranges, expected_output in test_cases:
        actual_output = get_vacations(input_date_ranges)

        if set(actual_output) == set(expected_output):
            print("pass -- vacations: {0}".format(input_date_ranges))
        else:
            print("FAIL -- vacations {0}\n  actual  {1}\n  expected  {2}".format(input_date_ranges, actual_output, expected_output))

if __name__ == "__main__":
    main()