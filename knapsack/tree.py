from collections import namedtuple, deque
from relaxation import best_relaxation

Node = namedtuple("Node", ['value', 'remain', 'expected', 'level', 'taken'])

def max_node(node_a, node_b):
    if node_a.value >= node_b.value:
        return node_a
    else:
        return node_b

def solver_depth_first_branch(capacity, items):

    n = len(items)
    weights = [item.weight for item in items]
    values = [item.value for item in items]

    relaxation = best_relaxation(capacity, items)
    # print("Relaxation:", relaxation)

    stack = deque()
    # https://www.geeksforgeeks.org/stack-in-python/

    node_0 = Node(0, capacity, relaxation, 0, [])
    best_node = node_0
    stack.append(node_0)

    while len(stack)>0:
        father = stack.pop()
        # print("Taken", father.taken)

        if father.value >= best_node.value:
            best_node = father
        if father.level < n:
            child_0 = Node(
                value=father.value, 
                remain=father.remain, 
                expected=father.expected,
                level=father.level+1, 
                taken=father.taken + [0]
            )
            child_1 = Node(
                value=father.value+values[father.level],
                remain=father.remain-weights[father.level],
                expected=father.expected-values[father.level],
                level=father.level+1,
                taken=father.taken + [1]
            )

            # print("Father:", father, "Child_0:", child_0, "Child_1", child_1)

            if child_0.remain >= 0:
                stack.append(child_0)
            # else:
            #     print("  Child - Taken", child_0.taken, child_0.remain)
            if child_1.remain>=0:
                stack.append(child_1)
            # else:
            #     print("  Child - Taken", child_1.taken, child_1.remain)

    # return best_node
    value = best_node.value
    taken = best_node

    return value, taken

if __name__=="__main__":
    import sys
    import time
    from utils import parse_input
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        inputs = parse_input(input_data)
        capacity = inputs.capacity
        items = inputs.items
        start = time.time()
        print(solver_depth_first_branch(capacity, items))
        end = time.time()
        print(f"Total time: {end-start}")

