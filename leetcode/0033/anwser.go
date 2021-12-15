package main

func search(nums []int, target int) int {
	n := len(nums)
	start, end := 0, n-1

	for start <= end {
		mid := (start + end) / 2
		if nums[mid] == target {
			return mid
		}
		if nums[0] <= nums[mid] {
			if nums[0] <= target && target < nums[mid] {
				end = mid - 1
			} else {
				start = mid + 1
			}
		} else {
			if nums[mid] < target && target <= nums[n-1] {
				start = mid + 1
			} else {
				end = mid - 1
			}
		}
	}
	return -1
}
