package main

func maxSubArray(nums []int) int {
	ret := nums[0]
	addMax := ret
	for _, num := range nums[1:] {
		addMax = max(num+addMax, num)
		ret = max(ret, addMax)
	}
	return ret
}

func max(x, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}