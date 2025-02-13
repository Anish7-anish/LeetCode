# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        stk = [root]
        graph = defaultdict(set)
        count = 0

        while stk:
            current_node = stk.pop()
            if current_node is None:
                continue
            count+=1
            if current_node.left:
                child = current_node.left
                graph[current_node.val].add(child.val)
                graph[child.val].add(current_node.val)
                stk.append(child)
            if current_node.right:
                child = current_node.right
                graph[current_node.val].add(child.val)
                graph[child.val].add(current_node.val)
                stk.append(child)
        
        print(graph)
        
        num_min = -1
        que = deque()
        que.append(start)
        infected = set([start])

        while que:
            size = len(que)
            num_min+=1
            for _ in range(size):
                curr = que.popleft()
                for nei_node in graph[curr]:
                    if nei_node not in infected:
                        infected.add(nei_node)
                        que.append(nei_node)
        return num_min


        