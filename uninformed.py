from collections import deque
import heapq


def bfs(graph, start, goal):
    """
    Breadth-First Search.

    Returns:
        path: list of cities from start to goal
        cost: total road distance of the path
        nodes_expanded: number of cities expanded
    """

    # Queue stores paths that still need to be explored.
    queue = deque([[start]])

    # Keep track of cities we have already discovered.
    visited = {start}

    nodes_expanded = 0

    while queue:
        # Get the oldest path from the queue.
        path = queue.popleft()

        # The last city in this path is the city we are currently exploring.
        current = path[-1]

        # We are expanding this city.
        nodes_expanded += 1

        # Did we reach the destination?
        if current == goal:
            cost = 0

            # Calculate the total road distance of the path.
            for i in range(len(path) - 1):
                cost += graph[path[i]][path[i + 1]]

            return {
                "path": path,
                "cost": round(cost, 2),
                "nodes_expanded": nodes_expanded
            }

        # Explore each neighboring city.
        for neighbor in graph.get(current, {}):
            if neighbor not in visited:
                visited.add(neighbor)

                # Create a new path that includes this neighbor.
                new_path = path + [neighbor]

                # Add the new path to the end of the queue.
                queue.append(new_path)

    # No path was found.
    return {
        "path": [],
        "cost": 0,
        "nodes_expanded": nodes_expanded
    }
## ALGORITHM 2 ###########

def dfs(graph, start, goal):
    """
    Depth-First Search.

    Returns:
        path: list of cities from start to goal
        cost: total road distance of the path
        nodes_expanded: number of cities expanded
    """

    # Stack stores paths that still need to be explored.
    stack = [[start]]

    # Keep track of cities we have already discovered.
    visited = {start}

    nodes_expanded = 0

    while stack:
        # Get the newest path from the stack.
        path = stack.pop()

        # The last city in this path is the city we are currently exploring.
        current = path[-1]

        nodes_expanded += 1

        # Did we reach the destination?
        if current == goal:
            cost = 0

            # Calculate the total road distance.
            for i in range(len(path) - 1):
                cost += graph[path[i]][path[i + 1]]

            return {
                "path": path,
                "cost": round(cost, 2),
                "nodes_expanded": nodes_expanded
            }

        # Explore neighboring cities.
        for neighbor in graph.get(current, {}):
            if neighbor not in visited:
                visited.add(neighbor)

                new_path = path + [neighbor]

                # Add the path to the top of the stack.
                stack.append(new_path)

    # No path was found.
    return {
        "path": [],
        "cost": 0,
        "nodes_expanded": nodes_expanded
    }
###Algorithm3 ############
def ucs(graph, start, goal):
    """
    Uniform-Cost Search.

    Returns:
        path: list of cities from start to goal
        cost: total road distance of the path
        nodes_expanded: number of cities expanded
    """

    # Priority queue entries:
    # (total_cost, path)
    priority_queue = [(0, [start])]

    # Best known cost to reach each city.
    best_cost = {start: 0}

    nodes_expanded = 0

    while priority_queue:
        # Get the path with the lowest total cost.
        current_cost, path = heapq.heappop(priority_queue)

        current = path[-1]

        # Ignore an outdated entry if we already found a cheaper route.
        if current_cost > best_cost.get(current, float("inf")):
            continue

        nodes_expanded += 1

        # Did we reach the goal?
        if current == goal:
            return {
                "path": path,
                "cost": round(current_cost, 2),
                "nodes_expanded": nodes_expanded
            }

        # Explore neighboring cities.
        for neighbor, distance in graph.get(current, {}).items():

            new_cost = current_cost + distance

            # Only consider this route if it is cheaper
            # than the best route we currently know.
            if new_cost < best_cost.get(neighbor, float("inf")):
                best_cost[neighbor] = new_cost

                new_path = path + [neighbor]

                heapq.heappush(
                    priority_queue,
                    (new_cost, new_path)
                )

    # No path was found.
    return {
        "path": [],
        "cost": 0,
        "nodes_expanded": nodes_expanded
    }

def depth_limited_search(graph, current, goal, limit, path, visited, stats):
    """
    Depth-Limited Search helper used by IDS.
    """

    stats["nodes_expanded"] += 1

    if current == goal:
        return path

    if limit == 0:
        return None

    for neighbor in graph.get(current, {}):
        if neighbor not in visited:
            visited.add(neighbor)

            result = depth_limited_search(
                graph,
                neighbor,
                goal,
                limit - 1,
                path + [neighbor],
                visited,
                stats
            )

            if result is not None:
                return result

    return None


def ids(graph, start, goal):
    """
    Iterative Deepening Search.

    Returns:
        path: list of cities from start to goal
        cost: total road distance of the path
        nodes_expanded: number of cities expanded
    """

    depth_limit = 0
    total_nodes_expanded = 0

    while True:
        stats = {"nodes_expanded": 0}

        visited = {start}

        path = depth_limited_search(
            graph,
            start,
            goal,
            depth_limit,
            [start],
            visited,
            stats
        )

        total_nodes_expanded += stats["nodes_expanded"]

        if path is not None:
            cost = 0

            for i in range(len(path) - 1):
                cost += graph[path[i]][path[i + 1]]

            return {
                "path": path,
                "cost": round(cost, 2),
                "nodes_expanded": total_nodes_expanded
            }

        depth_limit += 1