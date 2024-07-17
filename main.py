import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import csv

neuron_names:list[str] = []
x:list[int] = []
y:list[int] = []
z:list[int] = []

#working with raw data
with open('LowResAtlas.csv', newline='') as csvfile:
    neuron_positions = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in neuron_positions:
        items = row[0].split(',')
        neuron_names.append(items[0])
        x.append(float(items[1]))
        z.append(float(items[2]))
        y.append(float(items[3]))

#plotting/graphig/showing said data
fig = plt.figure(figsize=(15,7))
ax = fig.add_subplot(projection='3d')
ax.scatter(x,y,z, marker='2', alpha=0.5, color='red')
ax.set_box_aspect([10,1,2])

initial_azim:int = 180
ax.view_init(elev=30, azim=initial_azim)

def animate(angle):
    ax.view_init(elev=30, azim=(initial_azim + angle) % 360)


anim = FuncAnimation(fig, animate, frames=range(0, 360), interval=50)

#save animation
anim.save('c_elegans_neuron_rotation.gif', writer='pillow', fps=30)
#plt.show()