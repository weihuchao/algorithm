package main

func merge(nums1 []int, m int, nums2 []int, n int) {
	idx := m + n
	for true {
		if m == 0 || n == 0 {
			break
		}
		idx --
		if nums2[n-1] < nums1[m-1] {
			nums1[idx] = nums1[m-1]
			m--
		} else {
			nums1[idx] = nums2[n-1]
			n--
		}
	}
	for idx := 0; idx < n; idx++ {
		nums1[idx] = nums2[idx]
	}
}
