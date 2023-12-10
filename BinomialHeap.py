class BinomialNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.sibling = None

class BinomialHeap:
    def __init__(self):
        self.orderlist = [None]*1000
        self.min = BinomialNode(float("inf"))

    def make_heap(self, key):
        return BinomialNode(key)

    def Min(self):
        return self.min

    def insert(self, key):
        node = self.make_heap(key)
        if node.key < self.min.key:
            self.min = node
        if self.orderlist[0] is not None:
            self.merge(node, self.orderlist[0])
        else:
            self.orderlist[0] = node

    def merge(self, h1, h2):
        if h1.key < h2.key:
            h2.parent = h1
            h2.sibling = h1.child
            h1.child = h2
            self.orderlist[h1.degree] = None
            h1.degree += 1
            if len(self.orderlist) <= h1.degree:
                self.orderlist.append(h1)
            else:
                if self.orderlist[h1.degree] is None:
                    self.orderlist[h1.degree] = h1
                else:
                    temp = self.orderlist[h1.degree]
                    self.orderlist[h1.degree] = None
                    self.merge(h1,temp)

        else:
            h1.parent = h2
            h1.sibling = h2.child
            h2.child = h1
            self.orderlist[h2.degree] = None
            h2.degree += 1
            if len(self.orderlist) <= h2.degree:
                self.orderlist.append(h2)
            else:
                if self.orderlist[h2.degree] is None:
                    self.orderlist[h2.degree] = h2
                else:
                    temp = self.orderlist[h2.degree]
                    self.orderlist[h2.degree] = None
                    self.merge(h2,temp)
    
    def ExtractMin(self):
        pointer = self.min
        print("Extracted Minimum:",pointer.key)
        if pointer.degree == 0:
            self.orderlist[0] = None
        elif pointer.degree == 1:
            if self.orderlist[0] is None:
                self.orderlist[0] = pointer.child
                self.orderlist[pointer.degree] = None
            else:
                # print(pointer.child.key, self.orderlist[0].key)
                self.orderlist[pointer.degree] = None
                self.merge(pointer.child,self.orderlist[0])
        else:
            lis = []
            temp = pointer.child
            while temp:
                lis.append(temp)
                temp = temp.sibling
            self.orderlist[pointer.degree] = None
            for h in lis:
                h.sibling = None
                h.parent = None
                if self.orderlist[h.degree] is None:
                    self.orderlist[h.degree] = h
                else:
                    self.merge(h,self.orderlist[h.degree])
            

        self.min = BinomialNode(float("inf"))
        for h in self.orderlist:
            if h!=None and h.key < self.min.key:
                self.min = h
        
                
    def delete(self,key):
        i = self.decreaseKey(key,float("-inf"))
        self.min = self.orderlist[i]
        self.ExtractMin()

    def decreaseKey(self,old,new):
        idx = 0
        for i,h in enumerate(self.orderlist):
            x = self.findNode(h,old)
            if h is not None and x is not None:
                node = x
                idx = i
        
        if node is None:
            return
        
        node.key = new
        parent = node.parent
        while parent is not None and node.key < parent.key:
            temp = node.key
            node.key = parent.key
            parent.key = temp
            node = parent
            parent = parent.parent

        return idx
        
    def findNode(self, h, key):
        if (h == None):
            return None
    
        # check if key is equal to the root's data
        if (h.key == key):
            return h
    
        # Recur for child
        res = self.findNode(h.child, key)
        if (res != None):
            return res
    
        return self.findNode(h.sibling, key)
    
    def print_binomial_heap(self, heap):
        for i, tree in enumerate(heap.orderlist):
            if tree is not None:
                print(f"Trees of order {i}:")
                self.print_tree(tree)
                print()

    def print_tree(self, node, depth=0):
        if node is not None:
            print("  " * depth + f"{node.key} (degree {node.degree})")
            self.print_tree(node.child, depth + 1)
            self.print_tree(node.sibling, depth)


if __name__ == "__main__":
    binomial_heap = BinomialHeap()

    # Insert some elements
    elements_to_insert = [7,2,4,17,1,11,6,8,15,10,20,5]
    for element in elements_to_insert:
        binomial_heap.insert(element)

    binomial_heap.print_binomial_heap(binomial_heap)
    print("###############")
    # print(binomial_heap.orderlist[2].child.sibling.parent.key)


    binomial_heap.ExtractMin()
    binomial_heap.print_binomial_heap(binomial_heap)
    print("###############")
    binomial_heap.decreaseKey(15,1)
    binomial_heap.print_binomial_heap(binomial_heap)
    print("###############")
    binomial_heap.delete(1)
    binomial_heap.print_binomial_heap(binomial_heap)
    print("###############")
    binomial_heap.delete(2)
    # binomial_heap.ExtractMin()
    binomial_heap.print_binomial_heap(binomial_heap)
    # print("###############")
    # binomial_heap.ExtractMin()
    # binomial_heap.print_binomial_heap(binomial_heap)
    # print("###############")
    # binomial_heap.ExtractMin()
    # binomial_heap.print_binomial_heap(binomial_heap)
    # print("###############")
    # print(binomial_heap.ExtractMin())
    # binomial_heap.print_binomial_heap(binomial_heap)
    # # Create a new binomial heap for testing merge
    # binomial_heap_2 = BinomialHeap()
    # elements_to_insert_2 = [10, 9, 12, 11]
    # for element in elements_to_insert_2:
    #     binomial_heap_2.insert(element)

    # print("\nBinomial Heap 2:")
    # binomial_heap.print_binomial_heap(binomial_heap_2)

    # # Merge binomial_heap and binomial_heap_2

    # print("\nBinomial Heap after Merging with Binomial Heap 2:")
    # binomial_heap.print_binomial_heap(binomial_heap)
