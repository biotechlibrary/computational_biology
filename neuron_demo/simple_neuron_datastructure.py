#Modeling a neuron as a class. 

class Neuron:
  def __init__(self):
    self.dendrites=[]
    self.axon=[]
    self.soma=[]
    self.synapses=[]
    
  def add_dendrites(self, dendrite):
    self.dendrites.append(dendrite)
    
  def set_axon(self, axon):
    self.axon = axon
    
  def set_soma(self, soma):
    self.soma = soma
    
  def add_synapse(self, synapse):
    self.synapses.append(synapse)
    
    
