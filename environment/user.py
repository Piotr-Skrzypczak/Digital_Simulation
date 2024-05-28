import numpy as np
from parameters import Parameters

class User:
    def __init__(self):
        self.RB_ue = 1
        self.parameters = Parameters(file_name='parameters.json')
    def new_user(self, lambda_intensity):
        num_events = np.random.poisson(lambda_intensity)
        service_time = np.random.randint(low=self.parameters.time_service_min, high=self.parameters.time_service_max, size=num_events)

        return service_time



