# IsBinarySearchTree assume no duplicate int values
# read/video here https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

############ efficient implementation Time Complexity O(n), mem O(1) or O(n) if consider func call stack
def isBSTutil(node, min, max):
    # empty tree is BST
    if node is None:
        return True

    # BST current node must be bigger than its max left child and smaller than its min right child 
    if node.value < min or node.value > max:
        return False
    return isBSTutil(node.left, min, node.value-1) and isBSTutil(node.right, node.value+1, max)

def isBST(root):
    return isBSTutil(root, float('-inf'), float('inf'))

############ in order traversal implementation Time Complexity O(n)
# global variable prev to keep track of previous node during in order traversal
prev = None

def isbst(root):
    global prev
    prev = None
    return isbst_trav(root)

def isbst_trav(root):
    global prev

    if root is None:
        return True # empty tree is bst

    if isbst_trav(root.left) is False:
        return False

    if prev is not None and prev.value > root.value:
        return False

    prev = root
    return isbst_trav(root.right)

def main():
    # Driver program to test above function
    #         4
    #        / \
    #       2   5
    #      / \ 
    #     1   3
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    
    if (isBST(root)):
        print("Is BST")
    else:
        print("Not a BST")

    if (isbst(root)):
        print("Is bst")
    else:
        print("Not a bst")        

if __name__ == "__main__":
    main()    