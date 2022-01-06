from sjf import Sjf
import generator
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("data_file", type=str, help="type file with processes")
args = parser.parse_args()


# getting the data from file
with open(args.data_file, "r") as f:
    processes = f.readlines()
# preparing data to use
for elem in range(len(processes)):
    processes[elem] = processes[elem].split()

processes.sort()
# print(processes)

sjf_algorythm = Sjf(processes)
sjf_algorythm.main_loop()

