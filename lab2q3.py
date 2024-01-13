from enum import Enum

class labels(Enum):
    A=0
    B=1
    C=2
    D=3
    E=4



class Graph():
    def __init__(self,num_nodes):
        self.mat=[]
        self.num_nodes=num_nodes


    def createMat(self):
        for i in range(self.num_nodes):
            l1=[]
            for j in range(self.num_nodes):
                l1.append(0)
            self.mat.append(l1)

        

    def printMat(self):
        print(self.mat)
        # for i in range(len(self.mat)):
        #     for j in range(len(self.mat[i])):
        #         print(self.mat[i][j],end=" ")
        #     print("\n")

    def insert_directions(self):
        n1=input("node 1 ")
        n2=input("node 2 ")

        self.mat[labels[n1].value][labels[n2].value]=1
        self.mat[labels[n1].value][labels[n2].value]=1


num_nodes=int(input("enter number of nodes "))

g1=Graph(num_nodes)
g1.createMat()

while True:
    g1.insert_directions()
    
    ch=input("continue? ")
    if(ch!='y' and ch!='Y'):
        break

print("Adjaceny List",end="\n")
d={}
for i in range(num_nodes):
    d[labels(i).value]=[]
    for j in range(num_nodes):
        if(g1.mat[i][j]==1):
            d[labels(i).name].append(labels(j).name)

print(d)

 
