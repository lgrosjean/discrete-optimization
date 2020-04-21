import numpy as np

def best_relaxation(capacity, items):
    n = len(items)
    weights = [item.weight for item in items]
    values = [item.value for item in items]
    value_weight = [value/weight for (value, weight) in zip(values, weights)]

    id_sort = np.argsort(-np.array(value_weight))

    remain = capacity
    value = 0

    for i in id_sort:
        if remain<=0:
            break
        else:
            if weights[i] <= remain:
                value  += values[i]
                remain -= weights[i]
            else:
                value += value_weight[i]*remain
                remain -= remain
    
    return value


if __name__ == '__main__':
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
        print(best_relaxation(capacity, items))
        end = time.time()
        print(f"Total time: {end-start}")