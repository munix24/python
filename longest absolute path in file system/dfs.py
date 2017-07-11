#https://discuss.leetcode.com/topic/31565/the-longest-absolute-path-in-file-system
# Basic graph node class for this problem
class GraphNode(object):
    def __init__(self, string):
        self.string = string
        self.length = len(string)
        if '.' in self.string: # simplification to find files, could use a regex here for something more intensive
            self.file = True
        else:
            self.file = False
        self.adjacent = []
    def __repr__(self):
        return '<GraphNode {}>'.format(self.string)

class Solution(object):
    def longest_dir_path(self, path):
        cur_str = '' # store the current string that we are processing
        last_root = {} # stores the last root that was found for a certain level
        level = 0 # current tree level that we are on

        path += '\n' # terminate path by \n so we get the last node
        for n in path:
            if n == '\t':
                level += 1
                continue
            if n == '\n':
                x = GraphNode(cur_str)
                if level > 0:
                    last_root[level - 1].adjacent.append(x)
                else:
                    root = x
                last_root[level] = x
                level = 0
                cur_str = ''
                continue
            cur_str += n
        return self.dfs(last_root[0])

    def dfs(self, root):
        stack = [root] # DFS stack
        visited = {} # storing visited nodes
        distance = {root: 0} # storing the distance from the root node
        pre = {root: None} # predecessors
        max_distance = 0 # maximum distance
        max_node = None # largest node

        while stack:
            node = stack.pop()
            if node not in visited:
                for neighbor in node.adjacent:
                    if neighbor not in distance:
                        distance[neighbor] = 0
                    
                    # update distance with the maximum distance so far
                    if distance[neighbor] < distance[node] + node.length:
                        distance[neighbor] = distance[node] + node.length
                        pre[neighbor] = node

                        # update max distance and node only if the target node is a file
                        if distance[neighbor] > max_distance and neighbor.file == True:
                            max_distance = distance[neighbor]
                            max_node = neighbor
                    stack.append(neighbor)

        if not max_node:
            return -1 # no file, max node unknown, return -1

        # finally calculate length
        length = 0
        v = max_node
        while v != None: 
            length += v.length + 1 # remember the / separators
            v = pre[v]
        length -= 1 # no / separator on the root directory
        return length

#x = Solution()
# some test cases
#assert x.longest_dir_path('dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext') == len('dir/subdir2/subsubdir2/file2.ext')
#assert x.longest_dir_path('dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext') == len('dir/subdir2/file.ext')
#assert x.longest_dir_path('dir') == -1
#assert x.longest_dir_path('') == -1
#assert x.longest_dir_path('dir\n\tsubdir1') == -1
