
def displaying_list(list1):
	list_str = ''
	for i in range(len(list1)):
		list_str += str(i) + ' : ' + list1[i] + '\n' + ('-' * 50) + '\n'
	return list_str 

def display_main_menu():
	main_menu_str = "-"*15 + "Hello in todo list. Wish for you a good luck! :)" + "-"*15 +'''\n 
	The main menu :  \n
	\t1:Add item to the current list.\n
	\t2:Show the current list.\n
	\t3:Show checked list.\n
	\t0:Quit.\n
	'''
	return main_menu_str




def display_current_list(current_list):
	current_list_str = 'The current list: \n\n'  + displaying_list(current_list.get_list()) + '\n\n'
	return current_list_str


def display_checked_list(checkedlist):
	checked_list_str = '''The checked list: ') \n
	''' + displaying_list(checkedlist.get_archive()) + '\n\n'
	return checked_list_str
