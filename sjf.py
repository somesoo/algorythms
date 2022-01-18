class Sjf:
    # initialize some needed variable
    exe_time = 0
    delivered_processes = []
    ended_processes = []
    current_process = []
    processes = []

# init object, copy the table, estimate needed time to run
    def __init__(self, table_of_processes):
        self.processes = table_of_processes
        # count the overall time
        for i in range(len(self.processes)):
            self.exe_time += int(self.processes[i][1])
        # add some extra time - in case there is some time between processes
        self.exe_time += 50
        print(f"Time needed: {self.exe_time}s")

# buble sort delivered processes by their exe time
    def sorting(self):
        for ele in range(len(self.delivered_processes) - 1):
            for j in range(len(self.delivered_processes) - 1):
                if int(self.delivered_processes[j][1]) > int(self.delivered_processes[j + 1][1]):
                    helper = self.delivered_processes[j]
                    self.delivered_processes[j] = self.delivered_processes[j + 1]
                    self.delivered_processes[j + 1] = helper
    #    print(self.delivered_processes)

# check if at the current time any process arrived
    def check_for_processes(self, time):
        for el in range(len(self.processes)):
            if int(self.processes[el][2]) == time:
                self.delivered_processes.append(self.processes[el])
                Sjf.sorting(self)

# update waiting time for all processes that has come, and are not currently running
    def update_waiting_time(self):
        for i in range(len(self.delivered_processes)):
            if i != 0:
                self.delivered_processes[i][3] = int(self.delivered_processes[i][3]) + 1
                # print(self.delivered_processes[i][3])

# update current process run time, by decreasing it by 1, and check if it has finished
    def current_process_update(self):
        Sjf.sorting(self)
        if len(self.delivered_processes) != 0:
            self.current_process = self.delivered_processes[0]
            # print("\t\t", self.current_process)
            x = int(self.current_process[1])
            if x == 0:
                self.ended_processes.append(self.delivered_processes[0])
                del self.delivered_processes[0]
                Sjf.current_process_update(self)
            else:
                self.current_process[1] = str(x - 1)
                Sjf.update_waiting_time(self)

# sum waiting time for all processes at the end
    def count_wait_time(self):
        overall_waiting_time = 0
        for i in range(len(self.ended_processes)):
            overall_waiting_time += int(self.ended_processes[i][3])
        return overall_waiting_time

# using all above functions in correct order to get the finall result
    def main_loop(self):
        x, overall, avr = 0, 0, 0
        for i in range(self.exe_time):
            Sjf.check_for_processes(self, i)
            Sjf.current_process_update(self)
            if len(self.delivered_processes) == 0 and i > self.exe_time / 4:
                print(f"everything finished\noverall time used: {x}")
                break
            else:
                x += 1
                # print(f"{i} \t {self.current_process}")
        overall = Sjf.count_wait_time(self)
        avr = round(overall / len(self.ended_processes), 2)
        print(f"Overall waiting time: {overall}s")
        print(f"Average waiting time: {avr}s")
