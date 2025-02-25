from collections import defaultdict
import math

def max_points_on_line(points):
    """
    Find the maximum number of points that lie on the same straight line.
    
    Args:
        points: List of [x, y] coordinates
        
    Returns:
        Maximum number of points on any line
    """
    n = len(points)
    
    # If we have 0 or 1 points, return the number of points
    if n <= 1:
        return n
    
    max_points = 0
    
    # For each point
    for i in range(n):
        # Skip duplicate points for this iteration
        # We'll use a defaultdict to count points with the same slope
        slope_count = defaultdict(int)
        same_points = 0  # Count of duplicate points
        curr_max = 0     # Max points on a line passing through points[i]
        
        # Compare with all other points
        for j in range(n):
            if i == j:
                continue
                
            # Get the coordinates
            x1, y1 = points[i]
            x2, y2 = points[j]
            
            # Check for duplicate points
            if x1 == x2 and y1 == y2:
                same_points += 1
                continue
                
            # Calculate the slope
            # Handling vertical lines (infinite slope)
            if x1 == x2:
                slope = float('inf')
            else:
                # To avoid precision issues with floating point, we reduce the fraction
                dx = x2 - x1
                dy = y2 - y1
                gcd = math.gcd(dx, dy)
                
                # Ensure consistent representation of the slope
                # For negative slopes, we keep the numerator negative
                if dx < 0:
                    dx, dy = -dx, -dy
                    
                slope = (dy // gcd, dx // gcd)
                
            # Increment the count for this slope
            slope_count[slope] += 1
            curr_max = max(curr_max, slope_count[slope])
            
        # Add 1 to account for the point itself
        max_points = max(max_points, curr_max + 1 + same_points)
        
    return max_points

# Example usage:
if __name__ == "__main__":
    # Example 1
    points1 = [[1, 1], [2, 2], [3, 3]]
    print(f"Example 1 input: {points1}")
    print(f"Output: {max_points_on_line(points1)}")  # Expected: 3
    
    # Example 2
    points2 = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    print(f"Example 2 input: {points2}")
    print(f"Output: {max_points_on_line(points2)}")  # Expected: 4