import numpy as np
from parameters import Parameters

class User:
    def __init__(self, cell):
        self.rb_per_ue = 1
        self.parameters = Parameters(file_name='parameters.json')
        self.serving_cell = cell
        self.service_time = np.random.randint(low=self.parameters.time_service_min,
                                              high=self.parameters.time_service_max)




    def execute(self):
        return None






