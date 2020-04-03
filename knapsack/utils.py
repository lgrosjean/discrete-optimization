from collections import namedtuple

def parse_input(input_data):

    Item = namedtuple("Item", ['index', 'value', 'weight'])
    Inputs = namedtuple("Inputs", ['capacity', 'items'])
    
    lines = input_data.split('\n')

    first_line = lines[0].split()
    item_count = int(first_line[0])
    capacity = int(first_line[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        value = int(parts[0])
        weight = int(parts[1])
        item = Item(i-1, value, weight)
        items.append(item)

    inputs = Inputs(capacity, items)

    return inputs

def parse_output(value:int, taken:list, solved=0):

    output_data = str(value) + ' ' + str(solved) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data