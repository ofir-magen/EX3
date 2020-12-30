from GraphInterface import GraphInterface


class DiGraph(GraphInterface):
    def __init__(self):
        self.V = {}
        self.inE = {}
        self.outE = {}
        self.mc = 0
        self.esize = 0

    def v_size(self):
        return self.V.__sizeof__()

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
        if not (self.V.__contains__(node_id)):
            self.V.update({node_id: pos})
            self.outE.update({node_id: {}})
            self.inE.update({node_id: {}})

    def remove_node(self, node_id):
        if self.V.__contains__(node_id):
            for i in (self.outE.get(node_id).keys()):
                self.outE[node_id].pop(i)
                self.inE[i].pop(node_id)
                self.mc -= 1
                self.esize -= 1
            self.V.pop(node_id)
            return True
        return False

    def remove_edge(self, node_id1, node_id2):
        if node_id2 in self.outE[node_id1] and (self.V.__contains__(node_id1) and (self.V.__contains__(node_id2))):
            self.outE.get(node_id1).pop(node_id2)
            self.inE.get(node_id2).pop(node_id1)
            self.mc += 1
            self.esize -= 1

    def get_all_v(self):
        return self.V

    def all_in_edges_of_node(self, id1: int):
        return self.inE.get(id1)

    def all_out_edges_of_node(self, id1: int):
        return self.outE.get(id1)


if __name__ == '__main__':
    d = DiGraph()
    d.add_node(0)
    d.add_node(1)
    d.add_node(2)
    d.add_node(3)
    d.add_node(4)
    d.add_node(5)
    d.add_edge(0, 1, 3.5)
    d.add_edge(0, 1, 3.5)
    d.add_edge(0, 2, 4.5)
    d.add_edge(0, 3, 5.5)
    d.add_edge(0, 4, 6.5)
    d.add_edge(0, 5, 7.5)
    d.add_edge(3, 4, 1.7)
    print(d.outE)
    print(d.esize)
#   print(d.outE.get(0))
