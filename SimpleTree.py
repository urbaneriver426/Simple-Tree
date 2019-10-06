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
		result = []
		curNode = self.Root 
		cont = True 
		level = 1
		depth = {1:0} 
		direction = True 
		if curNode is None:
			return result
		elif len(curNode.Children) == 0:
			if curNode.NodeValue == val:
				result.append(curNode)
			return result
		else:
			if curNode.NodeValue == val:
				result.append(curNode)	
		while cont:
			if direction == True:
				if len(curNode.Children) != 0:
					level += 1
					if (level in depth) is False:
						curNode = curNode.Children[0]
						depth[level] = 0
						if curNode.NodeValue == val:
							result.append(curNode)
					else:
						depth[level] += 1
						curNode = curNode.Children[depth[leve]]
						if curNode.NodeValue == val:
							result.append(curNode)						
				else:
					curNode = curNode.Parent
					direction = False
			else:
				if len(curNode.Children) > depth[level]+1:
					depth[level] += 1
					curNode = curNode.Children[depth[level]]
					direction = True
					if curNode.NodeValue == val:
						result.append(curNode)
				else:
					if curNode is self.Root:
						return result
					else:
						curNode = curNode.Parent
						del depth[level]
						level -= 1

	def MoveNode(self, OriginalNode, NewParent):
		OriginalNode.Parent.Children.remove(OriginalNode)
		NewParent.Children.append(OriginalNode)
		OriginalNode.Parent = NewParent
   
	def Count(self):
		return len(self.GetAllNodes())

	def LeafCount(self):
		result = 0
		curNode = self.Root 
		cont = True 
		level = 1
		depth = {1:0} 
		direction = True 
		if curNode is None:
			return result
		elif len(curNode.Children) == 0:
			result += 1
			return result
		while cont:
			if direction == True:
				if len(curNode.Children) != 0:
					level += 1
					if (level in depth) is False:
						curNode = curNode.Children[0]
						depth[level] = 0
					else:
						depth[level] += 1
						curNode = curNode.Children[depth[leve]]						
				else:
					result += 1
					curNode = curNode.Parent
					direction = False
			else:
				if len(curNode.Children) > depth[level]+1:
					depth[level] += 1
					curNode = curNode.Children[depth[level]]
					direction = True
				else:
					if curNode is self.Root:
						return result
					else:
						curNode = curNode.Parent
						del depth[level]
						level -= 1
