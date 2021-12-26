# getting the data from file
with open("testowy.txt", "r") as f:
    processes = f.readlines()
# preparing data to use
for elem in range(len(processes)):
    processes[elem] = processes[elem].split()

print(processes)
exe_time = 0
delivered_processes = []
ended_processes = []

# count the overall time
for i in range(len(processes)):
    exe_time += int(processes[i][1])
    # add some extra time
exe_time += 20
print(exe_time)


def sorting():
    for ele in range(len(delivered_processes) - 1):
        for j in range(len(delivered_processes) - 1):
            if int(delivered_processes[j][1]) > int(delivered_processes[j + 1][1]):
                helper = delivered_processes[j]
                delivered_processes[j] = delivered_processes[j + 1]
                delivered_processes[j + 1] = helper
#    print(delivered_processes)


def check_for_processes(time):
    # loop looking for processes that has come
    for el in range(len(processes)):
        if int(processes[el][2]) == time:
            delivered_processes.append(processes[el])
            sorting()


def current_operation(time):
    print(time)


def current_process_update():
    sorting()
    if len(delivered_processes) != 0:
        current_process = delivered_processes[0]
        print("\t", current_process)
        x = int(current_process[1])
        if x == 0:
            ended_processes.append(delivered_processes[0])
            del delivered_processes[0]
            current_process_update()
        else:
            current_process[1] = str(x - 1)


def main_loop():
    for t in range(exe_time):
        check_for_processes(t)
        current_process_update()
        if len(delivered_processes) == 0 and t>exe_time/2:
            print("everything finished")
            break


main_loop()
