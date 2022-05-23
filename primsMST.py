import sys

class Graph():
    def __init__(self,vertices):
        self.v=vertices
        self.graph=[[0 for column in range(vertices)]
                    for row in range(vertices)] 
        
    def printMST(self,parent):
        print("Edge \tWeight")
        for i in range(self.v):
            print(parent[i],'-',i,'\t',self.graph[i][parent[i]])

    def minKey(self,key,mstSet):
        min=100
        for i in range(self.v):
            if key[i]<min and mstSet[i]==False:
                min=key[i]
                min_index=i

        return min_index


    def primMST(self):
        key=[10]* self.v
        parent=[None] * self.v
        key[0]=0
        mstSet=[False]*self.v

        parent[0]=-1

        for count in range(self.v):
            u=self.minKey(key,mstSet)
            mstSet[u]=True

            for x in range(self.v):
                if self.graph[u][x] >0 and mstSet[x]==False:
                    key[x]=self.graph[u][x]
                    parent[x]=u

        self.printMST(parent)


g=Graph(5)
g.graph=[[0,2,0,6,0],
        [2,0,3,8,5],
        [0,3,0,0,7],
        [6,8,0,0,9],
        [0,5,7,9,0]]

g.primMST()


