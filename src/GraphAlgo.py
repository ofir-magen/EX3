import math
from math import inf
from typing import List
import json
import matplotlib.pyplot as plt
import self as self

from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from src.DiGraph import DiGraph


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, g: GraphInterface = None):
        self.graph = g

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            file = open(file_name, "r")
            jsonn = json.load(file)
            file.close()
            newG = DiGraph()
            # print(jsonn)
            for i in jsonn["Nodes"]:
                if "pos" in i:
                    x = float(i["pos"].split(",")[0])
                    y = float(i["pos"].split(",")[1])
                    z = float(i["pos"].split(",")[2])
                    v = x, y, z
                    newG.add_node(i["id"], v)
                else:
                    newG.add_node(i["id"])

            for j in jsonn["Edges"]:
                newG.add_edge(j["src"], j["dest"], j["w"])

            self.graph = newG
        except Exception as e:
            print(e)
            return False
        return True

    def save_to_json(self, file_name: str) -> bool:

        jsonn = {}
        jsonn.update({"Edges": []})
        jsonn.update({"Nodes": []})
        if self.graph is not None:
            for i in self.graph.get_all_v():
                jsonARGS = {}
                if self.graph.get_all_v()[i] is not None:
                    x = self.graph.get_all_v()[i][0]
                    y = self.graph.get_all_v()[i][1]
                    z = self.graph.get_all_v()[i][2]
                    v = "" + str(x) + "," + str(y) + "," + str(z)
                    jsonARGS.update({"pos": v})
                jsonARGS.update({"id": i})
                jsonn["Nodes"].append(jsonARGS)
            for node in self.graph.get_all_v():
                for dest in self.graph.all_out_edges_of_node(node):
                    jsonARGS = {}
                    jsonARGS.update({"src": node})
                    jsonARGS.update({"w": self.graph.all_out_edges_of_node(node)[dest]})
                    jsonARGS.update({"dest": dest})
                    jsonn["Edges"].append(jsonARGS)
        file = open(file_name, "w")
        # print(file)
        file.write(json.dumps(jsonn))
        file.close()

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        path = []
        if self.graph.get_all_v() is None:
            return -1, path
        if id1 not in self.graph.get_all_v().keys() or id2 not in self.graph.get_all_v().keys():
            return -1, path

        distances = {int: float}
        for v in self.graph.get_all_v().keys():
            distances.update({v: -1})
        q = []
        distances.update({id1: 0})
        q.append(id1)

        while len(q) != 0:
            curr = q.pop(0)
            for i in self.graph.all_out_edges_of_node(curr).keys():
                if distances[i] == -1:
                    distances.update({i: self.graph.all_out_edges_of_node(curr).get(i) + distances.get(curr)})
                    q.append(i)
                elif distances[i] > self.graph.all_out_edges_of_node(curr).get(i) + distances.get(curr):
                    distances.update({i: self.graph.all_out_edges_of_node(curr).get(i) + distances.get(curr)})
                    q.append(i)

        if id1 is id2:
            path.append(id1)
            return 0, path
        if distances[id2] == -1:
            return math.inf, path
        else:

            tmp = id2
            path.append(tmp)

            while distances[tmp] != 0:
                for i in self.graph.all_in_edges_of_node(tmp).keys():
                    if distances[i] + self.graph.all_out_edges_of_node(i)[tmp] == distances[tmp]:
                        path.append(i)
                        tmp = i
                        break
            path.reverse()
        return distances[id2], path

    def connected_component(self, id1: int) -> list:
        l1 = []
        for l in self.connected_components():
            if id1 in l:
                return l
        return l1

    def connected_components(self) -> List[list]:
        if self.graph.get_all_v() is None:
            return []
        theRealSCC = []
        preorder = {}
        lowlink = {}
        scc_found = {}
        scc_queue = []
        i = 0
        for source in self.graph.get_all_v():
            if source not in scc_found:
                queue = [source]
                while queue:
                    v = queue[-1]
                    if v not in preorder:
                        i = i + 1
                        preorder[v] = i
                    done = 1
                    for w in self.graph.all_out_edges_of_node(v):
                        if w not in preorder:
                            queue.append(w)
                            done = 0
                            break
                    if done == 1:
                        lowlink[v] = preorder[v]
                        for w in self.graph.all_out_edges_of_node(v):
                            if w not in scc_found:
                                if preorder[w] > preorder[v]:
                                    lowlink[v] = min([lowlink[v], lowlink[w]])
                                else:
                                    lowlink[v] = min([lowlink[v], preorder[w]])
                        queue.pop()
                        if lowlink[v] == preorder[v]:
                            scc_found[v] = True
                            scc = [v]
                            while scc_queue and preorder[scc_queue[-1]] > preorder[v]:
                                k = scc_queue.pop()
                                scc_found[k] = True
                                scc.append(k)
                            theRealSCC.append(scc)
                        else:
                            scc_queue.append(v)
        return theRealSCC

    def plot_graph(self) -> None:
        for src in self.graph.get_all_v().keys():
            for j in self.graph.all_out_edges_of_node(src).keys():
                listX = []
                listY = []
                if self.graph.get_all_v()[src] is not None and self.graph.get_all_v()[j] is not None:
                    listX.append(self.graph.get_all_v()[src][0])
                    listX.append(self.graph.get_all_v()[j][0])
                    listY.append(self.graph.get_all_v()[src][1])
                    listY.append(self.graph.get_all_v()[j][1])
                    plt.plot(listX, listY, "b>")
                    plt.plot(listX, listY, "r-")

        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.title('Shai Sason Yehuda Aharon #1')
        plt.show()
