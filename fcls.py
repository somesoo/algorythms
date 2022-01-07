class FCLS:
	exe_time = 0
	delivered_processes = []
	ended_processes = []
	current_process = []
	processes = []

	def __init__(self, table_of_processes):
		self.processes = table_of_processes
		# count the overall time
		for i in range(len(self.processes)):
			self.exe_time += int(self.processes[i][1])
		# add some extra time - in case there is some time between processes
		self.exe_time += 200
		print(f"Time needed: {self.exe_time}s")

	def check_for_processes(self, time):
		for el in range(len(self.processes)):
			if int(self.processes[el][2]) == time:
				self.delivered_processes.append(self.processes[el])

	def update_waiting_time(self, curr_proc):
		for i in range(len(self.delivered_processes)):
			if self.delivered_processes[i] != curr_proc:
				self.delivered_processes[i][3] = int(self.delivered_processes[i][3]) + 1
	
	def current_process_update(self):
		if len(self.delivered_processes) != 0:
			self.current_process = self.delivered_processes[-1]
			# print("\t\t", self.current_process)
			x = int(self.current_process[1])
			if x == 0:
				self.ended_processes.append(self.delivered_processes[-1])
				del self.delivered_processes[-1]
				FCLS.current_process_update(self)
			else:
				self.current_process[1] = str(x - 1)
			FCLS.update_waiting_time(self, self.current_process)

	def count_wait_time(self):
		overall_waiting_time = 0
		for i in range(len(self.ended_processes)):
			overall_waiting_time += int(self.ended_processes[i][3])
		return overall_waiting_time	 		

	def main_loop(self):
		x, overall, avr = 0, 0, 0
		for i in range(self.exe_time):
			FCLS.check_for_processes(self, i)
			FCLS.current_process_update(self)
			print(i, "\t", self.current_process)
			if len(self.delivered_processes) == 0 and i > self.exe_time/4:
				print(f"everything finished\noverall time used: {x}")
				break
			else:
				x += 1
		# print(self.processes)
		overall = FCLS.count_wait_time(self)
		avr = round(overall/len(self.ended_processes), 2)
		print(f"Overall waiting time: {overall}s")
		print(f"Average waiting time: {avr}s")