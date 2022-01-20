with open("seeds.txt", "r") as fi:
    data = fi.readlines()
for item in range(len(data)):
    data[item] = data[item].split()



for i in range(5):
    x = int(data[i][0])
    print(f"python3 main.py 10_processes_{x}.txt 10_queue_{x}.txt 1 10 {x}")