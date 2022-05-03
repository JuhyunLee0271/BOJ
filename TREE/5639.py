import sys
sys.setrecursionlimit(10**9)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None        
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
            return
        
        cur_node = self.root
        while True:
            # left child traverse
            if cur_node.value > value:
                if cur_node.left == None:
                    cur_node.left = Node(value)
                    break
                else:
                    cur_node = cur_node.left
            
            # right child traverse
            else:                           
                if cur_node.right == None:
                    cur_node.right = Node(value)
                    break
                else:
                    cur_node = cur_node.right
    
# postorder: left -> right -> mid    
def postorder(node):
    if not node:
        return
    if node.left:
        postorder(node.left)
    if node.right:
        postorder(node.right)
    print(node.value)

# 후위 순회: left -> right -> mid
if __name__ == "__main__":
    bst = BST()
    while True:
        try:
            bst.insert(int(input()))
        except:
            break
    postorder(bst.root)