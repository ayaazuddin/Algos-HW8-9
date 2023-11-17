import matplotlib.pyplot as plt

import numpy as np

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, key, value):
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        current = self.head
        prev = None

        while current is not None:
            if current.key == key:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next

        return False

    def find(self, key):
        current = self.head

        while current is not None:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def increase(self, key):
        current = self.head

        while current is not None:
            if current.key == key:
                current.value += 1
                return True
            current = current.next

        return False

    def list_all_keys(self):
        keys = []
        current = self.head

        while current is not None:
            keys.append(current.key)
            current = current.next

        return keys

class HASH:
    def __init__(self,size):
        self.hash_table_size = size
        self.hash_table = [LinkedList() for _ in range(self.hash_table_size)]

    def hash_function(self, word):
        return sum(ord(char) for char in word) % self.hash_table_size

    def insert(self, word):
        hash_value = self.hash_function(word)
        linked_list = self.hash_table[hash_value]
        
        if linked_list.find(word) is not None:
            linked_list.increase(word)
            return
        
        linked_list.insert(word, 1)
    
    def save_histogram_plot(lengths, m):
        plt.hist(lengths, bins=range(0, max(lengths) + 2), alpha=0.7, align='left', rwidth=0.8)
        plt.title(f"Histogram of Collision List Lengths (m={m})")
        plt.xlabel("Length of Collision Lists")
        plt.ylabel("Frequency")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.savefig(f"histogram_m_{m}.png")
        plt.close()

    def delete(self, word):
        hash_value = self.hash_function(word)
        linked_list = self.hash_table[hash_value]

        return linked_list.delete(word)

    def increase(self, word):
        hash_value = self.hash_function(word)
        linked_list = self.hash_table[hash_value]

        return linked_list.increase(word)

    def find(self, word):
        hash_value = self.hash_function(word)
        linked_list = self.hash_table[hash_value]

        return linked_list.find(word)

    def list_all_keys(self):
        keys = []
        for linked_list in self.hash_table:
            keys.extend(linked_list.list_all_keys())
        return keys

    def collision_list_lengths(self):
        lengths = [len(linked_list.list_all_keys()) for linked_list in self.hash_table]
        return lengths
    
    def print_longest_lists(self):
        lengths = [(i, len(linked_list.list_all_keys())) for i, linked_list in enumerate(self.hash_table)]
        sorted_lengths = sorted(lengths, key=lambda x: x[1], reverse=True)
        top_percentage = int(len(sorted_lengths) * 0.1)

        print(f"\nTop {int(10)}% of Longest Lists:")
        for i in range(top_percentage):
            index, length = sorted_lengths[i]
            print(f"List {index}: Length {length}")

    def output_to_file(self, filename):
        with open(filename, 'w') as file:
            for linked_list in self.hash_table:
                for key in linked_list.list_all_keys():
                    file.write(f"{key}: {linked_list.find(key)}\n")



variance = []


test = ["food","bar","bar","drinks","bartender","dinner"]


word_counter = HASH(2)

for word in test:
    word_counter.insert(word)

word_counter.increase("food")

word_counter.delete("bar")

word_counter.output_to_file("test.txt")

# for m in [30, 300, 1000]:
#     word_counter = HASH(m)
#     # with open('alice_in_wonderland.txt','r') as file:   
#     #     for line in file:        
#     #         for word in line.split():
#     #             word_counter.insert(word)

#     collision_lengths = word_counter.collision_list_lengths()
#     print(collision_lengths)
#     print(word_counter.print_longest_lists())
#     mean = sum(collision_lengths)/m
#     var = sum((i - mean) ** 2 for i in collision_lengths) / m
#     variance.append(var)
#     plt.bar(range(1, m + 1), collision_lengths, alpha=0.7)
#     plt.title(f"Histogram of Collision List Lengths (m={m})")
#     plt.xlabel("Length of Collision Lists")
#     plt.ylabel("Frequency")
#     plt.grid(axis='y', linestyle='--', alpha=0.7)
#     plt.savefig(f"histogram_m_{m}.png")
#     plt.close()
    


word_counter.output_to_file("check.txt")

print(variance)

