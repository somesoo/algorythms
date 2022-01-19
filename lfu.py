class LFU:
    queue = []
    unique_list = []
    current_frame_status = [[0 for x in range(2)] for x in range(3)]
    changes = 0
    def __init__(self, table):
        self.queue = table

    def update_unique(self):
        for x in self.queue:
            temp = [0, 0]
            temp[0] = x[0]
            if temp not in self.unique_list:
                self.unique_list.append(temp)
        # print(self.unique_list)

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
            if int(i[0]) == int(self.queue[curr_time][0]):
                self.unique_list[int(self.queue[curr_time][0])][1] += 1
                i[1] = self.unique_list[int(self.queue[curr_time][0])][1]
                return 1
        return 0

    def update_next_frame(self, table, curr_time):
        if LFU.check_if_exist(self, table, curr_time):
            pass
        else:
            self.changes += 1
            x = LFU.choose_smalest(self, self.current_frame_status)
            # print(x)
            self.current_frame_status[x][0] = int(self.queue[curr_time][0])
            self.unique_list[int(self.queue[curr_time][0])][1] += 1
            self.current_frame_status[x][1] = self.unique_list[int(self.queue[curr_time][0])][1]

    def main_loop(self):
        LFU.update_unique(self)
        for x in range(len(self.queue)):
            LFU.update_next_frame(self, self.queue, x)
        print("LFU\tChanges: ", self.changes)