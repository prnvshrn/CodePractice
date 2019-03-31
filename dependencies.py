from collections import defaultdict, deque
class Solution(object):
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
            depth = 0
            while queue:
                curr, depth = queue.popleft()
                if curr in graph:
                    for nei in graph[curr]:
                        queue.append((nei, depth+1))
                else:
                    ans[curr] = 0
            ans[node] = depth
        
        ans = sorted(ans.items(), key=lambda x:x[1])
        print(ans)
    
if __name__ == "__main__":
        obj = Solution()
        edges = [['a','b'],['a','c'],['a','f'],['b','d'],['c','g'],['g','h']]
        obj.dependencies(edges)