import time
import pickle
import os
import display

class Project:
	def __init__(self, name):
		self.name = name
	def add_tasks(self, tasks):
		self.tasks = tasks.get_list()
	def get_tasks(self):
		return self.tasks


		#TODO : Add reminders(time alarm, notifactions .....etc)

class ToDoList(object):
	def __init__(self, tasks_caption):
		self.tasks_caption = tasks_caption
		self.list = []
		self.oldlist = []

	def add(self, item):
		self.list.append(item)

	def save(self, f):
		pickle.dump(self, f)

	def get_list(self):
		return self.list

	def check(self, choice):
		self.oldlist.append( self.list[choice]+ '      ' +time.ctime() )
		del self.list[choice]

	def get_archive(self):
		return self.oldlist

def load(f):
	c = pickle.load(f)
	return c

#########  Menus #########




######### Main program #########

def main():
	tasks = ToDoList('Test tasks')
	while True:
		os.system('clear || cls')
		print(display.display_main_menu())
		choice = input('Enter your choice :')
		if choice == '1':
			item = input('Enter the item : ')
			tasks.add(item)
		elif choice == '2':
			os.system('clear || cls')
			print(display.display_current_list(tasks))
			current_list_choice = input('c : Check\t q: Quit : ').lower()
			if current_list_choice == 'q':
				continue
		elif choice == '3':
			os.system('clear || cls')
			print(display.display_checked_list(tasks))
			checked_list_choice = input('Quit ? (y/n) : ')
			if checked_list_choice == 'y':
				continue
		elif choice == '0':
			os.system('clear || cls')
			break

def testmain():
	#testing the script ---------------------------------------------------------#
	test1 = ToDoList('test1')
	#list1 = ['test1', 'test2', 'test3']
	test1.add('test1')
	test1.add('test2')
	test1.add('test3')
	print ("The list is : ")
	print(test1.get_list())
	print()
	print("The first elemnet done. ")
	test1.check(0)
	print("The list now is :")
	print(test1.get_list())
	test1.check(1)
	print()
	print("Anther elemet checked.")
	print("The list now is : ")
	print(test1.get_list())
	print()
	print("The last list(archive) is : ")
	for i in test1.get_archive():
	        print (i)
	        print('-' * 50)

	test1.add('test for the project')

	print()
	print("Project info: ")
	p1 = Project("progtestpro1")
	p1.add_tasks(test1)
	for tsk in p1.get_tasks():
		print(tsk)
	print ('Saving.....')
	flist1 = open('list1.tdl', 'wb')
	test1.save(flist1)
	print('Saved.')
	flist1.close()
	print()
	flist2 = open('list1.tdl', 'rb')
	print('Loading....')
	list2 = load(flist2)
	print('Loaded.')
	flist2.close()
	print(list2.get_list())
	print()
	print(list2.get_archive())

if __name__ == '__main__':
	#testmain()
	main()
