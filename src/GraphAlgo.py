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
        # print(jsonn)
        for i in jsonn["Nodes"]:
            x = float(i["pos"].split(",")[0])
            y = float(i["pos"].split(",")[1])
            z = float(i["pos"].split(",")[2])
            v = x, y, z
            newG.add_node(i["id"],v)
        for j in jsonn["Edges"]:
            newG.add_edge(j["src"], j["dest"], j["w"])

        self.graph = newG
        # print(self.graph.get_all_v())
        return True

    def save_to_json(self, file_name: str) -> bool:
        jsonn = {}
        jsonn.update({"Edges": []})
        jsonn.update({"Nodes": []})
        for i in self.graph.get_all_v():
            jsonARGS = {}
            x = self.graph.get_all_v()[i][0]
            y = self.graph.get_all_v()[i][1]
            z = self.graph.get_all_v()[i][2]
            v = ""+str(x)+","+str(y)+","+str(z)
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
            for j in self.graph.all_out_edges_of_node(src).keys():
                listX = []
                listY = []
                listX.append(self.graph.get_all_v()[src][0])
                listX.append(self.graph.get_all_v()[j][0])
                listY.append(self.graph.get_all_v()[src][1])
                listY.append(self.graph.get_all_v()[j][1])
                plt.plot(listX, listY, "b>")
                plt.plot(listX, listY, "r-")



        # plotting the points



        # naming the x axis
        plt.xlabel('x - axis')
        # naming the y axis
        plt.ylabel('y - axis')

        # giving a title to my graph
        plt.title('My first graph!')

        # function to show the plot
        plt.show()
    # def connected_componentsofir(self) -> List[list]:
    #     tag={}
    #     q=[]
    #     for i in self.graph.get_all_v():
    #         tag.update(i,-1)
    #     q.append(self.graph.get_all_v()[0])
    #     i=0
    #     while q.__sizeof__() is not 0:
    #         for j in self.graph.all_out_edges_of_node(q[i]):
    #             tag[j]=0
    #             q.append(j)

        pass


