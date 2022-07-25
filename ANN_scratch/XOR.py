from ANN import *
import numpy as np

X = np.reshape([[0,0], [0,1], [1,0], [1,1]], (4, 2, 1))
Y = np.reshape([[0], [1], [1], [0]], (4, 1, 1))

network = [Dense(2, 3),
            Tanh(),
            Dense(3, 1),
            Tanh()]

epochs = 10000
learning_rate = 0.1

for e in range(epochs):
    error = 0
    for x, y in zip(X, Y):
        output = x
        for Layer in network:
            output = Layer.forward(output)

        error += mse(y, output)

        grad = mse_prime(y, output)
        for Layer in reversed(network):
            grad = Layer.backward(grad, learning_rate)

    error /= len(X)
    print("%d %d, error= %f" % (e-1, epochs, error))