import numpy as np

data = 4

def create_queue(sid, records, f_name):
	np.random.seed(sid)
	rad = 10
	table = [0 for i in range(records)]
	for i in range(len(table)):
		table[i] = np.random.randint(rad)
	with open(f_name, 'w') as file:
		for line in table:
			line_str = [str(line)]  # create string list from integer list
			file.write(" ".join(line_str) + "\n")

def generator(sid, records, f_name):
	np.random.seed(sid)
	table = [[0 for i in range(data)] for i in range(records)]
	for i in range(len(table)):
		table[i][0]= i+1
		table[i][1]= abs(int(np.random.normal(loc = 6, scale = 2, size = 1)))
		table[i][2]= np.random.randint(records)
	with open(f_name, 'w') as file:
		for line in table:
			line_str = [str(n) for n in line]  # create string list from integer list
			file.write(" ".join(line_str) + "\n")