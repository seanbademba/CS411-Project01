import heapq
import math


def heuristic(locations, city, goal):
    """
    Estimate the straight-line distance between two cities
    using their latitude and longitude.
    """
    lat1 = math.radians(locations[city]["lat"])
    lon1 = math.radians(locations[city]["lon"])

    lat2 = math.radians(locations[goal]["lat"])
    lon2 = math.radians(locations[goal]["lon"])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1)
        * math.cos(lat2)
        * math.sin(dlon / 2) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    earth_radius_miles = 3958.8

    return earth_radius_miles * c

def greedy_best_first(graph, locations, start, goal):
    """
    Greedy Best-First Search.

    Chooses the city that appears closest to the goal
    according to the heuristic.

    Returns:
        path: list of cities from start to goal
        cost: total road distance of the path
        nodes_expanded: number of cities expanded
    """
    priority_queue = [(heuristic(locations, start, goal), [start])]
    visited = {start}
    nodes_expanded = 0

    while priority_queue:
        _, path = heapq.heappop(priority_queue)
        current = path[-1]
        nodes_expanded += 1

        if current == goal:
            cost = 0
            for i in range(len(path) - 1):
                cost += graph[path[i]][path[i + 1]]

            return {
                "path": path,
                "cost": round(cost, 2),
                "nodes_expanded": nodes_expanded
            }

        for neighbor in graph.get(current, {}):
            if neighbor not in visited:
                visited.add(neighbor)

                priority = heuristic(locations, neighbor, goal)
                new_path = path + [neighbor]

                heapq.heappush(
                    priority_queue,
                    (priority, new_path)
                )

    return {
        "path": [],
        "cost": 0,
        "nodes_expanded": nodes_expanded
    }

def a_star(graph, locations, start, goal):
    """
    A* Search.

    Chooses the city with the smallest:
        f(n) = g(n) + h(n)

    where:
        g(n) = actual cost from start to current city
        h(n) = estimated cost from current city to goal

    Returns:
        path: list of cities from start to goal
        cost: total road distance of the path
        nodes_expanded: number of cities expanded
    """
    priority_queue = [(heuristic(locations, start, goal), 0, [start])]
    best_cost = {start: 0}
    nodes_expanded = 0

    while priority_queue:
        _, current_cost, path = heapq.heappop(priority_queue)
        current = path[-1]

        if current_cost > best_cost.get(current, float("inf")):
            continue

        nodes_expanded += 1

        if current == goal:
            return {
                "path": path,
                "cost": round(current_cost, 2),
                "nodes_expanded": nodes_expanded
            }

        for neighbor, distance in graph.get(current, {}).items():
            new_cost = current_cost + distance

            if new_cost < best_cost.get(neighbor, float("inf")):
                best_cost[neighbor] = new_cost

                h = heuristic(locations, neighbor, goal)
                f = new_cost + h

                new_path = path + [neighbor]

                heapq.heappush(
                    priority_queue,
                    (f, new_cost, new_path)
                )

    return {
        "path": [],
        "cost": 0,
        "nodes_expanded": nodes_expanded
    }