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

    def printlist(self):
        for u in self.adj_list:
            print(u +"->"+str(self.adj_list[u]))

    def degree(self,node):
        print("degree of "+str(node)+" is "+ str(len(self.adj_list[node])))
            

alledges=[("A","B"),("A","D"),("B","C"),("C","D"),("D","E"),("D","F"),("E","G"),("F","H"),("G","H")]
nodes=["A","B","C","D","E","F","G","H"]
g=Graph(nodes)
for (u,v) in alledges:
    g.addedge(u,v)
g.printlist()
g.degree("D")


                                                             

                                                             


                                                             

        
