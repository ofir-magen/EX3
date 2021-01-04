from typing import List
import queue

from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, g: GraphInterface):
        self.graph = g

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        pass

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        path = []
        if id1 not in self.graph.get_all_v() or id2 not in self.graph.get_all_v():
            return -1, path

        if id1 is id2:
            path.append(id1)
            return 0, path

        distances = {int: float}
        q = []
        distances.update({id1: 0})
        q.append(id1)


        while len(q) != 0:
            curr = q.pop(0)
            for i in self.graph.all_out_edges_of_node(curr).keys():
                if not distances.__contains__(i):
                    distances.update({i: self.graph.all_out_edges_of_node(curr).get(i) + distances.get(curr)})
                    q.append(i)
                elif distances[i] > self.graph.all_out_edges_of_node(curr).get(i) + distances.get(curr):
                    distances.update({i: self.graph.all_out_edges_of_node(curr).get(i) + distances.get(curr)})
                    q.append(i)

        if id2 not in distances:
            return -1, None
        else:

            tmp = id2
            path.append(tmp)

            while distances[tmp] != 0:

                for i in self.graph.all_in_edges_of_node(tmp).keys():
                    if distances[i] + self.graph.all_out_edges_of_node(i)[tmp] == distances[tmp]:
                        path.append(i)
                        tmp = i
            path.reverse()
        return distances[id2], path

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        pass



