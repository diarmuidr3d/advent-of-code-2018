class Graph:
    root = []
    nodes = {}

    def __str__(self):
        return ("root={0}, nodes={1}".format(self.root, str(self.nodes)))

    def add_node(self, node):
        self.nodes[node] = {'children':[], 'parents': []}
        self.root = []
        return self

    def add_child(self, node, child):
        if node not in self.nodes:
            self.add_node(node)
        self.nodes[node]['children'].append(child)
        if child not in self.nodes:
            self.add_node(child)
        self.nodes[child]['parents'].append(node)
        if self.root == child:
            self.root = None
        return self

    def get_parents(self, node):
        return self.nodes[node]['parents'] if node in self.nodes else None

    def get_children(self, node):
        return self.nodes[node]['children'] if node in self.nodes else None

    def get_root(self):
        if self.root:
            return self.root
        for node in self.nodes:
            if not self.nodes[node]['parents']:
                self.root.append(node)
        return self.root

import re

# input = """Step C must be finished before step A can begin.
# Step C must be finished before step F can begin.
# Step A must be finished before step B can begin.
# Step A must be finished before step D can begin.
# Step B must be finished before step E can begin.
# Step D must be finished before step E can begin.
# Step F must be finished before step E can begin."""
input = """Step F must be finished before step R can begin.
Step I must be finished before step P can begin.
Step C must be finished before step O can begin.
Step H must be finished before step K can begin.
Step Y must be finished before step N can begin.
Step M must be finished before step J can begin.
Step D must be finished before step W can begin.
Step B must be finished before step N can begin.
Step T must be finished before step A can begin.
Step R must be finished before step L can begin.
Step P must be finished before step S can begin.
Step O must be finished before step J can begin.
Step X must be finished before step N can begin.
Step A must be finished before step K can begin.
Step N must be finished before step G can begin.
Step W must be finished before step U can begin.
Step Q must be finished before step U can begin.
Step V must be finished before step U can begin.
Step J must be finished before step G can begin.
Step G must be finished before step S can begin.
Step Z must be finished before step U can begin.
Step U must be finished before step S can begin.
Step E must be finished before step L can begin.
Step K must be finished before step L can begin.
Step L must be finished before step S can begin.
Step M must be finished before step N can begin.
Step T must be finished before step E can begin.
Step J must be finished before step U can begin.
Step G must be finished before step L can begin.
Step D must be finished before step P can begin.
Step T must be finished before step Z can begin.
Step U must be finished before step L can begin.
Step Z must be finished before step K can begin.
Step Q must be finished before step V can begin.
Step G must be finished before step K can begin.
Step Z must be finished before step E can begin.
Step Q must be finished before step Z can begin.
Step J must be finished before step S can begin.
Step G must be finished before step U can begin.
Step I must be finished before step M can begin.
Step W must be finished before step K can begin.
Step Y must be finished before step V can begin.
Step B must be finished before step Q can begin.
Step Y must be finished before step D can begin.
Step I must be finished before step G can begin.
Step A must be finished before step S can begin.
Step X must be finished before step S can begin.
Step O must be finished before step N can begin.
Step M must be finished before step X can begin.
Step V must be finished before step Z can begin.
Step W must be finished before step Z can begin.
Step C must be finished before step L can begin.
Step Q must be finished before step G can begin.
Step A must be finished before step U can begin.
Step G must be finished before step Z can begin.
Step P must be finished before step Q can begin.
Step C must be finished before step Z can begin.
Step U must be finished before step K can begin.
Step Q must be finished before step L can begin.
Step X must be finished before step U can begin.
Step A must be finished before step N can begin.
Step N must be finished before step S can begin.
Step Z must be finished before step L can begin.
Step F must be finished before step D can begin.
Step D must be finished before step A can begin.
Step J must be finished before step K can begin.
Step W must be finished before step Q can begin.
Step T must be finished before step J can begin.
Step T must be finished before step W can begin.
Step E must be finished before step K can begin.
Step P must be finished before step U can begin.
Step O must be finished before step Z can begin.
Step D must be finished before step B can begin.
Step R must be finished before step J can begin.
Step O must be finished before step A can begin.
Step N must be finished before step E can begin.
Step D must be finished before step G can begin.
Step M must be finished before step Q can begin.
Step F must be finished before step W can begin.
Step T must be finished before step L can begin.
Step U must be finished before step E can begin.
Step X must be finished before step L can begin.
Step M must be finished before step G can begin.
Step Z must be finished before step S can begin.
Step F must be finished before step Y can begin.
Step N must be finished before step Z can begin.
Step T must be finished before step U can begin.
Step D must be finished before step O can begin.
Step H must be finished before step X can begin.
Step V must be finished before step E can begin.
Step M must be finished before step T can begin.
Step Y must be finished before step O can begin.
Step P must be finished before step E can begin.
Step C must be finished before step E can begin.
Step P must be finished before step L can begin.
Step M must be finished before step A can begin.
Step F must be finished before step T can begin.
Step I must be finished before step C can begin.
Step X must be finished before step Z can begin.
Step Y must be finished before step U can begin.
Step B must be finished before step E can begin."""


def get_next_letter(queue, graph, result):
    if not queue:
        return None
    next_letter = None
    i = 0
    while next_letter is None:
        parents = graph.get_parents(queue[i])
        if parents:
            parents_complete = True
            for each in parents:
                if each not in result:
                    parents_complete = False
            if parents_complete:
                next_letter = queue.pop(i)
        else:
            next_letter = queue.pop(i)
        i = i + 1
    return next_letter
    
regex = re.compile(r'(?:Step )([A-Z])(?: must be finished before step )([A-Z])')
lines = input.split('\n')
graph = Graph()
for line in lines:
    child = regex.search(line).group(2)
    parent = regex.search(line).group(1)
    graph.add_child(node=parent, child=child)


result = ""
queue = graph.get_root()
next_letter = get_next_letter(queue, graph, result)
while next_letter != None:
    result = result + next_letter
    children = graph.get_children(next_letter)
    if children is not None:
        for each in children:
            if each not in queue and each not in result:
                queue.append(each)
    queue = sorted(queue)
    next_letter = get_next_letter(queue, graph, result)

print(result)