class CostBoundedWalk(object):
    def __init__(self, originAPoint, maxCost, oobFunc, walkCostFunc):
        self.originAPoint = originAPoint
        self.maxCost = maxCost
        self.oobFunc = oobFunc
        self.walkCostFunc = walkCostFunc

    def do(self):
        costs = {self.originAPoint: 0}
        queue = [self.originAPoint]
        while len(queue) > 0:
            point = queue.pop(0)
            currCost = costs[point]
            neighbors = point.allHexNeighbors()
            for neighbor in neighbors:
                if self.oobFunc(neighbor):
                    continue
                walkCost = self.walkCostFunc(point, neighbor)
                if currCost + walkCost > self.maxCost:
                    continue
                if neighbor in costs and currCost + walkCost >= costs[neighbor]:
                    continue
                queue.append(neighbor)
                costs[neighbor] = currCost + walkCost
        return [point for point in costs.keys()]
