#LeetCode 1462: Course Schedule IV
#There are a total of numCourses courses you have to take, labeled from a to numCourses -1.
# You are given an array prerequisities where prerequisities[i] = [ai, bi] indicates that you must take course ai before course bi.

#Prerequistes can also be indirect. if course a is a prerequisite of course b, and course b is a prerequisite of course c, then course a is a prerequisite of course c.
#You are also given an array queries where queries[j] = [u1, vi]. For the jth query, you should answer whether course ui, us a prerequisit of course vi or not.

#Return a boolean array answer where answer[j] is the answer to the jth query.

#Example 1:
#Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
#Output: [false,true]
#Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
#Course 0 is not a prerequisite of course 1, but the opposite is true.

#Example 2:

#Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
#Output: [false,false]
#Explanation: There are no prerequisites, and each course is independent.

def checkIfPrerequisite(numCourses, prerequisites, queries):
    # Initialize a matrix to keep track of direct and indirect prerequisites
    prereq = [[False] * numCourses for _ in range(numCourses)]
    # Set direct prerequisites
    for a, b in prerequisites:
        prereq[a][b] = True
    # Use Floyd Warshall to compute transitive closure of prerequisites
    for k in range(numCourses):
        for i in range(numCourses):
            for j in range(numCourses):
                prereq[i][j] = prereq[i][j] or (prereq[i][k] and prereq[k][j])
    # Prepare result list based on queries
    return [prereq[u][v] for u, v in queries]


if __name__ == "__main__":
    # Example usage:
    numCourses = 3
    prerequisites = [[1,2],[1,0],[2,0]]
    queries = [[1,0],[1,2]]
    result = checkIfPrerequisite(numCourses, prerequisites, queries)
    print(result)  # Expected Output: [True, True]
