package main

import "fmt"

func isAnagram(s string, t string) bool {
	var km = make(map[rune]int)
	for _, ch := range s {
		if v, ok := km[ch]; ok {
			km[ch] = v + 1
		} else {
			km[ch] = 1
		}
	}
	for _, ch := range t {
		if v, ok := km[ch]; ok {
			km[ch] = v - 1
		} else {
			return false
		}
	}

	for _, v := range km {
		if v != 0 {
			return false
		}
	}

	return true
}

func main() {
	fmt.Println(isAnagram("anagram", "nagaram"))
}
