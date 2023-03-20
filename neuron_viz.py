import matplotlib.pyplot as plt

class NeuronVisualizer:
  def __init__(self,neuron):
    self.neuron = neuron
    self.fig = plt.figure()
    self.ax = self.fig.add_subplot(111, projection= '3d')
    
    def visualize(self):
      x,y,z = [], [], []
      sizes = []
      
        for dendrite in self.neuron.dendtrites:
          x.append(dendrite.position[0])
          y.append(dendrite.position[1])
          z.append(dendrite.position[2])
          sizes.append(dendrite.size)
          
        if self.neuron.axon is not None:
          axon = self.neuron.axon
          x.append(axon.position[0])
          y.append(axon.position[1])
          z.append(axon.position[2])
          sizes.append(axon.size)
        
        if self.neuron.soma. is not None:
          soma = self.neuron.soma
          x.append(soma.position[0])
          y.append(synapse.position[1])
          z.append(synapse.position[2])
          sizes.append(synapse.size)
          
         self.ax.scatter(x, y, s= sizes)
         self.ax.set_xlabel('X')
         self.ax.set_ylabel('Y')
         self.ax.set_zlabel('Z')
