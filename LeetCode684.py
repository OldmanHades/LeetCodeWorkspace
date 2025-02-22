#LeetCode 684: Redundant Connection
# In this problem, a tree is an undirected graph that is connected and has no cycles.
# You are given a graph that started as a tree with n nodes labeled from 1 to n.
# With one additional edge added. The added edge has two different vertices chosen from 1 to n and was not an edge that already existed. The graph is represented as an array edges of length n where edges[1] = [a,b] indicates that there is an edge between nodes a and b in the graph.
# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

#Example 1:
# Input: edges = [(1,2), (1,3), (2,3)]
# Output: [2,3]

#Example 2:
# Input: edges = [(1,2), (2,3), (3,4), (1,4), (1,5)]
# Output: [1,4]

import argparse

class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            if rank[px] > rank[py]:
                px, py = py, px
            parent[px] = py
            rank[py] += rank[px]
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]

        return []


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Run example usages for the LeetCode684 solution.")
    parser.add_argument("--example", type=str, default="default", help="Example name to run")
    args = parser.parse_args()

    # Define a dictionary of examples
    examples = {
        "default": [[1, 2], [1, 3], [2, 3]],
        "example1": [[1, 2], [1, 3], [2, 3]],
        "example2": [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]],
        "example3": [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5], [2, 5]]
    }

    if args.example not in examples:
        print(f"Example '{args.example}' not found. Available examples: {list(examples.keys())}")
    else:
        sol = Solution()
        result = sol.findRedundantConnection(examples[args.example])
        print("Result:", result)