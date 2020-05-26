import heapq
import collections


class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id):
        return id not in self.walls

    def neighbors(self, id):
        (x, y) = id
        results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1),
                   (x - 1, y - 1)]
        if (x + y) % 2 == 0:
            results.reverse()
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results


class GridWithWeights(SquareGrid):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.weights = {}

    def cost(self, from_node, to_node):
        return self.weights.get((from_node, to_node), 1)


class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far


def fill_weights(diagram, grid):
    for j in range(13):
        for i in range(7):
            if grid[i][j] != 3:
                x = grid[i][j]
            else:
                continue
            if j - 1 >= 0:
                if i - 1 >= 0:
                    diagram.weights[(j - 1, i - 1), (j, i)] = x
                diagram.weights[(j - 1, i), (j, i)] = x
                if i + 1 <= 6:
                    diagram.weights[(j - 1, i + 1), (j, i)] = x
            if j + 1 <= 12:
                if i - 1 >= 0:
                    diagram.weights[(j + 1, i - 1), (j, i)] = x
                diagram.weights[(j + 1, i), (j, i)] = x
                if i + 1 <= 6:
                    diagram.weights[(j + 1, i + 1), (j, i)] = x
            if i - 1 >= 0:
                diagram.weights[(j, i - 1), (j, i)] = x
            if i + 1 <= 7:
                diagram.weights[(j, i + 1), (j, i)] = x


def find_path(p, chars_grid, path_grid, pos, res):
    grid_diagram = GridWithWeights(13, 7)
    walls = []
    fill_weights(grid_diagram, path_grid)
    for j in range(13):
        for i in range(7):
            if path_grid[i][j] == 3 or (chars_grid != 0 and chars_grid != p):
                walls.append((j, i))
    grid_diagram.walls = walls
    path, costs = a_star(grid_diagram, pos, res)
    return path, costs, grid_diagram


'''from grid import path_grid
from implementation import draw_grid
a, b, c = find_path(path_grid, (6, 2), (6, 6))
print(c.weights)
print(a)
print(c)
draw_grid(c, width=3, point_to=a, start=(6, 2), goal=(6, 6))'''

'''           if j - 1 >= 0:
                if i - 1 >= 0:
                    diagram.weights[(j, i), (j - 1, i - 1)] = x
                diagram.weights[(j, i), (j - 1, i)] = x
                if i + 1 <= 6:
                    diagram.weights[(j, i), (j - 1, i + 1)] = x
            if j + 1 <= 12:
                if i - 1 >= 0:
                    diagram.weights[(j, i), (j + 1, i - 1)] = x
                diagram.weights[(j, i), (j + 1, i)] = x
                if i + 1 <= 6:
                    diagram.weights[(j, i), (j + 1, i + 1)] = x
            if i - 1 >= 0:
                diagram.weights[(j, i), (j, i - 1)] = x
            if i + 1 <= 7:
                diagram.weights[(j, i), (j, i + 1)] = x
'''
