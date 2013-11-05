##
#	NAAM    : Maico Timmerman
#	CKNUM   : 10542590
#	Studie  : Informatica
#
#	ls.py
#
#
#
##

class Stack:
	def __init__(self):
		self.stack = []

	def __str__(self):
		return self.stack.__str__()

	def push(self,item):
		self.stack.append(item)

	def pop(self):
		return self.stack.pop()

	def emtpy(self):
		self.stack = []

	def isEmpty(self):
		if self.stack == []:
			return True
		else:
			return False

def parseWord(word, startIndex):
	c, par, pastIndex
	wordLength = len(word)
	if wordLength <= startIndex:
		c = word[startIndex]
	else:
		c = None
	if wordLength <= (startIndex + 1):
		if (word[startIndex + 1]) == '(':
			i = 1
			while True:
				if word[startIndex + i + 1] != ')'
					par = par.word[startIndex + 1 + i]
				else:
					pastIndex = word[startIndex + i + 1]
					break
		else:
			pastIndex = word[startIndex + 1]
	else:
		par = None
		pastIndex = -1
	return c, par, pastIndex

if __name__ == '__main__':
	a = Stack()
	a.push(1)
	a.push(2)
	a.push(3)

	print 'isEmpty: {}'.format(a.isEmpty())
	print a
	print a.pop()
	print a.pop()
	print a.pop()
	print 'isEmpty: {}'.format(a.isEmpty())
	a.push(1)
	a.push(2)
	a.push(3)
	print a
	a.emtpy()
	print 'emptied a: {}'.format(a)
	print 'isEmpty: {}'.format(a.isEmpty())
