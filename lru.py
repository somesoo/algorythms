class LRU:
    queue = []
    current_frame_status = [[0 for x in range(2)] for x in range(3)]
    changes = 0
    def __init__(self, table):
        self.queue = table

    def choose_smalest(self, status):
        if status[0][1] <= status[1][1] and status[0][1] <= status[2][1]:
            return 0
        elif status[1][1] <= status[2][1] and status[1][1] <= status[0][1]:
            return 1
        elif status[2][1] <= status[0][1] and status[2][1] <= status[1][1]:
            return 2
        else:
            return -1

    def check_if_exist(self, table, curr_time):
        for i in self.current_frame_status:
            if i[0] == int(self.queue[curr_time][0]):
                i[1] = curr_time+1
                return 1
        return 0

    def update_next_frame(self, table, curr_time):
        if LRU.check_if_exist(self, table, curr_time):
            pass
        else:
            self.changes += 1
            x = LRU.choose_smalest(self, self.current_frame_status)
            # print(x)
            self.current_frame_status[x][0] = int(self.queue[curr_time][0])
            self.current_frame_status[x][1] = curr_time+1

    def main_loop(self):
        for x in range(len(self.queue)):
            LRU.update_next_frame(self, self.queue, x)
            # print(self.current_frame_status)
        print("LRU\tChanges: ", self.changes)    
