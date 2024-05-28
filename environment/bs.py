import numpy as np
from parameters import Parameters

class BaseStation:
    def __init__(self):
        self.parameters = Parameters(file_name='parameters.json')
        self.RB = self.parameters.rb
        self.service_times_bs = np.full(self.RB, -1)


    def add_user(self, service_time_ue):
        free_RB = False
        overload_users = []
        for serv_time in service_time_ue:
            for rb in range(self.RB):
                if self.service_times_bs[rb] == -1:
                    self.service_times_bs[rb] = serv_time
                    self.service_times_bs = sorted(self.service_times_bs, key=lambda x: (x <= -1, x))
                    free_RB = True
                    break
            if free_RB == False:
                overload_users.append(serv_time)
        return overload_users


    def bs_usage(self):
        utilize_rb=0
        for i in self.service_times_bs:
            if self.service_times_bs[i] != -1:
                utilize_rb += 1
        return utilize_rb


    def counter(self):
        self.service_times_bs = [x - 1 if x >= 2 else -1 for x in self.service_times_bs]
        self.service_times_bs = sorted(self.service_times_bs, key=lambda x: (x <= -1, x))


