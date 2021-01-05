from typing import List
import json
import matplotlib.pyplot as plt

from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from src.DiGraph import DiGraph


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, g: GraphInterface):
        self.graph = g

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        file = open(file_name, "r")
        jsonn = json.load(file)
        file.close()
        newG = DiGraph()
        print(jsonn)
        for i in jsonn["Nodes"]:
            newG.add_node(i["id"], tuple(i["pos"]))
        for j in jsonn["Edges"]:
            newG.add_edge(j["src"], j["dest"], j["w"])

        self.graph = newG
        return True

    def save_to_json(self, file_name: str) -> bool:
        jsonn = {}
        jsonn.update({"Edges": []})
        jsonn.update({"Nodes": []})
        for i in self.graph.get_all_v():
            jsonARGS = {}
            jsonARGS.update({"pos": str(self.graph.get_all_v()[i])})
            jsonARGS.update({"id": i})
            jsonn["Nodes"].append(jsonARGS)
        for node in self.graph.get_all_v():
            for dest in self.graph.all_out_edges_of_node(node):
                jsonARGS = {}
                jsonARGS.update({"src": node})
                jsonARGS.update({"w": self.graph.all_out_edges_of_node(node)[dest]})
                jsonARGS.update({"dest": dest})
                jsonn["Edges"].append(jsonARGS)
        print(jsonn)
        file = open(file_name, "w")
        print(file)
        file.write(json.dumps(jsonn))
        file.close()

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
        scc = self.connected_components()
        for list in scc:
            if id1 in list:
                return list
        else:
            return []

    def connected_components(self) -> List[list]:
        isVisited = []
        theAList = []
        lowLink = {}
        stack = []
        # for i in self.graph.get_all_v().keys():
        #     isVisited.update({i: False})

        for i in self.graph.get_all_v():
            if i not in isVisited:
                self.dfs(i, isVisited, lowLink, stack, theAList)

        return theAList

    def dfs(self, node: int, isVisited: list, lowLink: dict, stack: list, theAList: list):
        stack.append(node)
        lowLink.update({node: node})
        isVisited.append(node)

        for i in self.graph.all_out_edges_of_node(node).keys():
            if i not in isVisited:
                self.dfs(i, isVisited, lowLink, stack, theAList)
            if i in stack:
                lowLink[node] = min(lowLink[node], lowLink[i])

        if lowLink[node] is node:
            nodeSCC = []
            nodeSCC.append(node)
            while 1:
                curr = stack.pop()
                if curr is node:
                    break
                lowLink[curr] = node
                nodeSCC.append(curr)

            theAList.append(nodeSCC)

    def plot_graph(self) -> None:

        # x axis values
        for src in self.graph.get_all_v().keys():
            listX = []
            listY = []
            # for dest in self.graph.all_out_edges_of_node(src):

        x1 = [1, 2, 3]
        # corresponding y axis values
        y1 = [1, 2, 3]

        # plotting the points
        plt.plot(x1, y1, "*")
        plt.plot(x1, y1)

        # naming the x axis
        plt.xlabel('x - axis')
        # naming the y axis
        plt.ylabel('y - axis')

        # giving a title to my graph
        plt.title('My first graph!')

        # function to show the plot
        plt.show()
