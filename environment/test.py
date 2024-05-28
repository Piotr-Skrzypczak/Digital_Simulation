import numpy as np
# import matplotlib.pyplot as plt
#
#
# def poisson_process(lambda_intensity):
#     # Generowanie liczby zdarzeń z rozkładu Poissona
#     num_events = np.random.poisson(lambda_intensity)
#
#     service_time = np.random.randint(low=0, high=30, size=num_events)
#     print(num_events)
#     print(service_time)
#     print('---------------------')
#     return num_events
#
#
# # Parametry
# lambda_intensity = 0.75  # Intensywność zdarzeń na jednostkę czasu
#
# T = 10  # Całkowity czas symulacji
# for i in range (T):
#     # Generowanie procesu Poissona
#     event_times = poisson_process(lambda_intensity)
#
# # Wyświetlanie wyników
# print("Czasy zdarzeń:", event_times)

#
# h=[]
#
lambda_intensity = 0.75
tau = np.random.exponential(1 / lambda_intensity)
print(tau)