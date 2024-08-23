# from collections import deque, defaultdict

# def minimumTime(n, relations, time):
#     # We create a graph using a defaultdict. Each key is a course, and its value is a list of courses that depend on it.
#     graph = defaultdict(list)
#     # We also create an in_degree array to keep track of how many prerequisites each course has.
#     in_degree = [0] * n

#     # Build the graph and calculate in-degrees
#     # We populate these structures by iterating through the relations.
#     for prev, next in relations:
#         graph[prev - 1].append(next - 1)
#         in_degree[next - 1] += 1

#     # Step 2: Initialize the DP array with course durations
#     # We create a dp (dynamic programming) array initialized with the time required for each course. 
#     # This will store the minimum time needed to complete each course, including its prerequisites.
#     dp = time[:]

#     # Step 3: Topological Sort using BFS
#     # We use a topological sort (implemented with BFS) to process courses in order, starting with those that have no prerequisites.
#     # For each course, we update the minimum time needed for its dependent courses.
#     # The key line is dp[next_course] = max(dp[next_course], dp[course] + time[next_course]). 
#     # This ensures that we account for the longest chain of prerequisites.
#     queue = deque([i for i in range(n) if in_degree[i] == 0])
    
#     while queue:
#         course = queue.popleft()
        
#         # Process all courses that depend on the current course
#         for next_course in graph[course]:
#             dp[next_course] = max(dp[next_course], dp[course] + time[next_course])
#             in_degree[next_course] -= 1
#             if in_degree[next_course] == 0:
#                 queue.append(next_course)

#     # Step 4: The result is the maximum time in the DP array
#     return max(dp)



# # Example 1:
# n1 = 4
# relations1 = [[1, 2], [2, 3], [3, 4]]
# time1 = [2, 4, 3, 5]
# print(minimumTime(n1, relations1, time1))  # Output: 14

from collections import defaultdict, deque

def minimumTime(n, relations, time):
    print(f"Starting with {n} courses")
    print(f"Time required for each course: {time}")
    print(f"Prerequisite relations: {relations}")

    # Step 1: Create the graph and in-degree array
    graph = defaultdict(list)
    in_degree = [0] * n
    
    # Build the graph and calculate in-degrees
    for prev, next in relations:
        graph[prev - 1].append(next - 1)
        in_degree[next - 1] += 1
    
    print(f"\nGraph representation: {dict(graph)}")
    print(f"In-degree for each course: {in_degree}")

    # Step 2: Initialize the DP array with course durations
    dp = time[:]
    print(f"\nInitial DP array: {dp}")

    # Step 3: Topological Sort using BFS
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    print(f"\nInitial queue (courses with no prerequisites): {list(queue)}")
    
    while queue:
        course = queue.popleft()
        print(f"\nProcessing course {course + 1}")
        
        # Process all courses that depend on the current course
        for next_course in graph[course]:
            old_time = dp[next_course]
            dp[next_course] = max(dp[next_course], dp[course] + time[next_course])
            print(f"  Updating course {next_course + 1}: {old_time} -> {dp[next_course]}")
            
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)
                print(f"  Course {next_course + 1} is now ready. Adding to queue.")
        
        print(f"Current DP array: {dp}")
        print(f"Current queue: {list(queue)}")

    # Step 4: The result is the maximum time in the DP array
    result = max(dp)
    print(f"\nFinal DP array: {dp}")
    print(f"Minimum time to complete all courses: {result}")
    return result

# Test the function with Example 1
# n = 4
# relations = [[1,2], [2,3], [3,4]]
# time = [2,4,3,5]

# Test the function with Example 1
n = 4
relations = [[1, 4], [2, 4], [3, 4]]
time = [2, 3, 1, 4]

print("Example 1:")
minimumTime(n, relations, time)