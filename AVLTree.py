
"""A class represnting a node in an AVL tree"""

from re import search

class AVLNode(object):

	"""Constructor, you are allowed to add more fields.

	@type key: int or None
	@type value: any
	@param value: data of your node
	"""
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
		self.size = 0



	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child (if self is virtual)
	"""
	def get_left(self):
		return self.left



	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child (if self is virtual)
	"""
	def get_right(self):
		return self.right



	"""returns the parent

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def get_parent(self):
		return self.parent



	"""returns the key

	@rtype: int or None
	@returns: the key of self, None if the node is virtual
	"""
	def get_key(self):
		return self.key



	"""returns the value

	@rtype: any
	@returns: the value of self, None if the node is virtual
	"""
	def get_value(self):
		return self.value



	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def get_height(self):
		return self.height



	"""returns the size

	@rtype: int
	@returns: the size of self, 0 if the node is virtual
	"""
	def get_size(self):
		return self.size



	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def set_left(self, node):
		self.left = node



	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def set_right(self, node):
		self.right = node



	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def set_parent(self, node):
		self.parent = node



	"""sets key

	@type key: int or None
	@param key: key
	"""
	def set_key(self, key):
		self.key = key
		return None



	"""sets value

	@type value: any
	@param value: data
	"""
	def set_value(self, value):
		self.value = value
		return None



	"""sets the height of the node

	@type h: int
	@param h: the height
	"""
	def set_height(self, h):
		self.height = h
		return None



	"""sets size

	@type newsize: int
	@param newsize: the new size
	"""
	def set_size(self, newsize):
		self.size = newsize
		return None



	""""Adjusting the size according to the children
	"""
	def fix_size(self):
		self.set_size(self.right.size + self.left.size + 1)



	"""calculating the size according to the children

	@rtype: int
	@returns: the size of self, 0 if the node is virtual
	"""
	def calc_size(self):
		return self.right.size + self.left.size + 1



	""""Adjusting the height according to the children
	"""
	def fix_height(self):
		self.set_height(max(self.left.height , self.right.height) + 1)



	"""calculating the height according to the children

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def calc_height(self):
		if self.left is None and self.right is None: return -1
		return max(self.left.height , self.right.height) + 1



	"""returns the balance factor

	@rtype: int
	@returns: the balance factor of self
	"""
	def get_balance_factor(self):
		return self.left.height - self.right.height



	"""returns whether self is not a virtual node

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		if self.key is None: return False
		return True



	"""Sets node as the right child of self

	@type node: AVLNode
	@param node: a node
	"""
	def set_right_with_parent(self, node):
		self.right = node
		node.set_parent(self)



	"""Sets node as the left child of self

	@type node: AVLNode
	@param node: a node
	"""
	def set_left_with_parent(self, node):
		self.left = node
		node.set_parent(self)



	"""sets node as the child of self's father instead of self

	@type node: AVLNode
	@param node: a node
	"""
	def switch_parent(self, node):
		if self.parent is not None and self.key is not None:
			if self.parent.get_key() > self.key: self.parent.set_left_with_parent(node)
			else: self.parent.set_right_with_parent(node)
			self.parent = None



class AVLTree(object):

	"""
	Constructor, you are allowed to add more fields.

	"""
	def __init__(self, root: AVLNode = None):
		self.root = root
		if (self.root is not None) and (not self.root.is_real_node()):
			self.root = None
		if self.root is not None:
			self.root.parent = None



	"""searches for a AVLNode in the dictionary corresponding to the key

	@type key: int
	@param key: a key to be searched
	@rtype: AVLNode
	@returns: the AVLNode corresponding to key or None if key is not found.
	"""
	# time complexity O(log(n))

	def search(self, key):
		node = self.root
		while (node is not None) and (node.get_key() is not None):
			if node.get_key() == key: return node
			if node.get_key() < key: node = node.get_right()
			else: node = node.get_left()
		return None



	"""inserts val at position i in the dictionary

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: any
	@param val: the value of the item
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	# time complexity O(log(n))

	def insert(self, key, val):
		rebalancingOPs=0 #Counting the number of rebalancing operations
		if self.root == None: #An empty tree
			self.root = AVLNode(key,val)
			self.root.set_right_with_parent(AVLNode(None, None))
			self.root.set_left_with_parent(AVLNode(None, None))
			self.root.set_size(1)
			self.root.set_height(0)
			return 0 #no rebalancing operations

		else: #self is not an empty tree
			node = self.root
			while node.is_real_node(): #Navigating to the insertion location, Incrementing the sizes on the way
				if node.get_key() > key:
					node = node.get_left()
				else:
					node = node.get_right()
			node.set_key(key)
			node.set_value(val)
			node.set_height(0)
			node.set_size(1)
			node.set_right_with_parent(AVLNode(None, None))
			node.set_left_with_parent(AVLNode(None, None))
			y = node.get_parent()
			while y is not None: #Performing rotations if necessary
				BF = y.get_balance_factor()
				if BF >= -1 and BF <= 1: #valid balance factor
					if y.get_height() != y.calc_height(): #height has changed
						y.fix_height()
						y.fix_size()
						y = y.get_parent()
						rebalancingOPs += 1 #changing the height is defined as a rebalancing operation
					else: #height has not changed
						y.fix_size()
						y = y.get_parent()
				else: #Invalid balance factor - rotations are needed
					rebalancingOPs += self.rotate(y)
		return rebalancingOPs



	"""rotating the tree around the criminal, return the number of rotations

	@type node: AVLNode
	@pre: criminal is a real pointer to a node in self
	@rtype: int
	@returns: the number of rotations
	"""
	# time complexity O(1)

	def rotate(self, criminal):
		if criminal.get_balance_factor() ==2: #right-heavy
			if criminal.get_left().get_balance_factor() == -1: #Left Right rotations
				self.LeftRotate(criminal.get_left())
				self.RightRotate(criminal)
				rotates = 2
			else:
				self.RightRotate(criminal) #Right rotation
				rotates = 1
		else: #left-heavy
			if criminal.get_right().get_balance_factor() == 1: #Right Left rotations
				self.RightRotate(criminal.get_right())
				self.LeftRotate(criminal)
				rotates = 2
			else:
				self.LeftRotate(criminal) #Left Rotation
				rotates = 1
		return rotates #number of rotations



	""" rotating around node to the right

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	"""
	# time complexity O(1)

	def RightRotate(self, node):
		temp = node.get_left() #the new root of the subtree of node
		#fixing the parent
		if node.get_parent() is not None:
			key = node.get_key()
			if key > node.get_parent().get_key():
				node.get_parent().set_right_with_parent(temp)
			else:
				node.get_parent().set_left_with_parent(temp)
		else: #node was the root
			self.root = temp
			temp.set_parent(None)
		#setting pointers and attribute
		node.set_left_with_parent(temp.get_right())
		temp.set_right_with_parent(node)
		node.set_size(node.calc_size())
		temp.set_size(temp.calc_size())
		node.set_height(node.calc_height())
		temp.set_height(temp.calc_height())



	""" rotating around node to the left

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	"""
	# time complexity O(1)

	def LeftRotate(self, node):
		temp = node.get_right()  #the new root of the subtree of node
		#fixing the parent
		if node.get_parent() is not None:
			key = node.get_key()
			if key > node.get_parent().get_key():
				node.get_parent().set_right_with_parent(temp)
			else:
				node.get_parent().set_left_with_parent(temp)
		else: #node was the root
			self.root = temp
			temp.set_parent(None)
		#setting pointers and attribute
		node.set_right_with_parent(temp.get_left())
		temp.set_left_with_parent(node)
		node.set_size(node.calc_size())
		temp.set_size(temp.calc_size())
		node.set_height(node.calc_height())
		temp.set_height(temp.calc_height())



	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	# time complexity O(log(n))

	def delete(self, node):
		rebalancingOPs = 0 #Counting the number of rebalancing operations
		parent = self.regular_deletion(node) # Delete node from self as in a regular BST ; 'parent' refers to the node's parent
		temp = parent
		while temp is not None: #Performing rotations if necessary
			BF = temp.get_balance_factor()
			if BF >= -1 and BF <= 1: #valid balance factor
				if temp.calc_height() != temp.get_height(): #height has changed
					temp.set_height(temp.calc_height())
					temp.set_size(temp.calc_size())
					temp = temp.get_parent()
					rebalancingOPs += 1 #changing the height is defined as a rebalancing operation
				else: #height has not changed
					temp.set_size(temp.calc_size())
					temp = temp.get_parent()
			else: #Invalid balance factor - rotations are needed
				rebalancingOPs += self.rotate(temp)
				temp = temp.get_parent()
		return rebalancingOPs



	"""return the successor of node

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: AVLNode
	@returns: the successor of node, None if node has the max key
	"""
	# time complexity O(log(n))

	def successor(self,node):
		if node.get_right().get_key() is not None:
			temp = node.get_right()
			while temp.get_left().get_key() is not None:
				temp = temp.get_left()
			return temp
		else:
			temp = node
			while temp.get_parent is not None and temp.get_parent.get_right() is temp:
				temp = temp.get_parent
			return temp



	"""delete node from self as in regular BST and return its parent

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: AVLNode
	@returns: the parent of the deleted node, if node was the root return None
	"""
	# time complexity O(log(n))

	def regular_deletion(self,node):

		if node.get_left().get_key() is None and node.get_right().get_key() is None: #node is a leaf
				parent = node.get_parent()
				if parent is None: #node was the root
					self.root = None
				node.switch_parent(AVLNode(None, None))
				node.get_left().set_parent(None)
				node.get_right().set_parent(None)
				node.set_right(None)
				node.set_left(None)
				return parent
		elif node.get_left().get_key() is not None and node.get_right().get_key() is None: #node has only a left child
			y = node.get_parent()
			if y is None: #node was the root
				self.root = node.get_left()
				node.get_left().set_parent(None)
			else: node.switch_parent(node.get_left()) #connectiong node's father and node's left son
			node.get_right().set_parent(None)
			node.set_right(None)
			node.set_left(None)
			return y
		elif node.get_left().get_key() is None and node.get_right().get_key() is not None: #node has only a right child
			y = node.get_parent()
			if y is None: #node was the root
				self.root = node.get_right()
				node.get_right().set_parent(None)
			else: node.switch_parent(node.get_right()) #connectiong node's father and node's right son
			node.get_left().set_parent(None)
			node.set_right(None)
			node.set_left(None)
			return y
		else: #node has two children
			z = self.successor(node) #searching node's successor, z won't be null because node has a right child
			if z.get_parent() is not node: # node's successor is not its right child
				z_parent = z.get_parent()
			else: z_parent = z # node's successor is its right child
			z.switch_parent(z.get_right())
			if node == self.root: #node was the root
				self.root = z
			else: node.switch_parent(z)
			z.set_right_with_parent(node.get_right())
			z.set_left_with_parent(node.get_left())
			z.set_height(z.calc_height())
			node.set_left(None)
			node.set_right(None)
			node.set_parent(None)
			return z_parent



	"""returns an array representing dictionary

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	# time complexity O(n)

	def avl_to_array(self):
		#recursive helper
		def avl_to_array_rec(node : 'AVLNode', array):
			if node is None or not node.is_real_node():
				return
			avl_to_array_rec(node.get_left(), array)
			array.append((node.get_key(), node.get_value()))
			avl_to_array_rec(node.get_right(), array)

		array = []
		avl_to_array_rec(self.get_root(), array)
		return array



	"""returns the number of items in dictionary

	@rtype: int
	@returns: the number of items in dictionary
	"""
	# time complexity O(1()

	def size(self):
		if self.root == None: return 0
		return self.root.get_size()



	"""splits the dictionary at the i'th index

	@type node: AVLNode
	@pre: node is in self
	@param node: The intended node in the dictionary according to whom we split
	@rtype: list
	@returns: a list [left, right], where left is an AVLTree representing the keys in the
	dictionary smaller than node.key, right is an AVLTree representing the keys in the
	dictionary larger than node.key.
	"""
	# time complexity O(log(n))

	def split(self, node: AVLNode):
		if node.key == self.root.key:
			left = AVLTree(self.root.left)
			right = AVLTree(self.root.right)
			return [left, right]

		# node.key < self.root.key:
		if node.key < self.root.key:
			my_right = AVLTree(self.root.right)
			my_left = AVLTree(self.root.left)

			left, right = my_left.split(node)
			right.join(my_right, self.root.key, self.root.value)
			return [left, right]

		# node.key > self.root.key:
		my_left = AVLTree(self.root.left)
		my_right = AVLTree(self.root.right)

		left, right = my_right.split(node)
		left.join(my_left, self.root.key, self.root.value)
		return [left, right]



	"""joins self with key and another AVLTree

	@type tree2: AVLTree
	@param tree2: a dictionary to be joined with self
	@type key: int
	@param key: The key separting self with tree2
	@type val: any
	@param val: The value attached to key
	@pre: all keys in self are smaller than key and all keys in tree2 are larger than key
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined + 1
	"""
	# time complexity O(|h1-h2|)

	def join(self, tree2, key, val):
			if self.root is None or self.root.get_key() is None: # the smaller keys tree (self) is an empty tree
				tree2.insert(key, val)
				self.root = tree2.root
				return self.root.get_height() + 1
			if tree2.root is None or tree2.root.get_key() is None: # the higher keys tree (tree2) is an empty tree
				self.insert(key, val)
				return self.root.get_height() + 1
			if self.root.get_key() < key: # if the keys in self are smaller than the keys in tree2
				h1 = self.root.get_height()
				h2 = tree2.root.get_height()
				mid_node = AVLNode(key, val)
				if h1 <= h2: # tree2 is taller than or equal in height to self
					b = tree2.get_root()
					while b.get_height() > h1: #going to node b in tree2 which is a root of h1 height subtree
						b = b.get_left()
					c = b.get_parent()
					# Insertion of mid_node that connects the trees
					mid_node.set_left_with_parent(self.get_root())
					mid_node.set_right_with_parent(b)
					mid_node.set_size(mid_node.calc_size())
					mid_node.set_height(mid_node.calc_height())
					if c is not None: # is crucial as they may be equal
						c.set_left_with_parent(mid_node)
					self.root = tree2.get_root()
				else:  #self is higher than tree2
					a = self.get_root()
					while a.get_height() > h2: #going to node a in self which is a root of h2 height subtree
						a = a.get_right()
					c = a.get_parent()
					# Insertion of mid_node that connects the trees
					mid_node.set_left_with_parent(a)
					mid_node.set_right_with_parent(tree2.get_root())
					mid_node.set_size(mid_node.calc_size())
					mid_node.set_height(mid_node.calc_height())
					c.set_right_with_parent(mid_node)

				while self.root.get_parent() is not None: # assigning the root as the true root
					self.root = self.root.get_parent()
				while mid_node is not None:  #searching for AVL criminals
					# same algorithm of rotations as in delete
					bf = mid_node.get_balance_factor()
					if abs(bf) < 2 and mid_node.calc_height() != mid_node.get_height(): #valid balance factor and height has changed
						mid_node.set_height(mid_node.calc_height())
						mid_node.set_size(mid_node.calc_size())
						mid_node = mid_node.get_parent()
					elif abs(bf) < 2 and mid_node.calc_height() == mid_node.get_height(): #valid balance factor and height has not changed
						mid_node.set_size(mid_node.calc_size())
						mid_node = mid_node.get_parent()
					else:  #Invalid balance factor
						self.rotate(mid_node)
						mid_node = mid_node.get_parent()
				return abs(h1 - h2) + 1
			else: # if the keys in self are bigger than the keys in tree2
				difference = tree2.join(self, key, val)   # calling to join again, with switched parameters
				self.root = tree2.get_root()  # making self point at tree2 (because the joining was applied on tree)
				return difference



	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	#time comlexity O(1)

	def get_root(self):
			return self.root




