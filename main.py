from simulator.main_loop import MainLoop
from environment.bs import BaseStation

import json


if __name__ == "__main__":
    print('Started Simulation')

    main_loop = MainLoop()
    main_loop.run(100000000)
    print('Finish')



