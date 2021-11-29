import sys
from collections import defaultdict

class AdjGraph:
    def __init__(self):
        """
        The graph will be using a dictionary with the key is the start node, the value will be a dictionary with the end node is the key and the value is a tuple of edgeID and length. Check below for representation

        graph = {startNode1: {endNode1: (edgeID, length), endNode2:  (edgeID, length), ....}, startNode2: {endNode1:  (edgeID, length), endNode2:  (edgeID, length), ...), ....}
        2 variables to count how many edges and vertices the graph has
        """
        self.graph = defaultdict(lambda: defaultdict(tuple))
        self.numVertices = 0
        self.numEdges = 0

    def parseGraph(self, inputFile):
        """
        Function to parse the file into an adjacency graph representation.

        :param inputFile: the name of the input file
        :return None
        """
        file = open(inputFile, "r")
        lines = file.readlines()

        # Parsing line by line
        for line in lines:
            # Ignore comment lines that start with #
            if line[0] == "#":
                continue
            # The text will contain 4 values edgeID, startNode, endNode, length separated by space
            edgeID, startNode, endNode, length = line.rstrip().split(" ")
            # Convert text to numbers
            self.graph[int(startNode)][int(endNode)] = int(edgeID), float(length)
            self.numEdges = max(self.numEdges, int(edgeID))
            self.numVertices = max(self.numVertices, int(startNode), int(endNode))
        print("Done parsing graph: There are", self.numEdges, "edges and", self.numVertices, "vertices")

    def toFile(self):
        """
        Print the graph to file
        :return None
        """
        #TODO
        pass

    def DijkstraAlgo(self):
        #TODO
        pass

    def BellmanFordAlgo(self):
        #TODO
        pass





def main():
    """
    Main function of the project.
    :return:
    """

    # Parse the command line argument
    try:
        inputFile = sys.argv[1]
        outputFile = sys.argv[2]
    except:
        print("Run the program again with the exact command line $python main.py InputFile OutputFile")

    adjGraph = AdjGraph()
    adjGraph.parseGraph(inputFile)
    #TODO: Choose Bellman-Ford or Dijkstra for the algorithm for shortest path to implement and output to file

if __name__ == "__main__":
    main()