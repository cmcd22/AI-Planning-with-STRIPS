# searchMPP.py - Searcher with multiple-path pruning
# AIFCA Python3 code Version 0.9.5 Documentation at http://aipython.org
# Download the zip file and read aipython.pdf for documentation

# Artificial Intelligence: Foundations of Computational Agents http://artint.info
# Copyright David L Poole and Alan K Mackworth 2017-2022.
# This work is licensed under a Creative Commons
# Attribution-NonCommercial-ShareAlike 4.0 International License.
# See: http://creativecommons.org/licenses/by-nc-sa/4.0/deed.en

from searchGeneric import AStarSearcher, visualize
from searchProblem import Path

class SearcherMPP(AStarSearcher):
    """returns a searcher for a problem.
    Paths can be found by repeatedly calling search().
    """
    def __init__(self, problem):
        super().__init__(problem)
        self.explored = set()

    @visualize
    def search(self):
        """returns next path from an element of problem's start nodes
        to a goal node. 
        Returns None if no path exists.
        """
        while not self.empty_frontier():
            path = self.frontier.pop()
            if path.end() not in self.explored:
                self.display(2, "Expanding:",path,"(cost:",path.cost,")")
                self.explored.add(path.end())
                self.num_expanded += 1
                if self.problem.is_goal(path.end()):
                    self.display(1, self.num_expanded, "paths have been expanded and",
                            len(self.frontier), "paths remain in the frontier")
                    self.solution = path   # store the solution found
                    print('*SOLUTION FOUND*')
                    p = str(path).split('}')
                    print('*INITIAL STATE*: '+p[0]+'}')
                    print('*BEST PATH*')
                    count = 1
                    for i in p[1:len(p)-1]:
                        print(str(count)+') -> '+i+'}')
                        count += 1
                    print('---------------------------------------------------------------------')
                    return path
                else:
                    l = ''
                    pa = str(path).split('}')
                    for x in pa[1:len(pa)-1]:
                        xx = x.split('{')
                        xxx = xx[0]
                        xxxx = xxx+'\n'
                        l = l+xxxx
                    if l:
                        print('*PATH EXPLORED*')
                        print(str(l))
                    neighs = self.problem.neighbors(path.end())
                    self.display(3,"Neighbors are", neighs)
                    for arc in neighs:
                        self.add_to_frontier(Path(path,arc))
                    self.display(3,"Frontier:",self.frontier)
        self.display(1,"No (more) solutions. Total of",
                     self.num_expanded,"paths expanded.")
        return None


