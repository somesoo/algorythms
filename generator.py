import random
import numpy as np



data = 4

def create_queue(sid, records):
	np.random.seed(sid)
	table = [0 for i in range(records)]
	for i in range(len(table)):
		table[i] = np.random.randint(10)
	with open('queue.txt', 'w') as file:
		for line in table:
			line_str = [str(line)]  # create string list from integer list
			file.write(" ".join(line_str) + "\n")

def generator(sid, records):
	np.random.seed(sid)
	table = [[0 for i in range(data)] for i in range(records)]
	for i in range(len(table)):
		table[i][0]= i+1
		table[i][1]= abs(int(np.random.normal(loc = 6, scale = 2, size = 1)))
		table[i][2]= np.random.randint(records)
	# print(table)
	with open('100_processes.txt', 'w') as file:
		for line in table:
			line_str = [str(n) for n in line]  # create string list from integer list
			file.write(" ".join(line_str) + "\n")
