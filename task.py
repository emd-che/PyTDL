class Task:
	def __init__(self, caption, desc):
		self.caption = caption
		self.desc = desc

	def __str__(self):
		return "\"{}\"  :\n\t{}".format(self.caption, self.desc)




if __name__ == '__main__':
	t1 = Task('test', 'this is a desc test')
	print(t1)