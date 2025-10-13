class DoctorNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the doctor.
        left (DoctorNode): The left child node, representing the left report.
        right (DoctorNode): The right child node, representing the right report.
    '''

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class DoctorTree:
    '''
    A class to represent a binary tree for managing a doctor reporting structure.
    Attributes:
        root (EmployeeNode): The root of the tree, representing the head doctor.
    Methods:
        insert()
        preorder()
        inorder()
        postorder()
    '''
    def __init__(self):
        self.root = None

    def insert(self, manager_name, doctor_name, side, current_node=None):
        inserted = False
        if current_node == None:
            current_node = self.root
            if current_node == None:
                print('No doctors are in the directory.')
                return
            
        if current_node.name == manager_name:
            if side == 'right' and current_node.right == None:
                current_node.right = DoctorNode(doctor_name)
                return
            elif side == 'left' and current_node.left == None:
                current_node.left = DoctorNode(doctor_name)
                return
            else:
                print(f'The {side} side is not available for {manager_name}.')
                return
        
        if current_node.left:
            self.insert(manager_name, doctor_name, side, current_node.left)
            return
        if current_node.right:
            self.insert(manager_name, doctor_name, side, current_node.right)
            return
        
        print(f'{manager_name} not found in directory.')
    
    def preorder(self, node):
        if node is None:
            return list()
        
        result = list()

        result.append(node.name)
        result += self.preorder(node.left)
        result += self.preorder(node.right)

        return result

    def inorder(self, node):
        if node is None:
            return list()
        
        result = list()

        result += self.inorder(node.left)
        result.append(node.name)
        result += self.inorder(node.right)

        return result

    def postorder(self, node):
        if node is None:
            return list()
        
        result = list()

        result += self.postorder(node.left)
        result += self.postorder(node.right)
        result.append(node.name)

        return result

tree = DoctorTree()
tree.root = DoctorNode("Dr. Croft") 
# Insert values
tree.insert("Dr. Croft", "Dr. Goldsmith", "right") 
tree.insert("Dr. Croft", "Dr. Phan", "left")
tree.insert("Dr. Phan", "Dr. Carson", "right") 
tree.insert("Dr. Phan", "Dr. Morgan", "left")

print(tree.preorder(tree.root))
print(tree.inorder(tree.root))
print(tree.postorder(tree.root))