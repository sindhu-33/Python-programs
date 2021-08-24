#Deapth first search using logging.
import logging
#setting the logging level to debug and logging into a file and changing format of log.
logging.basicConfig(filename='test.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')
#dfs algorithm is used to search a node in graph or tree.
# a global dictionary to maintain connected nodes to each node.
gldic={ 'A' : ['B','C'], 'B' : ['D','E'], 'C' : [], 'D' : ['E'], 'E' : [] }
#a set to kepp track of previously visited nodes.
visit=set()
# function to traverse through nodes.
def dfs(node):
    #indicating gloabal variables to modify them.
    global gldic
    global visit
    # if the node is not present in set already then adding the node and visting its adjacent nodes.
    if(node not in visit):
        logging.debug(node)
        visit.add(node)
        for i in gldic[node]:
            #recursing the function through adjacent nodes.
            dfs(i)
#calling the function with the starting node
dfs('A')