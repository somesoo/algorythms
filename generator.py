import random
import numpy as np
 
def init_message():
	print("zaimportowano generator")

init_message()


records = 100000
data = 4
def fill_table_randomly():
	table = [[0 for i in range(data)] for i in range(records)]
	for i in range(len(table)):
		table[i][0]= i+1
		table[i][1]= np.random.randint(200)
		table[i][2]= np.random.randint(300)
	# print(table)
	with open('100_processes.txt', 'w') as file:
		for line in table:
			line_str = [str(n) for n in line]  # create string list from integer list
			file.write(" ".join(line_str) + "\n")


def create_queue():
	table = [0 for i in range(records)]
	for i in range(len(table)):
		table[i] = np.random.randint(10)
	with open('queue.txt', 'w') as file:
		for line in table:
			line_str = [str(line)]  # create string list from integer list
			file.write(" ".join(line_str) + "\n")

create_queue()
fill_table_randomly()
