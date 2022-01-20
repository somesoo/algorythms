from sjf import Sjf
from fcfs import FCFS
from fcls import FCLS
from lfu import LFU
from lru import LRU
import generator as gen
import argparse
import datetime as dt
from multiprocessing import Pool

parser = argparse.ArgumentParser()
parser.add_argument(dest="data_file", type=str, help="type file with processes")
parser.add_argument(dest="queue_file", type=str, help="type file with queue")
parser.add_argument(dest="use_generator", type=int, help="choose if you would like to use generators")
parser.add_argument(dest="number_of_processes", type=int, help="type number of processes")
parser.add_argument(dest="seed", type=int, help="seed that will be used")

args = parser.parse_args()

seed = args.seed
num_of_p = args.number_of_processes

# as arguments you need to provide seed and number of processes
if args.use_generator:
    gen.create_queue(seed, num_of_p, args.queue_file)
    gen.generator(seed, num_of_p, args.data_file)

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

my_foo_obj_list = [sjf_algorythm, fcfs_algorythm, fcls_algorythm, lfu_algorythm, lru_algorythm]
#my_foo_obj_list = [sjf_algorythm]
def work(foo):
    foo.main_loop()

pool = Pool()
pool.map(work, my_foo_obj_list)
pool.close()
pool.join()
