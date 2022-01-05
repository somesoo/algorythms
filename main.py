# getting the data from file
with open("testowy.txt", "r") as f:
    processes = f.readlines()
# preparing data to use
for elem in range(len(processes)):
    processes[elem] = processes[elem].split()


processes.sort()
print(processes)

# initalize some needed variable
exe_time = 0
delivered_processes = []
ended_processes = []
current_process = []



# count the overall time
for i in range(len(processes)):
    exe_time += int(processes[i][1])
    # add some extra time - in case there is some time between processes
exe_time += 20
print(exe_time)


def check_for_processes(time):
    # loop looking for processes that has come
    for el in range(len(processes)):
        if int(processes[el][2]) == time:
            delivered_processes.append(processes[el])
            sorting()


def sorting():
    # buble sort for processes that has been recived and are waiting
    for ele in range(len(delivered_processes) - 1):
        for j in range(len(delivered_processes) - 1):
            if int(delivered_processes[j][1]) > int(delivered_processes[j + 1][1]):
                helper = delivered_processes[j]
                delivered_processes[j] = delivered_processes[j + 1]
                delivered_processes[j + 1] = helper
#    print(delivered_processes)


def current_operation(time):
    print(time)


def update_waiting_time():
    for i in range(len(delivered_processes)):
        if i != 0:
            delivered_processes[i][3] = int(delivered_processes[i][3]) + 1
            print(delivered_processes[i][3])


def current_process_update():
    sorting()
    if len(delivered_processes) != 0:
        current_process = delivered_processes[0]
        print("\t\t", current_process)
        x = int(current_process[1])
        if x == 0:
            ended_processes.append(delivered_processes[0])
            del delivered_processes[0]
            current_process_update()
        else:
            current_process[1] = str(x - 1)
        update_waiting_time()

def count_wait_time():
    pass

def main_loop():
    x = 0
    for t in range(exe_time):
        check_for_processes(t)
        current_process_update()
        if len(delivered_processes) == 0 and t>exe_time/4:
            print("everything finished")
            print(f"overal time used: {x}")
            break
        else:
            x += 1
    print(processes)

main_loop()
