import matplotlib.pyplot as plt
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

ax = plt.figure(figsize=(15,7)).add_subplot(projection='3d')
ax.scatter(x,y,z, marker='2', alpha=0.5, color='red')
ax.set_box_aspect([10,1,2])
plt.show()