from random import *

# T: the mouse goes into the intersection
# S: the mouse goes straight at an intersection

# 1 is a dead end, 2 is a goal state, intersections have ids
maze = {
    'start': ['int1', 'int2', 1],
    'int1': ['int3', 'int4', 1],
    'int2': ['int5', 1],
    'int3': ['int6', 1],
    'int4': [1],
    'int5': [2],
    'int6': [1],
}


def choose_step(path):
    for i in range(len(path)):
        num = randint(0, 1)
        if num == 0:
            # choose that option
            if path[i] == 1:
                return 'dead'
            elif path[i] == 2:
                return 'win'
            else:
                return choose_step(maze[path[i]])
    # if the mouse didn't choose anything (or didn't eat the cheese!) it dies
    return 'dead'


counter = 0
repeat = 1000

for i in range(repeat):
    if choose_step(maze['start']) == 'win':
        counter = counter + 1

print("probability of mouse winning is", counter/repeat)
