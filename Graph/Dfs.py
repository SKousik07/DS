
class Graph:
    def __init__(self,nodes,is_direct=False):
        self.nodes=nodes
        self.adj_list={}
        self.is_direct=is_direct
        for node in self.nodes:
            self.adj_list[node]=[]
            
    def addedge(self,u,v):
        self.adj_list[u].append(v)
        if self.is_direct==False:
            self.adj_list[v].append(u)

    def Dfs(self,visited={},traversal=[],q=[],s="A"):
        for u in self.adj_list:
            visited[u]=0
    
            
        visited[s]=1
        q.append(s)
        while len(q)>0:
            u=q.pop()
            traversal.append(u)
            for v in self.adj_list[u]:
                if visited[v]==0:
                    visited[v]=1
                    q.append(v)
        print("Dfs Traversal ->"+str(traversal))
        """
        v=input("enter the node to find path : ")
        path=[]
        while v!= None:
            path.append(v)
            v=parent[v]
        print("->".join(path[::-1])) 
        
        print("printing longest path")
        d={k:v for k,v in level.items() if v==max(level.values()) }
        for p in d:
            path=[]
            while p!= None:
                path.append(p)
                p=parent[p]
            print("->".join(path[::-1]))
            """
        
            
  #these can be implemented without class also          
        
            

alledges=[("A","B"),("A","D"),("B","C"),("C","D"),("D","E"),("D","F"),("E","G"),("F","H"),("G","H")]
nodes=["A","B","C","D","E","F","G","H"]
g=Graph(nodes)
for (u,v) in alledges:
    g.addedge(u,v)
g.Dfs(s="A")

                
