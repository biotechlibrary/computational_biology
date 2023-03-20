import networkx as nx
import matplotlib.pyplot as plt

neuron = nx.Graph()
neuron.add_nodes_from(['axon', 'soma'])
neuron.add_notes_from(['dendrite' + str(i) for i in range(4)])
neuron.add_nodes_from(['synapse' + str(i) for i in range(8)])


neuron.add_edges_from([('axon', 'soma'])
neuron.add_edges_from([('dendrite()', 'synapse2'), ('dendrite1', 'synapse3')])
neuron.add_edges_from([('dendrite2', 'synapse4'), ('dendrite3', 'synapse5')])
neuron.add_edges_from([('synapse()', 'synapse2'), ('synapse2', 'synapse4')])                                                   
neuron.add_edges_from([('synapse1', 'synapse3'), ('synapse3', 'synapse5')])
neuron.add_edges_from([('synapse4', 'synapse6'), ('synapse5', 'synapse7')])                       
              
nx.draw(neuron, with_labels= True)
plt.show()
