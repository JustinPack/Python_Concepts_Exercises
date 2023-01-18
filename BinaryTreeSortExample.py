# This demonstrates how to sort a binary tree in Python.
# The binary tree is represented as a list of lists.
# The first element of the list is the root node.
# The second element of the list is a list of left nodes.
# The third element of the list is a list of right nodes.
# this is a recursive function that will sort the binary tree.


def BinaryTreeSort(tree):
    if len(tree) > 1:
        BinaryTreeSort(tree[1])
        BinaryTreeSort(tree[2])
    print(tree[0])


# this is the main function of the script
def main():
    # create a binary tree
    tree = [5, [3, [2], [4]], [7, [6], [8]]]
    # sort the binary tree
    BinaryTreeSort(tree)


# call the main function
main()

