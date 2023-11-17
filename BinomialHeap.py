class BinomialNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.sibling = None

class BinomialHeap:
    def __init__(self):
        self.head = None

    def make_heap(self):
        return BinomialHeap()

    def insert(self, key):
        new_heap = self.make_heap()
        new_heap.head = BinomialNode(key)
        self.head = self.union(self, new_heap)

    def minimum(self):
        if not self.head:
            return None

        min_node = self.head
        current = self.head.sibling

        while current:
            if current.key < min_node.key:
                min_node = current
            current = current.sibling

        return min_node.key

    def extract_min(self):
        if not self.head:
            return None

        min_node = self.head
        prev = None
        prev_next = None
        current = self.head.sibling

        while current:
            if current.key < min_node.key:
                min_node = current
                prev = prev_next
            prev_next = current
            current = current.sibling

        if prev:
            prev.sibling = min_node.sibling
        else:
            self.head = min_node.sibling

        child = min_node.child
        while child:
            next_child = child.sibling
            child.sibling = None
            new_heap = self.make_heap()
            new_heap.head = child
            self.head = self.union(self, new_heap)
            child = next_child

        return min_node.key

    def union(self, h1, h2):
        new_heap = self.make_heap()
        new_heap.head = self.merge(h1.head, h2.head)
        self.head = None
        h2.head = None
        return self.adjust_heap(new_heap)

    def decrease_key(self, node, new_key):
        if new_key > node.key:
            print("New key is greater than current key.")
            return

        node.key = new_key
        while node.parent and node.key < node.parent.key:
            node.key, node.parent.key = node.parent.key, node.key
            node = node.parent

    def delete(self, node):
        self.decrease_key(node, float('-inf'))
        self.extract_min()

    def merge(self, h1, h2):
        if not h1:
            return h2
        if not h2:
            return h1

        head = None
        tail = None
        while h1 and h2:
            if h1.degree <= h2.degree:
                next_heap = h1
                h1 = h1.sibling
            else:
                next_heap = h2
                h2 = h2.sibling

            if not head:
                head = next_heap
                tail = next_heap
            else:
                tail.sibling = next_heap
                tail = next_heap

        if h1:
            tail.sibling = h1
        else:
            tail.sibling = h2

        return head

    def adjust_heap(self, heap):
        current = heap.head
        prev = None
        next_node = current.sibling

        while next_node:
            if (current.degree != next_node.degree or
                    (next_node.sibling and next_node.sibling.degree == current.degree)):
                prev = current
                current = next_node
            else:
                if current.key <= next_node.key:
                    current.sibling = next_node.sibling
                    next_node.parent = current
                    next_node.sibling = current.child
                    current.child = next_node
                    current.degree += 1
                else:
                    if not prev:
                        heap.head = next_node
                    else:
                        prev.sibling = next_node
                    current.parent = next_node
                    current.sibling = next_node.child
                    next_node.child = current
                    next_node.degree += 1
                    current = next_node

            next_node = current.sibling

        return heap.head


# Example usage:
heap = BinomialHeap()

# Insert some keys
keys_to_insert = [5, 7, 2, 10, 3]
for key in keys_to_insert:
    heap.insert(key)

print("Heap after insertions:")
print("Minimum:", heap.minimum())
print("Extracted Min:", heap.extract_min())
print("Heap after extracting min:")
print("Minimum:", heap.minimum())

# Decrease key and delete
node_to_decrease = heap.head.child
heap.decrease_key(node_to_decrease, 1)
print("Heap after decreasing key:")
print("Minimum:", heap.minimum())

heap.delete(node_to_decrease)
print("Heap after deleting node:")
print("Minimum:", heap.minimum())
