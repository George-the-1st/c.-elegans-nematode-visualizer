import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from matplotlib.animation import FuncAnimation
import csv

neuron_names:list[str] = []
neuron_types:list[str] = []
x:list[float] = []
y:list[float] = []
z:list[float] = []
x_sensory:list[float] = []
y_sensory:list[float] = []
z_sensory:list[float] = []
x_motor:list[float] = []
y_motor:list[float] = []
z_motor:list[float] = []
x_inter:list[float] = []
y_inter:list[float] = []
z_inter:list[float] = []
connectome:list[list[tuple[float, float, float], tuple[float, float, float]]] = []

#working with raw data
with open('active data.csv', newline='', encoding='utf-16') as csvfile:
    neuron_positions = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in neuron_positions:
        neuron_data = row[0].split(',')
        neuron_names.append(neuron_data[0])
        neuron_types.append(neuron_data[1])
        x.append(float(neuron_data[2]))
        z.append(float(neuron_data[3]))
        y.append(float(neuron_data[4]))

        if 'sensoryneuron' in (neuron_type := neuron_data[1]):
            x_sensory.append(float(neuron_data[2]))
            y_sensory.append(float(neuron_data[4]))
            z_sensory.append(float(neuron_data[3]))
        elif 'motorneuron' in neuron_type:
            x_motor.append(float(neuron_data[2]))
            y_motor.append(float(neuron_data[4]))
            z_motor.append(float(neuron_data[3]))
        elif 'interneuron' in neuron_type:
            x_inter.append(float(neuron_data[2]))
            y_inter.append(float(neuron_data[4]))
            z_inter.append(float(neuron_data[3]))
        else:
            raise ValueError("Expected a value: sensoryneuron, motorneuron, or interneuron for input data")
        
with open('NeuronConnect.csv', newline='', encoding='utf-8') as csvfile:
    neuron_positions = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in neuron_positions:
        neuron_data = row[0].split(',')
        if neuron_data[0] not in neuron_names or neuron_data[1] not in neuron_names:
            continue
        index_of_neuron1 = neuron_names.index(neuron_data[0])
        index_of_neuron2 = neuron_names.index(neuron_data[1])
        connectome.append([(x[index_of_neuron1],y[index_of_neuron1],z[index_of_neuron1]),(x[index_of_neuron2],y[index_of_neuron2],z[index_of_neuron2])])

line_segments = Line3DCollection(connectome, linewidths=2, alpha=0.025, colors='grey')

#plotting/graphig/showing said data
fig = plt.figure(figsize=(15,7))
ax = fig.add_subplot(projection='3d')
#ax.scatter(x,y,z, marker='2', alpha=0.5, color='grey')
ax.add_collection(line_segments)
ax.scatter(x_sensory,y_sensory,z_sensory, marker='2', alpha=0.5, color='red')
ax.scatter(x_motor,y_motor,z_motor, marker='2', alpha=0.5, color='green')
ax.scatter(x_inter,y_inter,z_inter, marker='2', alpha=0.5, color='blue')
ax.set_box_aspect([10,1,2])

initial_azim:int = 180
ax.view_init(elev=30, azim=initial_azim)

def animate(angle):
    ax.view_init(elev=30, azim=(initial_azim + angle) % 360)


anim = FuncAnimation(fig, animate, frames=range(0, 360), interval=50)

#save animation
anim.save('c_elegans_neuron_rotation.gif', writer='pillow', fps=30)
#show output
plt.show()