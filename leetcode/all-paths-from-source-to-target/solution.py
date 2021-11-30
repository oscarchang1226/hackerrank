from typing import List

class Solution:

    def __init__(self):
        self.graph = []
        self.end = None


    def checkIfHasNextMove(self, path):
        idx = path[-1]
        return idx != self.end and len(self.graph[idx]) > 0



    """
    Use graph to traverse to n-1
    """
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        if len(graph) == 0:
            return []

        self.graph = graph
        self.end = len(graph) - 1

        # Set initial paths
        paths = [[0, i] for i in graph[0]]

        # For each paths get next steps
        done = len(list(filter(self.checkIfHasNextMove, paths))) == 0
        while paths and not done:
            newPaths = []
            for path in paths:
                idx = path[-1]
                if idx != self.end and graph[idx]:
                    newPaths += [ path + [j] for j in graph[idx]]
                else:
                    newPaths.append(path)
            paths = newPaths
            done = len(list(filter(self.checkIfHasNextMove, paths))) == 0




        return list(filter(lambda x: x[-1] == self.end, paths))

