# !python

# ==================================================================================
# File: scenario_3.py

# You have 5 carrier route lists, each with 10,000,000 (10m) entries (in arbitrary order)
# and a list of 10,000 phone numbers. How can you speed up your route cost lookup
# solution to handle this larger dataset

# Copyright © 2019 Jayce Azua and Asim Zaidi. All rights reserved.
# ==================================================================================

# scenario 1 - 3

import os
import time
import psutil
# scenario 3
from trie import Trie


class Trie_CallRouter(object):
    # ------------------------------------------------------------------------------
    # CallRoutes - Constructor
    # ------------------------------------------------------------------------------
    def __init__(self, carrier_route_path):
        """route_costs: trie tree of costs for routes"""
        self.route_costs = self.__convert_file_into_trie(carrier_route_path)
# ------------------------------------------------------------------------------
# CallRouter - Intended Private Methods
# ------------------------------------------------------------------------------

    def __convert_file_into_trie(self, file_path):
        """ Returns a Trie tree from the given file_path. Costs of routes."""
        # get number prefixes and costs from lines = numbers_and_costs_from(data_file_path)
        # print('in build_tree')
        trie_lookup = Trie()
        # iterates through routes and costs
        with open('data/' + file_path, 'r') as file:
            for line in file:
                line = line[:-1]
                route, cost = line.split(",")
                trie_lookup.insert(route, cost)
        return trie_lookup

    def read_number(self, path_to_file):
        with open('data/' + path_to_file, "r") as file:
            for line in file:
                line = line[:-1]
                cost = self.find_route_cost(line)
                self.write_cost(line, str(cost))
# ------------------------------------------------------------------------------
# CallRouter - Public Methods
# ------------------------------------------------------------------------------
    def find_route_cost(self, phone_number):
        return self.route_costs.search_and_return_cost(phone_number)

    def write_cost(self, phone_number, cost):
        with open('data/' + "call-costs-3.txt", "a") as f:
            f.write(phone_number + ", " + cost + "\n")


def test_call_router():
    start = time.time()
    carrier_route_path = 'route-costs-10000000.txt'
    call_router = Trie_CallRouter(carrier_route_path)
    load_time = round(time.time() - start, 4)
    print("\nBuilding the Trie took: {} seconds.".format(load_time))
    phone_number = 'phone-numbers-10000.txt'
    start = time.time()
    call_router.read_number(phone_number)
    load_time = round(time.time() - start, 4)
    print("\nLooking up 10000 numbers in a Trie took: {} seconds.".format(load_time))

# ------------------------------------------------------------------------------
# Memory Usage Function (Inspired by research)
# ------------------------------------------------------------------------------
def get_memory():
    """Print memory usage to stdout."""
    process = psutil.Process(os.getpid())
    print(process.memory_info().rss) # in bytes

if __name__ == '__main__':
    print("\nInitializing Scenario 3...")
    test_call_router()





