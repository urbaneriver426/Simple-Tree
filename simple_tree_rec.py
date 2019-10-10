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

	def GetAllNodes(self,result = [], count = 0):
		if count == 0:
			if self.Root is not None:
				result.append(self.Root)
			else:
				return result
		for i in range(len(result[count].Children)):
			result.append(result[count].Children[i])
		count += 1
		if count < len(result):
			return self.GetAllNodes(result, count)
		else:	
			return result		

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
