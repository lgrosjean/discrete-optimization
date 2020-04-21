#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

from utils import parse_input, parse_output
from functions import solver_example, solver_dp
from tree import solver_depth_first_branch
import time

def solve_it(input_data):
    # Read the inputs
    inputs = parse_input(input_data)
    capacity = inputs.capacity
    items = inputs.items

    # Solver Example
    #value, taken = solver_example(capacity, items)

    # Solver DP
    print("Capacity:", capacity, " | N:" ,len(items))
    start = time.time()
    if capacity*len(items) <  10000*10000:
        print("Solver DP")
        value, taken = solver_dp(capacity, items)
    else:
        print("Solver Tree")
        value, taken = solver_depth_first_branch(capacity, items)

    end = time.time()
    print("Time:", end-start)

    # Parse outputs
    output_data = parse_output(value, taken)
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

