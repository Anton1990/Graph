class Graph:
    
    graph_dict={}
    
    def addEdge(self,node,neighbour):  
        if node not in self.graph_dict:
            self.graph_dict[node]=[neighbour]
        else:
            self.graph_dict[node].append(neighbour)
        
    def show_edges(self):
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                print("(",node,", ",neighbour,")")
                
    def find_path(self,start,end,path=[]):
        
        path = path + [start]
        
        print(path)
        if start==end:
            return path
        for node in self.graph_dict[start]:
            if node not in path and node in self.graph_dict:
                newPath=self.find_path(node,end,path)
                if newPath:
                    return newPath
            elif node not in self.graph_dict:pass
            else: return -1
    def BFS(self,s):
        visited={}
        for i in self.graph_dict:
            visited[i]=False
        queue=[]
        queue.append(s)
        visited[s]=True
        while len(queue)!=0:
            s=queue.pop(0)
            for node in self.graph_dict[s]:
                if visited[node]!=True:
                    visited[node]=True
                    queue.append(node)
            print(s,end=" ")
            

g= Graph()
g.addEdge('12', '13')
g.addEdge('13', '1')
g.addEdge('1', '2')
g.addEdge('2', '12')
g.addEdge('2', '3')

g.addEdge('3', '12')


g.addEdge('4', '2')

#g.show_edges()
#print(g.find_path('4', '11'))
g.BFS('1')
