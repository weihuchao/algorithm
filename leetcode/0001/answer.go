package main

func twoSum(nums []int, target int) (ret []int) {
	targetMap := make(map[int]int)
	for idx, val := range nums {
		if v, ok := targetMap[val]; ok {
			return []int{idx, v}
		} else {
			targetMap[target-val] = idx
		}
	}
	return
}
