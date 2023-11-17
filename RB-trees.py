class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.color = "RED"

class Tree:
    def __init__(self) -> None:
        self.TNULL = TreeNode(None)
        self.TNULL.color = "BLACK"
        self.TNULL.right = None
        self.TNULL.left = None
        self.root = self.TNULL

    def sort(self):
        root = self.root
        sort = []
        return self.Inorder(root,sort)
    
    def Inorder(self,root,sort):
        if root!= self.TNULL:
            self.Inorder(root.left,sort)
            sort.append(root.val)
            self.Inorder(root.right,sort)
        return sort

    def search(self,node,val):
        if node == self.TNULL or node.val == val:
            return node
        if val < node.val:
            return self.search(node.left, val)
        return self.search(node.right, val)

    def FindMin(self,node):
        while node.left!=self.TNULL:
            node = node.left
        print(node.val)
        return node

    def FindMax(self,node):
        while node.right!=self.TNULL:
            node = node.right
        print(node.val)
        return node
    
    def Successor(self,node):
        if node.right!=self.TNULL:
            return self.FindMin(node.right)
        else:
            y = node.parent
            while y is not None and node == y.right:
                node = y
                y = y.parent
            print(y.val)
            return y

    def Predecessor(self,node):
        if node.left!=self.TNULL:
            return self.FindMax(node.left)
        else:
            y = node.parent
            while y is not None and node == y.left:
                node = y
                y = y.parent
            print(y.val)
            return y

    def Transplant(self,u,v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def delete_val(self,val):
        node = self.search(self.root,val)
        if node is not None:
            self.delete(node)
        else:
            print("Not present")

    def delete(self,node):
        if node.left == self.TNULL:
            self.Transplant(node,node.right)
        elif node.right == self.TNULL:
            self.Transplant(node,node.left)
        else:
            y = self.Successor(node)
            print(y.val)
            if y!= node.right:
                self.Transplant(y,y.right)
                y.right = node.right
                y.right.parent = y
            self.Transplant(node,y)
            y.left = node.left
            y.left.parent = y

    # def delete(self,node):
    #     if node.left is None and node.right is None:
    #         node.parent

    def LeftRotate(self,node):
        y = node.right
        node.right = y.left
        if y.left!= self.TNULL:
            y.left.parent = node
        y.parent = node.parent
        if node.parent is None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.left = node
        node.parent = y

    def RightRotate(self,node):
        y = node.left
        node.left = y.right
        if y.right != self.TNULL:
            y.right.parent = node
        y.parent = node.parent
        if node.parent is None:
            self.root = y
        elif node == node.parent.right:
            node.parent.right = y
        else:
            node.parent.left = y
        y.right = node
        node.parent = y

    def RBInsert(self,val):
        node = TreeNode(val)
        node.parent = None
        node.val = val
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = "RED"

        x = self.root
        y = None
        while x != self.TNULL:
            y = x
            if node.val < x.val:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y is None:
            self.root = node
        elif node.val < y.val:
            y.left = node
        else:
            y.right = node
        
        if node.parent is None:
            node.color = "BLACK"
            return

        if node.parent.parent is None:
            return
        
        self.Fixup(node)

    def Fixup(self,node):
        while node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                y = node.parent.parent.right
                if y.color == "RED":
                    node.parent.color = "BLACK"
                    y.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.LeftRotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.RightRotate(node.parent.parent)
            else:
                y = node.parent.parent.left
                if y.color == "RED":
                    node.parent.color = "BLACK"
                    y.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.RightRotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.LeftRotate(node.parent.parent)
            if node == self.root:
                break
        self.root.color = "BLACK"


class RBTreeVisualizer:
    def __init__(self, tree):
        self.tree = tree

    def visualize_tree(self):
        self._print_tree(self.tree.root, 0, "Root")

    def _print_tree(self, node, depth, side):
        if node!= self.tree.TNULL:
            self._print_tree(node.right, depth + 1, "R")
            print("           " * depth + f"{side}: {node.val} ({node.color})")
            self._print_tree(node.left, depth + 1, "L")
        # else:
        #     print("   " * depth + f"{side}: None (BLACK)")


# tree = Tree()
# nodes_to_insert = [10, 5, 15, 3, 7, 12, 18, 1, 6, 8]

# for val in nodes_to_insert:
#     tree.RBInsert(val)

def run_interactive_menu(tree):
        while True:
            print("###################################################################")
            print("\nOptions:")
            print("1. Search for a value")
            print("2. Insert a new value")
            print("3. Delete a value")
            print("4. Display tree")
            print("5. Sorted order")
            print("6. Predecessor")
            print("7. Successor")
            print("8. Max")
            print("9. Min")
            print("10. Exit")

            choice = input("Enter your choice (1-10): ")

            if choice == '1':
                value_to_search = int(input("Enter the value to search: "))
                node = tree.search(tree.root, value_to_search)
                if node.val == value_to_search:
                    print(f"Value {value_to_search} found in the tree.")
                else:
                    print(f"Value {value_to_search} not found in the tree.")
                visualizer = RBTreeVisualizer(tree)
                visualizer.visualize_tree()

            elif choice == '2':
                value_to_insert = int(input("Enter the value to insert: "))
                tree.RBInsert(value_to_insert)
                print(f"Value {value_to_insert} inserted into the tree.")
                visualizer = RBTreeVisualizer(tree)
                visualizer.visualize_tree()

            elif choice == '3':
                value_to_delete = int(input("Enter the value to delete: "))
                tree.delete_val(value_to_delete)
                print(f"Value {value_to_delete} deleted from the tree.")
                visualizer = RBTreeVisualizer(tree)
                visualizer.visualize_tree()
            
            elif choice == '4':
                visualizer = RBTreeVisualizer(tree)
                visualizer.visualize_tree()
            
            elif choice == '5':
                print(tree.sort())
            
            elif choice == '6':
                value_to_pred = int(input("Enter the value to find predecessor: "))
                node = tree.search(tree.root,value_to_pred)
                if node.val == value_to_pred:
                    tree.Predecessor(node)
                else:
                    print(f"Value {value_to_pred} not found in the tree.")
            
            elif choice == '7':
                value_to_succ = int(input("Enter the value to find successor: "))
                node = tree.search(tree.root,value_to_succ)
                if node.val == value_to_succ:
                    tree.Successor(node)
                else:
                    print(f"Value {value_to_pred} not found in the tree.")
            
            elif choice == '8':
                tree.FindMax(tree.root)
            
            elif choice == '9':
                tree.FindMin(tree.root)

            elif choice == '10':
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")






tree = Tree()
filename = "input_numbers.txt"  # Replace with your file path
with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]
        for val in numbers:
            tree.RBInsert(val)

run_interactive_menu(tree)




# # Visualize the tree
# sort = []
# print(tree.sort())  
# visualizer = RBTreeVisualizer(tree)
# visualizer.visualize_tree()
# print("###############")
# print(tree.root.left.left.val)
# tree.delete_val(15)  
# visualizer = RBTreeVisualizer(tree)
# visualizer.visualize_tree()