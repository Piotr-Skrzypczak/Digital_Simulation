import numpy as np
from parameters import Parameters
from environment.user import User

class BaseStation:
    def __init__(self, cell):
        self.parameters = Parameters(file_name='parameters.json')
        self.max_rb = self.parameters.rb
        self.cell = cell
        self.ues_in_cell = []
        self.rb_usage = 0
        self.bs_off = False
        self.bs_disabling = False
        self.free_rb = self.max_rb

    def next_new_ue(self):
        self.service_time = np.random.randint(low=self.parameters.time_service_min, high=2)

    def add_ue(self):
        self.service_time = np.random.randint(low=self.parameters.time_service_min, high=2)
        ue = User(self.cell)
        if len(self.ues_in_cell) < self.max_rb:
            self.ues_in_cell.append(ue)
            self.bs_usage()
            return ue
        else:
            return

    def gen_ue(self, bs_on):
        random_cell = np.random.randint(0,len(bs_on))
        self.service_time = np.random.randint(low=self.parameters.time_service_min, high=2)
        ue = User(bs_on[random_cell])
        return ue


    def bs_usage(self):
        self.rb_usage = ((len(self.ues_in_cell))/ self.max_rb)*100
        self.free_rb = self.max_rb - len(self.ues_in_cell)


    def ues_to_handover(self):
        return self.ues_in_cell

    def add_user_from_handover(self, ue_from_handover):
        self.ues_in_cell.append(ue_from_handover)
        self.bs_usage()

    def turn_on(self):
        self.bs_off = False



