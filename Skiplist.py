import random

class Node:
    def __init__(self, key, level):
        self.key = key
        self.next = [None] * (level + 1)

class SkipList:
    def __init__(self, max_level):
        self.MAX_LEVEL = max_level
        self.header = self.create_node(float('-inf'), self.MAX_LEVEL)
        self.level = 0

    def create_node(self, key, level):
        new_node = Node(key, level)
        return new_node

    def random_level(self):
        level = 0
        while random.random() < 0.5 and level < self.MAX_LEVEL:
            level += 1
        return level

    def insert(self, key):
        update = [None] * (self.MAX_LEVEL + 1)
        current = self.header

        # if self.search(key):
        #     print("Already exists")
        #     return

        for i in range(self.level, -1, -1):
            while current.next[i] and current.next[i].key < key:
                current = current.next[i]
            update[i] = current

        new_level = self.random_level()
        if new_level > self.level:
            for i in range(self.level + 1, new_level + 1):
                update[i] = self.header
            self.level = new_level

        new_node = self.create_node(key, new_level)

        for i in range(new_level + 1):
            new_node.next[i] = update[i].next[i]
            update[i].next[i] = new_node

    def search(self, key):
        current = self.header
        path = []
        # print(self.level)
        for i in range(self.level, -1, -1):
            while current.next[i] and current.next[i].key <= key:
                path.append(current.key)
                # print(current.next)
                if current.next[i].key == key:
                    path.append(current.next[i].key)
                    print(path)
                    return
                current = current.next[i]
                


        path.append(current.key)
        current = current.next[0]

        if current and current.key == key:
            path.append(current.key)
            print(path)
            return True
        return False

    def delete(self, key):
        update = [None] * (self.MAX_LEVEL + 1)
        current = self.header
        for i in range(self.level, -1, -1):
            while current.next[i] and current.next[i].key < key:
                current = current.next[i]
            update[i] = current

        current = current.next[0]

        if current and current.key == key:
            for i in range(self.level + 1):
                if update[i].next[i] != current:
                    break
                update[i].next[i] = current.next[i]

            while self.level > 0 and self.header.next[self.level] is None:
                self.level -= 1

    def display(self):
        for level in range(self.level + 1):
            current = self.header
            print(f"Level {level}: ", end="")
            while current.next[level]:
                print(f"{current.next[level].key} -> ", end="")
                current = current.next[level]
            print("END")



skip_list = SkipList(max_level=4)

keys_to_insert = [3, 6, 7, 9, 12, 19, 17, 26, 21, 25]
for key in keys_to_insert:
    skip_list.insert(key)

# skip_list.display()
# skip_list.insert(12)
# print("###########")
# skip_list.delete(19)
# skip_list.delete(19)
skip_list.search(17)
skip_list.display()

# skip_list.insert(3)
# skip_list.display()
# search_key = 19
# skip_list.search(search_key)

# skip_list.delete(17)
# skip_list.display()