from GraphInterface import GraphInterface


class DiGraph(GraphInterface):
    def __init__(self):
        self.V = {}
        self.inE = {}
        self.outE = {}
        self.mc = 0
        self.esize = 0

    def v_size(self):
        return len(self.V)

    def e_size(self):
        return self.esize

    def get_mc(self):
        return self.mc

    def add_edge(self, id1, id2, weight):
        if id1 in self.V and id2 in self.V:
            if id2 not in self.outE.get(id1) and id1 not in self.inE.get(id2):
                self.outE[id1].update({id2: weight})
                self.inE[id2].update({id1: weight})
                self.mc += 1
                self.esize += 1
            return True
        return False

    def add_node(self, node_id, pos=None):
        if not (node_id in self.V):
            self.V.update({node_id: pos})
            self.outE.update({node_id: {}})
            self.inE.update({node_id: {}})
            self.mc += 1

    def remove_node(self, node_id):
        if node_id in self.V:
            for i in (self.outE.get(node_id).keys()):
                self.inE[i].pop(node_id)
                self.esize -= 1
            for j in (self.inE.get(node_id).keys()):
                self.outE[j].pop(node_id)
                self.esize -= 1
            self.V.pop(node_id)
            self.inE.pop(node_id)
            self.outE.pop(node_id)
            self.mc += 1
            return True
        return False

    def remove_edge(self, node_id1, node_id2):
        if (node_id2 in self.V) and (node_id1 in self.V):
            if node_id2 in self.outE[node_id1] and node_id1 in self.inE[node_id2]:
                self.outE.get(node_id1).pop(node_id2)
                self.inE.get(node_id2).pop(node_id1)
                self.mc += 1
                self.esize -= 1
                return True
        return False

    def get_all_v(self):
        return self.V

    def all_in_edges_of_node(self, id1: int):
        return self.inE.get(id1)

    def all_out_edges_of_node(self, id1: int):
        return self.outE.get(id1)



