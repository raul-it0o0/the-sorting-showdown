import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

# # First create some toy data:
# x = np.linspace(0, 2*np.pi, 400)
# y = np.sin(x**2)

# # Create just a figure and only one subplot
# fig, ax = plt.subplots()
# ax.plot(x, y)
# ax.set_title('Simple plot')

# # Create two subplots and unpack the output array immediately
# f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
# ax1.plot(x, y)
# ax1.set_title('Sharing Y axis')
# ax2.scatter(x, y)

# # Create four polar axes and access them through the returned array
# fig, axs = plt.subplots(2, 2, subplot_kw=dict(projection="polar"))
# axs[0, 0].plot(x, y)
# axs[1, 1].scatter(x, y)

# # Share a X axis with each column of subplots
# plt.subplots(2, 2, sharex='col')

# # Share a Y axis with each row of subplots
# plt.subplots(2, 2, sharey='row')

# # Share both X and Y axes with all subplots
# plt.subplots(2, 2, sharex='all', sharey='all')

# # Note that this is the same as
# plt.subplots(2, 2, sharex=True, sharey=True)

# # Create figure number 10 with a single subplot
# # and clears it if it already exists.
# fig, ax = plt.subplots(num=10, clear=True)

fig, (ax_0_1,ax_1_2,ax_2_4) = plt.subplots(1,3)
ax_0_1.set_title('1 byte integers')
ax_0_1.plot([1,2,3],[4,5,6])

problem_sizes = [100,500,5000,10000,25000,50000,75000,100000]


plt.show()
