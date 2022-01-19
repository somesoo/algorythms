from sjf import Sjf
from fcfs import FCFS
from fcls import FCLS
from lfu import LFU
from lru import LRU
import generator
import argparse
import datetime as dt
from multiprocessing import Pool
import threading

parser = argparse.ArgumentParser()
parser.add_argument("data_file", type=str, help="type file with processes")
parser.add_argument("queue_file", type=str, help="type file with queue")

args = parser.parse_args()


# getting the data from file
with open(args.data_file, "r") as f:
    processes = f.readlines()
# preparing data to use
for elem in range(len(processes)):
    processes[elem] = processes[elem].split()

sjf_data = processes.copy()
fcfs_data = processes.copy()
fcls_data = processes.copy()

with open(args.queue_file, "r") as fi:
    queue = fi.readlines()
for item in range(len(queue)):
    queue[item] = queue[item].split()

lru_data = queue.copy()
lfu_data = queue.copy()



sjf_algorythm = Sjf(sjf_data)
fcfs_algorythm = FCFS(fcfs_data)
fcls_algorythm = FCLS(fcls_data)


lfu_algorythm = LFU(lfu_data)
lru_algorythm = LRU(lru_data)


# def run_sfj():
#czas_s = dt.datetime.now()
#with open(args.data_file, "r") as f:
#    processes = f.readlines()
# preparing data to use
#for elem in range(len(processes)):
#    processes[elem] = processes[elem].split()
# print(processes)
#print("SFJ:")
#sjf_algorythm = Sjf(processes)
# sjf_algorythm.main_loop()
#print(dt.datetime.now() - czas_s)
# def run_fcfs():
#with open(args.data_file, "r") as f:
#    processes = f.readlines()
# preparing data to use
#for elem in range(len(processes)):
#    processes[elem] = processes[elem].split()
#print("FCFS")
#fcfs_algorythm = FCFS(processes)
# fcfs_algorythm.main_loop()
# def run_fcls():
#with open(args.data_file, "r") as f:
#    processes = f.readlines()
#    # preparing data to use
#for elem in range(len(processes)):
#   processes[elem] = processes[elem].split()
#print("FCLS")
#fcls_algorythm = FCLS(processes)
# fcls_algorythm.main_loop()
# def run_lru():
#with open(args.queue_file, "r") as fi:
#   queue = fi.readlines()
#for item in range(len(queue)):
#    queue[item] = queue[item].split()
#print("LRU")
#lru_algorythm = LRU(queue.copy())
# lru_algorythm.main_loop()
# def run_lfu():
#with open(args.queue_file, "r") as fi:
#    queue = fi.readlines()
#for item in range(len(queue)):
#    queue[item] = queue[item].split()
#print("LFU")
#lfu_algorythm = LFU(queue.copy())
# lfu_algorythm.main_loop()

# run_lru()
# run_lfu()
# run_sfj()
# run_fcls()
# run_fcfs()

czas_s = dt.datetime.now()
my_foo_obj_list = [sjf_algorythm, fcfs_algorythm, fcls_algorythm, lfu_algorythm, lru_algorythm]
def work(foo):
    foo.main_loop()


pool = Pool()
pool.map(work, my_foo_obj_list)
pool.close()
pool.join()
print(dt.datetime.now() - czas_s)

