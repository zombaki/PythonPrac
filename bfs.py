class Node:
     def __init__(self):
         self.next = None
         self.left = None
         self.right = None
def bfs(root):
	if (root is None):
		return
	root.next=bfs(root.left)
	if (root.next is None):
		root.next=bfs(root.right)
	else:
		root.next.next=bfs(root.right)
	return root
