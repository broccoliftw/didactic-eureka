from random import *
class gameStatus():
	def __init__(self):
		self.sequence = ["s" for i in range(20)]
		self.current = 0
		self.done = 1
	
	def change_seq(self):
		for i in range(len(self.sequence)):
			self.sequence[i] = add_random_key()
	def check(self,s):
		if self.sequence[self.current] == s:
			return True
		else:
			return False
	def increase(self):
		if self.current == 19:
			self.current = 0
			self.done = 1
		else:
			self.current += 1
			
def add_random_key():
	n = randint(0,10)
	print("n = " + str(n))
	return look_up(n)
	
def look_up(n):
	return {
		0: "q",
        1: "e",
		2: "r",	
		3: "a",
		4: "d",
		5: "w",
		6: "f",
		7: "s",
		8: "z",
		9: "x",
		10: "c",
	}[n]
			