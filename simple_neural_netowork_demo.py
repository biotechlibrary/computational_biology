import numpy as np

# Define the input and target data
X = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])
y = np.array([[0,0,1,1]]).T

# Define the activation function (sigmoid)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Define the derivative of the activation function
def sigmoid_derivative(x):
    return x * (1 - x)

# Initialize the synaptic weights
synaptic_weights = 2 * np.random.random((3,1)) - 1

# Train the network for 10,000 iterations
for i in range(10000):
    # Forward propagation
    layer_0 = X
    layer_1 = sigmoid(np.dot(layer_0, synaptic_weights))
    
    # Backward propagation
    layer_1_error = y - layer_1
    layer_1_delta = layer_1_error * sigmoid_derivative(layer_1)
    synaptic_weights += np.dot(layer_0.T, layer_1_delta)

# Print the final output
print("Output after training:")
print(layer_1)
