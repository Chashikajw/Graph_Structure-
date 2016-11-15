class GraphUndirected:
    def __init__(self):
        self.vertex_dict = {}
        self.num_vertex = 0
        
        

    def add_vertex(self, data):
        self.num_vertex = self.num_vertex + 1
        self.vertex_dict.setdefault(data, {})

    def add_edges(self, frm,to,weight):
        if frm not in self.vertex_dict:
            self.add_vertex(frm)
        if to not in self.vertex_dict:
            self.add_vertex(to)

        self.vertex_dict[frm][to] = weight
        self.vertex_dict[to][frm] = weight

    def delete_vertex(self, data):
        if data in self.vertex_dict:
            del self.vertex_dict[data]
        for i in self.vertex_dict.keys():
            for j in self.vertex_dict[i].keys():
                if j== data:
                    del self.vertex_dict[i][j]
                    break

    def show_vertex(self):
        return self.vertex_dict.keys()

    def findAll_path(self, start , end,path =[] ):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.vertex_dict:
            return []
        paths =[]
        for node in self.vertex_dict[start]:
            if node not in path:
                newpaths = self.findAll_path(node,end,path)
                for newpath in newpaths:
                    paths.append(newpath)
        
        return paths

    def find_lengths(self, start , end, lengths =[] ):
        paths = self.findAll_path(start , end,path =[] )
        for i in range(len(paths)):
            lengths.append(len(paths[i])-1)
        return lengths

    def shortest_path(self,start, end, weights=[]):
        paths = self.findAll_path(start , end,path =[] )
        
        for i in range(len(paths)):
            tot = 0
            for j in range(len(paths[i])-1):
                tot = tot + self.vertex_dict[paths[i][j]][paths[i][j+1]]
            weights.append(tot)
                
        ind = weights.index(min(weights))
        return paths[ind],min(weights)

        

a= GraphUndirected()
a.add_edges("V1", "V2",200)
a.add_edges("V1", "V6",300)
a.add_edges("V2", "V6",100)
a.add_edges("V5", "V6",50)
a.add_edges("V3", "V6",150)
a.add_edges("V4", "V6",75)
a.delete_vertex("V3")




print(a.findAll_path("V5", "V2", path=[]))
print(a.find_lengths( "V5" ,"V2", lengths =[]))
print(a.shortest_path("V5","V2", weights =[]))
