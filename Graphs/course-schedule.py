class Solution:
    """
        (a,b)
        b -> a
        a has some dependency so increase degree for a
        adjList[a] = [b]
        dependencyCounter[]
        Your indices are your verticse
        
    """
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        
        adjList = {}
        dependencyFactor = [0]*numCourses
        for i in range(len(prerequisites)):
            if prerequisites[i][1] in adjList:
                adjList[prerequisites[i][1]].append(prerequisites[i][0])
            else:
                adjList[prerequisites[i][1]] = [prerequisites[i][0]]
            dependencyFactor[prerequisites[i][0]]+=1
    
        # push no dependency vertices to a queue
        queue = []
        for i in range(numCourses):
            if dependencyFactor[i] == 0:
                queue.append(i)
                
        # now do BFS on the queue
        print(queue,dependencyFactor)
        coursesTaken = 0
        while queue:
            topIndependentCourse = queue.pop(0)
            coursesTaken += 1
            # get this vertex neighbours
            print(adjList,topIndependentCourse)
            if topIndependentCourse in adjList:
                for nbr in adjList[topIndependentCourse]:
                    dependencyFactor[nbr] -= 1
                    # we check if nbr is independent or not
                    if dependencyFactor[nbr]  == 0:
                        queue.append(nbr) 
                    
        return coursesTaken == numCourses
            
            
            
        
s = Solution()
numCourses = 2
prerequisites = [[1,0]]
print(s.canFinish(numCourses,prerequisites))
        
        
        
                
            
        
        
        
        