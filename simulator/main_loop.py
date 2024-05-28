from parameters import Parameters
from environment.bs import BaseStation
from environment.user import User
import numpy as np



def sort_usage(utilize_RBs):

    utilize_RBs_idx = np.arange(len(utilize_RBs))

    combined = list(zip(utilize_RBs, utilize_RBs_idx))
    sorted_combined = sorted(combined)

    utilize_RBs, utilize_RBs_idx = zip(*sorted_combined)

    utilize_RBs = list(utilize_RBs)
    utilize_RBs_idx = list(utilize_RBs_idx)

    return utilize_RBs, utilize_RBs_idx

class MainLoop:
    def __init__(self) -> None:

        self.parameters = Parameters(file_name = 'parameters.json')
        self.bs_count = self.parameters.bs_count
        self.BSes = np.empty(self.parameters.bs_count, dtype = object)
        self.bs_usage = np.zeros(self.parameters.bs_count)
        self.lambda_intensity = self.parameters.lambda_intensity





    def run(self, max_time):

        #MAIN LOOP
        time=0

        #init BSes and UE
        for i in range(self.bs_count):
            self.BSes[i] = BaseStation()
        user = User()

        count = 0
        while time < max_time:

            print(f'Simulation time:{time} ms')
            
            for bs in range(self.bs_count):


                service_time = user.new_user(self.lambda_intensity)
                print(f'BS idx: {bs}, Usage: {self.BSes[bs].bs_usage()}, New user: {service_time}')
                overload_users = self.BSes[bs].add_user(service_time)
                print(self.BSes[bs].service_times_bs)
                if overload_users:
                    utilize_RBs_per_BS = np.zeros(self.bs_count)
                    for bs_I in range(self.bs_count):
                        utilize_RBs_per_BS[bs_I] = self.BSes[bs_I].bs_usage()
                    utilize_RBs_per_BS, utilize_RBs_idx_BS = sort_usage(utilize_RBs_per_BS)
                    for bs_I in utilize_RBs_idx_BS:
                        overload_users = self.BSes[bs_I].add_user(overload_users)
                        if not overload_users:
                            break
                    if overload_users:
                        count+=len(overload_users)

            time +=1
            for bs in range(self.bs_count):
                self.BSes[bs].counter()



        print(count)


