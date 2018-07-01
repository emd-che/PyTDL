import time
import pickle
import os
from task import Task

class Project:
	def __init__(self, name):
		self.name = name
	def add_tasks(self, tasks):
		self.tasks = tasks.get_list()
	def get_tasks(self):
		return self.tasks


		#TODO : Add reminders(time alarm, notifactions .....etc)

class ToDoList:
	def __init__(self, tasks_caption):
		self.tasks_caption = tasks_caption
		self.lst = [] #lst -> list
		self.oldlst = []
		self.display_func = lambda lst: "".join([str(i) + ' : ' + lst[i] + '\n' + ('-' * 50) + '\n' for i in range(len(lst))])
	def add(self, item):
		self.lst.append(item)

	def save(self, f):
		pickle.dump(self, f)

	def get_list(self):
		return self.lst

	def check(self, choice):
		self.oldlst.append( self.lst[choice]+ '      ' +time.ctime() )
		del self.lst[choice]

	def get_archive(self):
		return self.oldlst


	def display_current_list(self):
		current_list_str = 'The current list: \n\n'  + self.display_func(self.get_list()) + '\n\n'
		return current_list_str

	def display_checked_list(self):
		checked_list_str = 'The checked list: \') \n' + self.display_func(self.get_archive()) + '\n\n'
		return checked_list_str
		


def display_main_menu():
	main_menu_str = "-"*15 + "Hello in pyTDL. Wish for you a good luck! :)" + "-"*15 +'''\n 
	The main menu :  \n
	\t1:Add item to the current list.\n
	\t2:Show the current list.\n
	\t3:Show checked list.\n
	\t0:Quit.\n
	'''
	return main_menu_str

def load(f):
	c = pickle.load(f)
	return c


######### Main program #########

def main():
	tasks = ToDoList('Test tasks')
	while True:
		os.system('clear || cls')
		print(display_main_menu())
		choice = input('Enter your choice :')
		if choice == '1':
			title = input('Enter the task\'s title : ')
			desc = input('Enter the tasks\'s description: ')
			item = Task(title, desc)
			tasks.add(str(item))
		elif choice == '2':
			os.system('clear || cls')
			#print(display.display_current_list(tasks))
			print(tasks.display_current_list())
			current_list_choice = input('c : Check\t q: Quit : ').lower()
			if current_list_choice == 'c':
				checked = int(input("enter the task number: "))
				tasks.check(checked)
			elif current_list_choice == 'q':
				continue
		elif choice == '3':
			os.system('clear || cls')
			print(tasks.display_checked_list())
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
