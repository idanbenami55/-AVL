AVL Trees Project



    class Node:
        def __init__(self, key, value):
            """
            Constructor for the Node class - accepts a key and a value and constructs a node.
            """
        
        def get_left(self):
            """
            Method to return the left child of self.
            """
        
        def get_right(self):
            """
            Method to return the right child of self.
            """
        
        def get_parent(self):
            """
            Method to return the parent of self.
            """
        
        def get_key(self):
            """
            Method to return the key of self.
            """
        
        def get_value(self):
            """
            Method to return the value of self.
            """
        
        def get_height(self):
            """
            Method to return the height of self.
            """
        
        def get_size(self):
            """
            Method to return the size field that represents the number of nodes in the subtree rooted at self.
            """
        
        def set_left(self, node):
            """
            Method accepts an AVLNode node and sets it as the left child of self.
            """
        
        def set_right(self, node):
            """
            Method accepts an AVLNode node and sets it as the right child of self.
            """
        
        def set_parent(self, node):
            """
            Method accepts an AVLNode node and sets it as the parent of self.
            """
        
        def set_key(self, key):
            """
            Method accepts a key and sets it as the key of self.
            """
        
        def set_value(self, value):
            """
            Method accepts a value and sets it as the value of self.
            """
        
        def set_height(self, h):
            """
            Method accepts a height h and sets it as the height of self.
            """
        
        def set_size(self, newsize):
            """
            Method accepts an input newsize and sets it as the size of self.
            """
        
        def fix_size(self):
            """
            Method corrects the size field of self according to its children, as taught in the lecture, 
            it can be calculated through them (sum of the sizes of the children + 1).
            """
        
        def calc_size(self):
            """
            Method calculates and returns the size field of self according to its children, 
            as taught in the lecture, it can be calculated through them (sum of the sizes of the children + 1).
            """
        
        def fix_height(self):
            """
            Method corrects the height field of self according to its children, as taught in the lecture, 
            it can be calculated through them (the maximum height among the children + 1).
            """
        
        def calc_height(self):
            """
            Method calculates and returns the height field of self according to its children, 
            as taught in the lecture, it can be calculated through them (the maximum height among the children + 1).
            """
        
        def get_balance_factor(self):
            """
            Method returns the balance factor of self.
            """
        
        def is_real_node(self):
            """
            Method returns True if the node is not virtual, and False otherwise.
            """
    
        
        def set_right_with_parent(self, node):
            """
            Method sets node as the right child of self.
            """
    
        
        def set_left_with_parent(self, node):
            """
            Method sets node as the left child of self.
            """
    
        
        def switch_parent(self, node):
            """
            Method sets node as the child of self's parent in place of self.
            """

        
    class AVLTree:
        def __init__(self, root):
            """
            Constructor method that builds an AVL tree with the given root. 
            If the root is virtual or empty, it will be defined as empty.
            """
    
        def search(self, key):
            """
            Search method for the tree self given the key.
            Returns the appropriate node.
            The method starts at the root and moves left or right down the tree 
            based on the order of the keys, stopping when the appropriate node is found.
            The time complexity of this method is O(log n). In the worst case, 
            we search for a key that matches the deepest leaf, traversing the entire height of the tree.
            In any case, in an AVL tree, the tree height is asymptotically bounded by O(log n),
            so this will be the time complexity for search.
            """
    
        def insert(self, key, val):
            """
            Insert method for the tree self. Given a key and value, the method 
            will create an appropriate node with the values and insert it into the tree self,
            maintaining the balance factor and maintained fields.
            The method returns the number of balancing operations required to keep the AVL tree valid.
            The method differentiates between an empty tree, where it sets the node as the root,
            and a non-empty tree, where the node must be inserted based on its key.
            After finding the intended insertion point, the method goes up the chain of ancestors 
            of the node up to the root, updating heights and performing rotations as necessary to keep it balanced.
            A balance operation counter is maintained throughout the process and returned as output.
            The time complexity of this method is O(log n). The method includes finding the insertion point
            (logarithmic in the number of nodes), and if balancing is needed during the ascent, 
            it is done with constant time rotation operations.
            As taught in the lecture and implemented in the code, the total cost of the insertion operation is O(log n).
            """
    
        def rotate(self, criminal):
            """
            Balance operation for the tree. Given a node criminal, performs a series of rotations
            (RL/LR/R/L) based on the balance factor of the criminal and its children as taught in the lecture.
            BF(criminal) == 2 and BF(criminal.left) == -1 then LR rotate
            BF(criminal) == 2 and BF(criminal.left) != -1 then R rotate
            BF(criminal) == -2 and BF(criminal.right) == 1 then RL rotate
            BF(criminal) == -2 and BF(criminal.left) != -1 then L rotate
            The method returns the number of rotations required (1 or 2).
            """
    
        def right_rotate(self, node):
            """
            Right rotation method. Given a node, performs a right rotation by swapping pointers as taught in the lecture.
            Since this method is implemented by pointer swapping, its cost is O(1).
            """
    
        def left_rotate(self, node):
            """
            Left rotation method. Given a node, performs a left rotation by swapping pointers as taught in the lecture.
            Since this method is implemented by pointer swapping, its cost is O(1).
            """
    
        def delete(self, node):
            """
            Delete method for the tree self. Given a node assumed to exist in the tree self, the method deletes it 
            from the tree as in a regular BST using the deletion_regular method, and then performs a series of rotations
            along the path from the deleted node's location to the root to balance the tree and maintain fields if necessary.
            The method returns the number of balancing operations required to maintain a valid AVL tree after deletion.
            The time complexity of this method is O(log n). The method includes deletion as in a BST by the deletion_regular method
            (logarithmic in the number of nodes), and then traverses the path from the deleted node to the root,
            performing constant work (rotations and field updates) in each iteration along the path of asymptotic length O(log n).
            As taught in the lecture and implemented in the code, the total cost of the deletion operation is O(log n).
            """
    
        def successor(self, node):
            """
            Method to return the successor of the node in the tree self, returning None if the node is the maximum node.
            Given that the node has a right subtree, the successor will be the minimum in that subtree.
            If it does not have a right subtree, we ascend the path to the root, continuing as long as the node is the right child of its parent.
            The first time it is the left child of its parent, the parent is the successor of the node.
            If no left child is found for the parent, the node is the maximum, and we return None.
            The time complexity of this method is O(log n) since in the worst case we need to traverse the tree height
            logarithmic in the number of nodes (if the maximum is at depth O(log n) and we want to find its successor).
            """
    
        def regular_deletion(self, node):
            """
            The method accepts a node found in the tree self and deletes it as taught in the lecture for a regular BST.
            If the node was a leaf, simply disconnect it from its parent and create a virtual child for its parent in place of the node.
            We create a separation for the case where the node is a leaf and also the root, setting the tree to None.
            If the node had only a left child, set the parent of the node as the parent of the node's child, 
            and similarly handle the case where the node was the root, setting its child as the new root.
            If the node had only a right child, handle this symmetrically to the left child case.
            If the node had two children, replace it with the successor node by calling the successor method and update 
            the height field of the successor accordingly, since this should not be considered a balancing operation for calculation purposes.
            The time complexity of this method is O(log n), since in the worst case, a call to the successor method is required,
            logarithmic in the number of nodes in the tree.
            """
    
        def avl_to_array(self, node):
            """
            The method avl_to_array is implemented recursively. Its helper method rec_array_to_avl 
            accepts the root of the avl_to_array method and an empty array, checking if the current node is empty or virtual:
            If so, it returns nothing.
            Otherwise, the method calls itself recursively on the left child of the node.
            It appends the key and value of the node to the end of the array.
            After that, a recursive call is made on the right child of the node.
            The avl_to_array method calls rec_array_to_avl and returns an array of key-value pairs sorted in order.
            Since the method traverses each node up to 3 times, the complexity of the function is O(n), where n represents the number of nodes.
            """
    
        def size(self):
            """
            The method returns the number of nodes in the tree self.
            Each node maintains an updated size field (in the Node class), 
            and when we want to get the size of the tree, we ask the root of the tree for its size field.
            Therefore, the cost of the operation is O(1).
            """
    
        def split(self, node):
            """
            The split method is implemented recursively.
            Our stopping condition: the case where the node being split is the root of the tree.
            In this case, return the left subtree of the root and the right subtree of the root.
            For convenience, let's denote:
            x - the node by which we want to perform the split.
            a - the original tree root.
            b - the left child of a.
            Now we divide into two cases:
            1. a < x
            In this case, call split with x and b, then merge the right tree obtained from the split with a and the right subtree of a.
            2. a > x
            Symmetrical case to the first one.
            Note that recursively we descend to x and perform the described operations during the ascent back to the root.
            The number of joins performed is the number of nodes from x to a (the root of the tree), i.e., at most O(log n) joins.
            We discussed in the lecture that the difference between the height of the tree Ti and the height of the tree Ti with 
            the join operations of the previous trees is constant. Hence, the total cost of split is O(log n).
            """
    
        def join(self, tree2, key, val):
            """
            The method accepts another tree2 whose keys are all smaller or larger than all the keys in the tree self,
            as well as a key that lies between them. The method creates a node with the key and value and merges the two trees
            with it into a single tree. The method returns the "cost," defined as the height difference of the trees + 1.
            The operation implements the idea presented in the lecture, where we traverse the taller tree to the left 
            until we encounter a node whose height matches the second tree, merging the trees at this point by changing pointers.
            Then we fix the tree if AVL criminals are encountered to maintain a valid balance factor.
            Consideration is given to cases where one of the trees is empty, equating the operation to inserting a node into a non-empty tree.
            The time complexity of the method is O(log n) since in the worst case, one tree is very tall and the other is very short,
            and we need to traverse O(log n) to reach the intermediary node. After that, we change pointers at constant cost,
            and ascend the tree to look for AVL criminals at logarithmic cost in the number of nodes.
            If criminals are found, we perform a series of constant-cost rotations.
            Overall, the time complexity of join is O(log n).
            """
