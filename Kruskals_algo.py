class UnionFind:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=list(n*[0])

    def find(self,u):
        if self.parent[u]!=u:
            self.parent[u]=self.find(self.parent[u])
        return self.parent[u]
        
    def union(self,u,v):

        pu,pv=self.find(u),self.find(v)

        if pu==pv:
            return False
        
        if self.rank[pu]>self.rank[pv]:
            self.parent[pv]=pu

        elif self.rank[pv]>self.rank[pu]:
            self.parent[pu]=pv

        else:
            self.parent[pv]=pu
            self.rank[pu]+=1

        return True


def Kruskals(n,edges):
    edges.sort()

    uf=UnionFind(n)

    mst_weight=0
    mst_edges=[]

    for w,u,v in edges:
        if uf.union(u,v):
            mst_weight+=w
            mst_edges.append((w,u,v))
        
    return  mst_weight,mst_edges


n = 4
edges = [
    (1, 0, 1),
    (4, 0, 2),
    (3, 1, 2),
    (2, 2, 3),
    (5, 1, 3)
]

total_weight, mst_edges = Kruskals(n, edges)
print("MST Weight:", total_weight)
print("MST Edges:", mst_edges)

