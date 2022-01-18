from sjf import Sjf
from fcfs import FCFS
from fcls import FCLS
from lfu import LFU
from lru import LRU
import generator
import argparse

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

with open(args.queue_file, "r") as fi:
    queue = fi.readlines()
for item in range(len(queue)):
    queue[item] = queue[item].split()

def run_sfj():
    # print(processes)
    print("SFJ:")
    sjf_algorythm = Sjf(processes)
    sjf_algorythm.main_loop()
def run_fcfs():
    print("FCFS")
    fcfs_algorythm = FCFS(processes)
    fcfs_algorythm.main_loop()
def run_fcls():
    print("FCLS")
    fcls_algorythm = FCLS(processes)
    fcls_algorythm.main_loop()
def run_lru():
    print("LRU")
    lru_algorythm = LRU(queue.copy())
    lru_algorythm.main_loop()
def run_lfu():
    print("LFU")
    lfu_algorythm = LFU(queue.copy())
    lfu_algorythm.main_loop()

# run_lru()
# run_lfu()
run_sfj()
run_fcls()
run_fcfs()