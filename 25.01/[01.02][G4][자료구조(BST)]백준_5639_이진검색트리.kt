"""
백준 5639 이진 검색 트리 (골드4)

1. 이진탐색트리 일부 구현
2. 전위순회 결과 트리에 주입
3. 후위순회 진행
"""

data class Node(val key: Int, var left: Node? = null, var right: Node? = null)

class BinarySearchTree(var root: Node? = null) {

    fun add(key: Int) {
        if (this.root == null) {
            this.root = Node(key=key)
            return
        } else {
            val leafNode = getLeafNode(node=this.root!!, key=key)
            if (key<leafNode.key) {
                leafNode.left = Node(key=key)
            } else {
                leafNode.right = Node(key=key)
            }
        }
    }

    fun getLeafNode(node: Node, key: Int): Node {
        if (key<node.key) {
            if (node.left==null) {
                return node
            } else {
                return getLeafNode(node=node.left!!, key=key)
            }
        } else {
            if (node.right==null) {
                return node
            } else {
                return getLeafNode(node=node.right!!, key=key)
            }
        }
    }
    
    fun postorderTraversal() {
        fun printKey(node: Node) {
            if (node.left!=null) {
                printKey(node=node.left!!)
            }
            if (node.right!=null) {
                printKey(node=node.right!!)
            }
            println(node.key)
        }
        if (this.root!=null) {
        	printKey(node=this.root!!)    
        }
    }
}

fun main() = with(System.`in`.bufferedReader())  {
    val tree = BinarySearchTree()
    val lst = ArrayList<Int>()

    while(true) {
        try {
            tree.add(key=readLine().toInt())
        } catch(e: Exception) {
            break
        }
    }

    tree.postorderTraversal()
}





