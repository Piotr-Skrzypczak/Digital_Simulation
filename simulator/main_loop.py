from parameters import Parameters
from environment.bs import BaseStation
from environment.user import User
import numpy as np
import math


class MainLoop:
    def __init__(self) -> None:

        self.parameters = Parameters(file_name = 'parameters.json')
        self.bs_count = self.parameters.bs_count
        self.bs_usages = np.zeros(self.parameters.bs_count)
        self.lambda_intensity = self.parameters.lambda_intensity
        self.processes = []
        self.H = self.parameters.H
        self.L = self.parameters.L
        self.lost_ues = 0
    def sort_proceses(self):
        self.processes = sorted(self.processes, key=lambda proces1: proces1.service_time)

    def decrement_time(self, time):
        for proces in self.processes:
            proces.service_time -= time

    def count_of_bs_on(self):
        bs_on = 0
        for bs in self.bses:
            bs.bs_usage()
            if bs.bs_off == False:
                bs_on += 1
        return bs_on


    def execute_process(self):
        idx = 0
        bs_on = []
        for bs in self.bses:
            if bs.bs_off == False:
                bs_on.append(bs.cell)

        while True:
            if self.processes[idx].service_time == 0:

                if isinstance(self.processes[idx], BaseStation):
                    if self.processes[idx].bs_off == True:
                        ue = self.processes[idx].gen_ue(bs_on)
                        self.processes.append(ue)
                        self.bses[ue.serving_cell].ues_in_cell.append(ue)
                        idx += 1
                    else:
                        ue = self.processes[idx].add_ue()
                        if ue != None:
                            self.processes.append(ue)
                            idx += 1
                        else:
                            self.lost_ues+=1

                elif isinstance(self.processes[idx], User):
                    try:
                        self.bses[self.processes[idx].serving_cell].ues_in_cell.remove(self.processes[idx])

                    except ValueError as e:
                        print('error1')
                    try:
                        self.processes.remove(self.processes[idx])
                    except ValueError as e:
                        print('error2')

            else:
                break

    def energy_saving_off(self):
        bs_on = self.count_of_bs_on()
        if bs_on > 1:
            # exceeding level L:
            for bs in self.bses:
                if bs.bs_off != True and bs.rb_usage < self.L:
                    list_ues_to_handover = bs.ues_to_handover()
                    bs.bs_disabling = True
                    idx_bs_to_off = bs.cell
                    for bs in self.bses:
                        if bs.bs_off != True and bs.rb_usage >= self.L and bs.rb_usage > self.H:
                            return
                    break
            else:
                return
            # handover
            while (len(list_ues_to_handover)!=0):
                previous_count = len(list_ues_to_handover)
                for bs in self.bses:
                    if len(list_ues_to_handover) == 0:
                        break
                    elif bs.bs_disabling != True and bs.bs_off != True and bs.rb_usage < 100:
                        bs.ues_in_cell.append(list_ues_to_handover[0])
                        list_ues_to_handover[0].serving_cell = bs.cell
                        bs.bs_usage()
                        del list_ues_to_handover[0]
                if previous_count == len(list_ues_to_handover):
                    print(1)
                    self.lost_ues +=1
                    del list_ues_to_handover[0]

            self.bses[idx_bs_to_off]
            self.bses[idx_bs_to_off].bs_disabling = False
            self.bses[idx_bs_to_off].bs_off = True
            self.bses[idx_bs_to_off].service_time = 1
            print(f'BS OFF {idx_bs_to_off}')

    def energy_saving_on(self):

        bs_on = self.count_of_bs_on()
        if bs_on ==self.bs_count:
            return
        for bs in self.bses:
            if bs.bs_off == True:
                bs_to_turn_on_idx = bs.cell
                break


        #exceeding level H
        for bs in self.bses:
            if bs.rb_usage > self.H:
                break

        # turning ON BS and handovers
        self.bses[bs_to_turn_on_idx].turn_on()
        sum = 0
        for bs in self.bses:
             if bs.bs_off != True:
                 sum += len(bs.ues_in_cell)
        avg_rb_in_cell = sum / (bs_on + 1)

        for bs in self.bses:
            if bs.bs_off != True:
                ues_to_handover = math.ceil(len(bs.ues_in_cell) - avg_rb_in_cell)
                for ue in range(ues_to_handover):
                    bs.ues_in_cell[0].serving_cell = bs_to_turn_on_idx
                    try:
                        self.bses[bs_to_turn_on_idx].ues_in_cell.append(bs.ues_in_cell[0])
                    except ValueError as e:
                        print('error3')
                    try:
                        bs.ues_in_cell.remove(bs.ues_in_cell[0])
                    except:
                        print('error 4')
        print(f'BS ON {bs_to_turn_on_idx}')


    def run(self, max_time):

        #MAIN LOOP
        time = 0

        #init BSes and UE
        for idx in range(self.bs_count):
            self.processes.append(BaseStation(idx))
            self.processes[idx].next_new_ue()
        self.bses = self.processes.copy()
        self.sort_proceses()



        while time < max_time:
            time += self.processes[0].service_time
            self.decrement_time(self.processes[0].service_time) # todo tak nie moze zostac
            self.execute_process()
            self.sort_proceses()
            if time > self.parameters.start_energy_saving:
                self.energy_saving_off()
                self.sort_proceses()
                self.energy_saving_on()
                self.sort_proceses()






            



