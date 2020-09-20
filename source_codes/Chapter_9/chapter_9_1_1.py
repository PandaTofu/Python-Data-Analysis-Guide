import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4, 5, 3])

plt.savefig('fig9-1.png')

fig = plt.figure(figsize=(10, 10))

fig.suptitle('This is the title of this figure')

fig.subplots(2, 2)

