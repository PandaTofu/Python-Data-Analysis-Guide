import numpy

data = numpy.random.random(12)

import matplotlib.pyplot as plt

plt.plot(data)

time_label = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec']

plt.xticks(numpy.arange(12), time_label, rotation=45, fontsize='small')

plt.xlabel('X-axis')

plt.yticks(numpy.arange(0,1.1,0.1))

plt.ylabel('Y-axis')

data = numpy.random.randn(5)

fig = plt.figure(figsize=(6.4, 5))

ax = fig.add_subplot(1,1,1)

ax.set_xticks(numpy.arange(5))

ax.set_xticklabels(['t1','t2','t3','t4','t5'], rotation=45)

ax.set_xlabel('X-axis')

ax.set_ylabel('Y-axis')

ax.plot(data)

'X-axis'}

fig, ax_list = plt.subplots(1,2)

for ax in ax_list:
    ax.set(**axis_setting)
