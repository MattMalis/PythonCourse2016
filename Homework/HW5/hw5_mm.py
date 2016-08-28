class ListNode():
	def __init__ (self, value, next = None):
		self.value = value
		self.next = next
	def __str__ (self):
		return str(self.value)
	def __repr__ (self):
		return str(self.value)
	def __eq__ (self, other):
		return self.value==other.value and self.next.value==other.next.value
		## could check self.next==other.next, but then you'd need to describe 
		## 		the entire linked list in order to check for equality...
	def __ne__ (self, other):
		return self.value!=other.value or self.next!=other.next

## addNode, addNodeAfter, addNodeBefore, removeNode, removeNodesByValue, and reverse 
## 		all take linear time (where n is the length of the list)
## 	can't be done any faster unless the list has a tail or is doubly-linked
class LinkedList():
	def __init__(self, head):
		self.head = head
	def length(self):
		cur = self.head
		count = 1
		while cur.next is not None:
			cur = cur.next
			count += 1
		return count
	def addNode(self, new_value):
		new_node = ListNode(new_value)
		cur = self.head
		while cur.next is not None:
			cur = cur.next
		cur.next = new_node
	def addNodeAfter(self, new_value, after_node):
		## note: because of __eq__ override above, value for after_node
		## 		only needs to include its own value and next's value 
		##		(next.next can be None)
		new_node = ListNode(new_value)
		cur = self.head
		while cur!=after_node  and cur.next is not None:
			cur = cur.next
		new_node.next = cur.next
		cur.next = new_node
	def addNodeBefore(self, new_value, before_node):
		## see note in addNodeAfter
		new_node = ListNode(new_value)
		cur = self.head
		while cur.next!=before_node and cur.next is not None:
			cur = cur.next
		new_node.next = cur.next
		cur.next = new_node
	def removeNode(self, node_to_remove):
		## see note in addNodeAfter
		cur = self.head
		while cur.next!=node_to_remove:
			if cur.next is None:
				print "node_to_remove not found"
				return
			cur = cur.next
		if cur.next.next is None:
			cur.next = None
		else:
			cur.next = cur.next.next
	def removeNodesByValue(self, value):
		cur = self.head
		while cur.next is not None:
			if cur.next.value==value:
				cur.next = cur.next.next
			else:
				cur = cur.next
	def reverse(self):
		reversed = None
		cur = self.head
		while cur is not None:
			nxt = cur.next
			cur.next = reversed
			reversed = cur
			cur = nxt
		head.head = reversed
	def __str__(self):
		cur = self.head
		while cur is not None:
			print cur.value
			cur = cur.next
	def __repr__(self):
		nodes = []
		cur = self.head
		while cur is not None:
			nodes.append(cur.value)
			cur = cur.next
		return str(nodes)
		


	
	
ll = LinkedList(ListNode(10))
ll.addNode(20)
ll.addNode(30)
ll.addNode(40)
ll.addNodeBefore(35, ListNode(40))
ll.addNodeAfter(20, ListNode(40))
ll.removeNodesByValue(20)