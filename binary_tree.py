class TreeNode:
    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, new_value):
        self.value = new_value

    def set_left(self, node):
        set.left = node

    def set_right(self, node):
        set.right = node

    def get_value(self):
        return self.value
    
    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def balanced(self):
        return self.left and self.right
    
class BinaryTree:
    def __init__(self, root_node= None):
        self.root_node = root_node

    def set_root(self, new_root):
        self.root_node = new_root
    def _post_order(self,node):
        if node:
            return 1 + self._post_order(node.get_left()) + self._post_order(node.get_right())
        else:
            return 0

    def length(self):
        return self._post_order(self.root_node)

    def add_node(self, item):
        new_node = TreeNode(item)
        if self.root_node == None: # check if there is a root node in the tree
            self.root_node = new_node # if not then will set this node as root
         
        else:
            position = self._post_order(self.root_node)
            backtrack = []
            right = 0
            left = 1
            start = self.root_node
        # print(position)
            while position > 0:
                if position % 2 == 0:
                    backtrack.insert(0, right)
                else:
                    backtrack.insert(0, left)

                position = int((position -1 / 2 ))

            final = backtrack.pop()

            for command in backtrack:
                if command:
                    start = start.get_left()
                else:
                    start = start.get_right()
                        
new_tree = BinaryTree()
new_tree.add_node('Finally')
new_tree.add_node('Another')
new_tree.add_node('answer')

print(new_tree.length())