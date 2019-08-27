# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE IF YOU WANT TO PRACTICE ***"

    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    # print("problem here", vars(problem))

    current_node = (problem.getStartState(),'',0)
    next_node = util.Stack()
    _visitedlist = [current_node[0]]

    while not problem.isGoalState(current_node[0]):
        for successor in problem.getSuccessors(current_node[0]):
            if not _visitedlist.__contains__(successor[0]):
                next_node.push((successor[0],current_node[1]+successor[1]+' ',current_node[2]+successor[2]))
        if next_node.list.__len__() == 0:
            break
        current_node = next_node.pop()

        while _visitedlist.__contains__(current_node[0]):
            if next_node.list.__len__() == 0:
                break
            current_node = next_node.pop()
        _visitedlist.append(current_node[0])
    result = current_node[1].split(' ')
    result.pop()
    return result;

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE IF YOU WANT TO PRACTICE ***"

    current_node = (problem.getStartState(), '', 0)
    next_node = util.Queue()
    _visitedlist = [current_node[0]]

    while not problem.isGoalState(current_node[0]):
        for successor in problem.getSuccessors(current_node[0]):
            if not _visitedlist.__contains__(successor[0]):
                next_node.push((successor[0], current_node[1] + successor[1] + ' ', current_node[2] + successor[2]))
        if next_node.list.__len__() == 0:
            break
        current_node = next_node.pop()

        while _visitedlist.__contains__(current_node[0]):
            if next_node.list.__len__() == 0:
                break
            current_node = next_node.pop()
        _visitedlist.append(current_node[0])

    result = current_node[1].split(' ')
    result.pop()
    return result;


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE IF YOU WANT TO PRACTICE ***"
    current_node = (problem.getStartState(), '', 0)
    next_node = util.PriorityQueue()
    _visitedlist = [current_node[0]]

    while not problem.isGoalState(current_node[0]):
        for successor in problem.getSuccessors(current_node[0]):
            # if not _visitedlist.__contains__(successor[0]):
                next_node.push((successor[0], current_node[1] + successor[1] + ' ', current_node[2] + successor[2]),current_node[2] + successor[2])

        if next_node.heap.__len__() == 0:
            break
        current_node = next_node.pop()

        while _visitedlist.__contains__(current_node[0]):
            if next_node.heap.__len__() == 0:
                break
            current_node = next_node.pop()
        _visitedlist.append(current_node[0])

    result = current_node[1].split(' ')
    result.pop()
    return result

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE IF YOU WANT TO PRACTICE ***"
    current_node = (problem.getStartState(), '', 0)
    next_node = util.PriorityQueue()
    _visitedlist = [current_node[0]]

    while not problem.isGoalState(current_node[0]):
        for successor in problem.getSuccessors(current_node[0]):
            # if not _visitedlist.__contains__(successor[0]):
                next_node.push((successor[0], current_node[1] + successor[1] + ' ', current_node[2] + successor[2]),
                               current_node[2] + successor[2] + heuristic(successor[0],problem))

        if next_node.heap.__len__() == 0:
            break
        current_node = next_node.pop()

        while _visitedlist.__contains__(current_node[0]):
            if next_node.heap.__len__() == 0:
                break
            current_node = next_node.pop()
        _visitedlist.append(current_node[0])

    result = current_node[1].split(' ')
    result.pop()
    return result

def checkCircle(currend_node,next_node,problem):
    for node in next_node:
        if (currend_node[0][0] == node[0][0]) & (currend_node[0][1] == node[0][1])& (not currend_node[0] == problem.getStartState()):
            return True
    return False

def iterativeDeepeningSearch(problem):
    """Search the deepest node in an iterative manner."""
    "*** YOUR CODE HERE FOR TASK 1 ***"
    current_node = (problem.getStartState(), '', 0, 0)
    next_node = util.Stack()
    next_node.push(current_node)
    _visitedlist = [current_node[0]]
    deepdegree = 1

    while not problem.isGoalState(current_node[0]):
        deepdegree += 1
        current_node = (problem.getStartState(), '', 0,0)  # (state, action, cost, layer)
        next_node.push(current_node)
        _visitedlist = [current_node[0]]

        while (not next_node.list.__len__() == 0) & (not problem.isGoalState(current_node[0])):
            for successor in problem.getSuccessors(current_node[0]):
                if (not checkCircle(successor,next_node.list,problem)) & (not current_node[3] + 1 > deepdegree):
                    next_node.push((successor[0], current_node[1] + successor[1] + ' ', current_node[2] + successor[2],current_node[3]+1))
            if next_node.list.__len__() == 0:
                break
            current_node = next_node.pop()
            while _visitedlist.__contains__(current_node[0]):
                if next_node.list.__len__() == 0:
                    break
                current_node = next_node.pop()
            if not _visitedlist.__contains__(current_node[0]):
                _visitedlist.append(current_node[0])

    result = current_node[1].split(' ')
    result.pop()
    return result

def waStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has has the weighted (x 2) lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE FOR TASK 2 ***"

    W = 2
    current_node = (problem.getStartState(), '', 0)
    next_node = util.PriorityQueue()
    _visitedlist = [current_node[0]]

    while not problem.isGoalState(current_node[0]):
        for successor in problem.getSuccessors(current_node[0]):
            # if not _visitedlist.__contains__(successor[0]):
            next_node.push((successor[0], current_node[1] + successor[1] + ' ', current_node[2] + successor[2]),
                           current_node[2] + successor[2] + W * heuristic(successor[0], problem))

        if next_node.heap.__len__() == 0:
            break
        current_node = next_node.pop()

        while _visitedlist.__contains__(current_node[0]):
            if next_node.heap.__len__() == 0:
                break
            current_node = next_node.pop()
        _visitedlist.append(current_node[0])

    result = current_node[1].split(' ')
    result.pop()
    return result


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
ids = iterativeDeepeningSearch
wastar = waStarSearch

