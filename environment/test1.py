# import numpy as np
#
# n = 10000
# # np.random.seed(1)
# time_between_calls = np.random.exponential(scale=4, size = n)
# srednia = time_between_calls.mean()
# print(1)
#
#
#
# sr=np.random.randint(low=1,high=10, size = 1000)
#
# sr1 =sr.mean()
# print(2)

from sortedcontainers import SortedList

sorted_list = SortedList([])
sorted_list.add(5)

print(sorted_list[0])