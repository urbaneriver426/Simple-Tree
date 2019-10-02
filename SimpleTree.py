class SimpleTreeNode:
	
	def __init__(self, val, parent):
		self.NodeValue = val # значение в узле
		self.Parent = parent # родитель или None для корня
		self.Children = [] # список дочерних узлов
	
class SimpleTree:

	def __init__(self, root):
		self.Root = root; # корень, может быть None
	
	def AddChild(self, ParentNode, NewChild):
		ParentNode.Children.append(NewChild)
		NewChild.Parent = ParentNode
  
	def DeleteNode(self, NodeToDelete):
		NodeToDelete.Parent.Children.remove(NodeToDelete)
		NodeToDelete.Parent = None 

	def GetAllNodes(self):
		result = [] # то, что функция возвращает
		curNode = self.Root # проверяемый узел
		cont = True # условие для продолжение цикла 
		level = 0
		depth = {} # глубина и позиция провенного узла
		direction = True # направление

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
						if len(curNode.Children) == depth[level] + 1:
							direction = False
						else:
							depth[level] += 1
							curNode = curNode.Children[depth[leve]]
							result.append(curNode)						
				else:
					curNode = curNode.Parent
					direction = False
			else:
				if len(curNode.Children) > depth[level] + 1:
					depth[level] += 1
					curNode = curNode.Children[depth[level]]
					result.append(curNode)
					direction = True
				else:
					curNode = curNode.Parent
					if curNode is None:
						cont = False
		return result

	def FindNodesByValue(self, val):
		result = [] # то, что функция возвращает
		curNode = self.Root # проверяемый узел
		cont = True # условие для продолжение цикла 
		level = 0
		depth = {} # глубина и позиция провенного узла
		direction = True # направление

		if curNode is None:
			return result
		elif len(curNode.Children) == 0:
			if curNode.NodeValue == val:
				result.append(curNode)
				return result
		else:
			if curNode.NodeValue == val:
				result.append(curNode)
				return result		
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
						if len(curNode.Children) == depth[level] + 1:
							direction = False
						else:
							depth[level] += 1
							curNode = curNode.Children[depth[leve]]
							if curNode.NodeValue == val:
								result.append(curNode)						
				else:
					curNode = curNode.Parent
					direction = False
			else:
				if len(curNode.Children) > depth[level] + 1:
					depth[level] += 1
					curNode = curNode.Children[depth[level]]
					direction = True
					if curNode.NodeValue == val:
						result.append(curNode)
				else:
					curNode = curNode.Parent
					if curNode is None:
						cont = False
		return result
   
	def MoveNode(self, OriginalNode, NewParent):
		OriginalNode.Parent.Children.remove(OriginalNode)
		NewParent.Children.append(OriginalNode)
		OriginalNode.Parent = NewParent
   
	def Count(self):
		return len(self.GetAllNodes())

	def LeafCount(self):
		result = 0
		curNode = self.Root # проверяемый узел
		cont = True # условие для продолжение цикла 
		level = 0
		depth = {} # глубина и позиция провенного узла
		direction = True # направление

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
						if len(curNode.Children) == depth[level] + 1:
							direction = False
						else:
							depth[level] += 1
							curNode = curNode.Children[depth[leve]]
							result.append(curNode)						
				else:
					curNode = curNode.Parent
					result += 1
					direction = False
			else:
				if len(curNode.Children) > depth[level] + 1:
					depth[level] += 1
					curNode = curNode.Children[depth[level]]
					direction = True
				else:
					curNode = curNode.Parent
					if curNode is None:
						cont = False
		return result
