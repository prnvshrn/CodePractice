from collections import defaultdict, deque
class Solution(object):

    def topographicalUtil(self, node, visited, stack, graph):
        visited[node] = True
        for i in graph[node]:
            if visited[i] == False:
                self.topographicalUtil(i, visited, stack ,graph)
        stack.insert(0,node) 

    def topographicalSort(self, edges):
        visited = {}
        graph = {}
        for i in edges:
            visited[i[0]] = False
            visited[i[1]] = False
            graph[i[0]] = []
            graph[i[1]] = []

        for i in edges:
            graph[i[0]].append(i[1])

        stack = []
        for node in visited:
            if visited[node] == False:
                self.topographicalUtil(node, visited, stack, graph)
        print(stack[::-1])


    def dependencies(self, edges):
        # Build graph
        graph = {}
        ans = {}
        for i in edges:
            if i[0] not in graph:
                graph[i[0]] = [i[1]]
            else:
                graph[i[0]].append(i[1])
        # Perform bfs for every edge
        for node, value in graph.items():
            queue = deque()
            queue.append((node,0))
            temp = 0
            while queue:
                curr, depth = queue.pop()
                temp = max(temp, depth)
                if curr in graph:
                    for nei in graph[curr]:
                        depth += 1
                        queue.append((nei, depth))
                else:
                    ans[curr] = 0
            ans[node] = temp
        
        ans = sorted(ans.items(), key=lambda x:x[1])
        print([i[0] for i in ans])
    
if __name__ == "__main__":
        obj = Solution()
        #edges = [[5,2],[5,0],[4,0],[4,1],[2,3],[3,1]]
        #edges = [['a','b'],['c','f'],['c','g'],['c','d'],['a','c'],['a','f'],['b','d'],['g','h']]
        edges = [['d','f'],['a','b'],['b','c'],['a','d'],['d','e'],['c','f'],['e','f'],['d','b'],['b','f']]
        obj.topographicalSort(edges)
        obj.dependencies(edges)