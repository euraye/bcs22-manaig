from collections import defaultdict, deque

print("""
        1
     /     \\
    2       3 
   / \\     / \\
  4   5   6   7
           \\   \\
            8   9
""")

class traversal_order:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def vertical_traversal(root):
    def dfs(node, distance, level, result):
        if not node:
            return

        result[distance].append((level, node.key))

        dfs(node.left, distance - 1, level + 1, result)
        dfs(node.right, distance + 1, level + 1, result)

    if not root:
        return []

    vertical_order = defaultdict(list)
    dfs(root, 0, 0, vertical_order)

    sorted_dist = sorted(vertical_order.keys(), reverse=True)

    result = []
    for distance in sorted_dist:
        nodes_at_distance = sorted(vertical_order[distance], key=lambda x: x[0])
        result.extend(node[1] for node in nodes_at_distance)

    return result

root = traversal_order(1)
root.left = traversal_order(2)
root.right = traversal_order(3)
root.left.left = traversal_order(4)
root.left.right = traversal_order(5)
root.right.left = traversal_order(6)
root.right.right = traversal_order(7)
root.right.left.right = traversal_order(8)
root.right.right.right = traversal_order(9)

output = vertical_traversal(root)
print("─── ⋆⋅☆⋅⋆ ─────"*3)
print("Output:", output)