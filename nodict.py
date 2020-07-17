#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'Kevin Blount'


class Node:
    def __init__(self, key, value=None):
        """
        A method that initialized instance variables
        for __init__
        """
        self.hash = hash(key)
        self.key = key
        self.value = value
        return

    def __repr__(self):
        """
        A method for human-readable representation of its key/value contents
        """
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):
        """
        A method that compares itself to other Node objects 
        using the Python built-in == operator.
        """
        return self.hash == other.hash and self.key == other.key


class NoDict:
    def __init__(self, num_buckets=10):
        """
        A method that initialized instance variables
        for __init__ in NoDict.
        """
        self.buckets = [[] for _ in range(num_buckets)]
        self.size_buckets = num_buckets

    def __repr__(self):
        """Return a string representing the NoDict contents"""
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}' for i, bucket in enumerate(self.buckets)])

    def add(self, key, value):
        """
        This class method should accept a new key and value, and 
        store it into the NoDict instance
        Should not allow duplicates.
        """
        new_node = Node(key, value)
        current_bucket = self.buckets[new_node.hash % self.size_buckets]
        for element in current_bucket:
            if element == new_node:
                current_bucket.remove(element)
                break
        current_bucket.append(new_node)

    def get(self, key):
        """
        This class method should perform a key-lookup in the NoDict class. 
        It should accept just one parameter: The key to look up. If the key is found in the NoDict class, 
        return its associated value. 
        If the key is not found, raise a KeyError exception.
        """
        node_to_find = Node(key)
        current_bucket = self.buckets[node_to_find.hash % self.size_buckets]
        for element in current_bucket:
            if element == node_to_find:
                return element.value
        raise KeyError(f'{key} not found')

    def __getitem__(self, key):
        """
        This method will enable square-bracket reading behavior
        """
        return self.get(key)

    def __setitem__(self, key, value):
        """
        This will enable square-bracket assignment behavior
        """
        self.add(key, value)


# n1 = Node('Mike', 21)
# n2 = Node('Mike', 34)
# n3 = Node('Nick', 56)
# print(f'n1 == n2 ? {n1 == n2}')
# print(f'n2 == n3 ? {n2 == n3}')

my_dict = NoDict()
my_dict['Kevin'] = 21
my_dict['Nikal'] = 25
kevin_age = my_dict['Kevin']
print(my_dict)
print(kevin_age)
