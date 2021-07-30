class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        # Your code goes here
        cur = self.root
        if not cur:
            self.root = Node(new_val)
            return self.root

        while cur:
            if cur.value > new_val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = Node(new_val)
                    break
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = Node(new_val)
                    break

        return self.root


    def printSelf(self):
        # Your code goes here
        print(self.root)


        
    def search(self, find_val):
        # Your code goes here
        while self.root!=None:
            if self.root.value == find_val:
                return True 
            if self.root.value < find_val:
                self.root = self.root.right
            else:
                self.root = self.root.left
        return False

