import numpy as np
from parameters import Parameters

class User:
    def __init__(self, cell, service_time):
        self.rb_per_ue = 1
        self.parameters = Parameters(file_name='parameters.json')
        self.serving_cell = cell
        self.service_time = service_time




    def execute(self):
        return None






