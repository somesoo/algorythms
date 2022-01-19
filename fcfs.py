import datetime as dt
class FCFS:
	exe_time = 0
	delivered_processes = []
	ended_processes = []
	current_process = []
	processes = []
	finished_processes = 0

# init object, copy the table, estimate needed time to run
	def __init__(self, table_of_processes):
		self.processes = table_of_processes
		# count the overall time
		for i in range(len(self.processes)):
			self.exe_time += int(self.processes[i][1])
		# add some extra time - in case there is some time between processes
		self.exe_time += 5000
		# print(f"Time needed: {self.exe_time}s")

# check if at the current time any process arrived
	def check_for_processes(self, time):
		for el in range(len(self.processes)):
			if int(self.processes[el][2]) == time:
				self.delivered_processes.append(self.processes[el])

# update waiting time for all processes that has come, and are not currently running
	def update_waiting_time(self):
		for i in range(len(self.delivered_processes)):
			if i != 0:
				self.delivered_processes[i][3] = int(self.delivered_processes[i][3]) + 1
	
# update current process run time, by decreasing it by 1, and check if it has finished
	def current_process_update(self):
		if len(self.delivered_processes) != 0:
			self.current_process = self.delivered_processes[0]
			# print("\t\t", self.current_process)
			x = int(self.current_process[1])
			if x == 0:
				self.ended_processes.append(self.delivered_processes[0])
				del self.delivered_processes[0]
				self.finished_processes += 1
				FCFS.current_process_update(self)
			else:
				self.current_process[1] = str(x - 1)
			FCFS.update_waiting_time(self)

# sum waiting time for all processes at the end
	def count_wait_time(self):
		overall_waiting_time = 0
		for i in range(len(self.ended_processes)):
			overall_waiting_time += int(self.ended_processes[i][3])
		return overall_waiting_time	 		

#using all above functions in correct order to get the finall result
	def main_loop(self):
		czas_s = dt.datetime.now()
		x, overall, avr = 0, 0, 0
		while len(self.processes) != self.finished_processes:
			FCFS.check_for_processes(self, x)
			FCFS.current_process_update(self)
			if x % 1000 == 0:
				print(x, " FCFS\t", self.current_process)
			x += 1
		# print(self.processes)
		print(f"FCFS\teverything finished\n\toverall time used: {x}\n")
		print("FCFS\t", len(self.ended_processes))
		overall = FCFS.count_wait_time(self)
		avr = round(overall/len(self.ended_processes), 2)
		print(f"FCFS\tOverall waiting time: {overall}s")
		print(f"FCFS\tAverage waiting time: {avr}s")
		print("\tFCFS:\t",dt.datetime.now() - czas_s)