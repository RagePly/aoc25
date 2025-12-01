from typing import Any

def part1(src: str) -> Any:
	s = 50
	c = 0
	for l in src.splitlines():
		a = int(l[1:])

		if l[0] == "L":
			s = (s - a)% 100
		else:
			s = (s +  a) % 100
		
		if s == 0:
			c += 1
	return c

def part2(src: str) -> Any:
	s = 50
	c = 0
	for l in src.splitlines():
		a = int(l[1:])

		for i in range(a):
			if l[0] == "L":
				s = (s - 1) % 100
			else:
				s = (s +  1) % 100
		
			if s == 0:
				c += 1
	return c