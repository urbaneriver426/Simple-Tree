class SimpleTreeNode:
	
	def __init__(self, val, parent):
		self.NodeValue = val 
		self.Parent = parent 
		self.Children = [] 
	
class SimpleTree:

	def __init__(self, root):
		self.Root = root
	
	def AddChild(self, ParentNode, NewChild):
		ParentNode.Children.append(NewChild)
		NewChild.Parent = ParentNode
  
	def DeleteNode(self, NodeToDelete):
		NodeToDelete.Parent.Children.remove(NodeToDelete)
		NodeToDelete.Parent = None 

	def GetAllNodes(self):
		result = []
		curNode = self.Root 
		cont = True 
		level = 1
		depth = {1:0} 
		direction = True 
		if curNode is None:
			return result
		elif len(curNode.Children) == 0:
			result.append(curNode)
			return result
		else:
			result.append(curNode)	
		while cont:
			if direction == True:
				if len(curNode.Children) != 0:
					level += 1
					if (level in depth) is False:
						curNode = curNode.Children[0]
						result.append(curNode)
						depth[level] = 0
					else:
						depth[level] += 1
						curNode = curNode.Children[depth[leve]]
						result.append(curNode)						
				else:
					curNode = curNode.Parent
					direction = False
			else:
				if len(curNode.Children) > depth[level]+1:
					depth[level] += 1
					curNode = curNode.Children[depth[level]]
					result.append(curNode)
					direction = True
				else:
					if curNode is self.Root:
						return result
					else:
						curNode = curNode.Parent
						del depth[level]
						level -= 1	

	def FindNodesByValue(self, val):
		x = self.GetAllNodes()
		result = []
		for node in x:
			if node.NodeValue == val:
				result.append(node)
		return result

	def MoveNode(self, OriginalNode, NewParent):
		OriginalNode.Parent.Children.remove(OriginalNode)
		NewParent.Children.append(OriginalNode)
		OriginalNode.Parent = NewParent
   
	def Count(self):
		return len(self.GetAllNodes())

	def LeafCount(self):
		x = self.GetAllNodes()
		result = 0
		for node in x:
			if len(node.Children) == 0:
				result += 1
		return result


	def EvenTrees(self):
		allNodes = self.GetAllNodes()
		count = len(allNodes)-1
		pool = []
		result = []
		while len(allNodes)>2:
			if len(pool) == 0:
				pool.append(allNodes.pop())
				count -= 1
			else:
				if allNodes[count].Parent is pool[0].Parent:
					pool.append(allNodes.pop())
					count -= 1
				else:
					if len(pool)%2 != 0:
						result.insert(0, pool[0].Parent.Parent)
						result.insert(1, pool[0].Parent)
						allNodes.remove(pool[0].Parent)
						pool = []
						count = len(allNodes)-1
					else:
						pool = []
						count = len(allNodes)-1
		return result
