package main

func fib(n int) int {
	p, h := 0, 1
	for i := 0; i < n; i++ {
		p, h = h, p+h
	}
	return p
}
