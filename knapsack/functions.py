import numpy as np
from tqdm import tqdm

def solver_example(capacity, items):
    """Example for raw courses
    """

    value = 0
    weight = 0
    taken = [0]*len(items)

    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight

    return value, taken

def solver_dp(capacity, items):

    n = len(items)
    K = capacity

    value = 0
    taken = [0]*len(items)

    weights = [0] + [item.weight for item in items]
    values = [0] + [item.value for item in items]

    # Initalize the matrix for Dynamic programming
    m = np.zeros((K+1, n+1), dtype=np.int64)

    # Iterate through the Matrix
    for j in tqdm(range(1, n+1)):
        for k in range(1, K+1):
            if weights[j] > k:
                m[k, j] = m[k, j-1]
            else:
                m[k, j] = max(m[k, j-1], values[j] + m[k-weights[j], j-1])

    # Traceback
    k = K
    j = n
    value = m[k, j]

    while (j!=0 and k!=0):
        if m[k, j] == m[k, j-1]:
            taken[j-1] = 0 # we dont take it
            j = j-1
        else:
            taken[j-1] = 1
            k = k-weights[j]
            j = j-1

    return value, taken

