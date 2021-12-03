package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func zigzagLevelOrder(root *TreeNode) [][]int {
	var ret [][]int
	if root == nil {
		return ret
	}
	queue := []*TreeNode{root}

	for len(queue) > 0 {
		var current []int
		queueLen := len(queue)
		for i := 0; i < queueLen; i++ {
			node := queue[i]
			current = append(current, node.Val)
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		queue = queue[queueLen:]
		ret = append(ret, current)
	}

	for idx, val := range ret {
		if idx%2 == 1 {
			for jdx := 0; jdx < len(val)/2; jdx++ {
				val[jdx], val[len(val)-jdx-1] = val[len(val)-jdx-1], val[jdx]
			}
		}
	}
	return ret
}
