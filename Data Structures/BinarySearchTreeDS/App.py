from BinarySearchTreeDS.BinarySearchTree import BST

bst = BST()

bst.insert(12)
bst.insert(10)
bst.insert(1)
bst.insert(-5)

bst.traverse()

bst.remove(10)
print("\n")
bst.traverse()

print(("\n"))

print(bst.getMax())
print(bst.getMin())