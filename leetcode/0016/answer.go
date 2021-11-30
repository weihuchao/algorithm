package main

import (
	"math"
	"sort"
)

func threeSumClosest(nums []int, target int) int {
	sort.Ints(nums)
	nums_count := len(nums)
	current_target := math.MinInt32
	for idx := 0; idx < nums_count-2; idx++ {
		start, end := idx+1, nums_count-1
		for true {
			if start == end || end > nums_count {
				break
			}
			sum := nums[idx] + nums[start] + nums[end]
			if sum == target {
				return target
			}
			if math.Abs(float64(target-sum)) < math.Abs(float64(target-current_target)) {
				current_target = sum
			}
			if sum > target {
				end--
			} else {
				start++
			}
		}
	}
	return current_target
}