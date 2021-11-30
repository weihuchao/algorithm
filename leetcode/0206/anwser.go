package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	var pre *ListNode
	node := head
	for node != nil {
		next := node.Next
		node.Next = pre
		pre, node = node, next
	}
	return pre
}
