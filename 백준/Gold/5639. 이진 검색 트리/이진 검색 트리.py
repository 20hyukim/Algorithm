class Node:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None



def get_nodes():
    root_num = int(input())
    root_node = Node(root_num)

    while True:
        try:
            new_node = Node(int(input()))
            cur_node = root_node

            while True:
                if new_node.root < cur_node.root:
                    if cur_node.left is None:
                        cur_node.left = new_node
                        break
                    else:
                        cur_node = cur_node.left

                else:
                    if cur_node.right is None:
                        cur_node.right = new_node
                        break
                    else:
                        cur_node = cur_node.right
        except:
            return root_node


def postorder(root_node):
    stack = []
    cur_node = root_node

    while root_node:
        if cur_node.left:
            stack.append(cur_node)
            cur_node = cur_node.left
            continue
        elif cur_node.right:
            stack.append(cur_node)
            cur_node = cur_node.right
            continue
        else:
            print(cur_node.root)
            if stack:
                last_visit = stack.pop()
                if last_visit.left == cur_node:
                    last_visit.left = None
                else:
                    last_visit.right = None
                cur_node = last_visit
            else:
                break


if __name__ == "__main__":
    root_node = get_nodes()
    postorder(root_node)