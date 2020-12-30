from GraphInterface import GraphInterface


class DiGraph(GraphInterface):
    def __init__(self):
        self.V = {}
        self.inE ={}
        self.outE ={}



    def v_size(self):
        pass

    def e_size(self):
        pass

    def get_mc(self):
        pass

    def add_edge(self, id1, id2, weight):
        pass

    def add_node(self, node_id, pos=None):
        self.V.update({node_id: pos})
        print(self.V)
    def remove_node(self, node_id):
        pass

    def remove_edge(self, node_id1, node_id2):
        pass
    def getV(self) -> dict :
        print(self.V)


if __name__ == '__main__':
        d = DiGraph

