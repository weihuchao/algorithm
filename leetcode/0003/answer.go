package main

func max(v1, v2 int) int {
	if v1 >= v2 {
		return v1
	} else {
		return v2
	}
}

func lengthOfLongestSubstring(s string) int {
	ret, lastIndex, lastMap := 0, -1, make(map[int32]int)

	for idx, v := range s {
		if i, ok := lastMap[v]; ok && i > lastIndex {
			lastIndex = i
		}
		ret = max(ret, idx-lastIndex)
		lastMap[v] = idx
	}
	return ret
}