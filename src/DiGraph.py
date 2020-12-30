from GraphInterface import GraphInterface


class DiGraph(GraphInterface):
    def __init__(self):
        self.V = {}
        self.inE ={}
        self.outE ={}
        self.mc = 0
        self.esize = 0

    def v_size(self):
        return self.V.__sizeof__()

    def e_size(self):
        return self.esize

    def get_mc(self):
        return self.mc

    def add_edge(self, id1, id2, weight):
        pass

    def add_node(self, node_id, pos=None):
        if not(self.V.__contains__(node_id)):
            self.V.update({node_id: pos})
            self.inE.update({node_id: {}})
            self.outE.update({node_id: {}})

    def remove_node(self, node_id):
        pass


    def remove_edge(self, node_id1, node_id2):
        pass

    def get_all_v(self):
       return self.V

    def all_in_edges_of_node(self, id1: int):
        return self.inE.get(id1)

    def all_out_edges_of_node(self, id1: int):
        return self.outE.get(id1)





if __name__ == '__main__':
    d = DiGraph()
    d.add_node(0,(33,423,234))
    print(d.get_all_v())
    print(d.get_all_v())
