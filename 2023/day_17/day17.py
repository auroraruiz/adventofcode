"""
This module contains the solution to the Day 17 Advent of Code challenge.
"""
import os
import time
import heapq
from collections import defaultdict

def dijkstra(grid, start, end):
    """
    Implements Dijkstra's algorithm to find the least heat loss path.

    Args:
    grid (list of list): The grid representing the heat loss values.
    start (tuple): The starting coordinates.
    end (tuple): The destination coordinates.

    Returns:
    int: The minimum cost (heat loss) to reach the end.
    """
    queue = [(0, start[0], start[1], 0, 0, 0)]  # Priority queue initialized with (cost, x, y, dx, dy, straight)
    seen = defaultdict(lambda: float('inf'))  # Dictionary to track minimum costs

    while queue:
        cost, x, y, dx, dy, straight = heapq.heappop(queue)  # Get the lowest cost item
        
        if (x, y) == end:  # If reached the end, return the cost
            return cost

        if cost > seen[(x, y, dx, dy, straight)]:  # Ignore if cost is not minimal
            continue
        
        # Explore all possible movements
        for new_dx, new_dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = x + new_dx, y + new_dy  # Calculate new position
            new_straight = straight + 1 if (new_dx, new_dy) == (dx, dy) else 1  # Update straight movement count

            # Ensure valid movements
            if (new_x, new_y) == (x - dx, y - dy):  # Cannot reverse direction
                continue
            if not (0 <= new_x < len(grid) and 0 <= new_y < len(grid[0])):  # Check bounds
                continue
            if new_straight > 3:  # Limit straight movement
                continue
            
            new_cost = cost + grid[new_x][new_y]  # Calculate new cost
            if new_cost < seen[(new_x, new_y, new_dx, new_dy, new_straight)]:
                seen[(new_x, new_y, new_dx, new_dy, new_straight)] = new_cost
                heapq.heappush(queue, (new_cost, new_x, new_y, new_dx, new_dy, new_straight))  # Push new state onto queue
    
    return float('inf')  # Return infinity if no path found

def dijkstra2(grid, start, end):
    """
    Implements a modified Dijkstra's algorithm for ultra crucibles.

    Args:
    grid (list of list): The grid representing the heat loss values.
    start (tuple): The starting coordinates.
    end (tuple): The destination coordinates.

    Returns:
    int: The minimum cost (heat loss) to reach the end with ultra crucible rules.
    """
    initial_cost = sum(grid[0][i] for i in range(1, 4))  # Initial cost based on starting row
    queue = [(initial_cost, 0, 3, 0, 1, 3)]  # Initialize queue for ultra crucible
    seen = defaultdict(lambda: float('inf'))  # Track minimum costs
    
    while queue:
        cost, x, y, dx, dy, straight = heapq.heappop(queue)  # Get the lowest cost item
        
        if (x, y) == end and straight >= 4:  # Check for end condition with straight constraint
            return cost

        if cost >= seen[(x, y, dx, dy, straight)]:  # Ignore non-minimal costs
            continue
        
        seen[(x, y, dx, dy, straight)] = cost  # Record the current cost
        
        # Explore all possible movements
        for new_dx, new_dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = x + new_dx, y + new_dy  # Calculate new position
            
            if (new_dx, new_dy) == (-dx, -dy):  # Cannot reverse direction
                continue
            if not (0 <= new_x < len(grid) and 0 <= new_y < len(grid[0])):  # Check bounds
                continue
            
            new_straight = straight + 1 if (new_dx, new_dy) == (dx, dy) else 1  # Update straight movement count

            # Ensure movement constraints
            if new_straight > 10:  # Max straight movement for ultra crucible
                continue
            if (new_dx, new_dy) != (dx, dy) and straight < 4:  # Must have straight movement for turning
                continue
            
            new_cost = cost + grid[new_x][new_y]  # Calculate new cost
            heapq.heappush(queue, (new_cost, new_x, new_y, new_dx, new_dy, new_straight))  # Push new state onto queue
        
    return float('inf')  # Return infinity if no path found

if __name__ == "__main__":
    # Code to open the input file
    path = os.getcwd()
    FILE = "day17.txt"
    
    with open(os.path.join(path, FILE), encoding='utf-8') as f:
        lines = f.read().strip()
        grid = [list(map(int, x)) for x in lines.split('\n')]

    start_time = time.time()

    start = (0, 0)
    end = (len(grid) - 1, len(grid[0]) - 1)

    sol = dijkstra(grid, start, end)
    sol2 = dijkstra2(grid, start, end)

    # Part 1 solution
    print("Solution part 1: ", sol)
    # Part 2 solution
    print("Solution part 2: ", sol2)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")