

class Node:
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right


def preorder(curr_node):
    if curr_node.root == '.':
        return ''

    return curr_node.root + preorder(nodes[curr_node.left]) + preorder(nodes[curr_node.right])


def inorder(curr_node):
    if curr_node.root == '.':
        return ''

    return inorder(nodes[curr_node.left]) + curr_node.root + inorder(nodes[curr_node.right])


def postorder(curr_node):
    if curr_node.root == '.':
        return ''

    return postorder(nodes[curr_node.left]) + postorder(nodes[curr_node.right]) + curr_node.root


if __name__ == "__main__":
    node_num = int(input())
    nodes = {'.': Node('.', None, None)}
    for _ in range(node_num):
        root, left, right = input().split()
        nodes[root] = Node(root, left, right)

    print(preorder(nodes['A']))
    print(inorder(nodes['A']))
    print(postorder(nodes['A']))