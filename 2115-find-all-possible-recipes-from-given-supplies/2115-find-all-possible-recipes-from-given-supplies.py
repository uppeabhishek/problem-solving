class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def getGraph(self):
        return self.graph
    
    def topological_sort_helper(self, key, visited, order):
        
        visited.add(key)
        
        for k in self.graph[key]:
            if k not in visited:
                self.topological_sort_helper(k, visited, order)
        
        order.append(key)
        
    def topological_sort(self):
        visited = set()
        order = []
        for key in self.graph.keys():
            if key not in visited:
                self.topological_sort_helper(key, visited, order)
        return order
        
    
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        
        g = Graph()
        
        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                g.addEdge(recipe, ingredient)
                if ingredient not in g.getGraph():
                    g.getGraph()[ingredient] = []
            

        order = g.topological_sort()
        
        result = []
        
        recipesDict = defaultdict(int)
        
        for i, recipe in enumerate(recipes):
            recipesDict[recipe] = i
        
        currentSupplies = set(supplies)
        result = []
                
        for orderItem in order:
            
            if orderItem in recipesDict:
                ingredient = ingredients[recipesDict[orderItem]]
                
                all_present = True
                
                for i in ingredient:
                    if i not in currentSupplies:
                        all_present = False
                        break
                         
                if all_present:
                    currentSupplies.add(orderItem)
                    result.append(orderItem)
            
        return result
        