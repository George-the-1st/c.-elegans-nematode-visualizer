This is a C. Elegans Nematode brain visualizer visualizing the neurons, and their connections, in a geospacially accurate way.

It's set up to animate the results, and save them, but this can be changed by removing/commenting out 'anim' lines to turn it into an interactive model. You can alternative modify 'anim' or otherwise change things to save a simple png, if you like.

I made it for my own visualization needs. This model can be used as a basis for generating a scene for Blender, for example.

Cheers, and God bless!

![With Connections](c_elegans_neuron_rotation.gif)

![Without, Green=interneuron, Red=sensoryneuron, Blue=motorneuron](c_elegans_neuron_rotation1.gif)

The sources for the mapping come from these two sources:
1. for the synpases (2.1 Connectivity Data, and neuron type data from Fig 2):
    https://www.wormatlas.org/neuronalwiring.html
2. for the neurons:
    https://github.com/bluevex/elegans-atlas/blob/main/