package main

func search(nums []int, target int) int {
	start, end := 0, len(nums)-1
	for start <= end {
		mid := (start + end) / 2
		n := nums[mid]
		if target < n {
			end = mid - 1
		} else if target == n {
			return mid
		} else {
			start = mid + 1
		}
	}
	return -1
}