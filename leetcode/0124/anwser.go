package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

var ret int

func maxPathSum(root *TreeNode) int {
	ret = root.Val
	getChildMax(root)
	return ret
}

func getChildMax(node *TreeNode) int {
	if node == nil {
		return 0
	}
	leftMax := max(0, getChildMax(node.Left))
	rightMax := max(0, getChildMax(node.Right))
	ret = max(ret, node.Val+leftMax+rightMax)
	return node.Val + max(leftMax, rightMax)
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
