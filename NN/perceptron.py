import numpy as np

def sigmoid(x):
    return 1 / (1+np.exp(-x))

def sigmoid_deriviative(x):
    return x * (1 - x)


training_lenght = 50000


training_inputs = np.array([[0,0,1],
                            [1,1,1],
                            [1,0,1],
                            [0,1,1]])

training_outputs = np.array([[0,1,0,1]]).T

np.random.seed(1)

synaptic_weights = 2 * np.random.random((3,1)) - 1

print("Random starting synaptic weights: ")
print(synaptic_weights)

for iteration in range(training_lenght):

    input_layer = training_inputs

    outputs = sigmoid(np.dot(input_layer, synaptic_weights))

    error = training_outputs - outputs

    adjustment = error * sigmoid_deriviative(outputs)

    synaptic_weights += np.dot(input_layer.T, adjustment)

print("Synaptic weights after training: ")
print(synaptic_weights)
print("Outputs after training: ")
print(outputs)