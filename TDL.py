import time
import pickle
import os
from task import Task

class Project:
	'''this class is gonna be implemented later'''
	def __init__(self, name):
		self.name = name
	def add_tasks(self, tasks):
		self.tasks = tasks.get_list()
	def get_tasks(self):
		return self.tasks


		#TODO : Add reminders(time alarm, notifactions .....etc)

class ToDoList:
	'''this class is for the to do list tasks,
	 it contains a list (lst) for the new added tasks,
	 and another list for the checked tasks (oldlst), 
	 and a lambda function to display the task with a separator and a line number'''
	def __init__(self, tasks_caption):
		self.tasks_caption = tasks_caption
		self.lst = [] 
		self.oldlst = []
		self.display_func = lambda lst: "".join([str(i) + ' : ' + lst[i] + '\n' + ('-' * 50) + '\n' for i in range(len(lst))])
	def add(self, item):
		self.lst.append(item)

	def save(self, f):
		#change this to somthing else.
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
		
def load(f):
	'''this function takes a file object and return a ToDoList object'''
	c = pickle.load(f)
	return c

def display_main_menu():
	main_menu_str = "-"*15 + "Hello in pyTDL. Wish for you a good luck! :)" + "-"*15 +'''\n 
	The main menu :  \n
	\t1:Add item to the current list.\n
	\t2:Show the current list.\n
	\t3:Show checked list.\n
	\t4:Save list.\n #not working yet.
	\t0:Quit.\n
	'''
	return main_menu_str




######### Main program #########

def main():
	'''this function is just for testing the functionality of ToDoList class'''
	if os.path.exists("lst.tdl"): #saving is not working yet.
		with open("lst.tdl") as f:
			tasks = load(f)
	else:
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
		elif choice == '4': #doesn't work yet, I think because it vouldn't save the lambda func i don't know why!. 
			#os.system('clear || cls')
			#with open("lst.tdl", 'wb') as f:
			#	tasks.save(f)
			continue
		elif choice == '0':
			os.system('clear || cls')
			break

if __name__ == '__main__':
	main()
